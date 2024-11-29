from PapaAgent import PapaAgent

class SmartAlgo(PapaAgent):

    def heuristic(self,nx,ny):

        min = float("inf")
        for cy, cx in self.maze.coinLocations:
            current = (abs(nx - cx) + abs(ny - cy))
            if current < min:
                min = current

        coinDistance = min

        slimePenalty = 0
        for sy, sx in self.maze.slimeLocations:
            try:
                temp = 1/ (abs(nx - sx) + abs(ny - sy)) 
            except ZeroDivisionError:
                temp = 0
            finally:
                slimePenalty += temp

        return (2 * coinDistance) - slimePenalty + self.ManhattanHeuristic(nx,ny)
    
    def ManhattanHeuristic(self,nx,ny):
        max_x,max_y=self.target
        try:
            temp = (abs(nx - max_x) + abs(ny - max_y)) 
        except ZeroDivisionError: #back then manhattan was a secondary goal but not anymore so this part is irrelevant 
            temp = 0
        finally:
            return temp
