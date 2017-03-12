from maze import *
from graphics import *

class MazeGUI:
    '''A class that facilitates the graphical display of a maze and the process of solving the maze.'''
    def __init__(self):
        '''Sets up a graphical window to eventually display the maze.'''
        # Set up graphical window
        self.__mazeWin = GraphWin("Maze", 500, 500)

        # 2D list for rectangles representing the maze
        self.__squares = []

        self.__startLoc = (0, 0)
        self.__goalLoc = (0, 0)

        self.__agendaCount = 0

    def setMaze(self, maze):
        '''Displays the given maze in the window.'''
        self.__agendaCount = 0
        self.__mazeWin.setCoords(0,  maze.getNumRows(), maze.getNumColumns(), 0)

        # Create rectangles and color according to what the location holds
        for row in range(maze.getNumRows()):
            self.__squares.append([])
            for col in range(maze.getNumColumns()):
                self.__squares[row].append(Rectangle(Point(col, row), Point(col+1, row+1)))
                self.__squares[row][col].setOutline('Black')
                if maze.isWall(maze.getSquare(row, col)):
                    self.__squares[row][col].setFill('Black')
                elif maze.isStart(maze.getSquare(row, col)):
                    self.__startLoc = (row, col)
                    self.__squares[row][col].setFill('Green')
                elif maze.isGoal(maze.getSquare(row, col)):
                    self.__goalLoc = (row, col)
                    self.__squares[row][col].setFill('Red')
                self.__squares[row][col].draw(self.__mazeWin)

    def addLocToAgenda(self, row, col):
        '''Changes the color of a square that has been added to the agenda to light grey.'''
        self.__colorSquare(row, col, 'grey75')
        t = Text(Point(col + .5, row + .5), str(self.__agendaCount))
        t.setSize(30)
        t.draw(self.__mazeWin)
        self.__agendaCount += 1

    def visitLoc(self, row, col):
        '''Changes the color of a square that has been visited to dark grey.'''
        self.__colorSquare(row, col, 'grey50')

    def addLocToPath(self, row, col):
        '''Changes the color of a square that has been added to the solution path to gold.'''
        self.__colorSquare(row, col, 'gold')

    def __colorSquare(self, row, col, color):
        '''A private method that changes the color of a given square to the given color.'''
        if (row, col) != self.__startLoc and (row, col) != self.__goalLoc:
            self.__squares[row][col].setFill(color)
            self.__mazeWin.update()

    def wait(self):
        '''Pauses execution until the user clicks inside the window.'''
        self.__mazeWin.getMouse()

class NullMazeGUI(MazeGUI):
    """A subclass of MazeGUI that has no display whatsoever. All of its functions return without doing anything. Useful if you want the result as fast as possible, without having to watch the process."""
    def __init__(self):
        return

    def setMaze(self, maze):
        return

    def addLocToAgenda(self, row, col):
        return

    def addLocToPath(self, row, col):
        return

    def visitLoc(self, row, col):
        return

    def wait(self):
        return
