"""
Using PIL for Python and docstrings and OOP:

21. Write a program to generate a Sierpinski gasket as follows. Start with a white triangle. At
each step, use transformations to generate three similar triangles that are drawn over the
original triangle, leaving the center of the triangle white and the three corners black.
"""

from PIL import Image, ImageDraw, ImageTk
import tkinter as tk


class SierpinskiGasket:
    def __init__(self, size, iterations):
        """
        Sierpinski Gasket generator.

        Parameters:
        - size (int): Size of the image.
        - iterations (int): Number of iterations to generate the gasket.
        """
        self.size = size
        self.iterations = iterations
        self.image = Image.new('RGB', (size, size), color='white')
        self.draw = ImageDraw.Draw(self.image)

    def draw_triangle(self, vertices, color):
        """
        Draw a triangle on the image.

        Parameters:
        - vertices (list): List of three tuples representing the vertices of the triangle.
        - color (str): Color of the triangle.
        """
        self.draw.polygon(vertices, fill=color, outline='black')

    def generate_gasket(self, vertices, depth):
        """
        Recursively generate the Sierpinski Gasket.

        Parameters:
        - vertices (list): List of three tuples representing the vertices of the triangle.
        - depth (int): Current depth of recursion.
        """
        if depth == 0:
            self.draw_triangle(vertices, 'black')
        else:
            midpoint1 = ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2)
            midpoint2 = ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2)
            midpoint3 = ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)

            self.generate_gasket([vertices[0], midpoint1, midpoint3], depth - 1)
            self.generate_gasket([midpoint1, vertices[1], midpoint2], depth - 1)
            self.generate_gasket([midpoint3, midpoint2, vertices[2]], depth - 1)

    def save_image(self, filename='sierpinski_gasket.png'):
        """
        Save the generated image.

        Parameters:
        - filename (str): Name of the output image file.
        """
        self.image.save(filename)


class SierpinskiGasketApp(tk.Tk):
    def __init__(self, size, iterations):
        """
        GUI application for displaying the Sierpinski Gasket.

        Parameters:
        - size (int): Size of the image.
        - iterations (int): Number of iterations to generate the gasket.
        """
        super().__init__()
        self.size = size
        self.iterations = iterations
        self.title("Sierpinski Gasket")
        self.canvas = tk.Canvas(self, width=size, height=size)
        self.canvas.pack()
        self.generate_and_display_gasket()

    def generate_and_display_gasket(self):
        """
        Generate and display the Sierpinski Gasket on the canvas.
        """
        gasket = SierpinskiGasket(self.size, self.iterations)
        vertices = [(0, gasket.size), (gasket.size, gasket.size), (gasket.size / 2, 0)]
        gasket.generate_gasket(vertices, self.iterations)
        gasket.save_image()

        image = ImageTk.PhotoImage(gasket.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
        self.image = image


if __name__ == '__main__':
    # Generate and save the Sierpinski Gasket
    gasket_generator = SierpinskiGasket(size=800, iterations=5)
    gasket_generator.generate_gasket([(0, gasket_generator.size),
                                       (gasket_generator.size, gasket_generator.size),
                                       (gasket_generator.size / 2, 0)], gasket_generator.iterations)
    gasket_generator.save_image()

    # Display the Sierpinski Gasket using GUI
    app = SierpinskiGasketApp(size=800, iterations=5)
    app.mainloop()
