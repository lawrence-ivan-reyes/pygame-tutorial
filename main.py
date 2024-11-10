import pygame
from random import randint, choice

# importing from my new constants.py
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, lanes

# importing game objects from their respective files
from gameobject import GameObject
from ron import Ron
from hermione import Hermione
from voldemort import Voldemort
from player import Player  # reminder: this is harry
from floating import Floating

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load("./images/background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

ron = Ron()
hermione = Hermione()
player = Player() # this is now harry potter
voldemort = Voldemort()
float1 = Floating()
float2 = Floating()
float3 = Floating()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ron)
all_sprites.add(hermione)
all_sprites.add(voldemort)
all_sprites.add(float1)
all_sprites.add(float2)
all_sprites.add(float3)

fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(ron)
fruit_sprites.add(hermione)  

pygame.init()

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

    screen.blit(background_image, (0, 0))

    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()

    if pygame.sprite.collide_rect(player, voldemort):
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
