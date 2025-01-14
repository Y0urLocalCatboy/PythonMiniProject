import os
import time
import pygame


from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MUSIC_SWITCH
from utils.scene_utils import draw_background_image, music_on_off


def loading_scene(screen):
    draw_background_image(screen, "assets/images/loading.webp")
    pygame.display.update()
    time.sleep(1)
    return