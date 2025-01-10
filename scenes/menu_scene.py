import pygame

from scenes.loading_scene import loading_scene
from scenes.main_scene import main_scene
from scenes.settings_scene import settings_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import button, hover_over

def menu_scene(running):
    # pygame initialization
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH[0], SCREEN_HEIGHT[0]))
    loading_scene(screen)

    # font initialization
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    # button position and size
    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2 # rectangle isn't centered by default
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2
    spacing = SCREEN_HEIGHT[0] // 6 # spacing between buttons

    # button initialization
    main_scene_button = [button_x, button_y - spacing,
                         button_width, button_height,
                         "Start"]

    settings_button = [button_x, button_y,
                       button_width, button_height,
                       "Settings"]

    exit_button = [button_x, button_y + spacing,
                   button_width, button_height,
                   "Exit"]

    while running[0]:

        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(main_scene_button, mouse):
                    main_scene(screen, clock, running)
                elif hover_over(exit_button, mouse):
                    running[0] = False
                    break
                elif hover_over(settings_button, mouse):
                    settings_scene(screen, clock, running)
        if not running[0]:
            break

        # button drawing
        button(main_scene_button, mouse, screen, font)
        button(settings_button, mouse, screen, font)
        button(exit_button, mouse, screen, font)

        pygame.display.flip()
        clock.tick(FPS[0])

    pygame.quit()


