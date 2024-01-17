"""
Using PIL for Python and docstrings:
Write a program to generate a Sierpinski gasket as follows. Start with a white triangle. At
each step, use transformations to generate three similar triangles that are drawn over the
original triangle, leaving the center of the triangle white and the three corners black.
"""

from PIL import Image, ImageDraw

class SierpinskiGasket:
    def __init__(self, size, depth):
        """
        Initialize the SierpinskiGasket object.

        Parameters:
        - size (int): Size of the output image.
        - depth (int): Recursion depth.
        """
        self.size = size
        self.depth = depth
        self.image = Image.new("RGB", (size, size), "white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_triangle(self, p1, p2, p3, depth):
        """
        Draw a Sierpinski triangle.

        Parameters:
        - p1, p2, p3 (tuple): Coordinates of the vertices of the triangle.
        - depth (int): Recursion depth.
        """
        if depth == 0:
            # Base case: fill the triangle with black
            self.draw.polygon([p1, p2, p3], fill="black")
        else:
            # Calculate midpoints of the edges
            mid1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            mid2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
            mid3 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)

            # Recursively draw three smaller triangles
            self.draw_triangle(p1, mid1, mid3, depth - 1)
            self.draw_triangle(mid1, p2, mid2, depth - 1)
            self.draw_triangle(mid3, mid2, p3, depth - 1)

    def generate(self):
        """
        Generate the Sierpinski gasket image.
        """
        # Define the initial triangle vertices
        p1 = (self.size // 2, 0)
        p2 = (0, self.size)
        p3 = (self.size, self.size)

        # Draw the Sierpinski triangle
        self.draw_triangle(p1, p2, p3, self.depth)

    def show(self):
        """
        Display the generated image.
        """
        self.image.show()

    def save(self, filename):
        """
        Save the generated image to a file.

        Parameters:
        - filename (str): Name of the file to save the image.
        """
        self.image.save(filename)

if __name__ == "__main__":
    # Set the size and depth parameters
    image_size = 500
    recursion_depth = 5

    # Create a SierpinskiGasket object
    sierpinski_gasket = SierpinskiGasket(image_size, recursion_depth)

    # Generate and display the Sierpinski gasket
    sierpinski_gasket.generate()
    sierpinski_gasket.show()

    # Save the image to a file
    sierpinski_gasket.save("sierpinski_gasket_oop.png")
