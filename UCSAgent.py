from queue import PriorityQueue
from tiles import Tiles
from PapaAgent import PapaAgent

class UCSAgent(PapaAgent):
    def UCS(self):
        queue = PriorityQueue() 
        queue.put((0,(0, 0, set(),  [(0, 0)])))
        visited = set([(0, 0, frozenset(set()))])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while not queue.empty():
            cost, info = queue.get()
            x, y, coins, path = info
            
            if (x, y) == self.target and len(coins) == self.target_coins:
                return cost, path
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                nCost = 1
                if self.maze.is_valid_position(nx, ny):
                    new_coins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        new_coins.add((nx, ny))
                    if self.maze.maze[ny][nx] == Tiles.Slime:
                        nCost += 30
                    if (nx, ny, frozenset(new_coins)) not in visited:
                        visited.add((nx, ny, frozenset(new_coins)))
                        queue.put((cost+nCost,(nx, ny, new_coins, path + [(nx, ny)])))
        return None
