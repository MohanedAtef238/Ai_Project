from tiles import Tiles
from PapaAgent import PapaAgent

class IDSAgent(PapaAgent):
    def IDS(self):
        depth = 0
        while True:
            self.visited = set()
            result = self.dfs_with_depth_limit(depth)
            if result is not None:
                return result
            depth += 1

    def dfs_with_depth_limit(self, depth_limit):
        Stack = [(0, 0, set(), [(0, 0)])]
        while Stack:
            x, y, coins, path = Stack.pop()
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return 1, path
            
            if len(path) <= depth_limit:
                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy
                    if self.maze.IsValidPos(nx, ny):
                        AddedCoins = set(coins)
                        if self.maze.maze[ny][nx] == Tiles.Coin:
                            AddedCoins.add((nx, ny))
                        
                        state = (nx, ny, frozenset(AddedCoins))
                        if state not in self.visited:
                            self.visited.add(state)
                            Stack.append((nx, ny, AddedCoins, path + [(nx, ny)]))
        
        return None
