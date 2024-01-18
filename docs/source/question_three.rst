Question three
==============
Using the concept of a Current Transformation Matrix (push/pop matrices), write the
OpenGL or using whichever language code to define the object as illustrated below. Youmay assume that the object is composed of two squares and a circle of unit dimensions in
2D space.

ObjectWithShapes Class
----------------------

.. py:class:: ObjectWithShapes

   A class representing an object composed of squares and a circle in a 2D space.

   :ivar int width: The width of the image.
   :ivar int height: The height of the image.
   :ivar PIL.Image.Image image: The image object used for drawing shapes.
   :ivar PIL.ImageDraw.ImageDraw draw: The drawing context for the image.

   .. method:: __init__(width, height)

      Initializes an ObjectWithShapes instance.

      :param int width: The width of the image.
      :param int height: The height of the image.

   .. method:: draw_square(size, position)

      Draws a square on the image.

      :param int size: The size of the square.
      :param tuple position: The position of the top-left corner of the square (x, y).

   .. method:: draw_circle(radius, position)

      Draws a circle on the image.

      :param int radius: The radius of the circle.
      :param tuple position: The position of the center of the circle (x, y).

   .. method:: draw_object()

      Draws a composition of a circle in the middle, a square to the left, and a square to the right.

   .. method:: show_image()

      Displays the image.

.. function:: main()

   Main function to demonstrate the ObjectWithShapes class.

   Constants:
      - width (int): The width of the image (300).
      - height (int): The height of the image (200).

   Usage:
      - Create an instance of ObjectWithShapes.
      - Draw a composition of a circle in the middle, a square to the left, and a square to the right.
      - Display the image.

   Example usage:
   
   .. code-block:: python

      if __name__ == "__main__":
          main()

