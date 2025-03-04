import random
import numpy as np

# doors allocation
doors = np.eye(4)
doors_exploration = np.ones((4,4))
# queue 
queue = list(range(16))
# game
random.seed(123)
level_reached = 0
while level_reached<4 or len(queue)==0:
    for player in queue:
        for level in range(doors.shape[0]):
            tmp = doors_exploration[level,]
            unexplored_index = np.where(tmp != 0)[0]
            chosen_door = random.sample(list(unexplored_index),1)[0]
            # see a clown
            if doors[level,chosen_door]==0:
                doors_exploration[level,chosen_door]=0
                queue.pop()
                break
            level_reached += 1

# print(queue)
# print(doors_exploration)





    



