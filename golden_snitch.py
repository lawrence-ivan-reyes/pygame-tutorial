from gameobject import GameObject
from random import randint, choice
from constants import lanes

class GoldenSnitch(GameObject):
    def __init__(self):
        super(GoldenSnitch, self).__init__(0, 0, './images/snitch.png')  
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:  # want this to come from either horizontal or vertical axes
            self.reset()

    def reset(self):
        direction = randint(0, 1)  
        speed = (randint(0, 500) / 100) + 5  # want it to be faster so it's harder to catch

        if direction == 0:  
            self.x = -64  
            self.y = choice(lanes)
            self.dx = speed
            self.dy = 0
        else:  
            self.x = choice(lanes)
            self.y = -64  
            self.dx = 0
            self.dy = speed
