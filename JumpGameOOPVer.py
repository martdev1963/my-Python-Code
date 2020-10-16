import pygame
pygame.init()
# NOTE: the coordinate in pygame is in the top-left of an object on the screen. 
win = pygame.display.set_mode((500, 480))  # dimensions of the window object
pygame.display.set_caption("Guavadream Media LLC")

walkRight = [pygame.image.load('C:/Users/19542/Desktop/game101/Game/R1.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R2.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R3.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R4.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R5.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R6.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R7.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R8.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/R9.png')]
walkLeft = [pygame.image.load('C:/Users/19542/Desktop/game101/Game/L1.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L2.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L3.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L4.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L5.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L6.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L7.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L8.png'), pygame.image.load('C:/Users/19542/Desktop/game101/Game/L9.png')]
bg = pygame.image.load('C:/Users/19542/Desktop/game101/Game/bg.jpg')
char = pygame.image.load('C:/Users/19542/Desktop/game101/Game/standing.png')

clock = pygame.time.Clock()
#--------------------------------------------------------------------------------------------------------------------
#                                               OOP CODE OPTIMIZATION tutorial # 4
#----Class for character start---------------------------------------------------------------------------------------
class player(object): # class attributes
    def __init__(self, x, y, width, height): # this defines our character...
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27: # NOTICE: the FPS here is 27 FPS
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y)) # integer divide by 3 integer division excludes the remainder, all the decimals, rounds off the number
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y)) # integer divide by 3 integer division excludes the remainder, all the decimals, rounds off the number
            self.walkCount += 1 
        else:
            win.blit(char, (self.x,self.y))      

#----Class for character end-------------------------------------------------------------------------------------------    

# class object or instance
man = player(300, 410, 64, 64)

def redrawGameWindow():
    win.blit(bg, (0, 0)) # This loads: bg = pygame.image.load('C:/Users/19542/Desktop/game101/Game/bg.jpg')
    man.draw(win)
    pygame.display.update() # this refreshes the display thus showing the current code's result which is making a rectangular figure

#mainloop
run = True
while run:
    # optimizing the code to use the object's class attributes...ie: man.velocity, (self.velocity), etc...
    clock.tick(27) # 27 frames per second (27 FPS)
    for event in pygame.event.get(): # this event object can be used to detect keys clicked on too but pygame.key.get_pressed() is better
        if event.type == pygame.QUIT: # if user clicks on red button
            run = False               # then run == False  
    keys = pygame.key.get_pressed() # this checks for keys that are continually held down after the initial pressing of them.
    if keys[pygame.K_LEFT] and man.x > man.velocity:  
        man.x -= man.velocity  # to move left you subtract from the x coordinate
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:  # making sure x is less than the window object's width (win on LOC: 9 line of code )
        man.x += man.velocity  # to move right you add to the x coordinate
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    if not (man.isJump):  # if isJump not False then its True (negative logic because isJump is assigned False up top)
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0  # walkCount is = 0 because the character is not walking afterall, he is jumping at this point.  
    else:
        if man.jumpCount >= -10:
            neg = 1   # when rec character is going up neg variable == positive 1 thus multiplying by 1, nothing occurs... 
            if man.jumpCount < 0:
                neg = -1  # eventually jumpCount will be less than 1  ie; a negative number so neg will == negative 1 effecting the calculation 
            # and making the character come back down.     
            man.y -= (man.jumpCount ** 2) / 2 * neg # squared by 2 so this will cause the character to move 100 pixels upward and downward on the y axis.
            # y -= (jumpCount ** 2) * 0.5 * neg  this calculation also works exactly the same as the above one...
            man.jumpCount -= 1    # this will cause the character to speed up on the jump by 90 pixels, then 80 and 70 and so on...
            #plus if you leave it out  it won't come back down...It makes it come back down, slowly and smoothly.
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()        

pygame.quit()                         # and quit game... 
