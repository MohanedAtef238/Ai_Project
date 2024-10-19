from queue import PriorityQueue
from tiles import Tiles  
from PapaAgent import PapaAgent  

class AStarAgent(PapaAgent):
    def aStar(self):
        start = self.start  
        goal = self.target 
        
        g_score = {cell: float('inf') for cell in self.maze.grid} 
        g_score[start] = 0  # Starting point cost is zero
        
        f_score = {cell: float('inf') for cell in self.maze.grid}  
        f_score[start] = self.h1(start, goal)  # Heuristic from start to goal
        
        open_set = PriorityQueue() 
        open_set.put((f_score[start], start))  # Add starting cell
        
        came_from = {}  # To keep track of the best path
        
        while not open_set.empty():
            current_cell = open_set.get()[1]  # Get the cell with the lowest f_score
            
            if current_cell == goal:  # If goal is reached
                return self.reconstruct_path(came_from, current_cell)  # Return the path
            
            for d in 'ESNW':  # Explore neighbors
                if self.maze.maze_map[current_cell][d]:  # Check if the direction is valid
                    neighbor = self.get_neighbor(current_cell, d)  # Determine neighbor cell
                    
                    temp_g_score = g_score[current_cell] + 1  # Temp score
                    
                    # Calculate temp f_score using g_score and the heuristic
                    temp_f_score = temp_g_score + self.h1(neighbor, goal)
                    
                    if temp_f_score < f_score[neighbor]:  # A better path found
                        came_from[neighbor] = current_cell  # Update path
                        g_score[neighbor] = temp_g_score  # Update g_score
                        f_score[neighbor] = temp_f_score  # Update f_score
                        
                        if neighbor not in [i[1] for i in open_set.queue]:  # If neighbor not in open set
                            open_set.put((f_score[neighbor], neighbor))  # Add neighbor to the open set
        
        return None  # Return None if no path is found

    def h1(self, cell1, cell2):
        
        x1, y1 = cell1
        x2, y2 = cell2
        return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance heuristic


          # Getting the neighbor  direction
    def get_neighbor(self, current_cell, direction):
    #   move east south north or west 
        if direction == 'E':
            return (current_cell[0], current_cell[1] + 1)  
        elif direction == 'S':
            return (current_cell[0] + 1, current_cell[1])  
        elif direction == 'N':
            return (current_cell[0] - 1, current_cell[1]) 
        elif direction == 'W':
            return (current_cell[0], current_cell[1] - 1)  


#   Reconstructing the path from the came_from 
    def reconstruct_path(self, came_from, current_cell):
      
        total_path = [current_cell]
        while current_cell in came_from:  # Reconstruct the path
            current_cell = came_from[current_cell]
            total_path.append(current_cell)
        return total_path[::-1]  # Return reversed path
