import time

import pygame
from entities.blox import Blox
from entities.building import Building
from entities.status import Status
from scenes.loading_scene import loading_scene
from utils.config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.scene_utils import draw_road, draw_bloxes, generate_bloxes, gen_speed


def main_scene(screen, clock, running, amount, ill_amount, recovery_time):
    loading_scene(screen)
    with open('data.txt', 'w') as file:
        file.write("DATA FOR A SIMULATION\n\n")

    bloxes = generate_bloxes(amount, ill_amount, recovery_time)
    hospital = Building("Hospital", pygame.Vector2(100, 100), 10, bloxes)
    stats =[healthy, sick, recovered] = [0, 0, 0]
    current_time = 0
    while running[0]:
        current_time += clock.get_time() / 1000
        # Road
        draw_road(screen, SCREEN_WIDTH[0], SCREEN_HEIGHT[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.Vector2(event.pos)
                spawned_blox = Blox("SpawnedBlox", mouse_pos, pygame.Vector2(gen_speed(), gen_speed()), Status.SICK)
                bloxes.append(spawned_blox)
        # Building
        pygame.draw.rect(screen, "gray", (*hospital.position, SCREEN_WIDTH[0] / 10, SCREEN_HEIGHT[0] / 10))

        # Bloxes
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
        if current_time % 10 < clock.get_time() / 1000:
            with open('data.txt', 'a') as file:
                file.write(f"{current_time//10}\n Healthy: {healthy}\nSick: {sick}\nRecovered: {recovered}\n\n")
        healthy, sick, recovered = 0, 0, 0
        pygame.display.flip()
        clock.tick(FPS[0])
