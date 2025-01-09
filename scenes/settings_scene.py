import pygame

from scenes.loading_scene import loading_scene
from scenes.main_scene import main_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import button, hover_over

def settings_scene(screen, clock, running):
    loading_scene(screen)
    # button position and size
    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH - button_width) / 2  # rectangle isn't centered by default
    button_y = (SCREEN_HEIGHT - button_height) / 2
    spacing = SCREEN_HEIGHT // 6  # spacing between buttons
    # button initialization
    sound_button = [button_x, button_y - spacing,
                         button_width, button_height,
                         "Change Sound"]

    change_size_button = [button_x, button_y,
                       button_width, button_height,
                       "Change Size"]

    confirm_button = [button_x, button_y + spacing,
                      button_width, button_height,
                      "Confirm"]
    while running[0]:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False



        pygame.display.flip()
        clock.tick(FPS)