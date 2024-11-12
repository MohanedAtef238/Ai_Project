from tiles import Tiles
from PapaAgent import PapaAgent

class IDSAgent(PapaAgent):
    
    def dfs_forIDS(self, maxDepth):
        Stack = [(0, 0, set(), [(0, 0)], 0)]  
        self.visited.clear()
        while Stack:
            x, y, coins, path, curdepth = Stack.pop()
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return 1, path
            if curdepth < maxDepth:
                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy
                    if self.maze.IsValidPos(nx, ny):
                        AddedCoins = set(coins)
                        if self.maze.maze[ny][nx] == Tiles.Coin:
                            AddedCoins.add((nx, ny))
                        if (nx, ny, frozenset(AddedCoins)) not in self.visited:
                            self.visited.add((nx, ny, frozenset(AddedCoins)))
                            Stack.append((nx, ny, AddedCoins, path + [(nx, ny)], curdepth + 1))
        
        return 0, None  
    def IDS(self):
        depth = 1
        completed = False
        while not completed:
            done, path = self.dfs_forIDS(depth)
            completed = done
            depth += 3  

        if completed:
            return 1,path
        else:
            return 0,None
