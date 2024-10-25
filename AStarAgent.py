from queue import PriorityQueue
from tiles import Tiles  
from PapaAgent import PapaAgent  

class AStarAgent(PapaAgent):
    def aStar(self):
        start = self.start  
        goal = self.target 

        g_score = {start: 0}
        f_score = {start: self.h1(start, goal)}

        open_set = PriorityQueue() 
        open_set.put((f_score[start], start))  
        
        came_from = {}  

        while not open_set.empty():
            current_cell = open_set.get()
            
            
            if current_cell == goal and len(self.AddedCoins) == self.maxCoins:  
                return self.reconstruct_path(came_from, current_cell)

            for dx, dy in self.directions:  
                neighbor = (current_cell[0] + dx, current_cell[1] + dy)

                if self.maze.IsValidPos(neighbor[0], neighbor[1]) and self.maze.maze[neighbor[1]][neighbor[0]] in (Tiles.Empty, Tiles.Coin):
                    temp_g_score = g_score[current_cell] + 1  

                    AddedCoins = set(self.AddedCoins)  
                    if self.maze.maze[neighbor[1]][neighbor[0]] == Tiles.Coin:
                        AddedCoins.add(neighbor)  

                    temp_f_score = temp_g_score + self.h1(neighbor, goal)

                   
                    if (neighbor, frozenset(AddedCoins)) not in self.visited:
                        came_from[neighbor] = current_cell  
                        g_score[neighbor] = temp_g_score  
                        f_score[neighbor] = temp_f_score  
                        self.visited.add((neighbor, frozenset(AddedCoins)))  

                        if neighbor not in [i[1] for i in open_set.queue]:  
                            open_set.put((f_score[neighbor], neighbor))  

        
        return 1


# def h1(self, node, goal):
#         return abs(node[0] - goal[0]) + abs(node[1] - goal[1])