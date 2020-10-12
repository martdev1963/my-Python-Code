#-------------------------------------------------------------------------------------------------------------
# Pygame Tutorial #1 - Basic Movement and Key Presses
# https://www.youtube.com/watch?v=i6xMBig-pP4
# Tech With Tim
#-------------------------------------------------------------------------------------------------------------
import pygame
pygame.init()
# NOTE: the coodinate in pygame is in the top-left of an object on the screen. 
win = pygame.display.set_mode((500, 500))  # dimensions of the window object

pygame.display.set_caption("First Game")

x = 50
y = 425
width = 40
height = 60
velocity = 5

isJump = False
jumpCount = 10



run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get(): # this event object can be used to detect keys clicked on too but pygame.key.get_pressed() is better
        # suited for this particular functionality...of detecting the continual holding of a key for making the rectangle move. 
        if event.type == pygame.QUIT: # if user clicks on red button
            run = False               # then run == False  
    # keys that are held down...
    keys = pygame.key.get_pressed() # this checks for keys that are continually held down after the initial pressing of them.
    # checks for which key is being held down...
    #CODE BELOW: make sure the rectangle's x position is greater than velocity which == 5 so it won't move off the screen when moving left.
    if keys[pygame.K_LEFT] and x > velocity: 
        x -= velocity  # to move left you subtract from the x coordinate
    if keys[pygame.K_RIGHT] and x < 500 - width - velocity:  # making sure x is less than the window object's width (win on LOC: 9 line of code )
        x += velocity  # to move right you add to the x coordinate
    if not (isJump):    
        if keys[pygame.K_UP] and y > velocity: # so it won't go off the screen when going up.(the bigger the nunber, the lower on the y axis).     
            y -= velocity  # to move up you subtract from the y coordinate    
        if keys[pygame.K_DOWN] and y < 500 - height - velocity: # so it won't go off the screen when going down.  
            y += velocity  # to move down you add to the y coordinate
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1   # for moving down on the y axis  (pos numbers are low). Multiplying by the neg variable brings the charagcter back down.
            if jumpCount < 0:
                neg = -1  # for moving up on the y axis (neg numbers are high)
            y -= (jumpCount ** 2) / 2 * neg # squared by 2 so this will cause the character to move 100 pixels upward and downward on the y axis.
            # y -= (jumpCount ** 2) * 0.5 * neg  this calculation also works exactly the same as the above one...
            jumpCount -= 1    # this will cause the character to slow down on the jump by 90 pixels and so on...plus if you leave it out 
            # it won't come back down...It makes it come back down, slowly and smoothly.
        else:
            isJump = False
            jumpCount = 10



    # this code fill's the screen in black before you draw the red rectangle...
    win.fill((0,0,0)) # this makes the program fill the screen black thus erasing the previously drawn red rectangles giving 
    # the appearance of the red rectangle moving and not leaving traces as it did previously without this line of code...
                      # window, rgb color for the shape, dimensions of the shape        
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # parameters...Everythong in pygame is a surface
    pygame.display.update() # this refreshes the display thus showing the current code's result which is making a rectangular figure



pygame.quit()                         # and quit game... 

