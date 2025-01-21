import time
import pygame

from utils.scene_utils import draw_background_image, music_on_off


def loading_scene(screen):
    """
    Display the loading scene with a background image.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
    """
    # Draw the background image for the loading scene
    draw_background_image(screen, "assets/images/loading.webp")

    # Update the display to show the loading image
    pygame.display.update()

    # Pause for a short duration to simulate loading time
    time.sleep(1)

    return