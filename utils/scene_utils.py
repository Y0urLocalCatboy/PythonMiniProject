from random import random

import pygame
import random

from entities.blox import Blox
from entities.status import Status
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, MUSIC_SWITCH


def button(to_scene, mouse, screen, font):
    """
    Draw a button on the screen and change its color when hovered over.

    Args:
        to_scene (list): A list containing the button's position, size, and label.
        mouse (tuple): The current position of the mouse cursor.
        screen (pygame.Surface): The screen surface to draw on.
        font (pygame.font.Font): The font used to render the button's label.
    """
    if to_scene[0] <= mouse[0] <= to_scene[0] + to_scene[2] and to_scene[1] <= mouse[1] <= to_scene[1] + to_scene[3]:
        pygame.draw.rect(screen, "grey", [to_scene[0], to_scene[1], to_scene[2], to_scene[3]])
    else:
        pygame.draw.rect(screen, "blue", [to_scene[0], to_scene[1], to_scene[2], to_scene[3]])
    text_surface = font.render(to_scene[4], True, "white")
    text_rect = text_surface.get_rect(center=(to_scene[0] + to_scene[2] / 2, to_scene[1] + to_scene[3] / 2))
    screen.blit(text_surface, text_rect)

def hover_over(to_scene, mouse):
    """
    Check if the mouse is hovering over a given area.

    Args:
        to_scene (list): A list containing the area's position and size.
        mouse (tuple): The current position of the mouse cursor.

    Returns:
        bool: True if the mouse is hovering over the area, False otherwise.
    """
    if to_scene[0] <= mouse[0] <= to_scene[0] + to_scene[2] and to_scene[1] <= mouse[1] <= to_scene[1] + to_scene[3]:
        return True
    return False

def draw_background_image(screen, background_path):
    """
    Draw a background image on the screen.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        background_path (str): The file path to the background image.
    """
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH[0], SCREEN_HEIGHT[0]))
    screen.blit(background, (0, 0))

def draw_road(screen, width, height):
    """
    Draw a road on the screen.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        width (int): The width of the screen.
        height (int): The height of the screen.
    """
    screen.fill((34, 139, 34))
    road_width = width / 8
    road = pygame.Rect(width / 2 - road_width / 2, 0, road_width, height)
    pygame.draw.rect(screen, (64, 64, 64), road)


def draw_bloxes(screen, bloxes):
    """
    Draw bloxes on the screen.

    Args:
        screen (pygame.Surface): The screen surface to draw on.
        bloxes (list): A list of Blox objects to draw.
    """
    for blox in bloxes:
        pygame.draw.circle(screen, blox.status.get_color(), blox.position, blox.radius)

def music_on_off(path):
    """
    Toggle background music on or off.

    Args:
        path (str): The file path to the music file.

    Returns:
        bool: True if the music is playing, False if it is stopped.
    """
    music = pygame.mixer.music.load(path)
    if MUSIC_SWITCH[0]:
        pygame.mixer.music.play(-1)
        return True
    else:
        pygame.mixer.music.stop()
        return False

def change_size(width, height):
    """
    Change the size of the screen.

    Args:
        width (int): The new width of the screen.
        height (int): The new height of the screen.
    """
    SCREEN_WIDTH[0] = width
    SCREEN_HEIGHT[0] = height
    pygame.display.set_mode((width, height))

def generate_bloxes(amount, ill_amount, recovery_time, random_move):
    """
    Generate a list of bloxes with specified attributes.

    Args:
        amount (int): The total number of bloxes to generate.
        ill_amount (int): The number of initially ill bloxes.
        recovery_time (int): The recovery time for sick bloxes.
        random_move (bool): Whether the bloxes should move randomly.

    Returns:
        list: A list of generated Blox objects.
    """
    bloxes = []
    radius = SCREEN_WIDTH[0] / 100 if SCREEN_HEIGHT[0] > SCREEN_WIDTH[0] else SCREEN_HEIGHT[0] / 100

    for i in range(amount):
        position = pygame.Vector2(random.randint(0, SCREEN_WIDTH[0]), random.randint(0, SCREEN_HEIGHT[0]))
        if i < ill_amount:
            bloxes.append(
                Blox("Blox" + str(i), position, pygame.Vector2(gen_speed(), gen_speed()), Status.SICK, recovery_time, random_move=random_move))
        else:
            bloxes.append(Blox("Blox" + str(i), position, pygame.Vector2(gen_speed(), gen_speed()), Status.HEALTHY,
                               recovery_time, random_move=random_move))
    return bloxes

def gen_speed():
    """
    Generate a random speed for a blox.

    Returns:
        int: A random speed value between -4 and 4, excluding 0.
    """
    speed = 0
    while speed == 0:
        speed = random.randint(-4, 4)
    return speed