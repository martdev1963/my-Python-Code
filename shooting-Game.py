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
#                                               OOP CODE OPTIMIZATION 
# Applied: tutorials #4, #5
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
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27: # NOTICE: the FPS here is 27 FPS
            self.walkCount = 0

        if not (self.standing): # if not standing, then the character is walking...   
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y)) # integer divide by 3 integer division excludes the remainder, all the decimals, rounds off the number
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y)) # integer divide by 3 integer division excludes the remainder, all the decimals, rounds off the number
                self.walkCount += 1 
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y)) # shows the first animation of character looking to the right
            else:
                win.blit(walkLeft[0], (self.x, self.y))  # shows the first animation of character looking to the left  

            #win.blit(char, (self.x,self.y)) # this plays the animation of the character standing and facing the screen.     

#----Class for character end-------------------------------------------------------------------------------------------    
#
#                                             ******************************
#
#----Class for projectile START-----------------------------------------------------------------------------------------
class projectile(object):                   # facing parameter will == 1 or -1
    def __init__(self, x, y, radius, color, facing): # what facing does is tell us whether the bullet is moving left or right. 
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing # facing parameter will == 1 or -1 which will determine whether bullet will be facing left or right...

    def draw(self, win): # draw a circle
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) # putting a number 1 value after radius, just makes the circle outline, 
        # it does'nt fill in the cirle as well.


#----Class for projectile END-------------------------------------------------------------------------------------------

# class player() object or instance
man = player(300, 410, 64, 64)

# all objects on the screen are drawn from this function.
def redrawGameWindow():
    win.blit(bg, (0, 0)) # This loads: bg = pygame.image.load('C:/Users/19542/Desktop/game101/Game/bg.jpg')
    man.draw(win) # draw the player() class' character
    for bullet in bullets:
        bullet.draw(win) # draw the projectile class' bullets, which are objects of type: projectile

    pygame.display.update() # this refreshes the display thus showing the current code's result which is making a rectangular figure

#mainloop
bullets = []
run = True
while run:
    # optimizing the code to use the object's class attributes...ie: man.velocity, (self.velocity), etc...
    clock.tick(27) # 27 frames per second (27 FPS)
    for event in pygame.event.get(): # this event object can be used to detect keys clicked on too but pygame.key.get_pressed() is better
        if event.type == pygame.QUIT: # if user clicks on red button
            run = False   # then run == False      

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:   # checking that bullet is within the dimensions of our screen, then allow bullet to be shot        
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet)) # this code removes the bullet from the bullets list at that specific bullet index position
            # plus you're going to make more bullet objects anyway and fill the bullets list with them.
    keys = pygame.key.get_pressed() # this checks for keys that are continually held down after the initial pressing of them.

    if keys[pygame.K_SPACE]:
        if man.left: # if man.left == True then...
            facing = -1
        else:
            facing = 1    
        if len(bullets) < 5:       # 'synching' class projectile object's parameters: x,y,radius,color,facing to the player character 
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0,0,0), facing)) 
            # using integer division // this makes the bullet come from the middle of the man
            # notice how the projectile class' constructor is being called to populate the list with projectile objects

    if keys[pygame.K_LEFT] and man.x > man.velocity:  
        man.x -= man.velocity  # to move left you subtract from the x coordinate
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:  # making sure x is less than the window object's width (win on LOC: 9 line of code )
        man.x += man.velocity  # to move right you add to the x coordinate
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not (man.isJump):  # if isJump not False then its True (negative logic because isJump is assigned False up top)
        if keys[pygame.K_UP]:
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

pygame.quit()                         # quit game... 
