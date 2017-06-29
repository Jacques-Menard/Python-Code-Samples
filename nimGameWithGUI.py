# Note: if you want to use additional tkinter widgets, you will need to add their names to
# the import list below
from tkinter import *
from time import sleep
import random

# To run this code, load into Python, and execute runNim(n), where n is desired initial number
# of balls, in the Python shell
#

# This class is just like the solution to HW 6 Q2 with three small changes related to GUI.
# See comments starting with # ##.
class NimGame():

    def __init__(self, numberOfBalls):
        self.numberOfBallsRemaining = numberOfBalls
        print("Nim game initialized with {} balls.".format(self.numberOfBallsRemaining))

    def remainingBalls(self):
        return self.numberOfBallsRemaining
    
    def take(self, numberOfBalls):
        self.numberOfBallsRemaining = self.numberOfBallsRemaining - numberOfBalls
        statusLabel.configure(text="You took {} balls. {} remain.".format(numberOfBalls, self.numberOfBallsRemaining))
        if self.numberOfBallsRemaining == 0:
            statusLabel.configure(text="You win!")
        else:
            # ## After removing player-chosen balls, update graphics and then pause for 1.0 seconds
            # before removing computer-chosen balls.  This way the player can "see" the
            # intermediate status.  Perhaps think about a nicer way of showing this.
            updateGraphics()
            sleep(1.0)
            
            computerMaxBalls = min(3, self.numberOfBallsRemaining)
            # It is certainly okay to change this code so that the computer plays more intelligently!
            compBallsTaken = random.randint(1,computerMaxBalls)
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken

            # ## After removing computer-chosen balls, update graphics again.
            statusLabel.configure(text="Computer took {} balls. {} remain.".format(compBallsTaken, self.numberOfBallsRemaining))
            if self.numberOfBallsRemaining == 0:
                statusLabel.configure(text="Computer wins!")
            updateGraphics()
                
# global variables used for placement of balls
canvasHeight = 200
canvasWidth = 610
canvasBorderBuffer = 10
maxBallSize = 100
# the values of global variables below are computed and set in initializeNimAndGUI
# ballSize
# halfBallSize 
# spaceBetweenBalls 
# leftmostBallXPosition
# ballYPosition

# 1. clear the canvas
# 2. draw balls on canvas equal to number remaining in the Nim game
def updateGraphics():
    canvas.delete('all')   
    centerX = leftmostBallXPosition
    centerY = ballYPosition
    if(nimGame.numberOfBallsRemaining<1):
        button1.config(state=DISABLED)
    else:
        button1.config(state=NORMAL)
    if(nimGame.numberOfBallsRemaining<2):
        button2.config(state=DISABLED)
    else:
        button2.config(state=NORMAL)
    if(nimGame.numberOfBallsRemaining<3):
        button3.config(state=DISABLED)
    else:
        button3.config(state=NORMAL)
    for i in range(nimGame.remainingBalls()):
        canvas.create_oval(centerX - halfBallSize,
                           centerY - halfBallSize,
                           centerX + halfBallSize,
                           centerY + halfBallSize,
                           fill="#ff0000")
        centerX = centerX + spaceBetweenBalls + ballSize
        canvas.update_idletasks()


# Callback functions invoked by GUI buttons

def takeBalls(numberToTake):
    nimGame.take(numberToTake)
    
def initializeNewGame():
    
    if(ballCount.get()==''):
        numberOfBalls=(5)
    else:
        numberOfBalls =  int(ballCount.get()) # change this to read from Entry widget you add to GUI
    initializeNimAndGUI(numberOfBalls)   

#####

# 1. create a NimGame object with specified number of balls
# 2. clear the graphics canvas
# 3. based on number of balls, compute values ball size and spacing and set
#     global variable used for drawing the balls.
# 
def initializeNimAndGUI(numberOfBalls):
    global nimGame
    global ballSize, halfBallSize, spaceBetweenBalls, leftmostBallXPosition, ballYPosition
    
    nimGame = NimGame(numberOfBalls)

    canvas.delete('all') 
    ballSize = min(maxBallSize, int(((canvasWidth-canvasBorderBuffer)//numberOfBalls)/1.2))
    halfBallSize = ballSize // 2
    spaceBetweenBalls = int(0.2 * ballSize)
    leftmostBallXPosition = (canvasBorderBuffer//2) + (spaceBetweenBalls//2) + halfBallSize
    ballYPosition = canvasHeight // 2

    updateGraphics()
    statusLabel.configure(text="Started new game.")


# create GUI for Nim Game, including
# 1. canvas where balls will be shown
# 2. some buttons, to the right of the canvas, for taking balls or starting a new game
# 3. a label, below the canvas and buttons, for status messages
#
def createGUI():
    global rootWindow
    global canvas
    global statusLabel
    global textEntry
    global ballCount
    global button1,button2, button3
    rootWindow = Tk()    
    ballCount = StringVar()
    rootWindow.title("Play Nim")
    canvasAndButtons = Frame(rootWindow)
    canvas = Canvas(canvasAndButtons, height=canvasHeight, width=canvasWidth, bg='blue',relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)

    buttonframe = Frame(canvasAndButtons)
    button1 = Button(buttonframe, text='Take 1', command=lambda:takeBalls(1))
    button2 = Button(buttonframe, text='Take 2', command=lambda:takeBalls(2))
    button3 = Button(buttonframe, text='Take 3', command=lambda:takeBalls(3))
    button4 = Button(buttonframe, text='New Game', command=initializeNewGame)
    # replace this with an Entry widget
    textEnt = Entry(buttonframe,textvariable=ballCount)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    textEnt.pack()
    buttonframe.pack(side=RIGHT)
    canvasAndButtons.pack()
    statusLabel = Label(rootWindow)
    statusLabel.pack()
    
# Call 'runNim' with the desired number of initial balls
#
def runNim(numberOfBalls):
    createGUI()
    initializeNimAndGUI(numberOfBalls)
    rootWindow.mainloop()



