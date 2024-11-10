from gameobject import GameObject
from random import randint, choice
from constants import lanes

class Hermione(GameObject):
    def __init__(self):
        super(Hermione, self).__init__(0, 0, './images/hermione.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500: 
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice(lanes)