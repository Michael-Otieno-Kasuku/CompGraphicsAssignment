Question Eighteen
=================
Write a program to generate the locations of pixels along a rasterized line segment using
Bresenham’s algorithm. Check that your program works for all slopes and all possible
locations of the endpoints. What is the initial value of the decision variable?

BresenhamLine Class
-------------------

.. py:class:: BresenhamLine

   A class for generating pixel locations along a rasterized line segment using Bresenham's Line Drawing Algorithm.

   :ivar tuple start: (x, y) coordinates of the starting point.
   :ivar tuple end: (x, y) coordinates of the ending point.
   :ivar list points: List of pixel locations along the line.

   .. method:: __init__(start, end)

      Initialize the BresenhamLine object.

      :param tuple start: (x, y) coordinates of the starting point.
      :param tuple end: (x, y) coordinates of the ending point.

   .. method:: draw_line()

      Generate the locations of pixels along the rasterized line segment using Bresenham's algorithm.

   .. method:: create_image(filename='line_image.png')

      Create an image and draw the line on it.

      :param str filename: Name of the output image file (default is 'line_image.png').

   Example usage:

   .. code-block:: python

      if __name__ == "__main__":
          # Example usage
          start_point = (10, 20)
          end_point = (100, 80)

          bresenham_line = BresenhamLine(start_point, end_point)
          bresenham_line.draw_line()
          bresenham_line.create_image('output_line.png')

