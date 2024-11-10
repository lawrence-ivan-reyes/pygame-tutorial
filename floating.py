import pygame
import random
from gameobject import GameObject
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Floating(GameObject):
    def __init__(self):
        floating_images = ['./images/float1.png', './images/float2.png', './images/float3.png'] 
        image_path = random.choice(floating_images)
        super(Floating, self).__init__(0, 0, image_path)
        self.dx = random.randint(1, 3)  # want it to move a lot more slowly than my actual playing characters
        self.reset()

    def move(self):
        self.x += self.dx
        if self.x > SCREEN_WIDTH:
            self.reset()

    def reset(self):
        self.x = -64  
        self.y = random.randint(0, SCREEN_HEIGHT - 64)  # random y position within the screen
        floating_images = ['./images/float1.png', './images/float2.png', './images/float3.png']
        image_path = random.choice(floating_images)
        self.surf = pygame.image.load(image_path)  
