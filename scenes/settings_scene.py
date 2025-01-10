import pygame

from scenes.loading_scene import loading_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import button, hover_over

def settings_scene(screen, clock, running):
    from scenes.menu_scene import menu_scene
    loading_scene(screen)

    # font initialization
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    # button position and size
    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH - button_width) / 2  # rectangle isn't centered by default
    button_y = (SCREEN_HEIGHT - button_height) / 2
    spacing = SCREEN_HEIGHT // 6  # spacing between buttons

    # button initialization
    sound_button = [button_x, button_y - spacing,
                         button_width, button_height,
                         "Change Sound"]

    change_size_button = [button_x, button_y,
                       button_width, button_height,
                       "Change Size"]

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
                if hover_over(sound_button, mouse):
                    print("Change Sound")
                elif hover_over(change_size_button, mouse):
                    print("Change Size")
                elif hover_over(confirm_button, mouse):
                    menu_scene(screen, clock, running)
            if not running[0]:
                break

        # button drawing
        button(sound_button, mouse, screen, font)
        button(change_size_button, mouse, screen, font)
        button(confirm_button, mouse, screen, font)



        pygame.display.flip()
        clock.tick(FPS)