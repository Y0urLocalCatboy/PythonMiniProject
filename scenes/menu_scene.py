import pygame

from scenes.graph_scenes.graph_scene import graph_scene
from scenes.loading_scene import loading_scene
from scenes.settings_scene import settings_scene
from scenes.setup_scene import setup_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import button, hover_over, music_on_off

def menu_scene(running):
    """
    Display the main menu scene with options to start the simulation, adjust settings, or exit.

    Args:
        running (list): A list containing a single boolean element to control the running state.
    """

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH[0], SCREEN_HEIGHT[0]))
    music_on_off("assets/sounds/background_music.mid")
    loading_scene(screen)

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2
    spacing = SCREEN_HEIGHT[0] // 6

    main_scene_button = [button_x, button_y - spacing,
                         button_width, button_height,
                         "Start"]

    settings_button = [button_x, button_y,
                       button_width, button_height,
                       "Settings"]

    exit_button = [button_x, button_y + spacing,
                   button_width, button_height,
                   "Exit"]

    generate_graph_button = [button_x + spacing * 1.5, button_y - 2.5 * spacing,
                             button_width + spacing / 2, button_height,
                             "Generate Graph"]

    error_message = ""

    while running[0]:
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(main_scene_button, mouse):
                    setup_scene(screen, clock, running)
                elif hover_over(exit_button, mouse):
                    running[0] = False
                    break
                elif hover_over(settings_button, mouse):
                    settings_scene(screen, clock, running)
                elif hover_over(generate_graph_button, mouse):
                    graph_scene(screen, clock, running)
        if not running[0]:
            break

        button(main_scene_button, mouse, screen, font)
        button(settings_button, mouse, screen, font)
        button(exit_button, mouse, screen, font)
        button(generate_graph_button, mouse, screen, font)

        if error_message:
            error_surface = font.render(error_message, True, (255, 0, 0))
            error_rect = error_surface.get_rect(center=(SCREEN_WIDTH[0] / 2, generate_graph_button[1] + 60))
            screen.blit(error_surface, error_rect)

        pygame.display.flip()
        clock.tick(FPS[0])

    pygame.quit()