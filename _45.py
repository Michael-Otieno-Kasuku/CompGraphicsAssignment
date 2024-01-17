"""
Using PIL for Python and docstrings and OOP:

45. Write a PyOpenGL or using any other language program that will take as input a set of
control points and produce the interpolating, B-spline, and B ́ezier curves for these data.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class CurveGenerator:
    def __init__(self):
        self.control_points = []
        self.interpolating_curve = []
        self.bspline_curve = []
        self.bezier_curve = []
        self.t_values = [i / 100.0 for i in range(101)]

    def draw_point(self, x, y):
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    def draw_curve(self, curve, color):
        glColor3f(color[0], color[1], color[2])
        glBegin(GL_LINE_STRIP)
        for point in curve:
            glVertex2f(point[0], point[1])
        glEnd()

    def interpolate(self):
        self.interpolating_curve = []
        num_segments = len(self.control_points) - 1
        for i in range(num_segments):
            for t in self.t_values:
                x = (1 - t) * self.control_points[i][0] + t * self.control_points[i + 1][0]
                y = (1 - t) * self.control_points[i][1] + t * self.control_points[i + 1][1]
                self.interpolating_curve.append((x, y))

    def compute_bspline_basis(self, i, k, t):
        if k == 1:
            return 1 if self.knots[i] <= t < self.knots[i + 1] else 0
        else:
            w1 = 0 if self.knots[i + k - 1] == self.knots[i] else \
                (t - self.knots[i]) / (self.knots[i + k - 1] - self.knots[i]) * \
                self.compute_bspline_basis(i, k - 1, t)
            w2 = 0 if self.knots[i + k] == self.knots[i + 1] else \
                (self.knots[i + k] - t) / (self.knots[i + k] - self.knots[i + 1]) * \
                self.compute_bspline_basis(i + 1, k - 1, t)
            return w1 + w2

    def bspline(self):
        self.bspline_curve = []
        degree = 2  # Degree of the B-spline curve
        self.knots = [i for i in range(len(self.control_points) + degree + 1)]
        num_segments = len(self.control_points) - degree
        for i in range(num_segments):
            for t in self.t_values:
                x = 0
                y = 0
                for j in range(len(self.control_points)):
                    x += self.control_points[j][0] * self.compute_bspline_basis(j, degree + 1, t)
                    y += self.control_points[j][1] * self.compute_bspline_basis(j, degree + 1, t)
                self.bspline_curve.append((x, y))

    def compute_binomial_coefficient(self, n, k):
        if k == 0 or k == n:
            return 1
        else:
            return self.compute_binomial_coefficient(n - 1, k - 1) + self.compute_binomial_coefficient(n - 1, k)

    def compute_bezier_basis(self, i, n, t):
        return self.compute_binomial_coefficient(n, i) * (1 - t)**(n - i) * t**i

    def bezier(self):
        self.bezier_curve = []
        n = len(self.control_points) - 1
        for t in self.t_values:
            x = 0
            y = 0
            for i in range(n + 1):
                x += self.control_points[i][0] * self.compute_bezier_basis(i, n, t)
                y += self.control_points[i][1] * self.compute_bezier_basis(i, n, t)
            self.bezier_curve.append((x, y))

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for point in self.control_points:
            self.draw_point(point[0], point[1])

        if len(self.control_points) > 1:
            self.interpolate()
            self.draw_curve(self.interpolating_curve, (1, 0, 0))  # Red for interpolating curve

        if len(self.control_points) > 2:
            self.bspline()
            self.draw_curve(self.bspline_curve, (0, 1, 0))  # Green for B-spline curve

        if len(self.control_points) > 2:
            self.bezier()
            self.draw_curve(self.bezier_curve, (0, 0, 1))  # Blue for Bézier curve

        glutSwapBuffers()

    def mouse_click(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            viewport = glGetIntegerv(GL_VIEWPORT)
            normalized_x = (x - viewport[0]) / viewport[2]
            normalized_y = 1.0 - (y - viewport[1]) / viewport[3]
            world_x = normalized_x * 2.0 - 1.0
            world_y = normalized_y * 2.0 - 1.0
            self.control_points.append((world_x, world_y))

    def main_loop(self):
        glutMainLoop()


if __name__ == "__main__":
    curve_generator = CurveGenerator()

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutCreateWindow("Curve Generator")
    glutReshapeWindow(800, 600)
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(curve_generator.draw)
    glutMouseFunc(curve_generator.mouse_click)

    curve_generator.main_loop()
