#Jason Xu
#drawing CC logo
#CS 110 Final Project

from graphics import *

class CClogo:

    def __init__(self, win):
        self.win = win

        self.circ1 = Circle(Point(47, 45), 30)
        self.circ1.setFill('yellow4')
        self.circ1.setWidth(0)

        self.circ2 = Circle(Point(57, 45), 30)
        self.circ2.setFill('brown')
        self.circ2.setWidth(0)

        self.circ3 = Circle(Point(77, 45), 30)
        self.circ3.setFill('yellow4')
        self.circ3.setWidth(0)

        self.circ4 = Circle(Point(87, 45), 30)
        self.circ4.setFill('brown')
        self.circ4.setWidth(0)

    def display(self):
        self.circ1.draw(self.win)
        self.circ2.draw(self.win)
        self.circ3.draw(self.win)
        self.circ4.draw(self.win)

    def remove(self):
        self.circ2.undraw()
        self.circ1.undraw()
        self.circ3.undraw()
        self.circ4.undraw()
        
def main():
    win = GraphWin('CCLogo', 600, 600)
    win.setCoords(0,0,100,100)
    win.setBackground('brown')

    cclogo = CClogo(win)
    cclogo.display()

if __name__ == '__main__':
    main()
    

    
