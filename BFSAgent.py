from tiles import Tiles
from collections import deque
from PapaAgent import PapaAgent

class BFSAgent(PapaAgent):
    def bfs(self):
        queue = deque([(0, 0, set(),  [(0, 0)])]) 
        
        while queue:
            x, y, coins, path = queue.popleft()
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return 0,path
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.IsValidPos(nx, ny):
                    AddedCoins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        AddedCoins.add((nx, ny))
                    if (nx, ny, frozenset(AddedCoins)) not in self.visited:
                        self.visited.add((nx, ny, frozenset(AddedCoins)))
                        queue.append((nx, ny, AddedCoins, path + [(nx, ny)]))
        return None

