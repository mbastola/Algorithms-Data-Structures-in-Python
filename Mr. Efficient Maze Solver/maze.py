##################
## Manil Bastola
##################
from graph import *

class Maze:
    """A class that represents a maze"""
    def __init__(self, mazeFilename):
        """Creates the Maze object from the given text file"""
        #Store the filename
        self.__filename = mazeFilename

        #Open the file
        mazeFile = open(self.__filename)

        #Read and store the dimensions of the maze
        dimString = mazeFile.readline()
        dimList = dimString.split()
        self.__numColumns = int(dimList[0])
        self.__numRows = int(dimList[1])

        #Go through the maze and store the layout as a list of strings
        #Also store the location of the start and the goal
        self.__mazeLayout = []
        for row in range(self.__numRows):
            rowString = mazeFile.readline()
            self.__mazeLayout.append(rowString)
            for col in range(self.__numColumns):
                if self.isStart(rowString[col]):
                    self.__startLoc = (row, col)
                elif self.isGoal(rowString[col]):
                    self.__goalLoc = (row, col)

        #Close the file
        mazeFile.close()     

    def getNumColumns(self):
        """Returns the number of columns in the maze"""
        return self.__numColumns

    def getNumRows(self):
        """Returns the number of rows in the maze"""
        return self.__numRows

    def getStartLocation(self):
        """Returns the start location of the maze as a tuple (r, c)"""
        return self.__startLoc

    def getGoalLocation(self):
        """Returns the goal location of the maze as a tuple (r, c)"""
        return self.__goalLoc

    def getSquare(self, row, col):
        """Returns a character representing the type of square at the given position"""
        return self.__mazeLayout[row][col]
        
    def isWall(self, square):
        """Checks if the given character corresponds to a wall"""
        return square == '#'

    def isOpen(self, square):
        """Checks if the given character corresponds to open space"""
        return square == '.'

    def isStart(self, square):
        """Checks if the given character corresponds to the start"""
        return square == 'o'

    def isGoal(self, square):
        """Checks if the given character corresponds to the goal"""
        return square == '*'

    def __str__(self):
        """Returns a string representation of the maze"""
        mazeStr = ''
        for r in range(len(self.__mazeLayout)):
            mazeStr += self.__mazeLayout[r]
        return mazeStr

    def createGraph(self):
        myGraph = Graph()
        for i in range(self.getNumRows()):
            for j in range(self.getNumColumns()):
                if not self.isWall(self.getSquare(i,j)):
                    myGraph.addVertex((i,j))
                    toCheck = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                    for locToCheck in toCheck:
                        row = locToCheck[0]
                        col = locToCheck[1]
                        #---Neighbor check---
                        #If the neighbor is inside the maze
                        if row >= 0 and row < self.getNumRows() and col >= 0 and col < self.getNumColumns() and not self.isWall(self.getSquare(row,col)):
                            myGraph.addEdge((i,j),locToCheck)
        return myGraph

class NumberMaze(Maze):
    """A subclass of Maze that works with a file-format in which the types of squares in the maze are written as numbers"""
    def __init__(self, filename):
        super().__init__(filename)

    def isWall(self, square):
        """Checks if the given character corresponds to a wall"""
        return square == '1'

    def isOpen(self, square):
        """Checks if the given character corresponds to open space"""
        return square == '0'

    def isStart(self, square):
        """Checks if the given character corresponds to the start"""
        return square == '2'

    def isGoal(self, square):
        """Checks if the given character corresponds to the goal"""
        return square == '3'
