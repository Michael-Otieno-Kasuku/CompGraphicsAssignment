"""
Also make use of Pygame.
"""
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math


class BillboardPolygon:
    def __init__(self, vertices):
        """
        Simple polygon class for billboarding effect.

        Parameters:
        - vertices (list): List of 2D vertices of the polygon.
        """
        self.vertices = vertices
        self.size = 200  # Size of the canvas
        self.image = Image.new('RGBA', (self.size, self.size), color=(255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.center = [self.size / 2, self.size / 2]
        self.angle = 0

    def update_position(self, angle):
        """
        Update the position and orientation of the polygon.

        Parameters:
        - angle (float): Angle of rotation.
        """
        self.angle = angle
        self.draw_polygon()

    def draw_polygon(self):
        """
        Draw the polygon on the image.
        """
        self.image = Image.new('RGBA', (self.size, self.size), color=(255, 255, 255, 0))
        rotated_vertices = self.rotate_vertices(self.vertices, self.angle)
        translated_vertices = self.translate_vertices(rotated_vertices, self.center)
        self.draw.polygon(translated_vertices, fill=(0, 0, 0, 255))

    def rotate_vertices(self, vertices, angle):
        """
        Rotate vertices around the center.

        Parameters:
        - vertices (list): List of 2D vertices.
        - angle (float): Angle of rotation.

        Returns:
        - list: Rotated vertices.
        """
        rotated_vertices = []
        for vertex in vertices:
            x, y = vertex
            rotated_x = (x - self.center[0]) * math.cos(angle) - (y - self.center[1]) * math.sin(angle) + self.center[0]
            rotated_y = (x - self.center[0]) * math.sin(angle) + (y - self.center[1]) * math.cos(angle) + self.center[1]
            rotated_vertices.append((rotated_x, rotated_y))
        return rotated_vertices

    def translate_vertices(self, vertices, translation):
        """
        Translate vertices by a given translation vector.

        Parameters:
        - vertices (list): List of 2D vertices.
        - translation (list): Translation vector [dx, dy].

        Returns:
        - list: Translated vertices.
        """
        return [(x + translation[0], y + translation[1]) for x, y in vertices]


class BillboardApp(tk.Tk):
    def __init__(self):
        """
        GUI application for displaying a billboarding polygon.
        """
        super().__init__()

        self.billboard_polygon = BillboardPolygon([(0, 0), (50, 0), (50, 50), (0, 50)])

        self.canvas = tk.Canvas(self, width=self.billboard_polygon.size, height=self.billboard_polygon.size,
                                background='white')
        self.canvas.pack()

        self.angle = 0
        self.update_billboard()

    def update_billboard(self):
        """
        Update the position and orientation of the billboard polygon.
        """
        self.billboard_polygon.update_position(self.angle)
        tk_image = ImageTk.PhotoImage(self.billboard_polygon.image)
        self.canvas.create_image(self.billboard_polygon.size / 2, self.billboard_polygon.size / 2,
                                 anchor=tk.CENTER, image=tk_image)
        self.tk_image = tk_image

        # Increment the angle for animation
        self.angle += 0.02
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

        # Schedule the next update
        self.after(10, self.update_billboard)


if __name__ == '__main__':
    app = BillboardApp()
    app.title("Billboarding Polygon")
    app.geometry("250x250")
    app.mainloop()
