import pygame

from scenes.loading_scene import loading_scene
from scenes.menu_scene import menu_scene

if __name__ == "__main__":
    running = [True]
    pygame.init()
    menu_scene(running)
    pygame.quit()