"""
Using PIL for Python and docstrings and OOP:

22. Write a program that allows you to orient the cube with one mouse button, to translate it
with a second, and to zoom in and out with a third.
"""

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math


class Cube3D:
    def __init__(self, size):
        """
        3D Cube model.

        Parameters:
        - size (int): Size of the cube.
        """
        self.size = size
        self.angle_x = 0
        self.angle_y = 0
        self.translate_x = 0
        self.translate_y = 0
        self.zoom = 1

    def rotate(self, angle_x, angle_y):
        """
        Rotate the cube.

        Parameters:
        - angle_x (float): Angle of rotation around the x-axis.
        - angle_y (float): Angle of rotation around the y-axis.
        """
        self.angle_x += angle_x
        self.angle_y += angle_y

    def translate(self, delta_x, delta_y):
        """
        Translate the cube.

        Parameters:
        - delta_x (int): Translation along the x-axis.
        - delta_y (int): Translation along the y-axis.
        """
        self.translate_x += delta_x
        self.translate_y += delta_y

    def zoom_in(self):
        """Zoom in the cube."""
        self.zoom *= 1.1

    def zoom_out(self):
        """Zoom out the cube."""
        self.zoom /= 1.1

    def draw_cube(self):
        """
        Draw the 3D cube on an image.

        Returns:
        - Image: PIL Image containing the drawn cube.
        """
        image = Image.new('RGB', (self.size, self.size), color='white')
        draw = ImageDraw.Draw(image)

        # Cube vertices
        vertices = [
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
        rotated_vertices = self.rotate_vertices(vertices)
        translated_vertices = self.translate_vertices(rotated_vertices)
        scaled_vertices = self.scale_vertices(translated_vertices)

        # Project 3D vertices to 2D
        projected_vertices = []
        for vertex in scaled_vertices:
            x = vertex[0] * self.size / 4 + self.size / 2
            y = vertex[1] * self.size / 4 + self.size / 2
            projected_vertices.append([x, y])

        # Draw lines between vertices
        lines = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        for line in lines:
            draw.line([tuple(projected_vertices[line[0]]), tuple(projected_vertices[line[1]])], fill='black')

        return image

    def rotate_vertices(self, vertices):
        """
        Rotate vertices around the x and y axes.

        Parameters:
        - vertices (list): List of 3D vertices.

        Returns:
        - list: Rotated vertices.
        """
        rotated_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            rotated_x = x * math.cos(self.angle_y) - z * math.sin(self.angle_y)
            rotated_y = x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
            rotated_z = y * math.cos(self.angle_x) - rotated_y * math.sin(self.angle_x)
            rotated_y = y * math.sin(self.angle_x) + rotated_y * math.cos(self.angle_x)
            rotated_vertices.append([rotated_x, rotated_y, rotated_z])
        return rotated_vertices

    def translate_vertices(self, vertices):
        """
        Translate vertices.

        Parameters:
        - vertices (list): List of 3D vertices.

        Returns:
        - list: Translated vertices.
        """
        translated_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            translated_x = x + self.translate_x
            translated_y = y + self.translate_y
            translated_vertices.append([translated_x, translated_y, z])
        return translated_vertices

    def scale_vertices(self, vertices):
        """
        Scale vertices.

        Parameters:
        - vertices (list): List of 3D vertices.

        Returns:
        - list: Scaled vertices.
        """
        scaled_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            scaled_x = x * self.zoom
            scaled_y = y * self.zoom
            scaled_vertices.append([scaled_x, scaled_y, z])
        return scaled_vertices


class CubeViewerApp(tk.Tk):
    def __init__(self, size):
        """
        GUI application for viewing and interacting with the 3D cube.

        Parameters:
        - size (int): Size of the canvas.
        """
        super().__init__()
        self.size = size
        self.cube = Cube3D(size)
        self.title("3D Cube Viewer")
        self.canvas = tk.Canvas(self, width=size, height=size, background='white')
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.rotate_cube)
        self.canvas.bind("<B2-Motion>", self.translate_cube)
        self.canvas.bind("<B3-Motion>", self.zoom_cube)
        self.update_cube_image()

    def rotate_cube(self, event):
        """
        Rotate the cube based on mouse movement.

        Parameters:
        - event: Mouse event.
        """
        delta_x = event.x - self.size / 2
        delta_y = event.y - self.size / 2
        self.cube.rotate(delta_y * 0.01, delta_x * 0.01)
        self.update_cube_image()

    def translate_cube(self, event):
        """
        Translate the cube based on mouse movement.

        Parameters:
        - event: Mouse event.
        """
        delta_x = event.x - self.size / 2
        delta_y = event.y - self.size / 2
        self.cube.translate(delta_x * 0.02, delta_y * 0.02)
        self.update_cube_image()

    def zoom_cube(self, event):
        """
        Zoom in/out the cube based on mouse movement.

        Parameters:
        - event: Mouse event.
        """
        delta_y = event.y - self.size / 2
        if delta_y > 0:
            self.cube.zoom_in()
        else:
            self.cube.zoom_out()
        self.update_cube_image()

    def update_cube_image(self):
        """Update the cube image on the canvas."""
        cube_image = self.cube.draw_cube()
        tk_image = ImageTk.PhotoImage(cube_image)
        self.canvas.delete("all")
        self.canvas.create_image(self.size / 2, self.size / 2, anchor=tk.CENTER, image=tk_image)
        self.tk_image = tk_image


if __name__ == '__main__':
    app = CubeViewerApp(size=500)
    app.mainloop()
