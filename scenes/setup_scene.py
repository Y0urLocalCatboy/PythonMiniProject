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

    # Text input box settings
    bloxes_amount_input_box = pygame.Rect(50, 50, 200, 40)
    input_text = "10"
    active = False

    while running[0]:

        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running[0] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(confirm_button, mouse):
                    main_scene(screen, clock, running, amount=int(input_text))
                # If the user clicked on the input box, toggle the active variable
                if bloxes_amount_input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print("Entered text:", input_text)
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
        if not running[0]:
            break


        # button drawing
        button(confirm_button, mouse, screen, font)

        # Render the input box
        color = (200, 200, 200) if active else (0, 0, 0)
        pygame.draw.rect(screen, color, bloxes_amount_input_box, 2)

        # Render the text
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (bloxes_amount_input_box.x + 5, bloxes_amount_input_box.y + 5))
        bloxes_amount_input_box.w = max(200, text_surface.get_width() + 10)

        pygame.display.flip()
        clock.tick(FPS[0])