import pygame
from entities.blox import Blox
from entities.status import Status
from scenes.loading_scene import loading_scene
from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT

def main_scene(screen, clock, running):
    loading_scene(screen)

    bloxes = [
        Blox("Blox1", Status.HEALTHY, pygame.Vector2(200, 200)),
        Blox("Blox2", Status.SICK, pygame.Vector2(300, 300)),
        Blox("Blox3", Status.RECOVERED, pygame.Vector2(400, 400)),
    ]

    while running[0]:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False

        for blox in bloxes:
            pygame.draw.circle(screen, blox.status.get_color(), blox.position, SCREEN_WIDTH / 100 if  SCREEN_HEIGHT > SCREEN_WIDTH else SCREEN_HEIGHT / 100)

        pygame.display.flip()
        clock.tick(FPS)