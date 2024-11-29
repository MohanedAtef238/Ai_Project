from BFSAgent import BFSAgent
from DFSAgent import DFSAgent
from GBFSAgent import GBFSAgent
from UCSAgent import UCSAgent
from IDSAgent import IDSAgent
from AStarAgent import AStarAgent
from HillClimbing import HillClimbingAgent
from maze import Maze
from SimulatedAnnealing import SimulatedAnnealing
from Genetic_algorithmAgent import GeneticAlgorithmAgent
import tracemalloc
import time

maze = Maze()
maze.PutCoins()
maze.PutSlime()
maze.PrintMaze()

print("")

STime = time.perf_counter()
tracemalloc.start()
bfs = BFSAgent(maze)
path1 = bfs.bfs()
maze.PrintPath(path1)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time BFS: {ETime-STime:.4f} seconds")
print(f"BFS")

tracemalloc.start()
STime = time.perf_counter()
dfs = DFSAgent(maze)
path2 = dfs.dfs()
maze.PrintPath(path2)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time DFS: {ETime-STime:.4f} seconds")
print(f"DFS")



STime = time.perf_counter()
tracemalloc.start()
UCS = UCSAgent(maze)
path3= UCS.UCS()
maze.PrintPath(path3)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed timee for ucs : {ETime-STime:.4f} seconds")
print(f"UCS")

STime = time.perf_counter()
tracemalloc.start()
AStar = AStarAgent(maze)
path5 = AStar.AStar()
maze.PrintPath(path5)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time A-star: {ETime-STime:.4f} seconds")
print(f"A star")

STime = time.perf_counter()
tracemalloc.start()
GBFS = GBFSAgent(maze)
path4 = GBFS.GBFS()
maze.PrintPath(path4)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time for greedy: {ETime-STime:.4f} seconds")
print(f"Greedy")


STime = time.perf_counter()
tracemalloc.start()
STime = time.perf_counter()
HillClimbing = HillClimbingAgent(maze)
result = HillClimbing.hill_climbing()
x,y = result
maze.PrintPath(result)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time for Hill Climbing: {ETime-STime:.4f} seconds")
print(f"Hill Climbing")

STime = time.perf_counter()
tracemalloc.start()
STime = time.perf_counter()
ids = IDSAgent(maze)
result = ids.IDS()
maze.PrintPath(result)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time for IDS: {ETime-STime:.4f} seconds")
print(f"IDS")


print("")

STime = time.perf_counter()
tracemalloc.start()
STime = time.perf_counter()
sa = SimulatedAnnealing(maze)
schedule = lambda t: max(0.01, min(1, 1 - 0.001 * t))
result = sa.simulated_annealing(schedule)
maze.PrintPath(result)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time for Simulated Annealing: {ETime-STime:.4f} seconds")
print(f"Simulated Annealing")

STime = time.perf_counter()
tracemalloc.start()
GA = GeneticAlgorithmAgent(maze)
x, Thresh = path3
#uses UCS path cost 
path5 = GA.genetic_algorithm(GA.fitness, maze.PathCost(Thresh)+300 )
maze.PrintPath(path5)
for I in path5:
    print(I)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time for GA: {ETime-STime:.4f} seconds")
print(f"Genetic Algorithm")