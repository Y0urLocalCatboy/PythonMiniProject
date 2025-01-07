import Blob
import pygame
import EnumStatus

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
dt = 0
fps = 60
blobList = []
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
def update():
    screen.fill("white")
    x = 200
    y = 100
    blobList.clear()
    create_blob("Blob1", EnumStatus.Status.HEALTHY, pygame.Vector2(x, y))
    create_blob("Blob2", EnumStatus.Status.SICK, pygame.Vector2(x+10, y-50))
    create_blob("Blob3", EnumStatus.Status.RECOVERED, pygame.Vector2(x+50, y+50))
    for blob in blobList:
        color = blob.status.get_color()
        pygame.draw.circle(screen, color, blob.position, 40)
        x = x + 40
        y = y - 20

def create_blob(name, status, position):
    blob = Blob.Blob(name, status, position)
    blobList.append(blob)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_p]:
        pygame.time.delay(500)
        with open("StartScene.py") as file:
            exec(file.read())

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fps) / 1000

pygame.quit()