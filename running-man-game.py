import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

# this is the scrolling background pics...
bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()  # provides the movement flow...


"""
-----------------------------------------------------------------------------------------------------------------------
                                                ** CLASSES BEGIN **
-----------------------------------------------------------------------------------------------------------------------
"""

# PLAYER CLASS


class player(object):
    # corresponding images for such actions...
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')),
             pygame.image.load(os.path.join('images', 'S5.png'))]
    # jumpList has to do with jumping up and down...
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):  # constructor for the player...
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2  # has to do with the 'jumping math' (jumping algorithm)
            win.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide[self.slideCount // 10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount // 6], (self.x, self.y))
            self.runCount += 1


# SAW CLASS


class saw(object):
    img = [pygame.image.load(os.path.join('images', 'SAW0.png')),pygame.image.load(os.path.join('images', 'SAW1.png')),pygame.image.load(os.path.join('images', 'SAW2.png')),pygame.image.load(os.path.join('images', 'SAW3.png'))]

    def __init__(self, x, y, width, height):  # constructor and/or initialization method for the saw object...
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)  # give the hitbox a rectangle format or shape...
        self.count = 0

    def draw(self, win):  # the math here moves the saw up and down
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)     # THE BELOW MATH EXPLANATION:
        if self.count >= 8:  # for every 2 frames, we'll draw 1 frame of the saw so that it doesn't spin too fast...
            self.count = 0  # used as the index number for the saw images...
            # scale down the image of the saw...
        win.blit(pygame.transform.scale(self.img[self.count//2], (64, 64)), (self.x, self.y))  # using integer division
        self.count += 1
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2) # draw a thick red hitbox...


# SPIKE CLASS


class spike(saw):  # spike class inherits from saw class...so it will
    #  have the same properties in the saw's constructor...

    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y, 28, 315)
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255,0,0),self.hitbox,2)


"""
-----------------------------------------------------------------------------------------------------------------------
                                                ** CLASSES END **
-----------------------------------------------------------------------------------------------------------------------
"""


"""
-----------------------------------------------------------------------------------------------------------------------
                                              **  BEGIN MAIN LOOP **
-----------------------------------------------------------------------------------------------------------------------
"""

def redrawWindow():
    win.blit(bg, (bgX,0)) # these draw the scrolling background
    win.blit(bg, (bgX2, 0))
    runner.draw(win)    # player object calling its draw function to draw himself...
    for x in objects:
        x.draw(win)
    # bigSpike.draw(win)  # spike object calling its draw function to draw himself...
    # sawBlade.draw(win)  # saw object calling its draw function to draw himself...
    pygame.display.update()


# create a spike instance or object...
# bigSpike = spike(300,0,48,320)

# create a saw instance or object...
# sawBlade = saw(300,300,64,64)

# create a player instance or object...
runner = player(200, 313, 64, 64) # x, y , and the sprite's dimensions: 64x64
pygame.time.set_timer(USEREVENT+1, 500)  # every half second we're going to increase the speed by calling this event...
pygame.time.set_timer(USEREVENT+2, random.randrange(3000, 5000))  # this event is for the obstacle objects timing
speed = 30                                                        # as to how frequently they appear...
run = True

objects = []

while run:
    redrawWindow()
    # code below gets rid of the obstacle objects once they're off the screen
    for objectt in objects:
        objectt.x -= 1.4  # decrementing the obstacle object's x
        if objectt.x < objectt.width * -1:  # if obstacle's x is less than the obstacle's width,
            objects.pop(objects.index(objectt))  # this means the obstacle is off the screen so pop it off the list...
            # the obstacles will then be instantiated once again in the lower code segments within this while loop...
    bgX -= 1.4
    bgX2 -= 1.4
    # if bgX exceeds the negative x (negative width) value that means its off the screen (no longer visible
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()     # so, then make bgX = the positive width() again...
    if bgX2 < bg.get_width() * -1:  # bgX2 is directly behind bgX
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == USEREVENT+1:  # what the timer actually does is, it triggers
            speed += 1                 # the USEREVENT+1 to be true every 500 milli-seconds...(half a second)
            # so to check when this event is happening we have to do that within our event loop here...
        if event.type == USEREVENT+2:
            r = random.randrange(0,2) # the 2 is non-inclusive (randomly instantiate a saw or a spike)
            if r == 0:  # code below draws the saw and the spike objects by calling their constructors...
                objects.append(saw(810,310,64,64))  # then it appends new obstacle into our list...
            else:  # in this case r == 1
                objects.append(spike(810,0,48,320))  # append new obstacle into our list...

    # access the computer keyboard keys...
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(runner.jumping): # boolean variable: jumping
            runner.jumping = True
    if keys[pygame.K_DOWN]:
        if not (runner.sliding):
            runner.sliding = True

    clock.tick(speed)  # fps frames per second...

    """
    -------------------------------------------------------------------------------
                            ** COMPLETED VIDEO #1 **
    Pygame Side-Scroller Tutorial #1 - Scrolling Background/Character Movement
    https://www.youtube.com/watch?v=PjgLeP0G5Yw&t=139s
    
                               ** COMPLETED VIDEO #2 **
    Pygame Side-Scroller Tutorial #2 - Random Object Generation
    https://www.youtube.com/watch?v=fHlJNjRRXWY
    TIME STAMP: STOPPED VIDEO @ 16:52 / 19:20     -   TIME: 10:52am 3/27/21 Saturday
    
                                ** READY FOR VIDEO #3 **
    Pygame Side-Scroller Tutorial #3 - Collision
    https://www.youtube.com/watch?v=qTw0lYqTQSU                            
    TIME STAMP: STOPPED VIDEO @ 00:00 / 00:00     -   TIME: 00:00    / / 
    -------------------------------------------------------------------------------
    """
