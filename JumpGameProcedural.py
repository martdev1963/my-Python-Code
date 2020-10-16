#-----------------------------------------------------------------------------------------------------
# Procedural programming version: Can make a binary/executable out of this source code.
# lectures 1 through 3 
#-----------------------------------------------------------------------------------------------------
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

x = 50
y = 400
width = 64
height = 64
velocity = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0)) # This loads: bg = pygame.image.load('C:/Users/19542/Desktop/game101/Game/bg.jpg')

    if walkCount + 1 >= 27: # NOTICE: the FPS here is 27 FPS
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y)) # integer divide by 3 integer division excludes the remainder, all the decimals, rounds off the number
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y)) # integer divide by 3 integer division excludes the remainder, all the decimals, rounds off the number
        walkCount += 1  # [STOPPED TUT VID @ 12:23 / 15:42....Pygame Tutorial #3 - Character Animation & Sprites]
    else:
        win.blit(char, (x,y))    

    pygame.display.update() # this refreshes the display thus showing the current code's result which is making a rectangular figure

#mainloop
run = True
while run:
    
    clock.tick(27) # 27 frames per second (27 FPS)
    for event in pygame.event.get(): # this event object can be used to detect keys clicked on too but pygame.key.get_pressed() is better
        if event.type == pygame.QUIT: # if user clicks on red button
            run = False               # then run == False  
    keys = pygame.key.get_pressed() # this checks for keys that are continually held down after the initial pressing of them.
    if keys[pygame.K_LEFT] and x > velocity: 
        x -= velocity  # to move left you subtract from the x coordinate
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - velocity:  # making sure x is less than the window object's width (win on LOC: 9 line of code )
        x += velocity  # to move right you add to the x coordinate
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not (isJump):  # if isJump not False then its True (negative logic because isJump is assigned False up top)
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0  # walkCount is = 0 because the character is not walking afterall, he is jumping at this point.  
    else:
        if jumpCount >= -10:
            neg = 1   # when rec character is going up neg variable == positive 1 thus multiplying by 1, nothing occurs... 
            if jumpCount < 0:
                neg = -1  # eventually jumpCount will be less than 1  ie; a negative number so neg will == negative 1 effecting the calculation 
            # and making the character come back down.     
            y -= (jumpCount ** 2) / 2 * neg # squared by 2 so this will cause the character to move 100 pixels upward and downward on the y axis.
            # y -= (jumpCount ** 2) * 0.5 * neg  this calculation also works exactly the same as the above one...
            jumpCount -= 1    # this will cause the character to speed up on the jump by 90 pixels, then 80 and 70 and so on...
            #plus if you leave it out  it won't come back down...It makes it come back down, slowly and smoothly.
        else:
            isJump = False
            jumpCount = 10
    redrawGameWindow()        

pygame.quit()                         # and quit game... 
