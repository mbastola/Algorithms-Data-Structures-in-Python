from agenda import *
from maze import *
from mazesolver import *
import sys

def main():
    myMazegui=MazeGUI()
    maze=NumberMaze(sys.argv[1])
    if sys.argv[2] == 's':
        agenda=StackAgenda()
    elif sys.argv[2] == 'q':
        agenda=QueueAgenda()
    else:
        return 'None'
    solve=Mazesolver(agenda)
    print(solve.solveMaze(maze,myMazegui))
    myMazegui.wait()

main()
