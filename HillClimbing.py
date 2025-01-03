from tiles import Tiles
from SmartAlgo import SmartAlgo
import time
class HillClimbingAgent(SmartAlgo):
    def hill_climbing(self):
        current = (0, 0, frozenset(), [(0, 0)], 0)
        self.visited.add((0, 0, frozenset())) 

        while True:
            x, y, coins, path, cost = current
            Min = (float('inf'), (0, 0), frozenset())
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
                    if heuristic_value < Min[0] and (nx,ny, frozenset(AddedCoins)) not in self.visited:
                        Min = (heuristic_value, (nx, ny), AddedCoins)
                        stuck = False
            BestX,BestY = Min[1]
            CollectedCoins = Min[2]
            if not stuck:
                if (BestX,BestY, frozenset(CollectedCoins)) not in self.visited:
                        self.visited.add((BestX,BestY, frozenset(CollectedCoins)))
                        current = (BestX,BestY, CollectedCoins, path + [(BestX,BestY)], cost + 1)
            elif stuck:
                print("The Algorithm Failed to find a path and got stuck")
                toReturn = (1,path)
                return toReturn
