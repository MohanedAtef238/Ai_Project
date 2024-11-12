class PapaAgent:
    def __init__(self, maze):
        self.maze = maze
        self.maxCoins = len(maze.coins)
        self.start = (0, 0)  
        self.target = (maze.max_x - 1, maze.max_y - 1)
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visited = set([(0, 0, frozenset(set()))])

