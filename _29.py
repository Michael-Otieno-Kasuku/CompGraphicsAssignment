"""
Using PIL for Python, PyOpenGL and docstrings and OOP:

29. At the lowest level of processing, we manipulate bits in the framebuffer. In WebGL or
any other language, we can create a virtual framebuffer in our application as a two
dimensional array. You can experiment with simple raster algorithms, such as drawing
lines or circles, through a function that generates a single value in the array. Write a small
library that will allow you to work in a virtual framebuffer that you create in memory.
The core functions should be WritePixel and ReadPixel. Your library should allow you to
set up and display your virtual framebuffer and to run a user program that reads and
writes pixels using gl.POINTS in gl.drawArrays.
"""

from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np


class VirtualFramebuffer:
    """
    Virtual Framebuffer class for manipulating pixels in a virtual framebuffer.
    """

    def __init__(self, width, height):
        """
        Initialize the virtual framebuffer with the specified width and height.

        Parameters:
        - width: Width of the virtual framebuffer.
        - height: Height of the virtual framebuffer.
        """
        self.width = width
        self.height = height
        self.framebuffer = np.zeros((height, width, 3), dtype=np.uint8)

    def write_pixel(self, x, y, color):
        """
        Write a pixel with the specified color to the virtual framebuffer.

        Parameters:
        - x: X-coordinate of the pixel.
        - y: Y-coordinate of the pixel.
        - color: RGB color tuple.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.framebuffer[y, x] = color

    def read_pixel(self, x, y):
        """
        Read the color of a pixel from the virtual framebuffer.

        Parameters:
        - x: X-coordinate of the pixel.
        - y: Y-coordinate of the pixel.

        Returns:
        - RGB color tuple.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return tuple(self.framebuffer[y, x])
        else:
            return None

    def display_framebuffer(self):
        """
        Display the virtual framebuffer using PyOpenGL.
        """
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Virtual Framebuffer")

        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glDrawPixels(self.width, self.height, GL_RGB, GL_UNSIGNED_BYTE, self.framebuffer)

        glFlush()
        glutMainLoop()


if __name__ == "__main__":
    # Example usage
    virtual_framebuffer = VirtualFramebuffer(400, 300)

    # Write pixels to the virtual framebuffer
    virtual_framebuffer.write_pixel(100, 50, (255, 0, 0))  # Red pixel
    virtual_framebuffer.write_pixel(200, 150, (0, 255, 0))  # Green pixel
    virtual_framebuffer.write_pixel(300, 250, (0, 0, 255))  # Blue pixel

    # Read a pixel from the virtual framebuffer
    color = virtual_framebuffer.read_pixel(200, 150)
    print("Color at (200, 150):", color)

    # Display the virtual framebuffer using PyOpenGL
    virtual_framebuffer.display_framebuffer()
