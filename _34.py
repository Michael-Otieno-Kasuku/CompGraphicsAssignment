"""
Using PIL for Python and docstrings and OOP:

34. In animation, often we can save effort by working with two-dimensional patterns that are
mapped onto flat polygons that are always parallel to the camera, a technique known as
billboarding. Write a program that will keep a simple polygon facing the camera as the
camera moves.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class BillboardPolygon:
    def __init__(self, texture_path):
        """
        Initialize the BillboardPolygon.

        Parameters:
        - texture_path: Path to the texture image
        """
        self.texture_id = self.load_texture(texture_path)
        self.vertices = [
            (-1, -1, 0),
            (1, -1, 0),
            (1, 1, 0),
            (-1, 1, 0),
        ]

    def load_texture(self, texture_path):
        """
        Load the texture and return its ID.

        Parameters:
        - texture_path: Path to the texture image

        Returns:
        - texture_id: ID of the loaded texture
        """
        texture_surface = pygame.image.load(texture_path)
        texture_data = pygame.image.tostring(texture_surface, 'RGB', 1)

        width, height = texture_surface.get_size()

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        return texture_id

    def draw(self):
        """
        Draw the billboard polygon.
        """
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glBegin(GL_QUADS)
        for vertex in self.vertices:
            glTexCoord2f((vertex[0] + 1) / 2, (vertex[1] + 1) / 2)
            glVertex3fv(vertex)
        glEnd()

        glDisable(GL_TEXTURE_2D)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    billboard = BillboardPolygon("your_texture_image.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        billboard.draw()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
