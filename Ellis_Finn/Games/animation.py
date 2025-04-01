import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255,0,0), (random.randient(
0, windowwidth), random.randint(0, windowHeight), 10, 10))
    
    greenSquareX = windowWidth / 2
    greenSquareY = windowHeight / 2
    
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0, 255, 0),
     (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 1
    pygame.draw.rect(surface, (0, 0, 255),
        (blueSquareX, BlueSquareY, 10, 10))
    
    blueSquareX = 0.0
    blueSquareY = 0.0
    blueSquareVX = 1
    blueSquareVY = 1
    
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0, 0, 255),
        (blueSquareX, blueSquareY, 10, 10))
    blueSquareX += blueSquareVX 
    blueSquareY += blueSquareVY 
    blueSquareVX += 0.1
    blueSquareVY += 0.1
    blueSquare
    
    
