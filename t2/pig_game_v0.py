import random 
import numpy as np

'''
Two-Player Pig game
Description:
Simulate a pig game given a target and the strategies implemented in `pig_strategy` function

Arguments:
target (int): pig game target 
start_strategy: if the non random strategy starts

Output:
int: 1 if non random strategy wins 2 if the random strategy wins
'''
def pig_game(target: int,start_strategy:bool) -> int:
    # initialize the game 
    scores = [0,0]
    iter_max = 1000
    count, round = 0, 0
    if start_strategy:
        player_pos = 0 
    else: 
        player_pos = 1
    while(scores[0]<target and scores[1]<target) and count<iter_max:
        roll_value =  random.sample(range(1,7),1)[0]
        # finish game
        if roll_value == 1:
            player_pos = (player_pos + 1)%2
            round=0
        # make a decision
        else:
            round = round + roll_value
            hold = pig_strategy(scores,round,target,player_pos)
            if hold:
                scores[player_pos] = scores[player_pos]+round
                round = 0
                player_pos = (player_pos + 1)%2
            else:
                count+=1
                continue
    if count < iter_max:
        if(scores[0]>=target and scores[1]<target):
            #print("First player win")
            return(1)
        if(scores[1]>=target  and scores[0]<target):
            #print("Second player win")
            return(2)
        
'''
Pig strategy
Description:
Implement two strategies each one for each player

Arguments:
scores (list(int, int)): Current score for the players
round (int): Current accumulated score 
target (int): Target of the game
player_pos (int): ID for the player and the corresponding strategy. Values: 0,1
0: for non-random strategy
1: random strategy

Output:
hold (bool): If should hold or not depending of the strategy
'''
def pig_strategy(scores:list[int,int],round:int,target:int,player_pos:int) -> bool:
    if player_pos == 0:
        # strategy 1
        if round >= 10 or scores[player_pos]+round==target:
            hold=True
        else:
            hold=False
    if player_pos == 1:
        # random strategy
        if np.random.uniform(0,1,size = 1)[0]<0.5:
            hold=True
        else:
            hold=False
    return hold

# Competition of two strategies
np.random.seed(1)
simulation = []
for _ in range(1000):
    simulation.append(pig_game(50,False))
     
print(simulation.count(1))
print(simulation.count(2))