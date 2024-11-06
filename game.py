import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

apple = './images/apple.png'
strawberry = './images/strawberry.png'

objects = [
    GameObject(50, 50, './images/apple.png'), # row 1
    GameObject(150, 50, './images/strawberry.png'),
    GameObject(250, 50, './images/apple.png'),

    GameObject(50, 150, './images/strawberry.png'), #row 2
    GameObject(150, 150, './images/apple.png'),
    GameObject(250, 150, './images/strawberry.png'),

    GameObject(50, 250, './images/apple.png'), # row 3
    GameObject(150, 250, './images/strawberry.png'),
    GameObject(250, 250, './images/apple.png')
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    # apple.render(screen)
    # strawberry.render(screen)

    for obj in objects:
        obj.render(screen) # added to render every GameObject in the list for challegne 2
     
    pygame.display.flip()    

pygame.quit()
