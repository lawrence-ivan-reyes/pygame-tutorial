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
from golden_snitch import GoldenSnitch

pygame.init()

pygame.font.init()
font = pygame.font.Font('./font/HARRYP__.TTF', 30)
rules_font = pygame.font.Font('./font/HARRYP__.TTF', 20)  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# stretch challenge - adding sounds
game_over_sound = pygame.mixer.Sound('./sounds/over.mp3') 
point_sound = pygame.mixer.Sound('./sounds/point.mp3') 
background_music = './sounds/background.mp3' 
snitch_sound = pygame.mixer.Sound('./sounds/snitch.mp3') 

background_image = pygame.image.load("./images/background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

ron = Ron()
hermione = Hermione()
player = Player() # reminder that this is harry
voldemort = Voldemort()
float1 = Floating()
float2 = Floating()
float3 = Floating()
snitch = GoldenSnitch()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ron)
all_sprites.add(hermione)
all_sprites.add(voldemort)
all_sprites.add(float1)
all_sprites.add(float2)
all_sprites.add(float3)
all_sprites.add(snitch)

point_sprites = pygame.sprite.Group()
point_sprites.add(ron)
point_sprites.add(hermione)  
point_sprites.add(snitch)

# for stretch challenge
game_state = 'ready'
score = 0

running = True
while running:
    if game_state == 'ready':
        # stretch challenge: adding the starting screen
        screen.blit(background_image, (0, 0))

        title_font = pygame.font.Font('./font/HARRYP__.TTF', 40)  
        title_text = title_font.render("Harry's Great Escape", True, (255, 255, 255)) 
        screen.blit(title_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 120)) 

        rules_text1 = rules_font.render("Catch Ron or Hermione: +1 point", True, (255, 255, 255))
        rules_text2 = rules_font.render("Catch the Golden Snitch: +5 points", True, (255, 255, 255))
        rules_text3 = rules_font.render("Voldemort hits Ron/Hermione/Golden Snitch: Lose 1/1/5 points", True, (255, 255, 255))
        rules_text4 = rules_font.render("Hit by Voldemort: Game Over!", True, (255, 255, 255))
        rules_text5 = rules_font.render("Press any key to start", True, (255, 255, 255))

        screen.blit(rules_text1, (50, SCREEN_HEIGHT // 2 - 60)) 
        screen.blit(rules_text2, (50, SCREEN_HEIGHT // 2 - 20))
        screen.blit(rules_text3, (50, SCREEN_HEIGHT // 2 + 20))
        screen.blit(rules_text4, (50, SCREEN_HEIGHT // 2 + 60))
        screen.blit(rules_text5, (50, SCREEN_HEIGHT // 2 + 100))

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(background_music)
            pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game_state = 'playing'
                pygame.mixer.music.rewind()

    elif game_state == 'playing':
        screen.fill((255, 255, 255))

        screen.blit(background_image, (0, 0))

        for entity in all_sprites:
            entity.move()
            entity.render(screen)

        point = pygame.sprite.spritecollideany(player, point_sprites)
        if point:
            if isinstance(point, GoldenSnitch): 
                score += 5
                snitch_sound.play() # plays only when the golden snitch is caught
            else:
                score += 1
                point_sound.play()  
            point.reset()

        # stretch challenge: reduce points when voldemort collides with hermione, ron, or golden snitch
        collided_points = pygame.sprite.spritecollideany(voldemort, point_sprites)
        if collided_points:
            if isinstance(collided_points, GoldenSnitch):
                score -= 5  # lose 5 points for snitch
            else:
                score -= 1  # lose 1 point for ron or hermione
            collided_points.reset()

        if pygame.sprite.collide_rect(player, voldemort):
            game_over_sound.play()  # ill play the game over sound effect here
            game_state = 'game_over'

        if not pygame.mixer.music.get_busy():  
            pygame.mixer.music.load(background_music)
            pygame.mixer.music.play(-1)  # -1 to loop indefinitely (until the game resets)

        # for score stretch challenge
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  
        screen.blit(score_text, (10, 10)) 

    elif game_state == 'game_over':
        player.reset()
        ron.reset()
        hermione.reset()
        voldemort.reset()
        float1.reset()
        float2.reset()
        float3.reset()
        game_state = 'playing'
        pygame.mixer.music.stop()
        score = 0

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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
