import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:
    
    pygame.draw.ellipse(window, (255, 255, 255),
                               (100, 100, 550, 550))
    pygame.display.update()
    
    

