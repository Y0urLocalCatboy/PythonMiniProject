import pygame

from utils.config import SCREEN_WIDTH, SCREEN_HEIGHT, music_switch


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
    if music_switch[0]:
        pygame.mixer.music.play(-1)
        return True
    else :
        pygame.mixer.music.stop()
        return False
def change_size(width, height):
    SCREEN_WIDTH[0] = width
    SCREEN_HEIGHT[0] = height
    pygame.display.set_mode((width, height))
