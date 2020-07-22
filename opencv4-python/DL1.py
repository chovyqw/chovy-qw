import numpy as np
import random

r = np.array([[-1, -1, -1, -1, 0, -1], 
              [-1, -1, -1, 0, -1, 100],
              [-1, -1, -1, 0, -1, -1],
              [-1, 0, 0, -1, 0, -1],
              [0, -1, -1, 0, -1, 100],
              [-1, 0, -1, -1, 0, 100]])

q = np.zeros([6,6],dtype=np.float32)

gamma = 0.8

step = 0
#生成q表
while step < 1000:
    state = random.randint(0,5)
    if step%100 ==0:
        print('step %d:' % step)
        print(q)
    if state != 5:
        next_state_list=[]      
        for i in range(6):
            if r[state,i] != -1:
                next_state_list.append(i)
        next_state = next_state_list[random.randint(0,len(next_state_list)-1)]
        qval = r[state,next_state] + gamma * max(q[next_state])
        q[state,next_state] = qval     #更新q表
        step += 1       


for i in range(10):
    print("\nvalidation epoch: {}".format(i + 1))
    state = random.randint(0, 5)
    print('robot state: {}'.format(state))
    count = 0
    while state != 5:
        if count > 20:
            print('fail')
            break
        q_max = q[state].max()

        q_max_action = []
        for action in range(6):
            if q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        state = next_state
        count += 1


