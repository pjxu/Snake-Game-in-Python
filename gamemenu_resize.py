#Jason Xu of Connecticut College 2017
#for CS 110 Final Project
#this is a game menu intended for snake game

from graphics import *
from button import *

class GameMenu:
    def __init__(self, win):
        self.win = win

        #the introduction window
        self.title = Text(Point(50,60),'''
Welcome to my Snake Game!
Use arrow keys to change moving direction.
Hit space key to pause.
Hit ESC key to quit the game.''')
        self.intro = Text(Point(50,40),'''
You start with a head at the middle.
When you eat a fruit, you grow longer.
Try not to hit the border or yourself!\nHave fun!''')
        self.title.setFace('helvetica')
        self.intro.setFace('helvetica')
        self.title.setFill('blue4')
        self.intro.setFill('green4')
        self.title.setSize(20)
        self.intro.setSize(20)
        
        self.lv1button = Button(self.win, Point(25,20),15,8,'Easy')
        self.lv2button = Button(self.win, Point(50,20),15,8,'Medium')
        self.lv3button = Button(self.win, Point(75,20),15,8,'Hard')

    #display the menu
    def display(self):
        self.title.draw(self.win)
        self.intro.draw(self.win)
        self.lv1button.display()
        self.lv2button.display()
        self.lv3button.display()

    #undraw the menu
    def remove(self):
        self.title.undraw()
        self.intro.undraw()
        self.lv1button.remove()
        self.lv2button.remove()
        self.lv3button.remove()
