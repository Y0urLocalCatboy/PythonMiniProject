import pygame

from scenes.loading_scene import loading_scene
from scenes.main_scene import main_scene
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.scene_utils import button, hover_over

def setup_scene(screen, clock, running):
    """
    Display the setup scene where the user can specify the number of bloxes, recovery time, and initial ill bloxes.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        clock (pygame.time.Clock): The clock to control the frame rate.
        running (list): A list containing a single boolean element to control the running state.
    """
    loading_scene(screen)

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    bloxes_amount_input_box = pygame.Rect((SCREEN_WIDTH[0] - 200) / 2, SCREEN_HEIGHT[0] / 6, 200, 40)
    recovery_time_input_box = pygame.Rect((SCREEN_WIDTH[0] - 200) / 2, SCREEN_HEIGHT[0] / 6 + 100, 200, 40)
    ill_bloxes_amount_input_box = pygame.Rect((SCREEN_WIDTH[0] - 200) / 2, SCREEN_HEIGHT[0] / 6 + 200, 200, 40)

    amount_input_text = "100"
    recovery_time = "5"
    ill_bloxes_amount = "2"

    amount_of_bloxes_active = False
    recovery_time_active = False
    ill_bloxes_amount_active = False

    error_message = ""
    random_move = False

    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2
    button_y = ill_bloxes_amount_input_box.y + 120  # Adjusted to be lower

    confirm_button = [button_x, button_y + 80, button_width, button_height, "Confirm"]
    random_move_button = [button_x - 25, button_y - 50, button_width + 50, button_height, "Random move"]

    while running[0]:

        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(confirm_button, mouse):
                    try:
                        amount = int(amount_input_text)
                        recovery = int(recovery_time) + 1
                        ill_amount = int(ill_bloxes_amount)
                        main_scene(screen, clock, running, amount=amount, ill_amount=ill_amount, recovery_time=recovery, random_move=random_move)
                    except ValueError:
                        error_message = "Please enter valid numbers!"
                elif hover_over(random_move_button, mouse):
                    random_move = not random_move
                if bloxes_amount_input_box.collidepoint(event.pos):
                    amount_of_bloxes_active = True
                    recovery_time_active = False
                    ill_bloxes_amount_active = False
                elif recovery_time_input_box.collidepoint(event.pos):
                    amount_of_bloxes_active = False
                    recovery_time_active = True
                    ill_bloxes_amount_active = False
                elif ill_bloxes_amount_input_box.collidepoint(event.pos):
                    amount_of_bloxes_active = False
                    recovery_time_active = False
                    ill_bloxes_amount_active = True
                else:
                    amount_of_bloxes_active = False
                    recovery_time_active = False
                    ill_bloxes_amount_active = False
            elif event.type == pygame.KEYDOWN:
                if amount_of_bloxes_active:
                    if event.key == pygame.K_RETURN:
                        amount_input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        amount_input_text = amount_input_text[:-1]
                    else:
                        amount_input_text += event.unicode
                elif recovery_time_active:
                    if event.key == pygame.K_RETURN:
                        recovery_time = ""
                    elif event.key == pygame.K_BACKSPACE:
                        recovery_time = recovery_time[:-1]
                    else:
                        recovery_time += event.unicode
                elif ill_bloxes_amount_active:
                    if event.key == pygame.K_RETURN:
                        ill_bloxes_amount = ""
                    elif event.key == pygame.K_BACKSPACE:
                        ill_bloxes_amount = ill_bloxes_amount[:-1]
                    else:
                        ill_bloxes_amount += event.unicode
        if not running[0]:
            break

        button(confirm_button, mouse, screen, font)
        button(random_move_button, mouse, screen, font)

        label_surface = font.render("Specify amount of bloxes:", True, (0, 0, 0))
        label_rect = label_surface.get_rect(center=(SCREEN_WIDTH[0] / 2, bloxes_amount_input_box.y - 40))
        screen.blit(label_surface, label_rect)

        recovery_label_surface = font.render("Specify time to recovery:", True, (0, 0, 0))
        recovery_label_rect = recovery_label_surface.get_rect(center=(SCREEN_WIDTH[0] / 2, recovery_time_input_box.y - 40))
        screen.blit(recovery_label_surface, recovery_label_rect)

        ill_bloxes_label_surface = font.render("Starting number of Ill bloxes:", True, (0, 0, 0))
        ill_bloxes_label_rect = ill_bloxes_label_surface.get_rect(center=(SCREEN_WIDTH[0] / 2, ill_bloxes_amount_input_box.y - 40))
        screen.blit(ill_bloxes_label_surface, ill_bloxes_label_rect)

        color = (200, 200, 200) if amount_input_text != "" else (0, 0, 0)
        pygame.draw.rect(screen, color, bloxes_amount_input_box, 2)

        recovery_color = (200, 200, 200) if recovery_time else (0, 0, 0)
        pygame.draw.rect(screen, recovery_color, recovery_time_input_box, 2)

        ill_bloxes_color = (200, 200, 200) if ill_bloxes_amount else (0, 0, 0)
        pygame.draw.rect(screen, ill_bloxes_color, ill_bloxes_amount_input_box, 2)

        text_surface = font.render(amount_input_text, True, "black")
        screen.blit(text_surface, (bloxes_amount_input_box.x + 5, bloxes_amount_input_box.y + 5))
        bloxes_amount_input_box.w = max(200, text_surface.get_width() + 10)

        recovery_text_surface = font.render(recovery_time, True, "black")
        screen.blit(recovery_text_surface, (recovery_time_input_box.x + 5, recovery_time_input_box.y + 5))
        recovery_time_input_box.w = max(200, recovery_text_surface.get_width() + 10)

        ill_bloxes_text_surface = font.render(ill_bloxes_amount, True, "black")
        screen.blit(ill_bloxes_text_surface, (ill_bloxes_amount_input_box.x + 5, ill_bloxes_amount_input_box.y + 5))
        ill_bloxes_amount_input_box.w = max(200, ill_bloxes_text_surface.get_width() + 10)

        if error_message:
            error_surface = font.render(error_message, True, (255, 0, 0))
            error_rect = error_surface.get_rect(center=(SCREEN_WIDTH[0] / 2, confirm_button[1] - 30))
            screen.blit(error_surface, error_rect)

        random_move_text = "Random move on" if random_move else "Random move off"
        random_move_surface = font.render(random_move_text, True, (0, 0, 0))
        random_move_rect = random_move_surface.get_rect(center=(button_x + button_width / 2, button_y + 10))
        screen.blit(random_move_surface, random_move_rect)

        pygame.display.flip()
        clock.tick(FPS[0])