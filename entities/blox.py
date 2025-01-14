import pygame

from entities.entity import Entity
from entities.status import Status
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Blox(Entity):

    def __init__(self, name, position, status, speed=pygame.Vector2(1, 1),
                 radius=
                 SCREEN_WIDTH[0] / 100
                 if  SCREEN_HEIGHT[0] > SCREEN_WIDTH[0]
                 else SCREEN_HEIGHT[0] / 100):
        super().__init__(name, position)
        self.status = status
        self.speed = speed
        self.radius = radius

    def move(self, screen_width, screen_height):
        self.position += self.speed

        # Position correction if the Blox is going out of the screen
        if self.position.x - self.radius < 0:  # Left border
            self.position.x = self.radius
            self.speed.x *= -1

        if self.position.x + self.radius > screen_width:  # Right border
            self.position.x = screen_width - self.radius
            self.speed.x *= -1

        if self.position.y - self.radius < 0:  # Upper border
            self.position.y = self.radius
            self.speed.y *= -1

        if self.position.y + self.radius > screen_height:  # Lower border
            self.position.y = screen_height - self.radius
            self.speed.y *= -1

    def change_status(self):
        if self.status == Status.HEALTHY:
            self.status = Status.SICK
        elif self.status == Status.SICK:
            self.status = Status.RECOVERED
        elif self.status == Status.RECOVERED:
            self.status = Status.HEALTHY
