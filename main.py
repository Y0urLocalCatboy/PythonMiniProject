import pygame

from scenes.menu_scene import menu_scene
from utils.config import RUNNING

if __name__ == "__main__":
    """
    Main function to initialize the game and start the menu scene.
    """
    pygame.init()
    menu_scene(RUNNING)
    pygame.quit()