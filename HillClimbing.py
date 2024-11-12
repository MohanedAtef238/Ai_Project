from tiles import Tiles
from SmartAlgo import SmartAlgo
import time
class HillClimbingAgent(SmartAlgo):
    def hill_climbing(self):
        current = (0, 0, frozenset(), [(0, 0)], 0)
        self.visited.add((0, 0, frozenset())) 

        while True:
            x, y, coins, path, cost = current
            Minimum = (float('inf'), (0, 0), frozenset())
            stuck = True
            
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return 1, path
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.IsValidPos(nx, ny):
                    AddedCoins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        AddedCoins.add((nx, ny))
                    heuristic_value = self.heuristic(nx, ny)
                    if heuristic_value < Minimum[0] and (nx,ny, frozenset(AddedCoins)) not in self.visited:
                        Minimum = (heuristic_value, (nx, ny), AddedCoins)
                        stuck = False
            BestX,BestY = Minimum[1]
            CollectedCoins = Minimum[2]
            if not stuck:
                if (BestX,BestY, frozenset(CollectedCoins)) not in self.visited:
                        self.visited.add((BestX,BestY, frozenset(CollectedCoins)))
                        current = (BestX,BestY, CollectedCoins, path + [(BestX,BestY)], cost + 1)
            elif stuck:
                print("The Algorithm Failed to find a path and got stuck")
                toReturn = (-3,path)
                return toReturn
            # PrintP= (1,path)
            # self.maze.PrintPath(PrintP)
            # print(f"Current position: {(x, y)}")
            # print(f"Visited states: {self.visited}")
            # print(f"Minimum heuristic: {Minimum[0]}")
            # print(f"Stuck Status  {stuck}")
            # time.sleep(2)
            # print("running" , len(CollectedCoins))