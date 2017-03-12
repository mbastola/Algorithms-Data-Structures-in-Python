#Manil Bastola
#hw 6

def generateMaze(size):
    myMaze = open('maze'+str(size*size),'w')
    
    myMaze.write(str(size)+' '+str(size)+'\n')
    myMaze.write('*#'+'.'*(size-2)+'\n')
    myMaze.write('#' + '.'*(size-1)+'\n')
    myMaze.write('.'*(size-1)+'o'+'\n')
    for i in range(size-3):
        myMaze.write('.'*size+'\n')
    

def main():
    for i in range(10,101,10):
        generateMaze(i)
main()


