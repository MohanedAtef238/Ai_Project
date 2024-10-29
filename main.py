from BFSAgent import BFSAgent
from DFSAgent import DFSAgent
from GBFSAgent import GBFSAgent
from UCSAgent import UCSAgent
from IDSAgent import IDSAgent
from AStarAgent import AStarAgent
from maze import Maze
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
print(f"Elapsed time: {ETime-STime:.4f} seconds")
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
print(f"Elapsed time: {ETime-STime:.4f} seconds")
print(f"DFS")



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



tracemalloc.start()
GBFS = GBFSAgent(maze)
path4 = GBFS.GBFS()
maze.PrintPath(path4)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time a greedy: {ETime-STime:.4f} seconds")
print(f"Greedy")


tracemalloc.start()
AStar = AStarAgent(maze)
path5 = AStar.AStar()
maze.PrintPath(path5)
current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
ETime = time.perf_counter()
print(f"Elapsed time a star: {ETime-STime:.4f} seconds")
print(f"A star")