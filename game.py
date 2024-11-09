import pygame
from random import randint, choice

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
lanes = [93, 218, 343]

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, './images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500: 
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = -64

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, './images/player.png')  
        self.dx = 0 
        self.dy = 0
        self.pos_x = 1 
        self.pos_y = 1
        self.reset()
    
    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y
    
    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

# challenge for pt 5
class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, './images/bomb.png')  
        self.dx = 0 
        self.dy = 0 
        self.reset()  # thuis is b/c i want the bomb to start at a random direction

    def reset(self):
        direction = choice(["up", "down", "left", "right"]) # to pick a random direction

        if direction == "up":
            self.dy = -5  
            self.dx = 0  
        elif direction == "down":
            self.dy = 5 
            self.dx = 0  
        elif direction == "left":
            self.dx = -5 
            self.dy = 0  
        elif direction == "right":
            self.dx = 5  
            self.dy = 0   

        self.x = choice(lanes) 
        self.y = -64  # this is so the bomb starts off-screen (above the screen)

    def move(self):
        self.x += self.dx  
        self.y += self.dy 
        
        # to reset the bomb if it goes off the screen
        if self.x < 0 or self.x > 500 or self.y < 0 or self.y > 500:
            self.reset()  # here, the bomb will start over in a new random direction


apple = Apple()
player = Player()
bomb = Bomb()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(bomb)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()  
            elif event.key == pygame.K_RIGHT:
                player.right()  
            elif event.key == pygame.K_UP:
                player.up()  
            elif event.key == pygame.K_DOWN:
                player.down() 

    screen.fill((255, 255, 255))

    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    pygame.display.flip() 
    clock.tick(60)

pygame.quit()
