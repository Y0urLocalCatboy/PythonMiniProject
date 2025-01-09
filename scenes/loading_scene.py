import time
import pygame


from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import draw_background


def loading_scene(screen):
    draw_background(screen, "assets/loading.webp")
    pygame.display.update()
    time.sleep(1)
    return