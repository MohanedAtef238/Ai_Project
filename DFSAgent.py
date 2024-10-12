from tiles import Tiles

class DFSAgent:
    def __init__(self, maze):
        self.maze = maze
        self.target_coins = len(maze.coins) // 2
        self.start = (0, 0) 
        self.target = (maze.max_x - 1, maze.max_y - 1)  

    def dfs(self):
        Stack = [(0, 0, set(),  [(0, 0)])] 
        visited = set([(0, 0, frozenset(set()))])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while Stack:
            x, y, coins, path = Stack.pop()
            
            if (x, y) == self.target and len(coins) == self.target_coins:
                return path
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.maze.is_valid_position(new_x, new_y):

                    new_coins = set(coins)
                    if self.maze.maze[new_y][new_x] == Tiles.Coin:
                        new_coins.add((new_x, new_y))

                    if (new_x, new_y, frozenset(new_coins)) not in visited:
                        visited.add((new_x, new_y, frozenset(new_coins)))
                        Stack.append((new_x, new_y, new_coins, path + [(new_x, new_y)]))
        return None

