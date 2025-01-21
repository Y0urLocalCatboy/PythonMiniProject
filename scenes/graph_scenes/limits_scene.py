import pygame
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
import numpy as np

from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import button, hover_over

def limits_scene(screen, clock, running):
    """
    Limits scene of the simulation where the stabilization trends are analyzed and displayed.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        clock (pygame.time.Clock): The clock to control the frame rate.
        running (list): A list containing a single boolean element to control the running state.
    """
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

    # Analyze the stabilization trend for Sick, Recovered, and Healthy
    def predict_stable_value(y_values):
        """Predict the stable value by performing linear regression on the last N points."""
        N = 50  # Number of last points to consider
        if len(y_values) >= N:
            X = np.arange(len(y_values) - N, len(y_values)).reshape(-1, 1)
            y = y_values[-N:]
            model = LinearRegression()
            model.fit(X, y)
            return model.predict([[len(y_values)]])[0]  # Predicted value at the end
        else:
            return None

    predicted_healthy = predict_stable_value(df['Healthy'].values)
    predicted_sick = predict_stable_value(df['Sick'].values)
    predicted_recovered = predict_stable_value(df['Recovered'].values)

    # Create plots
    plt.figure(figsize=(10, 6))

    # Button position and size
    button_width = 140
    button_height = 40
    button_x = (SCREEN_WIDTH[0] - button_width) / 2  # Rectangle isn't centered by default
    button_y = (SCREEN_HEIGHT[0] - button_height) / 2
    spacing = SCREEN_HEIGHT[0] // 6  # Spacing between buttons

    back_button = [button_x + spacing * 1.5, button_y - 2.5 * spacing,
                   button_width + spacing / 2, button_height,
                   "Back"]

    # Font initialization
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    plt.plot(df['Time'], df['Healthy'], label='Healthy', color='green')
    plt.plot(df['Time'], df['Sick'], label='Sick', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='blue')

    # Annotate predictions
    if predicted_healthy:
        plt.axhline(predicted_healthy, color='green', linestyle='--', alpha=0.6, label=f'Predicted Healthy: {int(predicted_healthy)}')
    if predicted_sick:
        plt.axhline(predicted_sick, color='red', linestyle='--', alpha=0.6, label=f'Predicted Sick: {int(predicted_sick)}')
    if predicted_recovered:
        plt.axhline(predicted_recovered, color='blue', linestyle='--', alpha=0.6, label=f'Predicted Recovered: {int(predicted_recovered)}')

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_over(back_button, mouse):
                    return

        screen.fill("white")
        screen.blit(graph_image, graph_rect)
        button(back_button, mouse, screen, font)

        # Display predicted stabilization values
        predictions_text = [
            f'Predicted Healthy: {int(predicted_healthy)}' if predicted_healthy else "Healthy: Prediction not available",
            f'Predicted Sick: {int(predicted_sick)}' if predicted_sick else "Sick: Prediction not available",
            f'Predicted Recovered: {int(predicted_recovered)}' if predicted_recovered else "Recovered: Prediction not available"
        ]
        for i, text in enumerate(predictions_text):
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH[0] // 2, SCREEN_HEIGHT[0] - 100 + i * 30))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(FPS[0])