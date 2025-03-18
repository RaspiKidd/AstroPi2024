import pygame
pygame.init()
window = pygame.display.set_mode((500, 400))
while True:
    pygame.draw.rect(window, (255, 0, 0),
                             (0, 0, 50, 50))
    
    pygame.draw.rect(window, (0, 0, 255),                     
                             (80, 0, 50, 50))
    
    pygame.draw.rect(window, (0, 255, 0),
                             (40, 0, 50, 50))
    pygame.display.update()
