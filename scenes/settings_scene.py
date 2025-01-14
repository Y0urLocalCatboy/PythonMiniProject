import pygame

from scenes.loading_scene import loading_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MUSIC_SWITCH, BASE_SIZE
from utils.scene_utils import button, hover_over, music_on_off, change_size


def settings_scene(screen, clock, running):
    from scenes.menu_scene import menu_scene
    loading_scene(screen)

    # setting up the sizes for the game
    sizes = [BASE_SIZE,[800, 600], [800, 800], [1000, 1000], [1280, 720]]

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
                    MUSIC_SWITCH[0] = not MUSIC_SWITCH[0]
                    music_on_off("assets/sounds/background_music.mid")
                elif hover_over(change_size_button, mouse):
                    current_height = pygame.display.get_surface().get_size()[1]
                    if current_height == 400:
                        change_size(sizes[1][0], sizes[1][1])
                    elif current_height == 600:
                        change_size(sizes[2][0], sizes[2][1])
                    elif current_height == 800:
                        change_size(sizes[3][0], sizes[3][1])
                    elif current_height == 1000:
                        change_size(sizes[4][0], sizes[4][1])
                    else:
                        change_size(sizes[0][0], sizes[0][1])
                    # match current_height:
                    #     case 600:
                    #         change_size(sizes[1][0], sizes[1][1])
                    #     case 800:
                    #         change_size(sizes[2][0], sizes[2][1])
                    #     case 1000:
                    #         change_size(sizes[3][0], sizes[3][1])
                    #     case _:
                    #         change_size(sizes[0][0], sizes[0][1])
                    settings_scene(screen, clock, running)
                elif hover_over(confirm_button, mouse):
                    menu_scene(running)
            if not running[0]:
                break

        # button drawing
        button(sound_button, mouse, screen, font)
        button(change_size_button, mouse, screen, font)
        button(confirm_button, mouse, screen, font)



        pygame.display.flip()
        clock.tick(FPS[0])