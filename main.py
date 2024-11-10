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

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game_over_sound = pygame.mixer.Sound('./sounds/game_over.mp3') # stretch challenge
point_sound = pygame.mixer.Sound('./sounds/point.mp3')  # stretch challenge

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

point_sprites = pygame.sprite.Group()
point_sprites.add(ron)
point_sprites.add(hermione)  

# for stretch challenge
game_state = 'playing'

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
    
    if game_state == 'playing':
        screen.fill((255, 255, 255))

        screen.blit(background_image, (0, 0))

        for entity in all_sprites:
            entity.move()
            entity.render(screen)

        point = pygame.sprite.spritecollideany(player, point_sprites)
        if point:
            point_sound.play()
            point.reset()

        if pygame.sprite.collide_rect(player, voldemort):
            game_over_sound.play()  # ill play the game over sound effect here
            game_state = 'game_over'

    elif game_state == 'game_over':
        player.reset()
        ron.reset()
        hermione.reset()
        voldemort.reset()
        float1.reset()
        float2.reset()
        float3.reset()
        game_state = 'playing'

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
