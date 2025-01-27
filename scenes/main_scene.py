import time
import pygame
from entities.blox import Blox
from entities.status import Status
from scenes.loading_scene import loading_scene
from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import draw_road, draw_bloxes, generate_bloxes, gen_speed, button, hover_over
import pandas as pd
import os

def main_scene(screen, clock, running, amount, ill_amount, recovery_time, random_move):
    """
    Main scene of the simulation where the bloxes interact.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        clock (pygame.time.Clock): The clock to control the frame rate.
        running (list): A list containing a single boolean element to control the running state.
        amount (int): The initial number of bloxes.
        ill_amount (int): The initial number of sick bloxes.
        recovery_time (int): The time it takes for a blox to recover.
        random_move (bool): Whether the bloxes move randomly.
    """
    loading_scene(screen)

    bloxes = generate_bloxes(amount, ill_amount, recovery_time, random_move)
    stats = [healthy, sick, recovered] = [0, 0, 0]
    current_time = 0
    data = []

    button_width = 140
    button_height = 40
    back_button = [10, 10, button_width, button_height, "Back to Menu"]

    if not os.path.exists('data'):
        os.makedirs('data')

    file_number = 1
    while os.path.exists(f'data/data{file_number}.txt'):
        file_number += 1
    data_filename = f'data/data{file_number}.txt'

    while running[0]:
        current_time += clock.get_time() / 1000

        draw_road(screen, SCREEN_WIDTH[0], SCREEN_HEIGHT[0])
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(back_button, mouse):
                    from scenes.menu_scene import menu_scene
                    menu_scene(running)
                    return
                else:
                    mouse_pos = pygame.Vector2(event.pos)
                    spawned_blox = Blox("SpawnedBlox", mouse_pos, pygame.Vector2(gen_speed(), gen_speed()), Status.SICK,
                                        random_move=random_move)
                    bloxes.append(spawned_blox)

        button(back_button, mouse, screen, pygame.font.SysFont('Arial', 20))

        # Draw bloxes
        draw_bloxes(screen, bloxes)
        for blox in bloxes:
            if blox.status == Status.HEALTHY:
                healthy += 1
            elif blox.status == Status.SICK:
                sick += 1
            elif blox.status == Status.RECOVERED:
                recovered += 1
            blox.move(screen.get_width(), screen.get_height())
            blox.update_status(clock.get_time() / 1000)
            for other_blox in bloxes:
                if blox != other_blox:
                    blox.aura(other_blox)

        # Collect data every few seconds
        delay_for_data = 3
        if current_time % delay_for_data < clock.get_time() / 1000:
            data.append([current_time // delay_for_data, healthy, sick, recovered])
        # Create DataFrame and save to file
        df = pd.DataFrame(data, columns=['Time', 'Healthy', 'Sick', 'Recovered'])
        with open(data_filename, 'w') as file:
            file.write(f"Amount of starting bloxes: {amount}, "
                       f"Ill starting bloxes: {ill_amount}, "
                       f"Time for a recovery: {recovery_time} seconds, "
                       f"Randomized movement: {random_move}\n")
        df.to_csv(data_filename, mode='a', index=False, sep='\t')
        healthy, sick, recovered = 0, 0, 0
        pygame.display.flip()
        clock.tick(FPS[0])