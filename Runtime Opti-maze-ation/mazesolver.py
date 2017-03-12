from agenda import *
from maze import *
from mazegui import *

class MazeSolver:
    """A class that solves mazes"""
    def __init__(self, agenda):
        """Creates the MazeSolver and stores the Agenda"""
        self.__agenda = agenda

    def solveMaze(self, maze, gui):
        """Solves the given maze, displaying the process on the given MazeGUI"""
        #---Setup---

        #Stores tuples representing the locations that 
        #have been added to the agenda
        added = []
        for i in range(maze.getNumRows()):
            added.append([0]*maze.getNumColumns())
            
        
        #Key: tuple representing a location
        #Value: tuple representing the location that added the key 
        #       location to the agenda
        fromWhere = {}

        #Clear the agenda, in case solveMaze was called before
        self.__agenda.clear()

        #Set the maze for the gui
        gui.setMaze(maze)

        #Add the start location to the agenda
        start = maze.getStartLocation()
        self.__agenda.addItem(start)
        added[start[0]][start[1]] = 1
        gui.addLocToAgenda(start[0], start[1])

        #---Main loop---
        while not self.__agenda.isEmpty():
            loc = self.__agenda.getItem()

            gui.wait()
            gui.visitLoc(loc[0], loc[1])

            #---Goal check---
            #If the location is the goal, generate the path and return
            if maze.isGoal(maze.getSquare(loc[0], loc[1])):
                #---Make path---
                path = []
                #Work backwards to the start location
                while loc != start:
                    path.insert(0, loc)
                    gui.addLocToPath(loc[0], loc[1])
                    loc = fromWhere[loc]
                path.insert(0, start)
                gui.addLocToPath(start[0], start[1])
                return path
            #Otherwise, it is reachable empty space
            else:
                #---Neighbor loop---
                #Generate a list of candidate neighbors
                toCheck = [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]
                for locToCheck in toCheck:
                    r = locToCheck[0]
                    c = locToCheck[1]
                    #---Neighbor check---
                    #If the neighbor is inside the maze
                    if r >= 0 and r < maze.getNumRows() and c >= 0 and c < maze.getNumColumns():
                        #If it has not yet been added
                        if added[r][c] != 1:
                            #If it is not a wall
                            if not maze.isWall(maze.getSquare(r, c)):
                                #Add the neighbor to the agenda
                                self.__agenda.addItem((r, c))
                                added[r][c] =1
                                fromWhere[(r, c)] = loc
                                gui.addLocToAgenda(r, c)
        #If we are here, the maze is unsolvable
        return []
