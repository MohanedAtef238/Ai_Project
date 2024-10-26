
from queue import PriorityQueue
from tiles import Tiles
from PapaAgent import PapaAgent
from SmartAlgo import SmartAlgo

class AStarAgent(SmartAlgo): 
    def AStar(self): 
        queue = PriorityQueue() 
        queue.put((0,(0, 0, set(),  [(0, 0)])))
        while not queue.empty():
            cost, info = queue.get()
            x, y, coins, path = info
            
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return cost, path
            
            for dx, dy in self.directions:
                
                nx, ny = x + dx, y + dy
                if dx == -1 or dy == -1:
                    nCost = 2
                elif dx == 1 or dy == 1:
                    nCost = 1

                if self.maze.IsValidPos(nx, ny):
                    AddedCoins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        AddedCoins.add((nx, ny))
                    if self.maze.maze[ny][nx] == Tiles.Slime:
                        nCost += 30
                    if (nx, ny, frozenset(AddedCoins)) not in self.visited:
                        self.visited.add((nx, ny, frozenset(AddedCoins)))
                        queue.put((cost + nCost+self.heuristic(nx, ny),(nx,ny, AddedCoins, path + [(nx, ny)])))

        return None
    
