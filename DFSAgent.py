from tiles import Tiles
from PapaAgent import PapaAgent

class DFSAgent(PapaAgent):
    def dfs(self):
        Stack = [(0, 0, set(),  [(0, 0)])] 
        while Stack:
            x, y, coins, path = Stack.pop()
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return 1,path
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.IsValidPos(nx, ny):
                    AddedCoins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        AddedCoins.add((nx, ny))
                    if (nx, ny, frozenset(AddedCoins)) not in self.visited:
                        self.visited.add((nx, ny, frozenset(AddedCoins)))
                        Stack.append((nx, ny, AddedCoins, path + [(nx, ny)]))
        return None

