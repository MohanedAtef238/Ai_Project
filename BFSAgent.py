from tiles import Tiles
from collections import deque
from PapaAgent import PapaAgent

class BFSAgent(PapaAgent):
    def bfs(self):
        queue = deque([(0, 0, set(),  [(0, 0)])]) 
        
        while queue:
            x, y, coins, path = queue.popleft()
            if (x, y) == self.target and len(coins) == self.target_coins:
                return 0,path
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.is_valid_position(nx, ny):
                    new_coins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        new_coins.add((nx, ny))
                    if (nx, ny, frozenset(new_coins)) not in self.visited:
                        self.visited.add((nx, ny, frozenset(new_coins)))
                        queue.append((nx, ny, new_coins, path + [(nx, ny)]))
        return None

