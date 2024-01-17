"""
Using PIL for Python and docstrings and OOP:
The color gamut in chromaticity coordinates is equivalent to the triangle in RGB space
that is defined by the primaries. Write a program that will display this triangle and the
edges of the cube in which it lies. Each point on the triangle should have the color
determined by its coordinates in RGB space. This triangle is called the Maxwell triangle.
"""

from PIL import Image, ImageDraw

class MaxwellTriangle:
    def __init__(self, size):
        """
        Initialize the MaxwellTriangle object.

        Parameters:
        - size (int): Size of the output image.
        """
        self.size = size
        self.image = Image.new("RGB", (size, size), "white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_triangle(self):
        """
        Draw the Maxwell triangle and the edges of the RGB cube.
        """
        # Define RGB cube vertices
        cube_vertices = [
            (0, 0, 0),  # black (0,0,0)
            (255, 0, 0),  # red (255,0,0)
            (0, 255, 0),  # green (0,255,0)
            (0, 0, 255),  # blue (0,0,255)
            (255, 255, 0),  # yellow (255,255,0)
            (255, 0, 255),  # magenta (255,0,255)
            (0, 255, 255),  # cyan (0,255,255)
            (255, 255, 255)  # white (255,255,255)
        ]

        # Define RGB triangle vertices
        triangle_vertices = [
            (255, 0, 0),  # red
            (0, 255, 0),  # green
            (0, 0, 255)   # blue
        ]

        # Draw RGB cube edges
        for i in range(4):
            self.draw.line([self.rgb_to_xy(cube_vertices[i]), self.rgb_to_xy(cube_vertices[(i+1)%4])], fill="black")

        for i in range(4, 8):
            self.draw.line([self.rgb_to_xy(cube_vertices[i]), self.rgb_to_xy(cube_vertices[i-4])], fill="black")

        self.draw.line([self.rgb_to_xy(cube_vertices[0]), self.rgb_to_xy(cube_vertices[4])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[1]), self.rgb_to_xy(cube_vertices[5])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[2]), self.rgb_to_xy(cube_vertices[6])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[3]), self.rgb_to_xy(cube_vertices[7])], fill="black")

        # Draw Maxwell triangle
        self.draw.polygon([self.rgb_to_xy(v) for v in triangle_vertices], outline="black")

    def rgb_to_xy(self, rgb):
        """
        Convert RGB coordinates to image coordinates.

        Parameters:
        - rgb (tuple): RGB coordinates.

        Returns:
        - tuple: Image coordinates.
        """
        x = int(rgb[0] / 255 * (self.size - 1))
        y = self.size - 1 - int(rgb[1] / 255 * (self.size - 1))
        return x, y

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
    # Set the size parameter
    image_size = 500

    # Create a MaxwellTriangle object
    maxwell_triangle = MaxwellTriangle(image_size)

    # Draw and display the Maxwell triangle with RGB cube edges
    maxwell_triangle.draw_triangle()
    maxwell_triangle.show()

    # Save the image to a file
    maxwell_triangle.save("maxwell_triangle_oop.png")
