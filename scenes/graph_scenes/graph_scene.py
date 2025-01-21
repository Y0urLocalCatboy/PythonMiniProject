import pygame

from scenes.graph_scenes.end_scene import end_scene
from scenes.graph_scenes.limits_scene import limits_scene
from scenes.graph_scenes.time_scene import time_scene
from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import button, hover_over

def graph_scene(screen, clock, running):
    button_width = 200
    button_height = 50
    spacing = SCREEN_HEIGHT[0] // 8

    button_x = (SCREEN_WIDTH[0] - button_width) / 2
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2 - 2 * spacing

    back_button = [button_x, button_y, button_width, button_height, "Back"]
    end_scene_button = [button_x, button_y + spacing, button_width, button_height, "End Scene"]
    limits_scene_button = [button_x, button_y + 2 * spacing, button_width, button_height, "Limits Scene"]
    time_scene_button = [button_x, button_y + 3 * spacing, button_width, button_height, "Time Scene"]

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    while running[0]:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(back_button, mouse):
                    return
                if hover_over(end_scene_button, mouse):
                    end_scene(screen, clock, running)
                    return
                if hover_over(limits_scene_button, mouse):
                    limits_scene(screen, clock, running)
                    return
                if hover_over(time_scene_button, mouse):
                    time_scene(screen, clock, running)
                    return

        screen.fill("white")
        button(back_button, mouse, screen, font)
        button(end_scene_button, mouse, screen, font)
        button(limits_scene_button, mouse, screen, font)
        button(time_scene_button, mouse, screen, font)

        pygame.display.flip()
        clock.tick(FPS[0])
