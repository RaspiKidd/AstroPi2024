import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')
squareX = 0
squareY = 0

greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2
    
blueSquareX = 0.0
blueSquareY = 0.0
blueSquareVX = 1
blueSquareVY = 1

while True:
    
    # chunk 1

    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255,0,0), (random.randint(
0, windowWidth), random.randint(0, windowHeight), 10, 10))
    
   #chunk 2
    
   
    pygame.draw.rect(surface, (0, 255, 0),
     (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 1
    greenSquareY += 1
    
    # chunk 3
    
    pygame.draw.rect(surface, (0, 0, 255),
        (blueSquareX, blueSquareY, 10, 10))
    
    blueSquareX += blueSquareVX 
    blueSquareY += blueSquareVY 
    blueSquareVX += 0.1
    blueSquareVY += 0.1
    
    # chunk 4
    
rectX = windowWidth / 2
rectY = windowHeight / 2
rectWidth = 50
rectHeight = 50
    pygame.draw.rect(surface, (255,255,0), (
rectX-rectWidth /2, rectY-rectHeight /2, rectWidth,rectHeight))
    
    #page 24 of the dinner.
    
    
    #bottom1 (Ellis):)
    
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
    