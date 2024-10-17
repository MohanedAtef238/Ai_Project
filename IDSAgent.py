from PapaAgent import PapaAgent
from tiles import Tiles
from collections import deque

class IDSAgent(PapaAgent):
    def IDS(self):
        maxDepth= 10
        Stack = [(0, 0, set(),  [(0, 0)])] 
        queue = deque()
        done = False
        while not done:
            if curDepth == maxDepth:
                curDepth=0
                Stack.clear()
                # Still not done, i need to fix this logic so i perform BFS once every cycle and DFS inbetween. 
            if queue:
                x, y, coins, path = queue.popleft()
            for dx, dy in self.directions:
                nx1, ny1 = x + dx, y + dy
                if self.maze.IsValidPos(nx1, ny1):
                    AddedCoins = set(coins)
                    if self.maze.maze[ny1][nx1] == Tiles.Coin:
                            AddedCoins.add((nx1, ny1))
                    if (nx1, ny1, frozenset(AddedCoins)) not in self.visited:
                            self.visited.add((nx1, ny1, frozenset(AddedCoins)))
                            queue.append((nx1, ny1, AddedCoins, path + [(nx1, ny1)]))
            while Stack and curDepth != maxDepth :
                    x, y, coins, path = Stack.pop()
                    curDepth +=1


                    if (x, y) == self.target and len(coins) == self.maxCoins:
                        return 2,path
                    

                    AddedCoins = set(coins)


                    for dx, dy in self.directions:
                        nx, ny = x + dx, y + dy
                        if self.maze.IsValidPos(nx, ny):
                            if self.maze.maze[ny][nx] == Tiles.Coin:
                                AddedCoins.add((nx, ny))
                            if (nx, ny, frozenset(AddedCoins)) not in self.visited:
                                self.visited.add((nx, ny, frozenset(AddedCoins)))
                                Stack.append((nx, ny, AddedCoins, path + [(nx, ny)]))
                                queue.append((nx,ny, AddedCoins, path + [(nx,ny)] ))
            return None