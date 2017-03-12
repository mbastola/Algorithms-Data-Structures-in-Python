##Manil Bastola

class Maze:
    def __init__(self, myMaze):
        '''initializes the class Maze'''
        self.myMaze = open(myMaze, 'r')
        '''opens the txt file for reading'''
        self.myList = []
        self.mystr = ''
        self.line = self.myMaze.readline()
        self.column = int(self.line.split()[0])
        self.rows = int(self.line.split()[1])
        while self.line != '':
            self.myList.append(self.line[:-1])
            self.line = self.myMaze.readline()
            self.mystr = self.mystr + self.line
        for item in self.myList[1:]:
            for each in item:
                if self.isStart(each):
                    self.startLocation = (self.myList[1:].index(item), item.index(each))
                if self.isGoal(each):
                    self.goalLocation = (self.myList[1:].index(item), item.index(each))

        self.myMaze.close()
        
    def getNumColumns(self):
        '''gives number of column in the maze'''
        return self.column

    def getNumRows(self):
        '''gives number of rows in the maze'''
        return self.rows

    def getStartLocation(self):
        '''gets start location from the maze'''
        return self.startLocation

    def getGoalLocation(self):
        '''gets target location from the maze'''
        return self.goalLocation

    def getSquare(self, row, col):
        '''gets the character at a given location from the maze'''
        return self.myList[1:][row][col]

    def isWall(self, square):
        '''checks wether the character is a wall'''
        return square == '#'

    def isOpen(self,square):
        '''checks wether the character is open'''
        return square == '.'

    def isStart(self,square):
        '''checks wether the character is starting point'''
        return square == 'o'

    def isGoal(self,square):
        '''checks wether the character is target point'''
        return square == '*'
        
    def __str__(self):
        '''prints the maze'''
        return self.mystr

    

class NumberMaze(Maze):
    def __init__(self, myMaze):
        '''initializes the subclass NumberMaze'''
        super().__init__(myMaze)

    def isWall(self, square):
        '''overrides the isWall method of its superclass and checks wether the character is a wall'''
        return square == '1'

    def isOpen(self,square):
        '''overrides the isOpen method of its superclass and checks wether the character is open'''
        return square == '0'

    def isStart(self,square):
        '''overrides the isStart method of its superclass and checks wether the character is starting point'''
        return square == '2'

    def isGoal(self,square):
        '''overrides the isStart method of its superclass and checks wether the character is goal'''
        return square == '3'

    

        

            
            
        
    

    
        
        
        
        
        
        

    

    
        
        
        
        
        
        
