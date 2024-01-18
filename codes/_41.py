"""
Using PIL for Python and docstrings and OOP:

41. Write a program that will allow the user to construct simple articulated figures from a
small collection of basic shapes. Your program should allow the user to place the joints,
and it should animate the resulting figures.
"""

import pygame
from pygame.locals import *
from PIL import Image, ImageDraw
import math

class ArticulatedFigure:
    def __init__(self):
        self.joints = []
        self.link_length = 50
        self.angle_offsets = [0] * 10

    def add_joint(self, x, y):
        self.joints.append((x, y))

    def update_angles(self, angles):
        self.angle_offsets = angles

    def draw_figure(self):
        image = Image.new("RGB", (800, 600), "white")
        draw = ImageDraw.Draw(image)

        for i, joint in enumerate(self.joints):
            angle = math.radians(self.angle_offsets[i])
            link_x = joint[0] + self.link_length * math.cos(angle)
            link_y = joint[1] + self.link_length * math.sin(angle)

            draw.line([(joint[0], joint[1]), (link_x, link_y)], fill="black", width=5)
            draw.ellipse([link_x - 10, link_y - 10, link_x + 10, link_y + 10], fill="red")

        pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
        pygame_surface = pygame.image.tostring(pygame_image, 'RGBA')
        pygame_surface = pygame.image.fromstring(pygame_surface, image.size, 'RGBA')

        pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
        pygame.display.get_surface().blit(pygame_surface, (0, 0))
        pygame.display.flip()

    def animate(self):
        pygame.init()
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            angles = [30 * math.sin(math.radians(pygame.time.get_ticks() % 360))] * len(self.joints)
            self.update_angles(angles)
            self.draw_figure()

            clock.tick(60)

if __name__ == "__main__":
    figure = ArticulatedFigure()

    # Add joints to create a simple articulated figure
    figure.add_joint(400, 300)
    figure.add_joint(400, 200)
    figure.add_joint(400, 100)

    # Animate the figure
    figure.animate()
