Question Sixteen
================
Write a program to generate a Sierpinski gasket as follows. Start with a white triangle. At
each step, use transformations to generate three similar triangles that are drawn over the
original triangle, leaving the center of the triangle white and the three corners black.

SierpinskiGasket Class
----------------------

.. py:class:: SierpinskiGasket

   A class for generating and displaying the Sierpinski Gasket image.

   :ivar int size: Size of the output image.
   :ivar int depth: Recursion depth.
   :ivar PIL.Image image: Image object for storing the generated image.
   :ivar PIL.ImageDraw draw: Draw object for drawing on the image.

   .. method:: __init__(size, depth)

      Initialize the SierpinskiGasket object.

      :param int size: Size of the output image.
      :param int depth: Recursion depth.

   .. method:: draw_triangle(p1, p2, p3, depth)

      Draw a Sierpinski triangle.

      :param tuple p1: Coordinates of the first vertex.
      :param tuple p2: Coordinates of the second vertex.
      :param tuple p3: Coordinates of the third vertex.
      :param int depth: Recursion depth.

   .. method:: generate()

      Generate the Sierpinski Gasket image.

   .. method:: show()

      Display the generated image.

   .. method:: save(filename)

      Save the generated image to a file.

      :param str filename: Name of the file to save the image.

   Example usage:

   .. code-block:: python

      if __name__ == "__main__":
          # Set the size and depth parameters
          image_size = 500
          recursion_depth = 5

          # Create a SierpinskiGasket object
          sierpinski_gasket = SierpinskiGasket(image_size, recursion_depth)

          # Generate and display the Sierpinski Gasket
          sierpinski_gasket.generate()
          sierpinski_gasket.show()

          # Save the image to a file
          sierpinski_gasket.save("sierpinski_gasket_oop.png")

