
class PapaAgent:
    def __init__(self, maze):
        self.maze = maze
        self.target_coins = len(maze.coins)
        self.start = (0, 0)  
        self.target = (maze.max_x - 1, maze.max_y - 1)

