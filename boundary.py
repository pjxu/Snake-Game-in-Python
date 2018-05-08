#Jason Xu CC 2017
#snake game's boundary
#CS 110 Final Project

from graphics import *

'''this class has several parameters
   refX: the left X coord of the rect
   refY: the left Y coord of the rect
   endX: the right X coord
   endY: the right Y coord'''

class Boundary:
    def __init__(self, win, refX, refY, endX, endY):
        self.win = win
        
        self.x = refX
        self.y = refY

        self.endX = endX
        self.endY = endY

        self.refPoint = Point(self.x, self.y)
        self.endPoint = Point(self.endX, self.endY)

        self.rect = Rectangle(self.refPoint, self.endPoint)
        self.rect.setFill('blue')
        self.rect.setWidth(0)

    def display(self):
        self.rect.draw(self.win)

    def remove(self):
        self.rect.undraw()

'''def main():
    win = GraphWin('Boundary', 600, 600)
    win.setCoords(0,0,100,100)
    
    boundaryD = Boundary(win, 0, 0, 100, 5)
    boundaryL = Boundary(win, 0, 0, 5, 100)
    boundaryU = Boundary(win, 0, 95, 100, 100)
    boundaryR = Boundary(win, 95, 0, 100, 100)

    boundaryL.display()
    boundaryD.display()
    boundaryU.display()
    boundaryR.display()

main()'''
