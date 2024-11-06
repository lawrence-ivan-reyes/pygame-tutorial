import pygame 
pygame.init()

screen = pygame.display.set_mode((500, 500))

running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    color = (255, 0, 255)
    position = (250, 250)  
    pygame.draw.circle(screen, color, position, 75)

    pygame.display.flip()
