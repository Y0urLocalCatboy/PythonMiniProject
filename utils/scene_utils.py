from random import random

import pygame
import random

from entities.blox import Blox
from entities.status import Status
from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, MUSIC_SWITCH


def button(to_scene, mouse, screen, font):
    if to_scene[0] <= mouse[0] <= to_scene[0] + to_scene[2] and to_scene[1] <= mouse[1] <= to_scene[1] + to_scene[3]:
        pygame.draw.rect(screen, "grey",
                         [to_scene[0], to_scene[1], to_scene[2], to_scene[3]])
    else:
        pygame.draw.rect(screen, "blue",
                         [to_scene[0], to_scene[1], to_scene[2], to_scene[3]])
    # text rendering
    text_surface = font.render(to_scene[4], True, "white")
    text_rect = text_surface.get_rect(center=(to_scene[0] + to_scene[2] / 2, to_scene[1] + to_scene[3] / 2))
    screen.blit(text_surface, text_rect)

def hover_over(to_scene, mouse):
    if to_scene[0] <= mouse[0] <= to_scene[0] + to_scene[2] and to_scene[1] <= mouse[1] <= to_scene[1] + to_scene[3]:
        return True
    return False

def draw_background_image(screen, background_path):
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH[0], SCREEN_HEIGHT[0]))
    screen.blit(background, (0, 0))

def draw_road(screen, width, height):
    screen.fill((34, 139, 34))
    road_width = width / 8
    road = pygame.Rect(width / 2 - road_width / 2, 0, road_width, height)
    pygame.draw.rect(screen, (64, 64, 64), road)

def draw_bloxes(screen, bloxes):
    for blox in bloxes:
        pygame.draw.circle(screen, blox.status.get_color(), blox.position, blox.radius)
def music_on_off(path):
    music = pygame.mixer.music.load(path)
    if MUSIC_SWITCH[0]:
        pygame.mixer.music.play(-1)
        return True
    else :
        pygame.mixer.music.stop()
        return False
def change_size(width, height):
    SCREEN_WIDTH[0] = width
    SCREEN_HEIGHT[0] = height
    pygame.display.set_mode((width, height))

def generate_bloxes(amount, ill_amount, recovery_time):
    bloxes = []
    radius = SCREEN_WIDTH[0] / 100 if SCREEN_HEIGHT[0] > SCREEN_WIDTH[0] else SCREEN_HEIGHT[0] / 100

    for i in range(amount):
        position = pygame.Vector2(random.randint(0, SCREEN_WIDTH[0]), random.randint(0, SCREEN_HEIGHT[0]))
        if i < ill_amount:
            bloxes.append(
                Blox("Blox" + str(i), position, pygame.Vector2(gen_speed(), gen_speed()), Status.SICK, recovery_time))
        else:
            bloxes.append(Blox("Blox" + str(i), position, pygame.Vector2(gen_speed(), gen_speed()), Status.HEALTHY,
                               recovery_time))
    return bloxes
def gen_speed():
    speed = 0
    while speed == 0:
        speed = random.randint(-4, 4)
    return speed
