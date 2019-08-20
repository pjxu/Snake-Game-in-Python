#Jason Xu CONNCOLL 2017
#Last modified on June 12th, 2016
#this version has been modified after the final ended
#Intended to add an enemy snake to it

#CS 110 Final Project

#This is the classic snake game remake.

#date 8-1-2019 Fix Wrong Line Order on Github

#There are three levels of difficulties with increasing speed, and in the hard level the fruit will move.
#the game is designed such that once the player enters the actual game, it cannot
#choose a different level unless the snake dies. However, the player can choose to pause the game.
#there is no display of the score until the snake dies and on the main menu the highest score will be shown.
#the snake will gradually fade in color.

from graphics import *
from time import *
from random import *
from audioplayer import *
from button import *
from gamemenu_resize import *
from boundary import *
from cclogo import *

'''
speed: determine the speed of the snake
hard: determine if the game is in hard mode'''

class SnakeGame:
    def __init__(self, win, speed, hard):
        #set a variable to see if the game is in hard mode
        
        self.hardmode = hard
        
        #play the bgm
        if self.hardmode == False:
            startSound("bgm.wav", async=True, loop=True)
        else:
            startSound("bgm2.wav", async=True, loop=True)
        
        #self.win = GraphWin('SnakeGame', 600, 600)

        self.win = win

        self.boundaryD = Boundary(self.win, 0, -1, 100, 5)
        self.boundaryL = Boundary(self.win, 0, 0, 5, 90)
        self.boundaryU = Boundary(self.win, 0, 85, 101, 90)
        self.boundaryR = Boundary(self.win, 96, 0, 101, 90)

        self.cclogo = CClogo(self.win)

        self.cclogo.display()

        self.boundaryL.display()
        self.boundaryU.display()
        self.boundaryR.display()
        self.boundaryD.display()

        
        self.running = True

        #set a variable to see if the key is pressed
        self.keypressed = False

        #set a variable to see if game is in the pausemenu
        self.allowkey = True

        #set a variable to store the direction of the moving snake, 0 = still, 4 = up, 1 = right, 2 = down, 3 = left
        self.direction = 0

        #set a variable to see if we allow an object to move
        self.allowmove = True

        #set a variable to see if drawing is allowed
        self.allowdraw = True

        #set a variable to see if the object is still, not used
        self.isStill = True

        #pass a variable to see if enemy snake almost hits its tail
        self.eAlmostHit = False

        #keybinding
        self.win.bind('<Left>', self.leftKey)
        self.win.bind('<Right>', self.rightKey)
        self.win.bind('<Escape>', self.escKey)
        self.win.bind('<Up>', self.upKey)
        self.win.bind('<Down>', self.downKey)
        self.win.bind('<space>', self.spaceKey)
        self.win.focus_set()

        #draw the head
        #now since there is an enemy snake, to be fair, we place our snake at the bottom right
        #and place the enemy snake at the top left
        
        self.rect = Rectangle(Point(90, 10), Point(92,12))

        #now draw the enemy snake
        self.ehead = Rectangle(Point(10, 80), Point(12, 82))
        self.ehead.setWidth(0)

        self.rect.draw(self.win)
        self.rect.setFill("black")

        self.ehead.draw(self.win)
        self.ehead.setFill('white')

        #create a list to store cubes of the tail
        self.cubelist = []
        #create another list to store cubes of the enemy tail
        self.ecubelist = []

        '''#create a list to store cubes in narrow phase in collision detection
        self.narrowList = []'''

        #set a variable to check if there is a tail

        self.hasTail = False
        self.ehasTail = False

        if len(self.cubelist) > 0:
            self.hasTail = True

        if len(self.ecubelist) > 0:
            self.ehasTail = True 

        #set the movement of the fruit at hard level
        self.fruitdx = randrange(-1,1)
        self.fruitdy = randrange(-1,1)

        while self.fruitdx == 0 or self.fruitdy == 0:
            self.fruitdx = randrange(-1,1)
            self.fruitdy = randrange(-1,1)

        #the change of speed occurs here!
        self.speed = speed
        self.tempspeed = speed

        #draw the fruit
        self.fruit()

        #moving direction
        self.dx = 0
        self.dy = 0

        #moving direction of the enemy snake
        self.edx = 0
        self.edy = 0

        #set the initial score
        self.score = 0

        #draw the statusbar
        self.statusbar()

        #the best score
        self.bestscore = 0
        self.win.after(0, self.run)
        self.win.mainloop()

    #key binding    
    def leftKey(self, event):
        #print ("Left key pressed")
        #check if keys are allowed to press
        if self.allowkey == True:
            #check if the opposite direction is allowed to press and if there is a tail
            if self.direction != 1 and self.hasTail == True:
                self.dx = -self.speed
                self.dy = 0
                self.keypressed = True
                self.direction = 3

            #at the starting condition when there is no tail, the head can move freely
            if self.hasTail == False:
                self.dx = -self.speed
                self.dy = 0
                self.keypressed = True
                self.direction = 3

    #key binding
    def rightKey(self, event):
        #print ("Right key pressed")
        if self.allowkey == True:
            if self.direction != 3 and self.hasTail == True:
                self.dx = self.speed
                self.dy = 0
                self.keypressed = True
                self.direction = 1
            if self.hasTail == False:
                self.dx = self.speed
                self.dy = 0
                self.keypressed = True
                self.direction = 1
    #key binding    
    def upKey(self, event):
        #print ("Up key pressed")
        if self.allowkey == True:
            if self.direction != 2 and self.hasTail == True:
                self.dx = 0
                self.dy = self.speed
                self.keypressed = True
                self.direction = 4

            if self.hasTail == False:
                self.dx = 0
                self.dy = self.speed
                self.keypressed = True
                self.direction = 4
    #key binding
    def downKey(self, event):
        #print ("Down key pressed")
        if self.allowkey == True:
            if self.direction != 4 and self.hasTail == True:
                self.dx = 0
                self.dy = -self.speed
                self.keypressed = True
                self.direction = 2
                
            if self.hasTail == False:
                self.dx = 0
                self.dy = -self.speed
                self.keypressed = True
                self.direction = 2

    #key binding
    def escKey(self, event):
        print ("esc key pressed")
        self.running = False
        
        stopSound()
        self.win.close()
        self.win.master.quit()

    def spaceKey(self, event):
        if self.allowkey == True:
            try:
                self.allowmove = False
                self.allowkey = False
                #stop the snake
                if self.keypressed == True:
                    if self.isStill == True:
                        self.dx = self.dy = 0
                        self.allowkey = False
                #the following portion is to draw the continue button on appropriate situation
                if self.allowdraw == True:
                    self.contibutton = Button(self.win, Point(50,50), 20, 8, 'Continue')
                    self.contibutton.display()
                while True:
                    pt = self.win.getMouse()
                    #check if the player clicked the continue button
                    if self.contibutton.clicked(pt):
                        self.allowmove = True
                        self.speed = self.tempspeed
                        if self.direction == 1:
                            self.dx = self.speed
                        elif self.direction == 2:
                            self.dy = -self.speed
                        elif self.direction == 3:
                            self.dx = -self.speed
                        elif self.direction == 4:
                            self.dy = self.speed
                        else:
                            self.dx = self.dy = 0

                        self.contibutton.remove()
                        self.allowkey = True
                        break

            except (GraphicsError):
                stopSound()
                return

    #the following method is not fully used, reserved for fun
    def initfruit(self, size):
        ''' this method is reserved for future use when I want to change the size of the fruit'''
        #draw the perimeters of the fruit
        self.fruitposXleft = self.fruitx - size 
        self.fruitposXright = self.fruitx + size 
        self.fruitposYup = self.fruity + size 
        self.fruitposYdown = self.fruity - size 
        self.fruitpt = Point(self.fruitx, self.fruity)
        self.circle = Circle(self.fruitpt, size)

    #the fruit
    def fruit(self):
        '''this method creates the fruit randomly on screen'''
        try:
            self.fruitx = randrange(6,84)
            self.fruity = randrange(6,84)

            #check if the randomly generated position is on the snake
            for cube in self.cubelist:
                while self.fruitx - 1 == cube.getCenter().getX() + 1 and self.fruity == cube.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

                while self.fruitx + 1 == cube.getCenter().getX() - 1 and self.fruity == cube.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

                while self.fruitx == cube.getCenter().getX() and self.fruity - 1 == cube.getCenter().getY() + 1:
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

                while self.fruitx == cube.getCenter().getX() and self.fruity + 1 == cube.getCenter().getY() - 1:
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

            #check if the randomly generated position is on the enemy snake
            for cube in self.ecubelist:
                while self.fruitx - 1 == cube.getCenter().getX() + 1 and self.fruity == cube.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

                while self.fruitx + 1 == cube.getCenter().getX() - 1 and self.fruity == cube.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

                while self.fruitx == cube.getCenter().getX() and self.fruity - 1 == cube.getCenter().getY() + 1:
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

                while self.fruitx == cube.getCenter().getX() and self.fruity + 1 == cube.getCenter().getY() - 1:
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

            #check if the randomly generated position is on the head
            if self.fruitx == self.rect.getCenter().getX():
                if self.fruity == self.rect.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)
            if self.fruitx == self.ehead.getCenter().getX():
                if self.fruity == self.ehead.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

            #in the hard mode, the fruit does not appear on the axises where the head is on
            if self.hardmode == True:
                if self.fruitx == self.rect.getCenter().getX() or self.fruity == self.rect.getCenter().getY():
                    self.fruitx = randrange(6,84)
                    self.fruity = randrange(6,84)

            #these lines are intended to change the size of the fruit in different modes
            #test if it is in the hard mode
            if self.speed < 10:
                self.initfruit(1)
            else:
                self.initfruit(3)                   
            self.circle.draw(self.win)
            self.circle.setFill(color_rgb(255,255,255))

        except (GraphicsError):
            return

    def tail(self):
        try:
            self.i = randrange(500,550)
            #check if the randomly generated number is the coords of any tail cube
            #still need these lines for unknown reason
            for cube in self.cubelist:
                if self.i + 2 == cube.getCenter().getX():
                    if self.i + 2 == cube.getCenter().getY():
                        self.i = randrange(500,550)

            self.cube = Rectangle(Point(self.i, self.i), Point(self.i + 2,self.i + 2))            
            self.cube.setWidth(0)
            self.cubelist.append(self.cube)

            #set the color of each cube with gradual decadence from black to white
            r,g,b = -3,-3,-3
            for cube in self.cubelist:
                if -3 <= r <= 254 and -3 <= g <= 254 and -3 <= b <= 254:
                    r += 3
                    g += 3
                    b += 3

                else:
                    r,g,b = 255,255,255
                cube.setFill(color_rgb(r,g,b))
            self.cube.draw(self.win)
            
        except (GraphicsError):
            return

