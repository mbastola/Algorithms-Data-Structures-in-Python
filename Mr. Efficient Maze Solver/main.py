from mazesolver import *
from maze import *
from agenda import *
from mazegui import *
import sys

def main():
    """Drives the process of solving a maze. Takes command line parameters for the maze file and the type of agenda to be used."""
    filename = sys.argv[1]
    agendaType = sys.argv[2]

    maze = Maze(filename)

    #Make the right agenda
    if agendaType == 's':
        agenda = StackAgenda()
    elif agendaType == 'q':
        agenda = QueueAgenda()
    elif agendaType == 'p':
        Eval = ManhattanDistanceEvaluator(maze.getGoalLocation())
        agenda = PriorityQueueAgenda(Eval)
    elif agendaType == 'a':
        Eval = ManhattanDistanceEvaluator(maze.getGoalLocation())
        agenda = AStarAgenda(Eval)

    solver = MazeSolver()
    gui = MazeGUI()
    print(solver.solveMaze(maze, agenda, gui))
    gui.wait()

main()
