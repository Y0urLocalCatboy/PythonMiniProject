import pygame
import pandas as pd
import matplotlib.pyplot as plt
import os

from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import button, hover_over

def graph_scene(screen, clock, running):
    # Ensure the data folder exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Determine the latest data file
    file_number = 1
    while os.path.exists(f'data/data{file_number + 1}.txt'):
        file_number += 1
    data_filename = f'data/data{file_number}.txt'
    graph_filename = f'data/graph{file_number}.png'

    # Load data from the latest data file
    with open(data_filename, 'r') as file:
        settings = file.readline().strip()
    df = pd.read_csv(data_filename, sep='\t', skiprows=1)

    # Create plots
    plt.figure(figsize=(10, 6))

    # button position and size
    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2  # rectangle isn't centered by default
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2
    spacing = SCREEN_HEIGHT[0] // 6  # spacing between buttons

    back_button = [button_x + spacing * 1.5, button_y - 2.5 * spacing,
                             button_width + spacing / 2, button_height,
                             "Back"]
    # font initialization
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    plt.plot(df['Time'], df['Healthy'], label='Healthy', color='green')
    plt.plot(df['Time'], df['Sick'], label='Sick', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='blue')

    plt.xlabel('Time [s]')
    plt.ylabel('Count [bloxes]')
    plt.title(f'Simulation Data Over Time\n{settings}')
    plt.legend()

    # Save the plot as an image
    plt.savefig(graph_filename)
    plt.close()

    # Load the image with pygame
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