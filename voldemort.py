from gameobject import GameObject
from random import randint, choice
from constants import lanes

class Voldemort(GameObject):
    def __init__(self):
        super(Voldemort, self).__init__(0, 0, './images/voldemort.png')
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        # adding to choose a random direction (0: up, 1: down, 2: left, 3: right)
        direction = randint(0, 3)
        # calculating speed first, to avoid repetition
        speed = (randint(0, 200) / 100) + 3 # a little faster to make it harder

        if direction == 0:  # up
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
            self.dy = -speed 
        elif direction == 1:  # down
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = speed
        elif direction == 2:  # left
            self.x = 500
            self.y = choice(lanes)
            self.dx = -speed
            self.dy = 0
        elif direction == 3:  # right
            self.x = -64
            self.y = choice(lanes)
            self.dx = speed
            self.dy = 0