#not sure how to use polymorphism in python, so I'll just copy past here
    def etail(self):
        try:
            self.ii = randrange(500,550)
            #check if the randomly generated number is the coords of any tail cube
            #still need these lines for unknown reason
            for cube in self.ecubelist:
                if self.ii + 2 == cube.getCenter().getX():
                    if self.ii + 2 == cube.getCenter().getY():
                        self.ii = randrange(500,550)

            self.ecube = Rectangle(Point(self.ii, self.ii), Point(self.ii + 2,self.ii + 2))            
            self.ecube.setWidth(0)
            self.ecubelist.append(self.ecube)

            #set the color of each cube with gradual decadence from black to white
            r,g,b = 258,258,258
            for cube in self.ecubelist:
                if 3 <= r <= 258 and 3 <= g <= 258 and 3 <= b <= 258:
                    r -= 3
                    g -= 3
                    b -= 3
                else:
                    r,g,b = 0,0,0
                cube.setFill(color_rgb(r,g,b))            
            
            self.ecube.draw(self.win)
            
        except (GraphicsError):
            return
        
    def topscoredisplay(self):
        #display player's best score
        self.scoredisplay = Text(Point(50,80),'Best score: ' + str(self.bestscore))
        self.scoredisplay.setFace('courier')
        self.scoredisplay.setSize(30)
        self.scoredisplay.setStyle('bold')
        self.scoredisplay.setFill('yellow4')
        self.scoredisplay.draw(self.win)

    #show the highest score of the player
    def lastscore(self):
        #show the score
        self.scoreboard = Text(Point(50,70),'you ate ' + str(self.score) + ' fruits')
        self.scoreboard.setFace('helvetica')
        self.scoreboard.setSize(25)
        self.scoreboard.setFill('green')
        self.scoreboard.draw(self.win)

    #the best score display and redraw the menu
    def menu(self):
        stopSound()

        self.boundaryL.remove()
        self.boundaryU.remove()
        self.boundaryR.remove()
        self.boundaryD.remove()

        self.cclogo.remove()

        #draw the menu
        menu = GameMenu(self.win)
        menu.display()
        self.isStill = True

        while True:
            pt = self.win.getMouse()
            if menu.lv1button.clicked(pt):
                menu.remove()
                self.bestscore = 0
                self.scoredisplay.undraw()
                myGame = SnakeGame(self.win, 1, False)            
            elif menu.lv2button.clicked(pt):
                menu.remove()
                self.bestscore = 0
                self.scoredisplay.undraw()
                myGame = SnakeGame(self.win, 2, False)
            elif menu.lv3button.clicked(pt):
                menu.remove()
                self.bestscore = 0
                self.scoredisplay.undraw()
                myGame = SnakeGame(self.win, 2, True)
        
    #show this menu when player loses the game
    def pausemenu(self, losemsg):
        ''' show a menu to let player choose to keep playing the samel level
        or go back to main menu'''
        try:
            #startSound("busted.wav", async=True, loop=False)
            self.allowmove = False
            #stop the snake
            if self.keypressed == True:
                self.dx = self.dy = 0
            self.allowdraw = False
            self.isStill = True
            self.allowkey = False

            #remove the fruit
            self.circle.undraw()
            self.losemsg = losemsg
            self.end = Text(Point(50,50), self.losemsg)
            self.end.setSize(20)
            self.end.draw(self.win)

            #display the last score the player just hit
            self.lastscore()

            #the try-again button
            self.againButton = Button(self.win, Point(50,30), 15, 8, 'Try Again')
            self.againButton.display()

            #the menu button
            self.tomenuButton = Button(self.win, Point(50,20), 15, 8, 'Game Menu')
            self.tomenuButton.display()

            #accumulator for the best score
            if self.score > self.bestscore:
                self.bestscore = self.score

            while True:
                self.clickpt = self.win.getMouse()
                if self.againButton.clicked(self.clickpt):
                    #now allow input
                    self.allowkey = True
                    #allow to move
                    self.allowmove = True
                    #set the direction to 0
                    self.direction = 0
                    self.tomenuButton.remove()
                    self.againButton.remove()
                    #update the score

                    if self.score > self.bestscore:
                        self.bestscore = self.score
                    self.fruit()
                    self.end.undraw()
                    self.scoreboard.undraw()
                    self.score = 0
                    self.rect.undraw()

                    #undraw every cube in the list
                    for cube in self.cubelist:
                        cube.undraw()

                    self.ehead.undraw()

                    #undraw every cube in the enemy tail
                    for cube in self.ecubelist:
                        cube.undraw()

                    #and then empty the lists
                    self.cubelist = []
                    self.ecubelist = []

                    #re-initialize the snake head
                    self.rect = Rectangle(Point(90, 10), Point(92,12))
                    self.rect.draw(self.win)
                    self.rect.setFill("black")

                    #now draw the enemy snake
                    self.ehead = Rectangle(Point(10, 80), Point(12, 82))
                    self.ehead.setWidth(0)
                    self.ehead.draw(self.win)
                    self.ehead.setFill("white")
                    break

                #this is the go-to-menu button, largely similar to the again button
                elif self.tomenuButton.clicked(self.clickpt):
                    self.direction = 0
                    self.allowkey = True
                    self.rect.undraw()
                    self.ehead.undraw()

                    #undraw every cube in the enemy tail
                    for cube in self.cubelist:
                        cube.undraw()

                    #undraw every cube in the enemy tail
                    for cube in self.ecubelist:
                        cube.undraw()

                    #empty the lists
                    self.cubelist = []
                    self.ecubelist = []

                    self.how1.setFill('green4')
                    self.how2.setFill('green4')
                    self.how3.setFill('green4')
                    self.circle.undraw()
                    self.end.undraw()
                    self.scoreboard.undraw()
                    self.score = 0
                    self.againButton.remove()
                    self.tomenuButton.remove()
                    self.topscoredisplay()
                    self.menu()
                    break

        except (GraphicsError):
            print("ge")
            return

    #the status bar on top of the screen
    def statusbar(self):
        ''' show a bar on top of the window indicating player's score'''
        #the status bar
        self.topbar = Rectangle(Point(-1,90),Point(101,101))
        self.topbar.setFill('green4')
        self.topbar.draw(self.win)

        #display instructions
        #note the positions of instructions are different on mac and windows
        self.how1 = Text(Point(20,97),'ARROW keys to change directions')
        self.how1.setSize(15)
        self.how1.setFill('blue')
        self.how1.draw(self.win)
        self.how2 = Text(Point(11,93),'Hit ESC to quit the game')
        self.how2.setSize(15)
        self.how2.setFill('blue')
        self.how2.draw(self.win)
        self.how3 = Text(Point(89,95),'Hit SPACE to pause')
        self.how3.setSize(15)
        self.how3.setFill('blue')
        self.how3.draw(self.win)

    #main game loop
    def run(self):
        if not self.running:
            return
        
        self.allowdraw = True
        #check if the snake hits itself
        for cube in self.cubelist[4:]:
            if self.rect.getCenter().getX() - 1 < cube.getCenter().getX() + 1:
                if self.rect.getCenter().getX() + 1 > cube.getCenter().getX() - 1:
                    if self.rect.getCenter().getY() + 1 > cube.getCenter().getY() - 1:
                        if self.rect.getCenter().getY() - 1 < cube.getCenter().getY() + 1:
                            self.pausemenu('you hit yourself')

        #check if the enemy snake hits itself
        for cube in self.ecubelist[4:]:
            if self.ehead.getCenter().getX() - 1 < cube.getCenter().getX() + 1:
                if self.ehead.getCenter().getX() + 1 > cube.getCenter().getX() - 1:
                    if self.ehead.getCenter().getY() + 1 > cube.getCenter().getY() - 1:
                        if self.ehead.getCenter().getY() - 1 < cube.getCenter().getY() + 1:
                            self.pausemenu('Your enemy hits itself! You win!')

        #check if the snake hits the boundary
        if self.rect.getCenter().getX() > 94 or self.rect.getCenter().getX() < 7 or self.rect.getCenter().getY() > 83 or self.rect.getCenter().getY() < 7:
            self.pausemenu('you hit the boundary')

        #check if the enemy snake hits the boundary
        if self.ehead.getCenter().getX() > 94 or self.ehead.getCenter().getX() < 7 or self.ehead.getCenter().getY() > 83 or self.ehead.getCenter().getY() < 7:
            self.pausemenu('You foe hits the boundary. You win!')

        #in hard level, move the fruit to add a little challenge
        if self.hardmode == True:
            if self.allowmove == True:
                self.circle.move(self.fruitdx, self.fruitdy)

                #record the current position of the fruit and keep it updated
                self.fruitx = self.circle.getCenter().getX()
                self.fruity = self.circle.getCenter().getY()
                self.fruitx = self.fruitx + self.fruitdx
                self.fruity = self.fruity + self.fruitdy

                #update the perimeters of the fruit for hard mode
                self.fruitposXleft = self.fruitx - 1.5
                self.fruitposXright = self.fruitx + 1.5
                self.fruitposYup = self.fruity + 1.5
                self.fruitposYdown = self.fruity - 1.5
               
                #let the fruit move and bounce
                if self.fruitx < 6 or self.fruitx > 95:
                    self.fruitdx = -self.fruitdx
                elif self.fruity  < 6 or self.fruity > 84:
                    self.fruitdy = -self.fruitdy

                #the fruit bounces back when it touches the snake
                for cube in self.cubelist:
                    if self.fruitposXright == cube.getCenter().getX():
                        self.fruitdx = -self.fruitdx
                    elif self.fruitposXleft == cube.getCenter().getX():
                        self.fruitdx = -self.fruitdx
                    elif self.fruitposYup == cube.getCenter().getY():
                        self.fruitdy = -self.fruitdy
                    elif self.fruitposYdown == cube.getCenter().getY():
                        self.fruitdy = -self.fruitdy

        #first to test if it is allowed it to move
        if self.allowmove == True:
            #record the current position of the head and keep it updated
            self.currPosX = self.rect.getCenter().getX()
            self.currPosY = self.rect.getCenter().getY()
            self.currPosX = self.currPosX + self.dx
            self.currPosY = self.currPosY + self.dy

            #check if the snake eats the fruit
            if self.fruitposXleft < self.currPosX + 1:
                if self.currPosX - 1 < self.fruitposXright:
                    if self.fruitposYdown < self.currPosY + 1:
                        if self.currPosY - 1 < self.fruitposYup:
                            startSound("eatfruit.wav", async=True, loop=False)
                            #increase the score by 1
                            self.score += 1
                            #undraw the previous fruit
                            self.circle.undraw()
                            #draw another fruit
                            self.fruit()                        

                            self.tail()
                            self.tail() 
                            self.tail()
                            self.tail()
                            
                            self.hasTail = True

            self.currPosX = self.rect.getCenter().getX()
            self.currPosY = self.rect.getCenter().getY()
            self.currPosX = self.currPosX + self.dx
            self.currPosY = self.currPosY + self.dy
            self.rect.move(self.dx,self.dy)

            for cube in self.cubelist:
                self.nextPosX = self.currPosX
                self.nextPosY = self.currPosY
                self.currPosX = cube.getCenter().getX()
                self.currPosY = cube.getCenter().getY()
                self.setPosition(cube, self.nextPosX, self.nextPosY)

            #the following code is to make the enemy snake move
            if self.ehead.getCenter().getX() > self.fruitx:
                self.edx = -self.speed
                self.edy = 0
            elif self.ehead.getCenter().getX() < self.fruitx:
                self.edx = self.speed
                self.edy = 0
            elif self.ehead.getCenter().getY() > self.fruity:
                self.edx = 0
                self.edy = -self.speed
            elif self.ehead.getCenter().getY() < self.fruity:
                self.edx = 0
                self.edy = self.speed

            #record the current position of the enemy head and keep it updated
            self.currPosXe = self.ehead.getCenter().getX()
            self.currPosYe = self.ehead.getCenter().getY()
            self.currPosXe = self.currPosXe + self.edx
            self.currPosYe = self.currPosYe + self.edy

            #check if the enemy snake eats the fruit
            if self.fruitposXleft < self.currPosXe + 1:
                if self.currPosXe - 1 < self.fruitposXright:
                    if self.fruitposYdown < self.currPosYe + 1:
                        if self.currPosYe - 1 < self.fruitposYup:
                            startSound("eatfruit.wav", async=True, loop=False)
                            #increase the score by 1
                            #self.score += 1
                            #undraw the previous fruit
                            self.circle.undraw()
                            #draw another fruit
                            self.fruit()                        

                            self.etail()
                            self.etail()
                            self.etail()
                            self.etail()
                            
                            self.ehasTail = True

            self.currPosXe = self.ehead.getCenter().getX()
            self.currPosYe = self.ehead.getCenter().getY()
            self.currPosXe = self.currPosXe + self.edx
            self.currPosYe = self.currPosYe + self.edy
            self.ehead.move(self.edx, self.edy)

            for cube in self.ecubelist:
                self.nextPosXe = self.currPosXe
                self.nextPosYe = self.currPosYe
                self.currPosXe = cube.getCenter().getX()
                self.currPosYe = cube.getCenter().getY()
                self.setPosition(cube, self.nextPosXe, self.nextPosYe)

        #we want to draw all things in one instance and keep the graphics updating
        #we set autoflush to false to avoid screen stuttering
        self.win.update()
        self.win.after(33, self.run)
        #print('loop')

    def setPosition(self, rect, x, y):
        """set the absolute position of rect object. move method is for relative move
        but this one will move rect to exact position specified"""
        cp = rect.getCenter()
        cx = cp.getX()
        cy = cp.getY()
        #compute relative distance from the center of rect to x, y
        dx = x - cx
        dy = y - cy
        #move rect by delta
        rect.move(dx, dy)

def main():
    win = GraphWin('SnakeGame', 600, 600, autoflush = False)
    win.setCoords(0,0,100,100)
    win.setBackground('brown')

    #welcome screen before the game menu
    start = Text(Point(50,50),'Start')
    start.setSize(30)
    start.setFace('helvetica')
    start.setFill('blue')
    start.setStyle('bold')
    start.draw(win)

    pt = win.getMouse()

    #the following lines are to enter the menu where the player can see the instruction and choose game difficulty
    start.undraw()

    menu = GameMenu(win)
    menu.display()

    try:
        while True:
            pt = win.getMouse()
            if menu.lv1button.clicked(pt):
                menu.remove()
                myGame = SnakeGame(win, 1, False)            

            elif menu.lv2button.clicked(pt):
                menu.remove()
                myGame = SnakeGame(win, 2, False)

            elif menu.lv3button.clicked(pt):
                menu.remove()
                myGame = SnakeGame(win, 2, True)

    except (GraphicsError):
        stopSound()
        return

if __name__ == '__main__':

    main()
