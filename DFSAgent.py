from tiles import Tiles
from PapaAgent import PapaAgent

class DFSAgent(PapaAgent):
    def dfs(self):
        Stack = [(0, 0, set(),  [(0, 0)])] 
        while Stack:
            x, y, coins, path = Stack.pop()
            if (x, y) == self.target and len(coins) == self.target_coins:
                return 1,path
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.is_valid_position(nx, ny):
                    new_coins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        new_coins.add((nx, ny))
                    if (nx, ny, frozenset(new_coins)) not in self.visited:
                        self.visited.add((nx, ny, frozenset(new_coins)))
                        Stack.append((nx, ny, new_coins, path + [(nx, ny)]))
        return None

