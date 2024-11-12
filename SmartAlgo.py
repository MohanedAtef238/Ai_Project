from PapaAgent import PapaAgent

class SmartAlgo(PapaAgent):

    def heuristic(self,nx,ny):
        coinDistance = min(abs(nx - cx) + abs(ny - cy) for cy, cx in self.maze.coinLocations)
        slime_penalty = sum((abs(nx - sx) + abs(ny - sy)) for sy, sx in self.maze.slimeLocations)
        return coinDistance + slime_penalty
    
    def ManhattinHeuristic(self,nx,ny):
        max_x,max_y=self.target
        return abs(nx-max_x) + abs(ny-max_y)