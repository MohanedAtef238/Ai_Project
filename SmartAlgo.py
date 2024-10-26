from PapaAgent import PapaAgent

class SmartAlgo(PapaAgent):

    def heuristic(self,nx,ny):
        max_x,max_y=self.target
        return abs(nx-max_x) + abs(ny-max_y)