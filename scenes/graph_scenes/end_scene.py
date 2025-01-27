import pygame
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import button, hover_over

def end_scene(screen, clock, running):
    """
    End scene of the simulation where the results are displayed.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        clock (pygame.time.Clock): The clock to control the frame rate.
        running (list): A list containing a single boolean element to control the running state.
    """
    file_number = 1
    while os.path.exists(f'data/data{file_number + 1}.txt'):
        file_number += 1
    data_filename = f'data/data{file_number}.txt'
    graph_filename = f'data/graph{file_number}.png'

    with open(data_filename, 'r') as file:
        settings = file.readline().strip()
    df = pd.read_csv(data_filename, sep='\t', skiprows=1)

    population = df['Healthy'].iloc[0] + df['Sick'].iloc[0] + df['Recovered'].iloc[0]
    threshold = 0.05 * population

    end_time = None
    for time, sick_count in zip(df['Time'], df['Sick']):
        if sick_count <= threshold and time > 5:
            end_time = time
            break

    # Predict the end of the epidemic using a trend line
    predicted_end_time = None
    if end_time is None:
        # Fit a trend line to the last N points
        N = 50  # Number of last data points to consider
        if len(df) >= N:
            last_times = df['Time'].iloc[-N:]
            last_sick_counts = df['Sick'].iloc[-N:]
            # Fit a linear regression (polyfit of degree 1)
            coeffs = np.polyfit(last_times, last_sick_counts, 1)
            slope, intercept = coeffs
            if slope < 0:  # Check if the trend is downward
                predicted_end_time = (threshold - intercept) / slope

    plt.figure(figsize=(10, 6))

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

    plt.plot(df['Time'], df['Healthy'], label='Healthy', color='green')
    plt.plot(df['Time'], df['Sick'], label='Sick', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='blue')

    plt.xlabel('Time [s]')
    plt.ylabel('Count [bloxes]')
    plt.title(f'Simulation Data Over Time\n{settings}')
    plt.legend()

    if end_time is not None:
        plt.annotate(f'Epidemic ends: {end_time:.2f}s',
                     xy=(end_time, threshold), xytext=(end_time + 50, threshold + 10),
                     arrowprops=dict(facecolor='black', arrowstyle='->'),
                     fontsize=10, color='black')
        plt.text(0.5, -0.12, f'Epidemic ended at {end_time:.2f} seconds.',
                 fontsize=12, color='black', transform=plt.gca().transAxes, ha='center')
    elif predicted_end_time is not None:
        plt.annotate(f'Predicted end: {predicted_end_time:.2f}s',
                     xy=(predicted_end_time, threshold), xytext=(predicted_end_time + 50, threshold + 10),
                     arrowprops=dict(facecolor='black', arrowstyle='->'),
                     fontsize=10, color='blue')
        plt.text(0.5, -0.12, f'Predicted epidemic end time: {predicted_end_time:.2f} seconds.',
                 fontsize=12, color='blue', transform=plt.gca().transAxes, ha='center')
    else:
        plt.text(0.5, -0.12, f'Epidemic end time could not be determined.',
                 fontsize=12, color='red', transform=plt.gca().transAxes, ha='center')

    plt.savefig(graph_filename)
    plt.close()

    graph_image = pygame.image.load(graph_filename)
    graph_rect = graph_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    while running[0]:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(back_button, mouse):
                    return

        screen.fill("white")
        screen.blit(graph_image, graph_rect)
        button(back_button, mouse, screen, font)
        pygame.display.flip()
        clock.tick(FPS[0])