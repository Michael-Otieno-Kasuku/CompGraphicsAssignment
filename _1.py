"""
1. Using the PNGWriter class,use PIL for Python to write a program to create a PNG image
(called image.png) with dimensions 300 pixels by 300 pixels and containing a red primary
diagonal line (top left to bottom right) and a green secondary diagonal line (bottom left to top right), then
fill the lowest bounded quadrant in blue. 10 Marks
"""
from PIL import Image, ImageDraw

class PNGWriter:
    """
    PNGWriter class for creating and manipulating PNG images using PIL (Pillow).

    Parameters:
    - width (int): Width of the image.
    - height (int): Height of the image.
    """

    def __init__(self, width, height):
        """
        Initialize the PNGWriter with the specified width and height.

        Args:
        - width (int): Width of the image.
        - height (int): Height of the image.
        """
        self.image = Image.new("RGB", (width, height), color="white")
        self.draw = ImageDraw.Draw(self.image)

    def save(self, filename):
        """
        Save the generated image to a file.

        Args:
        - filename (str): The name of the file to save the image to.
        """
        self.image.save(filename)

    def draw_primary_diagonal(self, color):
        """
        Draw the primary diagonal of the image with the specified color.

        Args:
        - color (str): Color of the diagonal line.
        """
        for i in range(min(self.image.width, self.image.height)):
            self.draw.point((i, i), fill=color)

    def draw_secondary_diagonal(self, color):
        """
        Draw the secondary diagonal of the image with the specified color.

        Args:
        - color (str): Color of the diagonal line.
        """
        for i in range(min(self.image.width, self.image.height)):
            self.draw.point((i, self.image.height - 1 - i), fill=color)

    def fill_quadrant(self, color, quadrant):
        """
        Fill a specified quadrant of the image with the specified color.

        Args:
        - color (str): Color to fill the quadrant with.
        - quadrant (int): Quadrant to fill (0: top-left, 1: top-right, 2: bottom-left, 3: bottom-right).
        """
        width, height = self.image.size
        x_range = range(width // 2) if quadrant % 2 == 0 else range(width // 2, width)
        y_range = range(height // 2) if quadrant < 2 else range(height // 2, height)

        for x in x_range:
            for y in y_range:
                self.draw.point((x, y), fill=color)

# Create PNG image with specified requirements
png_writer = PNGWriter(300, 300)

# Draw primary diagonal in red
png_writer.draw_primary_diagonal("red")

# Draw secondary diagonal in green
png_writer.draw_secondary_diagonal("green")

# Fill lowest bounded quadrant in blue
png_writer.fill_quadrant("blue", 3)

# Save the image
png_writer.save("image.png")
