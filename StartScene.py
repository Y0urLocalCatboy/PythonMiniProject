import pygame

import MainScene

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
dt = 0
fps = 60
height = screen.get_height()
width = screen.get_width()

while running:
    screen.fill("white")

    mouse = pygame.mouse.get_pos()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if screen.get_width() / 2 <= mouse[0] <= screen.get_width() / 2 + 140 and screen.get_height() / 2 <= mouse[1] <= screen.get_height() / 2 + 40:
                with open("MainScene.py") as file:
                    exec(file.read())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        pygame.time.delay(500)
        with open("MainScene.py") as file:
            exec(file.read())        # if mouse is hovered on a button it
        # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, "grey", [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, "red", [width / 2, height / 2, 140, 40])

        # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fps) / 1000