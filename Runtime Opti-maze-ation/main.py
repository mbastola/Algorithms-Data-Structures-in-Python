import time
from maze import *
from mazesolver import *
from agenda import *
from mazegui import *

def main():
    """Times the solveMaze method of MazeSolver with mazes of various sizes"""
    agenda = StackAgenda()
    solver = MazeSolver(agenda)
    #NullMazeGUI does not display any graphics, so it won't interfere
    #with timing
    gui = NullMazeGUI()
    #Go from 10x10 up to 100x100
    for i in range(10, 101, 10):
        #Maze files should be named maze100, maze400, maze900, ..., maze10000
        filename = "maze"+str(i*i)
        maze = Maze(filename)
        before = time.time()
        solver.solveMaze(maze, gui)
        after = time.time()
        print(str(i*i) + "\t" + str(after - before))

main()
