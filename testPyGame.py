#-------------------------------------------------------------------------------------------------------------
# Pygame Tutorial #1 - Basic Movement and Key Presses
# https://www.youtube.com/watch?v=i6xMBig-pP4
# Tech With Tim
#-------------------------------------------------------------------------------------------------------------
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)

   for event in pygame.event.get(): # this event object can be used to detect keys clicked on too but pygame.key.get_pressed() is better
        # suited for this particular functionality...of detecting the continual holding of a key for making the rectangle move. 
        if event.type == pygame.QUIT: # if user clicks on red button
            run = False               # then run == False  
    # keys that are held down...
    keys = pygame.key.get_pressed() # this checks for keys that are continually held down after the initial pressing of them.
    # checks for which key is being held down...
    if keys[pygame.K_LEFT]:
        x -= velocity  # to move left you subtract from the x coordinate
    if keys[pygame.K_RIGHT]:  
        x += velocity  # to move right you add to the x coordinate
    if keys[pygame.K_UP]:     
        y -= velocity  # to move up you subtract from the y coordinate    
    if keys[pygame.K_DOWN]:   
        y += velocity  # to move down you add to the y coordinate

    # this code fill's the screen in black before you draw the red rectangle...
    win.fill((0,0,0)) # this makes the program fill the screen black thus erasing the previously drawn red rectangles giving 
    # the appearance of the red rectangle moving and not leaving traces as it did previously without this line of code...
                      # window, rgb color for the shape, dimensions of the shape        
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # parameters...Everything in pygame is a surface
    pygame.display.update() # this refreshes the display thus showing the current code's result which is making a rectangular figure



pygame.quit()                         # and quit game... 
