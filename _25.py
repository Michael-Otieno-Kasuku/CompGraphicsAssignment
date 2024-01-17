"""
Using PIL for Python and docstrings and OOP:

25. Write a program to display a rotating cube in a box with three light sources. Each light
source should project the cube onto one of the three visible sides of the box.
"""

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math


class RotatingCube:
    def __init__(self, size):
        """
        Rotating cube class with three light sources.

        Parameters:
        - size (int): Size of the box.
        """
        self.size = size
        self.angle = 0
        self.image = Image.new('RGB', (size, size), color='white')
        self.draw = ImageDraw.Draw(self.image)
        self.light_sources = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def rotate_cube(self, angle):
        """
        Rotate the cube.

        Parameters:
        - angle (float): Angle of rotation.
        """
        self.angle = angle
        self.draw_cube()

    def draw_cube(self):
        """
        Draw the rotating cube with three light sources.
        """
        self.image = Image.new('RGB', (self.size, self.size), color='white')
        cube_vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1],
        ]

        # Projection matrix
        projection_matrix = [
            [1, 0, 0],
            [0, 1, 0]
        ]

        # Apply transformations
        rotated_vertices = self.rotate_vertices(cube_vertices, self.angle)

        # Project 3D vertices to 2D for each light source
        for light_source in self.light_sources:
            projected_vertices = self.project_vertices(rotated_vertices, light_source, projection_matrix)
            self.draw_edges(projected_vertices)

    def rotate_vertices(self, vertices, angle):
        """
        Rotate vertices around the x and y axes.

        Parameters:
        - vertices (list): List of 3D vertices.
        - angle (float): Angle of rotation.

        Returns:
        - list: Rotated vertices.
        """
        rotated_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            rotated_x = x * math.cos(angle) - z * math.sin(angle)
            rotated_z = x * math.sin(angle) + z * math.cos(angle)
            rotated_vertices.append([rotated_x, y, rotated_z])
        return rotated_vertices

    def project_vertices(self, vertices, light_source, projection_matrix):
        """
        Project 3D vertices to 2D using a light source and projection matrix.

        Parameters:
        - vertices (list): List of 3D vertices.
        - light_source (tuple): Light source vector [lx, ly, lz].
        - projection_matrix (list): Projection matrix.

        Returns:
        - list: Projected vertices.
        """
        projected_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            dot_product = sum([a * b for a, b in zip(vertex, light_source)])
            if dot_product > 0:
                projection = [sum([a * b for a, b in zip(vertex, row)]) for row in projection_matrix]
                projected_vertices.append(projection)
        return projected_vertices

    def draw_edges(self, vertices):
        """
        Draw the edges of the cube based on projected vertices.

        Parameters:
        - vertices (list): List of projected vertices.
        """
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        for edge in edges:
            if 0 <= edge[0] < len(vertices) and 0 <= edge[1] < len(vertices):
                start_point = (int(vertices[edge[0]][0] * self.size / 4 + self.size / 2),
                               int(vertices[edge[0]][1] * self.size / 4 + self.size / 2))
                end_point = (int(vertices[edge[1]][0] * self.size / 4 + self.size / 2),
                             int(vertices[edge[1]][1] * self.size / 4 + self.size / 2))
                self.draw.line([start_point, end_point], fill='black')


class CubeViewerApp(tk.Tk):
    def __init__(self, size):
        """
        GUI application for displaying a rotating cube in a box with three light sources.

        Parameters:
        - size (int): Size of the box.
        """
        super().__init__()

        self.size = size
        self.cube_viewer = RotatingCube(size)
        self.title("Rotating Cube Viewer")
        self.canvas = tk.Canvas(self, width=size, height=size, background='white')
        self.canvas.pack()
        self.bind("<B1-Motion>", self.rotate_cube)
        self.update_cube_image()

    def rotate_cube(self, event):
        """
        Rotate the cube based on mouse movement.

        Parameters:
        - event: Mouse event.
        """
        delta_x = event.x - self.size / 2
        delta_y = event.y - self.size / 2
        angle = delta_x * 0.01
        self.cube_viewer.rotate_cube(angle)
        self.update_cube_image()

    def update_cube_image(self):
        """Update the cube image on the canvas."""
        self.cube_viewer.draw_cube()
        tk_image = ImageTk.PhotoImage(self.cube_viewer.image)
        self.canvas.delete("all")
        self.canvas.create_image(self.size / 2, self.size / 2, anchor=tk.CENTER, image=tk_image)
        self.tk_image = tk_image
        self.after(10, self.update_cube_image)


if __name__ == '__main__':
    app = CubeViewerApp(size=400)
    app.mainloop()
