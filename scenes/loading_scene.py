import os
import time
import pygame


from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import draw_background


def loading_scene(screen):
    draw_background(screen, "assets/images/loading.webp")
    pygame.display.update()
    music = pygame.mixer.music.load('assets/sounds/background_music.mid')
    pygame.mixer.music.play(-1)
    time.sleep(1)
    return