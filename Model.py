import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from maze import Maze
class Agent:
    CurrentMaze = Maze.getMaze()
    def __init__(self, initX = 0, initY= 0, requiredCoins=0):
        self.posX = initX 
        self.posY = initY 
        self.CoinsToGet = requiredCoins
    def OptimalBFS(self):
        Map = CurrentMaze


