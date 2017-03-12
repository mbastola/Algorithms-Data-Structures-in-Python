##Manil Bastola

from agenda import *
from maze import *
from mazegui import *

class Mazesolver:
    def __init__(self, agenda):
        '''initailizes the class'''
        self.agenda = agenda

    def solveMaze(self, maze, mazeGUI):
        '''solves the maze'''
        mazeGUI.setMaze(maze)
        self.agenda.clear()
        self.agenda.addItem(maze.getStartLocation())
        itemsAdded= [maze.getStartLocation()]
        path = {}
        traceList = []
        while not self.agenda.isEmpty():
            loc = self.agenda.getItem()
            mazeGUI.wait()
            mazeGUI.visitLoc(loc[0], loc[1])
            if loc == maze.getGoalLocation():
                traceList.append(loc)
                while loc != maze.getStartLocation():
                    traceList.append(path[loc])
                    mazeGUI.addLocToPath(path[loc][0], path[loc][1])
                    
                    loc = path[loc]
                traceList.reverse()
                print(itemsAdded)
                return traceList
                    
            else:
                for i in [-1,1]:
                    if -1 < loc[0]+ i < maze.getNumRows():
                        if not maze.isWall(maze.getSquare(loc[0]+i,loc[1])) and (loc[0]+i,loc[1]) not in itemsAdded:
                            self.agenda.addItem((loc[0]+i,loc[1]))
                            mazeGUI.addLocToAgenda(loc[0], loc[1])
                            itemsAdded.append((loc[0]+i,loc[1]))
                            path[(loc[0]+i,loc[1])] = loc
                    if -1 < loc[1]+ i < maze.getNumColumns():      
                        if not maze.isWall(maze.getSquare(loc[0],loc[1]+i)) and (loc[0],loc[1]+i) not in itemsAdded:
                            self.agenda.addItem((loc[0],loc[1]+i))
                            mazeGUI.addLocToAgenda(loc[0], loc[1])
                            itemsAdded.append((loc[0],loc[1]+i))
                            path[(loc[0],loc[1]+i)]= loc

############################################################################################

    


            

    


        

                            

                

            
    
                
                    
                    
                
            
        
        
