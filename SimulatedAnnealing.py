from math import exp
from itertools import count
import random
from tiles import Tiles
from SmartAlgo import SmartAlgo

class SimulatedAnnealing(SmartAlgo):
    def simulated_annealing(self, schedule):
        
        current_state = (0, 0, frozenset(), [(0, 0)], 0)
        current_value = self.heuristic(*current_state[:2])
        self.visited.add((0, 0, frozenset()))

        for t in count():
            T = schedule(t) 
            if (current_state[0], current_state[1]) == self.target and len(current_state[2]) == self.maxCoins:
                return 1, current_state[3]
            if T == 0: 
                return 1, current_state[3]

            next_states = []
            x, y, coins, path, cost = current_state
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.maze.IsValidPos(nx, ny):
                    new_coins = set(coins)
                    if self.maze.maze[ny][nx] == Tiles.Coin:
                        new_coins.add((nx, ny))
                    if (nx, ny, frozenset(new_coins)) not in self.visited:
                        next_states.append((nx, ny, new_coins, path + [(nx, ny)], cost + 1))

            if not next_states:
                return 1, path

            next_state = random.choice(next_states)
            next_value = self.heuristic(*next_state[:2])
            delta = next_value - current_value
            if delta < 0 or random.random() < exp(-delta / T):
                current_state, current_value = next_state, next_value
                self.visited.add((current_state[0], current_state[1], frozenset(current_state[2])))

        return 1, current_state[3]

