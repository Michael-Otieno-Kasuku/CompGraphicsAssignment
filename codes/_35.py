"""
Using PIL for Python and docstrings and OOP:

35. Write a program that will fly around above a mesh. Your program should allow the user
to look around at the hills and valleys rather than always looking at a single point.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Terrain:
    def __init__(self):
        self.vertices = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
        ]
        self.edges = (
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
        )

    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

class Camera:
    def __init__(self):
        self.x, self.y, self.z = 0, 0, -5
        self.pitch, self.yaw = 0, 0

    def apply(self):
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.pitch, 1, 0, 0)
        glRotatef(self.yaw, 0, 1, 0)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    terrain = Terrain()
    camera = Camera()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                dx, dy = event.rel
                camera.yaw += dx
                camera.pitch -= dy
                pygame.mouse.set_pos(display[0] // 2, display[1] // 2)

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            camera.z += 0.1
        if keys[K_s]:
            camera.z -= 0.1
        if keys[K_a]:
            camera.x += 0.1
        if keys[K_d]:
            camera.x -= 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        camera.apply()
        terrain.draw()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
