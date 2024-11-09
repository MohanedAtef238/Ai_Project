from tiles import Tiles
from SmartAlgo import SmartAlgo

class HillClimbingAgent(SmartAlgo):
    def hill_climbing(self):
        
        current = (0, 0, set(), [(0, 0)], 0)  
        self.visited.add((0, 0, frozenset()))

        while True:
            x, y, coins, path, cost = current 
            if (x, y) == self.target and len(coins) == self.maxCoins:
                return cost, path

            neighbors = []
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.IsValidPos(nx, ny):
                    nCost = 1 if dx == 1 or dy == 1 else 2 
                    if self.maze.maze[ny][nx] == Tiles.Slime:
                        nCost += 30 
                    new_coins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        new_coins.add((nx, ny))
                    if (nx, ny, frozenset(new_coins)) not in self.visited:
                        self.visited.add((nx, ny, frozenset(new_coins)))
                        neighbors.append((nx, ny, new_coins, path + [(nx, ny)], cost + nCost))
            next_state = min(neighbors, key=lambda n: self.heuristic(n[0], n[1])) # Hena bychoose neighbor b a2l heuristic value hnghyrha random ashan el stochastic 
            if self.heuristic(next_state[0], next_state[1]) >= self.heuristic(x, y):
                break
            current = next_state

        return None  