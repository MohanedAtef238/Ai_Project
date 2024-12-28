import numpy as np
import random
from tiles import Tiles
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
        #four dimensional Q table, with the dimensions, coins and the actions that could be taken
        self.q_table = np.zeros(
            (self.maze.max_y + 1, self.maze.max_x + 1, self.max_coins + 1, len(self.directions))
        )
        self.discountFactor = discountFactor
        self.start = (0, 0)  
        #this goal can be changed dynamically but for now its bottom right corner.
        self.target = (maze.max_x - 1, maze.max_y - 1)
        self.decreasing_factor = 0.7
        self.required_coins = self.max_coins // 3

    def q_function(self, x, y, c, action, reward, nx, ny, c_next):
        action_idx = self.directions.index(action)
        old_q = self.q_table[y, x, c, action_idx]
        pruposed_q = np.max(self.q_table[ny, nx, c_next, :])
        new_q = old_q + self.learnRate * (reward + self.discountFactor * pruposed_q - old_q)
        self.q_table[y, x, c, action_idx] = new_q

    def epsilon_action(self, state, coin_count, epsilon):
        x, y = state
        cur_eps = max(0.0015, epsilon)
        if random.uniform(0, 1) < cur_eps:
            return random.choice(self.directions)
        else:
            pruposed_action = np.argmax(self.q_table[y, x, coin_count, :])
            return self.directions[pruposed_action]

    #explained in detail in the documentation
    def reward_function(self, state, coin_count, next_state, new_coin_c):
        x, y = next_state
        ox, oy = state
        #penalizes going over the same state over and over, alleviates the penalties depending on how many coins were collected
        if next_state in self.visited_states_current_episode:
            return -7 + (0.02*len(self.AddedCoins))
        #rewards coin collection heavily and makes sure the model doesnt abuse one coin by going over it a million times
        if self.maze.maze[y][x] == Tiles.Coin and (y, x) not in self.AddedCoins:
            self.AddedCoins.add((y, x))
            return 7500*len(self.AddedCoins)
        #just like repetitive states, we penalize and alleviate it as more coins are collected
        elif self.maze.maze[y][x] == Tiles.Slime:
            return -5 + (0.05*len(self.AddedCoins))
        #even more rewards for eaching the exit with more coins than the required number
        elif next_state == self.target:
            if new_coin_c >= self.required_coins:
                return 7000*len(self.AddedCoins)
            else:
                return 200
        else:
        #makes sure the model is still aware that it needs to go to the exit by adjusting penalties
            current_distance = (abs(oy - self.maze.max_y) + abs(ox - self.maze.max_x))
            next_distance = (abs(y - self.maze.max_y) + abs(x - self.maze.max_x))
            return -2 + (current_distance - next_distance) * 0.08

    def action_taker(self, state, action):
        x, y = state
        dx, dy = action
        next_state = x + dx, y + dy
        if self.maze.IsValidPos(next_state[0], next_state[1]):
            return next_state
        return state

    #this function fills the Q table 
    def q_episode_travesing(self, max_episodes):
        max_steps_allowed = 4200
        initial_epsilon = 0.25
        epsillon_factor = initial_epsilon
        plt.ion()
        fig, ax = plt.subplots()
        rewards_history = []
        #Here we start exploring to fill the Q table
        for i in range(max_episodes):
            #keeps track of the visited states so we can penalize it in rewards, so the agent doesnt loop 
            self.visited_states_current_episode = set()
            state = self.start
            #some paramters
            coin_count = 0
            steps = 0
            total_rewards = 0

            while state != self.target and steps <= max_steps_allowed:
                #adding state to the visited states
                self.visited_states_current_episode.add(state)
                #picking an action
                current_action = self.epsilon_action(state, coin_count, epsillon_factor)
                #taking the action and recording it in the new state
                incoming_state = self.action_taker(state, current_action)
                new_coin_count = coin_count
                nx, ny = incoming_state
                x, y = state
                if self.maze.maze[ny][nx] == Tiles.Coin:
                    new_coin_count = min(coin_count + 1, self.max_coins)
                #calcualting the reward for the current action
                current_reward = self.reward_function(state, coin_count, incoming_state, new_coin_count)
                #adding it to the Q table
                self.q_function(x, y, coin_count, current_action, current_reward, nx, ny, new_coin_count)
                #replacing current state and coin count for the next iteration
                state, coin_count = incoming_state, new_coin_count
                total_rewards += current_reward
                steps += 1

            #decreasing epsillon to reduce exploration as we find more favorable answers
            epsillon_factor *= self.decreasing_factor

            #plotting shenanigins from the documentation
            rewards_history.append(total_rewards)
            ax.clear()
            ax.plot(rewards_history, label='Episode Reward')
            ax.set_xlabel('Episode')
            ax.set_ylabel('Total Reward')
            ax.set_title('Q-Learning Rewards Over Time')
            ax.legend()
            plt.pause(0.005)
            print(f"Episode {i+1}, Current Reward Total = {total_rewards}")
        print("done done :D")
        plt.ioff()
        plt.show()
        return
    
    #this traverses the maze using the Q table 
    def path_generation_test(self):
        x, y = self.start
        coin_count = 0
        #initializes path with the default values inserted above
        path = [(x, y, coin_count)]
        #records current visited nodes with a key 1 for count of visits
        visit_count = {(x, y, coin_count): 1}
        #maximum amount of steps to avoid infinite paths
        step_limit = self.maze.max_x * self.maze.max_y * 5
        steps = 0
        #we're only inside this loop when we're under the step limit or didnt find the goal yet 
        while (x, y) != self.target and steps < step_limit:
            found_state = True
            steps += 1
            #this shows the values for each action depending on the state and coin_count
            qvals = self.q_table[y, x, coin_count, :]
            #this sorts the values we just got in descending order so we can explore them accordingly
            all_actions = np.argsort(qvals)[::-1]
            #this records the best action
            best_action_idx = np.argmax(qvals)
            #this fetches the action required to get the max action value
            best_action = self.directions[best_action_idx]
            #here we record the new best action
            nx, ny = self.action_taker((x, y), best_action)
            #updates the coin count
            new_coin_count = coin_count
            if self.maze.maze[ny][nx] == Tiles.Coin and new_coin_count < self.max_coins:
                new_coin_count += 1
            next_state = (nx, ny, new_coin_count)
            #this block was made to handle loops and overly repeating traversal
            if visit_count.get(next_state, 0) >= 10:
                found_state = False
                for index in all_actions[1:]:
                    new_act = self.directions[index]
                    new_nx, new_ny = self.action_taker((x, y), new_act)

                    if self.maze.maze[new_ny][new_nx] == Tiles.Coin:
                        n_coin_count = coin_count + 1
                    else:
                        n_coin_count = coin_count

                    alt_state = (new_nx, new_ny, n_coin_count)

                    if visit_count.get(alt_state, 0) < 10:
                        next_state = alt_state
                        found_state = True
                        break
            # if we initialize the value by false and we are unable to exit the for loop after trying all the possible actions 
            # if no action was found that has less visit counts than the node we were at, we terminate the loop. this usually means our
            # Q table wasnt generated favorably and another attempt is needed               
            if not found_state:
                print("stuck in a loop (count-based)")
                return path
            x, y, coin_count = next_state
            path.append(next_state)
            visit_count[next_state] = visit_count.get(next_state, 0) + 1

        if (x, y) == self.target:
            print("Path found")
            return path
        else:
            print("infinite loop")
            return path
