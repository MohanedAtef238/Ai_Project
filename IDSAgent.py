from PapaAgent import PapaAgent
from tiles import Tiles

class IDSAgent(PapaAgent):
    def dfs(self):
        Stack = [(0, 0, set(),  [(0, 0)])] 
        visited = set([(0, 0, frozenset(set()))])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while Stack:
            x, y, coins, path = Stack.pop()
            if (x, y) == self.target and len(coins) == self.target_coins:
                return 1,path
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.maze.is_valid_position(nx, ny):
                    new_coins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        new_coins.add((nx, ny))
                    if (nx, ny, frozenset(new_coins)) not in visited:
                        visited.add((nx, ny, frozenset(new_coins)))
                        Stack.append((nx, ny, new_coins, path + [(nx, ny)]))
        return None