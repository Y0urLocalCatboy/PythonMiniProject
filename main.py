import pygame

from scenes.menu_scene import menu_scene

if __name__ == "__main__":
    running = [True]
    pygame.init()
    menu_scene(running)
    pygame.quit()