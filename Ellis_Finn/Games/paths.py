import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:
    
    pygame.draw.lines(window,(255,255,255), True, ((
    50, 50), (75, 75), (63,100), (38, 100), (25, 75)), 1)
    
    pygame.display.update()
    
    