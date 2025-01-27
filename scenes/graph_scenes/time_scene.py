import pygame
import pandas as pd
import matplotlib.pyplot as plt
import os
from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import button, hover_over

def calculate_stabilization_times(df, threshold=50, window=20):
    """
    Calculate the stabilization times for Healthy, Sick, and Recovered bloxes.

    Args:
        df (pd.DataFrame): DataFrame containing the simulation data.
        threshold (int): The maximum allowed difference to consider the values stabilized.
        window (int): The number of consecutive moments in time to check for stabilization.

    Returns:
        dict: A dictionary with stabilization times for each group.
    """
    stabilization_times = {}

    for column in ["Healthy", "Sick", "Recovered"]:
        differences = df[column].diff().abs()
        for i in range(len(differences) - window):
            if differences[i:i + window].max() <= threshold:
                stabilization_times[column] = df["Time"].iloc[i + window]
                break
        else:
            stabilization_times[column] = None

    return stabilization_times

def time_scene(screen, clock, running):
    """
    Time scene of the simulation where the stabilization times are displayed.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        clock (pygame.time.Clock): The clock to control the frame rate.
        running (list): A list containing a single boolean element to control the running state.
    """
    if not os.path.exists('data'):
        os.makedirs('data')

    file_number = 1
    while os.path.exists(f'data/data{file_number + 1}.txt'):
        file_number += 1
    data_filename = f'data/data{file_number}.txt'
    graph_filename = f'data/graph{file_number}.png'

    with open(data_filename, 'r') as file:
        settings = file.readline().strip()
    df = pd.read_csv(data_filename, sep='\t', skiprows=1)

    stabilization_times = calculate_stabilization_times(df)

    plt.figure(figsize=(10, 6))

    plt.plot(df['Time'], df['Healthy'], label='Healthy', color='green')
    plt.plot(df['Time'], df['Sick'], label='Sick', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='blue')

    plt.xlabel('Time [s]')
    plt.ylabel('Count [bloxes]')
    plt.title(f'Simulation Data Over Time\n{settings}')
    plt.legend()

    stabilization_text = "\n".join([f"{group}: {time:.2f}s" if time is not None else f"{group}: Not stabilized"
                                    for group, time in stabilization_times.items()])
    plt.figtext(0.5, -0.1, f"Stabilization Times:\n{stabilization_text}", wrap=True, horizontalalignment='center',
                fontsize=10)

    plt.savefig(graph_filename, bbox_inches='tight')
    plt.close()

    graph_image = pygame.image.load(graph_filename)
    graph_rect = graph_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2
    spacing = SCREEN_HEIGHT[0] // 6

    back_button = [button_x + spacing * 1.5, button_y - 2.5 * spacing,
                   button_width + spacing / 2, button_height,
                   "Back"]

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    while running[0]:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(back_button, mouse):
                    return

        screen.fill("white")
        screen.blit(graph_image, graph_rect)
        button(back_button, mouse, screen, font)
        pygame.display.flip()
        clock.tick(FPS[0])