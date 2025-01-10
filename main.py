import pygame

from scenes.menu_scene import menu_scene
from utils.config import running

if __name__ == "__main__":
    pygame.init()
    menu_scene(running)
    pygame.quit()