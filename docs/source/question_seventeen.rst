Question Seventeen
==================
The color gamut in chromaticity coordinates is equivalent to the triangle in RGB space
that is defined by the primaries. Write a program that will display this triangle and the
edges of the cube in which it lies. Each point on the triangle should have the color
determined by its coordinates in RGB space. This triangle is called the Maxwell triangle.

MaxwellTriangle Class
---------------------
.. py:class:: MaxwellTriangle

   A class for generating and displaying the Maxwell Triangle with RGB cube edges.

   :ivar int size: Size of the output image.
   :ivar PIL.Image image: Image object for storing the generated image.
   :ivar PIL.ImageDraw draw: Draw object for drawing on the image.

   .. method:: __init__(size)

      Initialize the MaxwellTriangle object.

      :param int size: Size of the output image.

   .. method:: draw_triangle()

      Draw the Maxwell triangle and the edges of the RGB cube.

   .. method:: rgb_to_xy(rgb)

      Convert RGB coordinates to image coordinates.

      :param tuple rgb: RGB coordinates.

      :returns: Tuple of image coordinates.

   .. method:: show()

      Display the generated image.

   .. method:: save(filename)

      Save the generated image to a file.

      :param str filename: Name of the file to save the image.

   Example usage:

   .. code-block:: python

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

