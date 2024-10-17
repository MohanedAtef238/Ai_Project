from queue import PriorityQueue
from tiles import Tiles
from PapaAgent import PapaAgent

class UCSAgent(PapaAgent):
    def UCS(self):
        queue = PriorityQueue() 
        queue.put((0,(0, 0, set(),  [(0, 0)])))
        
        while not queue.empty():
            cost, info = queue.get()
            x, y, coins, path = info
            
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return cost, path
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                nCost = 1
                if self.maze.IsValidPos(nx, ny):
                    AddedCoins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        AddedCoins.add((nx, ny))
                    if self.maze.maze[ny][nx] == Tiles.Slime:
                        nCost += 30
                    x2, y2, coins2, path2 = self.visited[x][y] 
                    if (nx, ny, frozenset(AddedCoins)) not in self.visited or (nx,ny, frozenset(AddedCoins)) in self.visited and :
                        self.visited.add((nx, ny, frozenset(AddedCoins)))
                        queue.put((cost+nCost,(nx, ny, AddedCoins, path + [(nx, ny)])))
        return None
