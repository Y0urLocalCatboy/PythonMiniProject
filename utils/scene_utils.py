import pygame

from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT


def button(to_scene, mouse, screen, font):
    if to_scene[0] <= mouse[0] <= to_scene[0] + to_scene[2] and to_scene[1] <= mouse[1] <= to_scene[1] + to_scene[3]:
        pygame.draw.rect(screen, "grey",
                         [to_scene[0], to_scene[1], to_scene[2], to_scene[3]])
    else:
        pygame.draw.rect(screen, "blue",
                         [to_scene[0], to_scene[1], to_scene[2], to_scene[3]])
    # text rendering
    text_surface = font.render(to_scene[4], True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(to_scene[0] + to_scene[2] / 2, to_scene[1] + to_scene[3] / 2))
    screen.blit(text_surface, text_rect)

def hover_over(to_scene, mouse):
    if to_scene[0] <= mouse[0] <= to_scene[0] + to_scene[2] and to_scene[1] <= mouse[1] <= to_scene[1] + to_scene[3]:
        return True
    return False

def draw_background(screen, background_path):
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0, 0))