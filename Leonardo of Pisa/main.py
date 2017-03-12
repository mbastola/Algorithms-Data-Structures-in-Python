from graphics import *

def sierpinskiSquare(point1, point2, level, window):
    if level == 0:
        square = Rectangle(point1, point2)
        square.draw(window)
    else:
        third = getThird(point1, point2)
        sierpinskiSquare(Point( point2.getX()-third[0], point2.getY()+third[0]), point2 , level - 1, window)
        sierpinskiSquare(Point(point2.getX()-2*third[0],point2.getY()+third[0]), Point(point2.getX()-third[0],point2.getY()) , level - 1, window)
        sierpinskiSquare(Point(point1.getX(),point1.getY()-2*third[1]), Point(point2.getX()-2*third[0],point2.getY()) , level - 1, window)
        sierpinskiSquare(Point(point1.getX(),point1.getY()-third[1]), Point(point2.getX()-2*third[0],point2.getY()+third[0]), level - 1, window)
        sierpinskiSquare(point1,Point(point1.getX()+third[0], point1.getY()-third[0]), level - 1, window)
        sierpinskiSquare(Point(point1.getX()+third[0],point1.getY()),Point(point1.getX()+2*third[0], point1.getY()-third[1]),level - 1, window)
        sierpinskiSquare(Point(point1.getX()+2*third[0],point1.getY()), Point(point2.getX(),point2.getY()+2*third[1]), level - 1, window)
        sierpinskiSquare(Point(point1.getX()+2*third[0], point1.getY()-third[1]), Point(point2.getX(),point2.getY()+third[1]), level - 1, window)
                         
        
def getThird(point1, point2):
    thirdX = (point1.getX() - point2.getX())/3
    thirdY = (point1.getY() - point2.getY())/3
    return (abs(thirdX), abs(thirdY))

def main():
    window = GraphWin('Sierpinski Square', 500, 500)
    window.setCoords(0, 0, 1, 1)
    sierpinskiSquare(Point(0, .9),Point(.9, 0), 5, window)
    window.getMouse()

main()


