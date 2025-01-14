import time

import pygame
from entities.blox import Blox
from entities.building import Building
from entities.status import Status
from scenes.loading_scene import loading_scene
from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import draw_road, draw_bloxes


def main_scene(screen, clock, running):
    loading_scene(screen)

    bloxes = [
        Blox("Blox1", pygame.Vector2(200, 200), Status.HEALTHY, pygame.Vector2(0, 2)),
        Blox("Blox2", pygame.Vector2(300, 300), Status.SICK, pygame.Vector2(-2, 3)),
        Blox("Blox3", pygame.Vector2(400, 400), Status.RECOVERED),
    ]
    hospital = Building("Hospital", pygame.Vector2(500, 500), 10, bloxes)

    while running[0]:
        draw_road(screen, SCREEN_WIDTH[0], SCREEN_HEIGHT[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False

        # Building
        pygame.draw.rect(screen, "gray", (*hospital.position, SCREEN_WIDTH[0] / 10, SCREEN_HEIGHT[0] / 10))

        # Bloxes
        draw_bloxes(screen, bloxes)
        for blox in bloxes:
            blox.move(screen.get_width(), screen.get_height())
        pygame.display.flip()
        clock.tick(FPS[0])