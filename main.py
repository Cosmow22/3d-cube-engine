import pygame
from cube import Cube
from settings import *

cube = Cube()
cube.compute()

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 : 
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                x, y = event.rel
                if x > 0: # → Souris vers la droite
                    cube.b += MOUSE_ROTATION_STEP
                elif x < 0: # ← Souris vers la gauche
                    cube.b -= MOUSE_ROTATION_STEP
                if y > 0: # ↓ Souris vers le bas
                    cube.a -= MOUSE_ROTATION_STEP   
                elif y < 0: # ↑ Souris vers le haut
                    cube.a += MOUSE_ROTATION_STEP        
                cube.compute()
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                SCALE += CUBE_SIZE_STEP
            else:
                SCALE -= CUBE_SIZE_STEP
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               cube.b -= MOUSE_ROTATION_STEP
            if event.key == pygame.K_LEFT:
                cube.b += MOUSE_ROTATION_STEP
            if event.key == pygame.K_DOWN:
                cube.a += MOUSE_ROTATION_STEP
            if event.key == pygame.K_UP:
                cube.a -= MOUSE_ROTATION_STEP
            cube.compute()

    screen.fill("grey0") 
    
    # draw faces
    for face, color, _ in cube.faces:
        face_points = []
        for (X, Y, Z) in face:
            face_points.append(screen_coordinates(X,Y))
        pygame.draw.polygon(screen, color, face_points)
            
    pygame.display.flip()

    clock.tick(60)

pygame.quit()