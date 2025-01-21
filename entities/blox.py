import random

import pygame
from entities.entity import Entity
from entities.status import Status
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Blox(Entity):
    """
    Represents a Blox entity in the game.

    Attributes:
        name (str): The name of the Blox.
        position (pygame.Vector2): The position of the Blox.
        speed (pygame.Vector2): The speed vector of the Blox.
        status (Status): The current status of the Blox.
        recovery_time (int): The time it takes for the Blox to recover.
        radius (float): The radius of the Blox.
        random_move (bool): Whether the Blox moves randomly.
    """
    def __init__(self, name, position, speed=pygame.Vector2(1, 1), status = Status.HEALTHY, recovery_time=3,
                 radius=SCREEN_WIDTH[0] / 100 if SCREEN_HEIGHT[0] > SCREEN_WIDTH[0] else SCREEN_HEIGHT[0] / 100,
                 random_move=False):
        """
        Initializes a new Blox instance.

        Args:
            name (str): The name of the Blox.
            position (pygame.Vector2): The initial position of the Blox.
            speed (pygame.Vector2, optional): The speed vector of the Blox. Defaults to pygame.Vector2(1, 1).
            status (Status, optional): The initial status of the Blox. Defaults to Status.HEALTHY.
            recovery_time (int, optional): The time it takes for the Blox to recover. Defaults to 3.
            radius (float, optional): The radius of the Blox. Defaults to a calculated value based on screen size.
            random_move (bool, optional): Whether the Blox moves randomly. Defaults to False.
        """
        super().__init__(name, position)
        self.status = status
        self.speed = speed
        self.radius = radius
        self.status_timer = 0
        self.recovery_time = recovery_time
        self.random_move = random_move

    def move(self, screen_width, screen_height):
        """
        Moves the Blox based on its speed and handles screen boundary collisions.

        Args:
            screen_width (int): The width of the screen.
            screen_height (int): The height of the screen.
        """
        def gen_speed():
            speed = 0
            while speed == 0:
                speed = random.randint(-4, 4)
            return speed
        if self.random_move and random.randint(0, 100) < 3:
            self.speed = pygame.Vector2(gen_speed(),gen_speed())

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

    def change_state(self):
        """
        Changes the status of the Blox in a cyclic manner:
        HEALTHY -> SICK -> RECOVERED -> HEALTHY.
        Resets the status timer after changing the status.
        """
        if self.status == Status.HEALTHY:
            self.status = Status.SICK
        elif self.status == Status.SICK:
            self.status = Status.RECOVERED
        elif self.status == Status.RECOVERED:
            self.status = Status.HEALTHY
        self.status_timer = 0  # Reset the timer when status changes

    def aura(self, blox):
        """
        Infects a nearby healthy Blox if this Blox is sick, or gets infected by a nearby sick Blox.

        Args:
            blox (Blox): Another Blox instance to check for infection.
        """
        if self.status == Status.SICK and blox.status == Status.HEALTHY:
            if self.position.distance_to(blox.position) <= self.radius * 2:
                blox.change_state()
        elif blox.status == Status.SICK and self.status == Status.HEALTHY:
            if self.position.distance_to(blox.position) <= self.radius * 2:
                self.change_state()

    def update_status(self, dt):
        """
        Updates the status of the Blox based on the elapsed time.

        Args:
            dt (float): The time delta since the last update.
        """
        self.status_timer += dt
        if self.status == Status.SICK and self.status_timer >= self.recovery_time:
            self.change_state()
        elif self.status == Status.RECOVERED and self.status_timer >= self.recovery_time / 2:
            self.change_state()