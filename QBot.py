import numpy as np
import random

class QBot:
    def __init__(self, maze, learnRate, discountFactor):
        assert 0 < learnRate < 1 
        assert 0 < discountFactor < 1

        self.learnRate = learnRate
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.q_table = np.zeros((maze.max_y, maze.max_x, len(self.directions)))
        self.discountFactor = discountFactor
        self.maze = maze
        self.maxCoins = len(maze.coins)
        self.start = (0, 0)  
        self.target = (maze.max_x - 1, maze.max_y - 1)

    def update_q_table(self, current_state, action, reward, next_state):
        # here i used the current states that will be given in the traversing function to find the update values according to the next state influences by the function 
        # the action variable will be used to map the 3d component to make sure each state has a Q value for the future for each action taken
        current_x, current_y = current_state
        action_index = self.directions.index(action)  
        next_x, next_y = next_state
        max_next_q = np.max(self.q_table[next_y, next_x])  

        # da basically el bellmen's equation substituted with the appropriate variables. hoping this works 
        self.q_table[current_y, current_x, action_index] += self.learnRate * (
            reward + self.discountFactor * max_next_q - self.q_table[current_y, current_x, action_index]
        )


