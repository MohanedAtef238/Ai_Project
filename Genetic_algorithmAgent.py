import random
from tiles import Tiles 
from SmartAlgo import SmartAlgo

class GeneticAlgorithmAgent(SmartAlgo):
    def __init__(self, maze):
        # print("initialized Agent")
        super().__init__(maze)
        self.population = []
    def genetic_algorithm(self, fitness_fn, f_thres=0, ngen=300):
        f_thres = -2000 + (30 * (len(self.maze.slimeLocations)/2)) - 50*(self.maxCoins) - 100
        for i in range(ngen):
            print("initializing...")
            self.init_population()
            print(f"Generation {i+1}")
            self.population = [
                self.mutate(self.recombine(*self.select(2, fitness_fn)))
                for _ in range(len(self.population))
            ]
            fittest_individual = min(self.population, key=fitness_fn)
            print(f"Best fitness: {fitness_fn(fittest_individual)}")
            if fitness_fn(fittest_individual) <= f_thres:
                # fittest_individual = self.convert_state_to_path(fittest_individual)
                return (1, fittest_individual)
        return (None, min(self.population, key=fitness_fn))


    
    def init_population(self):
        g = 4
        for i in range(100):
            path = [(0, 0)]
            j, Q = 0, 1000
            while j < Q:
                Cx, Cy = path[-1]
                valid_moves = []
                for dx, dy in self.directions:
                    X, Y = Cx + dx, Cy + dy
                    if self.maze.IsValidPos(X, Y) and (X, Y) not in path:
                        valid_moves.append((dx, dy))

                if not valid_moves:
                    break

                nx, ny = random.choice(valid_moves)
                X, Y = Cx + nx, Cy + ny

                if (X, Y) == self.target:
                    break
                path.append((X, Y))
                j += 1

            self.population.append(path)
        return self.population




    def fitness(self, state):
        path = [(0, 0)]
        fitvalue = 0
        coinscollected = 0
        for dx, dy in state:
            Cx, Cy = path[-1]
            path += [(Cx + dx, Cy + dy)]
            Cx, Cy = path[-1]
            if not self.maze.IsValidPos(Cx, Cy):
                continue
            else:
                fitvalue -= 1    
                if self.maze.maze[Cy][Cx] == Tiles.Coin:
                    coinscollected += 1
                    fitvalue -= 50 

                if self.maze.maze[Cy][Cx] == Tiles.Slime:
                    fitvalue += 30  

                if (Cx, Cy) == self.target:
                    fitvalue -= 100
                    return fitvalue
                
                fitvalue -=2*self.heuristic(Cx,Cy)

        Cx, Cy = path[-1]    
        if len(state) < 1000 and (Cx, Cy) != self.target:
            fitvalue +=5000
        if coinscollected == self.maxCoins:
            fitvalue -= 1000
            if (Cx, Cy) == self.target:
                fitvalue -= 1000
        return fitvalue


    def mutate(self,state):
        # print("Mutating")
        if random.uniform(0, 1) >= 0.1:
            return state         
        else:
            n = len(state)
            g = len(self.directions)
            c = random.randrange(0, n)
            r = random.randrange(0, g)

            new_gene = self.directions[r]
            return state[:c] + [new_gene] + state[c+1:]
        

    def select(self,k,fitness_fn):
        # print("Selecting")
        selected = random.choices(self.population, k=k) 
        selected = sorted(selected, key=fitness_fn, reverse=True)  
        return selected[:2]  
        
        
    def recombine(self,x, y):
        # print("Recombining")
        n = len(x)
        c = random.randrange(0, n)
        return x[:c] + y[c:]

    def convert_state_to_path(self,state):
        path = [(0, 0)]
        print("PRINTINGG PATHH EDITING AAAAAAAAAAAAAAAAAA")
        for X, Y in state:
            print(path[-1])
            Cx, Cy = path[-1]
            path += [(Cx + X, Cy + Y)]
        return path
            
