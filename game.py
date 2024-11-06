import pygame
pygame.init()

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 255))  
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

box = GameObject(120, 300, 50, 50)  

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
    box.render(screen)           
    pygame.display.flip()    

pygame.quit()
