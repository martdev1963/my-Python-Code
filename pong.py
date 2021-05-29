"""-------------------------------------------------------------------------------------------------------------
Simple Pong in Python 3 for Beginners
Written in Functional Programming not OOP
TokyoEdTech
Part 1 Getting Started
y = +300 is up y -300 is down
x = +300 is to the right x = -300 is to the left  
x, y == 0 is in the center
vid:8:58 / 6:43:42)
https://www.youtube.com/watch?v=XGf2GcyHPhc

--------------------------------------------------------------------------------------------------------------"""

import turtle
import winsound

# a window object of sorts...
wn = turtle.Screen()
wn.title("Pong by Martin B for Guavadream Media LLC")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops window from updating thus it speeds up the game...
# you then have to manually update your game.
# otherwise, your game would run too slow.


# Score
score_a = 0
score_b = 0



"""----------------------------------------------------------------------------------------------------------
                                                 **TURTLE OBJECTS**
-----------------------------------------------------------------------------------------------------------"""

# Paddle A 
paddle_a = turtle.Turtle()  # small t for the module name turtle and Big T for the class name Turtle...
# speed of animation....sets the speed to the maximum possible speed. It has to be done for the turtle module.
# otherwise things would be really slow.
paddle_a.speed(0)  # animaton speed, not the movement speed...
paddle_a.shape("square") # shape of the paddle...among other shapes available
paddle_a.color("white")
# default size of paddle is 20px x 20px...(width x height)
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 20px * 5 and 20px * 1
paddle_a.penup() # turtle usually draws lines...
paddle_a.goto(-380, 0) # x, y coordinate   0, 0 is the center of the screen for x , y.


# ready to code paddle_b in tutorial! REFER TO VID TIME UP TOP : vid:8:58 / 6:43:42)

# Paddle B
paddle_b = turtle.Turtle()  # small t for the module name turtle and Big T for the class name Turtle...
# speed of animation....sets the speed to the maximum possible speed. It has to be done for the turtle module.
# otherwise things would be really slow.
paddle_b.speed(0)  # animaton speed, not the movement speed...
paddle_b.shape("square") # shape of the paddle...among other shapes available
paddle_b.color("white")
# default size of paddle is 20px x 20px...(width x height)
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 20px * 5 and 20px * 1
paddle_b.penup() # turtle usually draws lines...
paddle_b.goto(380, 0) # x, y coordinate   0, 0 is the center of the screen for x , y.

# Ball 
ball = turtle.Turtle()  # small t for the module name turtle and Big T for the class name Turtle...
# speed of animation....sets the speed to the maximum possible speed. It has to be done for the turtle module.
# otherwise things would be really slow.
ball.speed(0)  # animaton speed, not the movement speed...
ball.shape("square") # shape of the paddle...among other shapes available
ball.color("white")
# default size of paddle is 20px x 20px...(width x height)
ball.penup() # turtle usually draws lines...
ball.goto(0, 0) # x, y coordinate   0, 0 is the center of the screen for x , y.
ball.dx = 2 # d for delta or change... positive 2 is to the right for x
ball.dy = -2 # ball moves by 2 pixels   positive 2 is up on y


# Pen for the score-keeping mechanism...
pen = turtle.Turtle()
pen.speed(0) # animaton speed, not the movement speed...
pen.color("white")
pen.penup() # this is because we don't want to draw a line when the pen moves...
# Every turtle object starts at the dead center of the screen (0,0) and then we move it somewhere...
# If we don't do pen up, you'll see a line moving between those two points...
pen.hideturtle() # because we don't need to see this turtle in this case...unlike the paddle and ball objects...
pen.goto(0, 260) # the coordinates of the score display object...
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


"""----------------------------------------------------------------------------------------------------------
                                                 **FUNCTIONS**
-----------------------------------------------------------------------------------------------------------"""
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


"""----------------------------------------------------------------------------------------------------------
                                                 **Keyboard binding**
-----------------------------------------------------------------------------------------------------------"""


# Keyboard binding
wn.listen() # listens for keyboard input
wn.onkeypress(paddle_a_up, "w") # when user presses lowercase w, call function paddle_a_up...
wn.onkeypress(paddle_a_down, "s") # when user presses lowercase s, call function paddle_a_dwon...
wn.onkeypress(paddle_b_up, "Up") # when user presses lowercase w, call function paddle_b_up...
wn.onkeypress(paddle_b_down, "Down") # when user presses lowercase s, call function paddle_b_down...

"""----------------------------------------------------------------------------------------------------------
                                                 **GAME LOOP**
-----------------------------------------------------------------------------------------------------------"""
while True:
    wn.update() # everytime loop runs, this updates the screen.


    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # gets current x coodinate of ball plus dx (ball starts at 0,0)
    # it goes 2 pixels per the game loop
    # this is dependant on your computer's speed...
    ball.sety(ball.ycor() + ball.dy) # gets current y coodinate of ball plus dy (ball starts at 0,0)


"""----------------------------------------------------------------------------------------------------------
                                                 **BORDER CHECK**
-----------------------------------------------------------------------------------------------------------"""

    # Border check
    #must take window dimensions into account...wn.setup(width=800, height=600)
    # so the top y coordinate is +300 and the bottom y coordinate is -300
    # the ball dimensions; are 20 high by 20 wide...so ergo 300-10 == 290
if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # this reverses the direction of the ball...
        winsound.PlaySound("hitWall.wav",winsound.SND_ASYNC) # if asynchronous the sound will play in thye background
if ball.ycor() < -290:                                       # if not asyncnronous the program will stop. 
        ball.sety(-290)
        ball.dy *= -1 # this reverses the direction of the ball...    
        winsound.PlaySound("hitWall.wav",winsound.SND_ASYNC)
    # so for x coordinate its +400 on right and -400 on left
if ball.xcor() > 390: # the ball has gone past the paddle and off the screen if > than 390...  
        ball.goto(0, 0)
        ball.dx *= -1  # make ball go in opposite direction...
        winsound.PlaySound("hitWall.wav",winsound.SND_ASYNC)
        score_a += 1   # increment player A's score 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

if ball.xcor() < -390: # the ball has gone past the paddle and off the screen if < than 390...  
        ball.goto(0, 0)
        ball.dx *= -1  # make ball go in opposite direction...
        winsound.PlaySound("hitWall.wav",winsound.SND_ASYNC)   
        score_b += 1   # increment player B's score 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#--------------------------------------------------------------------------------------------------------------------
#                                             PADDLE AND BALL COLLISIONS
# the x coordinate of the center is 350...where the right paddle is
# the paddles are 20px wide by 100px tall...
# we need to make sure that the ball is bouncing off of the edges of the paddle's dimensions...
# if it is, then we'll call that a bounce...
# This code takes into account the dimensions of the ball and the paddles in the math...
#--------------------------------------------------------------------------------------------------------------------
if (ball.xcor() > 340 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(330) # set ball back to the left a little bit...
        ball.dx *= -1 # reverses the direction of the bounce
        winsound.PlaySound("hitPaddle.wav",winsound.SND_ASYNC)


if (ball.xcor() < -340 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-330) # set ball back to the left a little bit...
        ball.dx *= -1    
        winsound.PlaySound("hitPaddle.wav",winsound.SND_ASYNC)


""" STOPPED VIDEO @ 45:38 / 6:43:42 END OF PONG TUTORIAL"""
