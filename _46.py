"""
Using PIL for Python and docstrings and OOP:

46. Write a program to generate a cubic B ́ezier polynomial from an arbitrary number of
points entered interactively. The user should be able to manipulate the control points
interactively.
"""
import pygame
from pygame.locals import *
import sys
import numpy as np


class BezierCurveGenerator:
    def __init__(self):
        self.points = []
        self.dragging_point = None
        self.resolution = 100
        self.curve_color = (255, 255, 255)
        self.point_color = (255, 0, 0)
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Cubic Bézier Curve Generator")
        self.clock = pygame.time.Clock()

    def draw_curve(self):
        for t in range(self.resolution):
            t /= float(self.resolution - 1)
            x, y = self.de_casteljau_algorithm(t, self.points)
            pygame.draw.circle(self.screen, self.curve_color, (int(x), int(y)), 1)

    def draw_points(self):
        for point in self.points:
            pygame.draw.circle(self.screen, self.point_color, point, 5)

    def de_casteljau_algorithm(self, t, points):
        while len(points) > 1:
            new_points = []
            for i in range(len(points) - 1):
                x = (1 - t) * points[i][0] + t * points[i + 1][0]
                y = (1 - t) * points[i][1] + t * points[i + 1][1]
                new_points.append((x, y))
            points = new_points
        return points[0]

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.points.append(event.pos)
                    elif event.button == 3 and self.points:
                        self.points.pop()
                elif event.type == MOUSEMOTION and self.dragging_point is not None:
                    self.points[self.dragging_point] = event.pos
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        self.dragging_point = None

            self.screen.fill((0, 0, 0))
            self.draw_curve()
            self.draw_points()
            pygame.display.flip()
            self.clock.tick(30)


if __name__ == "__main__":
    bezier_generator = BezierCurveGenerator()
    bezier_generator.main_loop()
