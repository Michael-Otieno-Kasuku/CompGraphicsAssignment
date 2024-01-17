"""
3. Using the concept of a Current Transformation Matrix (push/pop matrices), using PIL for Python write a
code to define the object such that one circle is in the middle,one square to the left of the circle
and another square to the right of the circle.You may assume that the object is composed of two squares
and a circle of unit dimensions in 2D space.
"""

from PIL import Image, ImageDraw

class ObjectWithShapes:
    """
    A class representing an object composed of squares and a circle in a 2D space.

    Attributes:
    - width (int): The width of the image.
    - height (int): The height of the image.
    - image (PIL.Image.Image): The image object used for drawing shapes.
    - draw (PIL.ImageDraw.ImageDraw): The drawing context for the image.

    Methods:
    - draw_square(size, position): Draws a square on the image.
    - draw_circle(radius, position): Draws a circle on the image.
    - draw_object(): Draws a composition of a circle in the middle, a square to the left, and a square to the right.
    - show_image(): Displays the image.
    """

    def __init__(self, width, height):
        """
        Initializes an ObjectWithShapes instance.

        Parameters:
        - width (int): The width of the image.
        - height (int): The height of the image.
        """
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_square(self, size, position):
        """
        Draws a square on the image.

        Parameters:
        - size (int): The size of the square.
        - position (tuple): The position of the top-left corner of the square (x, y).
        """
        self.draw.rectangle([position, (position[0] + size, position[1] + size)], outline="black")

    def draw_circle(self, radius, position):
        """
        Draws a circle on the image.

        Parameters:
        - radius (int): The radius of the circle.
        - position (tuple): The position of the center of the circle (x, y).
        """
        self.draw.ellipse([position[0] - radius, position[1] - radius, position[0] + radius, position[1] + radius], outline="black")

    def draw_object(self):
        """
        Draws a composition of a circle in the middle, a square to the left, and a square to the right.
        """
        # Draw a circle in the middle
        circle_radius = 10
        circle_center = (self.width // 2, self.height // 2)
        self.draw_circle(circle_radius, circle_center)

        # Draw a square to the left
        square_size = 20
        square_top_left = (circle_center[0] - circle_radius * 2 - square_size, circle_center[1] - square_size // 2)
        self.draw_square(square_size, square_top_left)

        # Draw a square to the right
        square_top_right = (circle_center[0] + circle_radius * 2, circle_center[1] - square_size // 2)
        self.draw_square(square_size, square_top_right)

    def show_image(self):
        """
        Displays the image.
        """
        self.image.show()

def main():
    """
    Main function to demonstrate the ObjectWithShapes class.
    """
    width, height = 300, 200
    object_with_shapes = ObjectWithShapes(width, height)
    object_with_shapes.draw_object()
    object_with_shapes.show_image()

if __name__ == "__main__":
    main()
