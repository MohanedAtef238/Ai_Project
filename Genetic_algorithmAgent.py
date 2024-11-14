import random
from tiles import Tiles 
from SmartAlgo import SmartAlgo

class GeneticAlgorithmAgent(SmartAlgo):
    
    
    def genetic_algorithm(self, fitness_fn, f_thres=700, ngen=1000):
       
        for i in range(ngen):
          
            self.population = [
                self.mutate(self.recombine(*self.select(2, self.population, fitness_fn)))
                for _ in range(len(self.population))
            ]

           
            fittest_individual = min(self.population, key=fitness_fn)
            if fitness_fn(fittest_individual) == f_thres:
                return 1,fittest_individual

            
        
        return min(self.population, key=fitness_fn)

    
    def init_population(self):
        g =4
        self.population = []
        for i in range(100):
            new_individual = [self.directions[random.randrange(0, g)] for j in range(1000)]
            self.population.append(new_individual)

        return self.population



    def fitness(self, state):
        current = self.start
        fitvalue = 0
        coinscollected = 0

        for dx, dy in state:
            current[0], current[1] = current[0] + dx, current[1] + dy
            if not self.maze.IsValidPos(current[0], current[1]):
                return float("inf")  
            
            fitvalue += 1  
            
        
            if self.maze.maze[current[1]][current[0]] == Tiles.Coin:
                coinscollected += 1
                fitvalue -= 50 
            
        
            if self.maze.maze[current[1]][current[0]] == Tiles.Slime:
                fitvalue += 30  
            
            
            if (current[0], current[1]) == self.target:
                fitvalue -= 100  
        
    
        if coinscollected == self.maxCoins:
            fitvalue -= 150 
        
        return fitvalue


    def mutate(self,state):
        if random.uniform(0, 1) >= 0.2:
            return state         
        else:
            n = len(state)
            g = len(self.directions)
            c = random.randrange(0, n)
            r = random.randrange(0, g)

            new_gene = self.directions[r]
            return state[:c] + [new_gene] + state[c+1:]
        

    def select(self,k,fitness_fn):
        
        selected = random.choices(self.population, k=k) 
        selected = sorted(selected, key=fitness_fn, reverse=True)  
        return selected[:2]  
        
        
    def recombine(self,x, y):
        n = len(x)
        c = random.randrange(0, n)
        return x[:c] + y[c:]


