import pygame
from cube import Cube
from settings import *

cube = Cube()
screen_coordinates = lambda X, Y: (X*SCALE + OFFSET_X, Y*SCALE + OFFSET_Y)

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dragging = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            dx, dy = event.rel
            # Rotation horizontale → autour de Y
            cube.rotate((0, 1, 0), dx * MOUSE_ROTATION_STEP)
            # Rotation verticale → autour de X
            cube.rotate((1, 0, 0), (-dy) * MOUSE_ROTATION_STEP)

        elif event.type == pygame.MOUSEWHEEL:
            SCALE += CUBE_SIZE_STEP if event.y > 0 else -CUBE_SIZE_STEP

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cube.rotate((0, 1, 0), MOUSE_ROTATION_STEP)
            elif event.key == pygame.K_LEFT:
                cube.rotate((0, 1, 0), -MOUSE_ROTATION_STEP)
            elif event.key == pygame.K_DOWN:
                cube.rotate((1, 0, 0), MOUSE_ROTATION_STEP)
            elif event.key == pygame.K_UP:
                cube.rotate((1, 0, 0), -MOUSE_ROTATION_STEP)

    screen.fill("grey0")

    # Dessiner les faces dans l’ordre
    for pts, color, _ in cube.faces:
        poly = [screen_coordinates(x, y) for (x, y, z) in pts]
        pygame.draw.polygon(screen, color, poly)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
