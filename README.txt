{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww13740\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs28 \cf0 *Jason Xu class of 2017 of Conncoll\
*CS 110 Final Project\
*tested on mac, may have unexpected occurrence on windows\
\
*music credits not owned by me\
\
*enter run.py to play\
\
______About My Snake Game______\
\
This project is to recreate the classical snake game, aka, nibbler, with some new design on my side. In case you are unfamiliar with the snake game, it is a game such that the player moves the snake to eat food, say a fruit, and as the snake eats more food, it grows longer. The goal of the game is to eat as many fruits as possible without hitting the snake tail or the boundary, otherwise game over.\
\
Note in my snake game, the snake can eat food even the head is not completely on the axises of the fruit.\
\
In this project, there are several features other than the basic game system.\
(There are some unused codes that reserved for future use)\
\
1. Level System\
\
It has a level system where the player can choose the difficulty of the game in the game menu. There are in total three levels of difficulty.\
\
Easy: Snake moves at a regular speed.\
Medium: Snake moves fast.\
Hard: Snake moves fast and the fruit bounces.\
\
(In the future, I may implement another level where there will be an enemy snake that competes against player in trying to eat the fruit, and there will be result of who scores higher. In fact, I may implement it across all levels.)\
\
2. Pause\
\
When the player presses the space key during the game, the game is paused. The player can then hit the continue button to continue the game. However, I intentionally removed the menu button where the player can exit the game to the game menu during the game so that player needs to play at least one round of the game.\
\
3. Status Bar\
\
There will be a green status bar on top of the window when player begins his/her first round of game, and the green bar will stay until the player exit the window. On the bar, there will be instructions of how to play during the game but once player enters the game menu, the instructions will disappear. \
\
(In the future, I may make the green bar disappear every time player enters the menu.)\
\
4. Score\
\
There will be display of how many fruits you eat in the last round when you lost, and when you return to the game menu, there will be display of the highest score you earned from the very first round to the last try. Note that highest scores across different levels are not commutative and the score is cleared when you exit to the game menu. \
\
(In the future, I may change the highest score to display only in different levels)\
\
5. Sound Effect\
\
The BGM is intended to mimic the old school game music. There are two bgm, one for easy and medium levels and the other one for hard level. In the future, there may be a menu that lets player choose which bgm to play or I\'92ll implement such that different bgm is played in sequence. Note that the bgm will not start until the player selects a level; it will then continue to play until the player exits to the game menu.\
\
There will be sound effects when the snake eats a fruit and when the game is over.\
\
6. Exit button\
\
There is no exit button but player can freely close the window during the game by hitting the ESC key. But during the game menu, the esc key is not available and player can close the window anytime.\
\
7. Boundary\
\
There is boundary in the game where if the snake hits it, game is over.\
\
DESIGN COMPONENTS\
\
1. SnakeGame Class:\
\
parameters: win, speed, hard(True or False)\
return: the game\
\
Method:\
\
a. left, right, up, down, esc, space keys\
\
moves the snake and assign esc and space keys to functions described above.\
\
b. initfruit and fruit\
\
initialize fruits and randomly display the circle. Also set the boundaries of the fruit\
\
c. tail\
\
initialize the tail. the tails are drawn randomly outside the window. Also the tail will fade in color by using for loop\
\
d. topscoredisplay\
\
display the highest score\
\
e. lastscore\
\
display the result of the last round\
\
f. menu\
\
where things are undrawn when back to the game menu and the game menu is called\
\
g. pausemenu\
\
where the again button and menu button are drawn and the result of the last round is shown.\
 \
h. statusbar\
\
display the rectangle on top and the instructions during the game\
\
i. run\
\
the main loop of the game where collision detections are implemented, the movement is implemented, the tail is updated and the fruit is updated. In the case of the hard mode, the fruit movement is implemented.\
\
j. setPosition\
\
The method to move an object to a designated position, used to move the snake\
\
2. Boundary Class:\
\
draw the boundary of the game\
\
3. Button Class:\
\
used to create buttons\
\
Method:\
\
clicked()\
\
parameter: p (to get mouse click)\
\
used to check if the button is clicked, and do actions, return true or false\
\
4. CClogo Class:\
\
draw the CC logo in the game, i.e., four circles\
\
5. GameMenu Class:\
\
used to create the game menu\
\
2,3,4,5 classes all have display and remove methods to draw and undraw objects in the class.\
\
Note 2,3,4,5 classes are stored in another python files and imported into the main program.\
\
TESTS I HAVE DONE:\
\
Test: collision detections, continuous movements, sound, drawing and undrawing items properly, snake updated properly, color adjustment, label positioned properly, laggy movements of snake, key press responds properly, game difficulty, menus display timely and properly, etc.}