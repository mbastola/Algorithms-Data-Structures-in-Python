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
        self.myList = []
        mystr = ''
        while dimString != '':
            dimString = mazeFile.readline()
            self.myList.append(dimString)
            mystr = mystr + dimString
            
        for item in self.myList:
            for each in item:
                if self.isStart(each):
                    self.startLocation = (self.myList.index(item), item.index(each))
                if self.isGoal(each):
                    self.goalLocation = (self.myList.index(item), item.index(each))
    
        
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
        return self.startLocation

    def getGoalLocation(self):
        """Returns the goal location of the maze as a tuple (r, c)"""
        return self.goalLocation 

    def getSquare(self, row, col):
        """Returns a character representing the type of square at the given position"""
        return self.myList[row][col]
        
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
        return self.mystr

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
