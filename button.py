#Jason Xu of Connecticut College 2017
#partial source code from Professor James Lee of CC CS Department
#this is a button class that allows you to create and use a button

from graphics import *

class Button:
    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        self.win = win
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.label = Text(center, label)
        self.label.setFace('helvetica')
        self.label.setStyle('bold')
        self.label.setFill('blue')
        self.active = True

    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        if self.active:
            if self.xmin <= p.getX() <= self.xmax:
                if self.ymin <= p.getY() <= self.ymax:
                    return True

    #undraw the button
    def remove(self):
        self.rect.undraw()
        self.label.undraw()

    #display the button
    def display(self):
        self.rect.draw(self.win)
        self.label.draw(self.win)
