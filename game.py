import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

surf = pygame.Surface((50, 50))  
surf.fill((255, 111, 33))  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    pygame.display.flip()

    screen.fill((255, 255, 255))  
    screen.blit(surf, (100, 120))  
    pygame.display.flip()        

pygame.quit()
