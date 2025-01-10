import os
import time
import pygame


from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, music_switch
from utils.scene_utils import draw_background_image, music_on_off


def loading_scene(screen):
    draw_background_image(screen, "assets/images/loading.webp")
    pygame.display.update()
    music_on_off("assets/sounds/background_music.mid")
    time.sleep(1)
    return