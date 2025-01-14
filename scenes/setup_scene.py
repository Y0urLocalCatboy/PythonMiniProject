import pygame

from scenes.loading_scene import loading_scene
from scenes.main_scene import main_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MUSIC_SWITCH, BASE_SIZE
from utils.scene_utils import button, hover_over, music_on_off, change_size


def setup_scene(screen, clock, running):
    loading_scene(screen)

    # font initialization
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    # button position and size
    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2  # rectangle isn't centered by default
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2
    spacing = SCREEN_HEIGHT[0] // 6  # spacing between buttons

    # button initialization
    confirm_button = [button_x, button_y + spacing,
                      button_width, button_height,
                      "Confirm"]
    while running[0]:

        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(confirm_button, mouse):
                    main_scene(running)
            if not running[0]:
                break

        # button drawing
        button(confirm_button, mouse, screen, font)



        pygame.display.flip()
        clock.tick(FPS[0])