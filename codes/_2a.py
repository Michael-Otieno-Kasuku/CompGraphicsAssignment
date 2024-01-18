"""
2. Given a 3-dimensional space which is defined by an 800 x 600 viewport and whose
coordinate axes have their origins at the center of the viewport, using PIL for python write
program statements which will produce the following effects:
a) Define a 3-dimensional equilateral triangle (a triangle pyramid) whose y-axis in
local space is located through the center of the triangle pyramid. The base of the
3D triangle may be aligned to the x-axis.
Note: The base of the equilateral traingle should be shaded grey
"""

"""
Draw 3D Equilateral Triangle with Grey Base

This script uses the Python Imaging Library (PIL) to draw a 3D equilateral triangle
with a grey-colored base. The triangle is displayed in a blank image with a white
background.

Constants:
    width (int): Width of the image.
    height (int): Height of the image.
    viewport_center (tuple): Center coordinates of the viewport.
    triangle_side_length (int): Length of the equilateral triangle's side.

Attributes:
    image (PIL.Image.Image): Blank image with white background.
    draw (PIL.ImageDraw.ImageDraw): Drawing context for the image.

Functions:
    draw_3d_triangle(viewport_center, triangle_side_length):
        Draws the 3D equilateral triangle with a grey-colored base.

    main():
        Main function to execute the drawing and display of the image.
"""

from PIL import Image, ImageDraw
import math

class EquilateralTriangle3D:
    """
    A class for drawing a 3D equilateral triangle with a grey-colored base.

    Attributes:
        width (int): Width of the image.
        height (int): Height of the image.
        viewport_center (tuple): Center coordinates of the viewport.
        triangle_side_length (int): Length of the equilateral triangle's side.
        image (PIL.Image.Image): Blank image with white background.
        draw (PIL.ImageDraw.ImageDraw): Drawing context for the image.
    """

    def __init__(self, width, height, triangle_side_length):
        """
        Initializes the EquilateralTriangle3D instance.

        Parameters:
            width (int): Width of the image.
            height (int): Height of the image.
            triangle_side_length (int): Length of the equilateral triangle's side.
        """
        self.width = width
        self.height = height
        self.viewport_center = (width // 2, height // 2)
        self.triangle_side_length = triangle_side_length
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def _calculate_vertices(self):
        """
        Calculates the vertices of the equilateral triangle in local space.

        Returns:
            tuple: Vertices of the equilateral triangle.
        """
        triangle_height = math.sqrt(3) / 2 * self.triangle_side_length
        vertex1 = (self.viewport_center[0] - self.triangle_side_length / 2, self.viewport_center[1] + triangle_height / 2)
        vertex2 = (self.viewport_center[0] + self.triangle_side_length / 2, self.viewport_center[1] + triangle_height / 2)
        vertex3 = (self.viewport_center[0], self.viewport_center[1] - triangle_height / 2)
        return vertex1, vertex2, vertex3

    def _draw_base(self, vertices):
        """
        Draws the base of the equilateral triangle with a grey fill.

        Parameters:
            vertices (tuple): Vertices of the equilateral triangle.
        """
        base_color = (169, 169, 169)
        self.draw.polygon([vertices[0], vertices[1], self.viewport_center, vertices[0]], fill=base_color, outline="black")

    def _draw_edges(self, vertices):
        """
        Draws the missing edges of the equilateral triangle.

        Parameters:
            vertices (tuple): Vertices of the equilateral triangle.
        """
        self.draw.line([vertices[0], vertices[1]], fill="black")
        self.draw.line([vertices[1], vertices[2]], fill="black")
        self.draw.line([vertices[2], vertices[0]], fill="black")

    def draw_3d_triangle(self):
        """
        Draws the 3D equilateral triangle on the image.
        """
        vertices = self._calculate_vertices()

        # Draw lines connecting the vertices to the center of the viewport to represent the 3D pyramid
        self.draw.line([self.viewport_center, vertices[0]], fill="black")
        self.draw.line([self.viewport_center, vertices[1]], fill="black")
        self.draw.line([self.viewport_center, vertices[2]], fill="black")

        # Draw the base of the triangle
        self._draw_base(vertices)

        # Draw the missing edges of the triangle
        self._draw_edges(vertices)

    def show_image(self):
        """
        Displays the image with the drawn 3D equilateral triangle.
        """
        self.image.show()

def main():
    """
    Main function to create and display the 3D equilateral triangle.
    """
    # Constants
    width, height = 800, 600
    triangle_side_length = 100

    # Create an instance of EquilateralTriangle3D
    triangle_3d = EquilateralTriangle3D(width, height, triangle_side_length)

    # Draw and display the 3D equilateral triangle
    triangle_3d.draw_3d_triangle()
    triangle_3d.show_image()

if __name__ == "__main__":
    main()
