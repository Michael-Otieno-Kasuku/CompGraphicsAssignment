Question one
============
Using the PNGWriter class, write a program to create a PNG image (called image.png)
with dimensions 300 pixels by 300 pixels and containing a red primary diagonal line (top
left to bottom right) and a green secondary diagonal line (bottom left to top right), then
fill the lowest bounded quadrant in blue. 10 Marks

PNGWriter Class
---------------

.. py:class:: PNGWriter

   PNGWriter class for creating and manipulating PNG images using PIL (Pillow).

   :ivar int width: Width of the image.
   :ivar int height: Height of the image.

   .. method:: __init__(width, height)

      Initialize the PNGWriter with the specified width and height.

      :param int width: Width of the image.
      :param int height: Height of the image.

   .. method:: save(filename)

      Save the generated image to a file.

      :param str filename: The name of the file to save the image to.

   .. method:: draw_primary_diagonal(color)

      Draw the primary diagonal of the image with the specified color.

      :param str color: Color of the diagonal line.

   .. method:: draw_secondary_diagonal(color)

      Draw the secondary diagonal of the image with the specified color.

      :param str color: Color of the diagonal line.

   .. method:: fill_quadrant(color, quadrant)

      Fill a specified quadrant of the image with the specified color.

      :param str color: Color to fill the quadrant with.
      :param int quadrant: Quadrant to fill (0: top-left, 1: top-right, 2: bottom-left, 3: bottom-right).

