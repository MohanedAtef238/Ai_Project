import numpy as np
import random
from tiles import Tiles
from SmartAlgo import SmartAlgo
import time 
import matplotlib.pyplot as plt

class QBot:
    def __init__(self, maze, learnRate, discountFactor):
        assert 0 < learnRate < 1 
        assert 0 < discountFactor < 1
        self.AddedCoins = set()
        self.learnRate = learnRate
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.maze = maze
        self.max_coins = len(self.maze.coins)
        self.q_table = np.zeros(
            (self.maze.max_y + 1, self.maze.max_x + 1, self.max_coins + 1, len(self.directions))
        )
        self.discountFactor = discountFactor
        self.start = (0, 0)  
        self.target = (maze.max_x - 1, maze.max_y - 1)
        self.decreasing_factor = 0.95
        self.required_coins = self.max_coins // 3

    def q_function(self, x, y, c, action, reward, nx, ny, c_next):
        action_idx = self.directions.index(action)
        old_q = self.q_table[y, x, c, action_idx]
        future_q = np.max(self.q_table[ny, nx, c_next, :])
        new_q = old_q + self.learnRate * (reward + self.discountFactor * future_q - old_q)
        self.q_table[y, x, c, action_idx] = new_q

    def epsilon_action(self, state, coin_count, epsilon):
        x, y = state
        cur_eps = max(0.06, epsilon * self.decreasing_factor)
        if random.uniform(0, 1) < cur_eps:
            return random.choice(self.directions)
        else:
            pruposed_action = np.argmax(self.q_table[y, x, coin_count, :])
            return self.directions[pruposed_action]

    def reward_function(self, state, coin_count, next_state, new_coin_c):
        x, y = next_state
        ox, oy = state
        if next_state in self.visited_states_current_episode:
            return -7 + (0.02*len(self.AddedCoins))
        if self.maze.maze[y][x] == Tiles.Coin and (y, x) not in self.AddedCoins:
            self.AddedCoins.add((y, x))
            return 7500*len(self.AddedCoins)
        elif self.maze.maze[y][x] == Tiles.Slime:
            return -5 + (0.05*len(self.AddedCoins))
        elif next_state == self.target:
            if new_coin_c >= self.required_coins:
                return 7000*len(self.AddedCoins)
            else:
                return 200
        else:
            current_distance = (abs(oy - self.maze.max_y) + abs(ox - self.maze.max_x))
            next_distance = (abs(y - self.maze.max_y) + abs(x - self.maze.max_x))
            return -2 + (current_distance - next_distance) * 0.15

    def action_taker(self, state, action):
        x, y = state
        dx, dy = action
        next_state = x + dx, y + dy
        if self.maze.IsValidPos(next_state[0], next_state[1]):
            return next_state
        return state

    def q_episode_travesing(self, max_episodes):
        max_steps_allowed = 5000
        initial_epsilon = 0.8
        epsillon_factor = initial_epsilon
        plt.ion()
        fig, ax = plt.subplots()
        rewards_history = []
        for i in range(max_episodes):
            self.visited_states_current_episode = set()
            state = self.start
            coin_count = 0
            steps = 0
            total_rewards = 0
            while state != self.target and steps <= max_steps_allowed:
                self.visited_states_current_episode.add(state)
                current_action = self.epsilon_action(state, coin_count, epsillon_factor)
                incoming_state = self.action_taker(state, current_action)
                new_coin_count = coin_count
                nx, ny = incoming_state
                x, y = state
                if self.maze.maze[ny][nx] == Tiles.Coin:
                    new_coin_count = min(coin_count + 1, self.max_coins)
                current_reward = self.reward_function(state, coin_count, incoming_state, new_coin_count)
                self.q_function(x, y, coin_count, current_action, current_reward, nx, ny, new_coin_count)
                state, coin_count = incoming_state, new_coin_count
                total_rewards += current_reward
                steps += 1
            epsillon_factor *= self.decreasing_factor
            rewards_history.append(total_rewards)
            ax.clear()
            ax.plot(rewards_history, label='Episode Reward')
            ax.set_xlabel('Episode')
            ax.set_ylabel('Total Reward')
            ax.set_title('Q-Learning Rewards Over Time')
            ax.legend()
            plt.pause(0.0005)
            print(f"Episode {i+1}, Current Reward Total = {total_rewards}")
        print("done done :D")
        plt.ioff()
        plt.show()
        return

    def path_generation_test(self):
        x, y = self.start
        coin_count = 0
        path = [(x, y, coin_count)]
        visit_count = {(x, y, coin_count): 1}
        step_limit = self.maze.max_x * self.maze.max_y * 5
        steps = 0
        while (x, y) != self.target and steps < step_limit:
            steps += 1
            qvals = self.q_table[y, x, coin_count, :]
            best_action_idx = np.argmax(qvals)
            best_action = self.directions[best_action_idx]
            nx, ny = self.action_taker((x, y), best_action)
            new_coin_count = coin_count
            if self.maze.maze[ny][nx] == Tiles.Coin and new_coin_count < self.max_coins:
                new_coin_count += 1
            next_state = (nx, ny, new_coin_count)
            if visit_count.get(next_state, 0) >= 10:
                all_actions = sorted(
                    range(len(self.directions)),
                    key=lambda idx: self.q_table[x, y, coin_count, idx],
                    reverse=True
                )
                for alt_idx in all_actions[1:]:
                    alt_action = self.directions[alt_idx]
                    alt_nx, alt_ny = self.action_taker((x, y), alt_action)
                    alt_coin_count = coin_count
                    if self.maze.maze[alt_ny][alt_nx] == Tiles.Coin and alt_coin_count < self.max_coins:
                        alt_coin_count += 1
                    alt_state = (alt_nx, alt_ny, alt_coin_count)
                    if visit_count.get(alt_state, 0) < 10:
                        next_state = alt_state
                        break
                else:
                    print("No valid path found - stuck in a loop (count-based)")
                    return path
            x, y, coin_count = next_state
            path.append(next_state)
            visit_count[next_state] = visit_count.get(next_state, 0) + 1
        if (x, y) == self.target:
            print("Path found successfully!")
            return path
        else:
            print("Path too long - possible infinite loop or no solution.")
            return path
