import time
import pygame

from utils.scene_utils import draw_background_image, music_on_off


def loading_scene(screen):
    """
    Display the loading scene with a background image.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
    """

    draw_background_image(screen, "assets/images/loading.webp")

    pygame.display.update()

    time.sleep(1)

    return