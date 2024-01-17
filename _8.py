"""
Using PIL for Python and docstrings:
Implement the suggestion about displaying a rotating cube in the program. Add a button
that, when the cube is loaded, can update the locations of the cube vertices by computing
them with a new value of t, the amount to rotate. To make the animation look smooth, try
changing t by .05 radians per button click.
"""

from PIL import Image, ImageDraw
from PIL import ImageTk
import tkinter as tk
import math
import colorsys

class RotatingCube:
    def __init__(self, master):
        """
        Initialize the RotatingCube object.

        Parameters:
        - master (tk.Tk): The main Tkinter window.

        Returns:
        None
        """
        self.master = master
        self.master.title("Rotating Cube")
        self.master.configure(bg='#f0f0f0')  # Set background color

        self.width = 400
        self.height = 400
        self.t = 0  # Initial rotation angle
        self.cube_size = 100
        self.vertices = self.calculate_cube_vertices()

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg='#ffffff')  # Set canvas background color
        self.canvas.pack()

        self.update_button = tk.Button(self.master, text="Rotate", command=self.update_rotation, bg='#4caf50', fg='white', relief=tk.FLAT)  # Stylish button
        self.update_button.pack(pady=10)

        self.draw_cube()

    def calculate_cube_vertices(self):
        """
        Calculate the vertices of the cube based on the current rotation angle.

        Returns:
        list: List of cube vertices.
        """
        center_x = self.width // 2
        center_y = self.height // 2

        vertices = []
        for i in range(8):
            x = center_x + self.cube_size * (math.cos(self.t) + math.cos(self.t + math.pi/4 * i))
            y = center_y + self.cube_size * (math.sin(self.t) + math.sin(self.t + math.pi/4 * i))
            vertices.append((x, y))
        return vertices

    def draw_cube(self):
        """
        Draw the cube on the canvas.

        Returns:
        None
        """
        self.canvas.delete("all")  # Clear the canvas

        # Connect the cube vertices to form the faces
        for face, color in zip([(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)],
                               ['#f44336', '#2196f3', '#ff9800', '#4caf50', '#ffeb3b', '#9c27b0']):
            face_vertices = [self.vertices[i] for i in face]
            self.canvas.create_polygon(face_vertices, outline="black", fill=color, width=2)

    def update_rotation(self):
        """
        Update the rotation angle and redraw the cube with smooth transitions.

        Returns:
        None
        """
        for _ in range(30):  # Smooth transition with 30 frames
            self.t += 0.01
            self.vertices = self.calculate_cube_vertices()
            self.draw_cube()
            self.master.update()
            self.master.after(20)  # 20 milliseconds delay for smooth animation

if __name__ == "__main__":
    root = tk.Tk()
    rotating_cube = RotatingCube(root)
    root.mainloop()
