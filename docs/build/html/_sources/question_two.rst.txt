Question two
============
Given a 3-dimensional space defined by an 800 x 600 viewport, with coordinate axes having their origins at the center of the viewport, write OpenGL (or any language you understand) program statements to achieve the following effects:

a. Define a 3-dimensional equilateral triangle (a triangle pyramid) with its y-axis in local space located through the center of the triangle pyramid. The base of the 3D triangle may be aligned to the x-axis.

b. Transpose three (3) object instances of the 3-dimensional triangle (defined in part (i) above) to global space, along the same z-plane. Position the left object tilted 30 degrees left of the y-axis, the center object aligned vertically with the y-axis, and the right object tilted 30 degrees right of the y-axis.

Hint: You may use a separate function to define the object in local space and call that function in your display/render function to position the objects in world space.

Part a
------
.. py:class:: EquilateralTriangle3D

   A class for drawing a 3D equilateral triangle with a grey-colored base.

   :ivar int width: Width of the image.
   :ivar int height: Height of the image.
   :ivar tuple viewport_center: Center coordinates of the viewport.
   :ivar int triangle_side_length: Length of the equilateral triangle's side.
   :ivar PIL.Image.Image image: Blank image with white background.
   :ivar PIL.ImageDraw.ImageDraw draw: Drawing context for the image.

   .. method:: __init__(width, height, triangle_side_length)

      Initializes the EquilateralTriangle3D instance.

      :param int width: Width of the image.
      :param int height: Height of the image.
      :param int triangle_side_length: Length of the equilateral triangle's side.

   .. method:: _calculate_vertices()

      Calculates the vertices of the equilateral triangle in local space.

      :returns: tuple: Vertices of the equilateral triangle.

   .. method:: _draw_base(vertices)

      Draws the base of the equilateral triangle with a grey fill.

      :param tuple vertices: Vertices of the equilateral triangle.

   .. method:: _draw_edges(vertices)

      Draws the missing edges of the equilateral triangle.

      :param tuple vertices: Vertices of the equilateral triangle.

   .. method:: draw_3d_triangle()

      Draws the 3D equilateral triangle on the image.

   .. method:: show_image()

      Displays the image with the drawn 3D equilateral triangle.

.. function:: main()

   Main function to create and display the 3D equilateral triangle.

   Constants:
      - width (int): Width of the image (800).
      - height (int): Height of the image (600).
      - triangle_side_length (int): Length of the equilateral triangle's side (100).

   Usage:
      - Create an instance of EquilateralTriangle3D.
      - Draw and display the 3D equilateral triangle.

   Example usage:
   
   .. code-block:: python

      if __name__ == "__main__":
          main()

Part b
------
.. py:class:: EquilateralTriangle3D

   A class for drawing a 3D equilateral triangle with a grey-colored base.

   :ivar int width: Width of the image.
   :ivar int height: Height of the image.
   :ivar tuple viewport_center: Center coordinates of the viewport.
   :ivar int triangle_side_length: Side length of the equilateral triangle.
   :ivar PIL.Image.Image image: Blank image with white background.
   :ivar PIL.ImageDraw.ImageDraw draw: Drawing context for the image.

   .. method:: __init__(width, height, triangle_side_length)

      Initialize an EquilateralTriangle3D object.

      :param int width: Width of the image.
      :param int height: Height of the image.
      :param int triangle_side_length: Side length of the equilateral triangle.

   .. method:: _calculate_vertices_local()

      Calculate the local coordinates of the vertices of the equilateral triangle.

      :returns: tuple: Tuple containing three vertices as (x, y) coordinates.

   .. method:: _rotate_vertices(vertices, angle)

      Rotate vertices around their centroid by a specified angle.

      :param list of tuple vertices: List of vertices as (x, y) coordinates.
      :param float angle: Rotation angle in degrees.

      :returns: list of tuple: List of rotated vertices as (x, y) coordinates.

   .. method:: _translate_vertices(vertices, translation)

      Translate vertices by a specified translation vector.

      :param list of tuple vertices: List of vertices as (x, y) coordinates.
      :param tuple translation: Translation vector as (dx, dy).

      :returns: list of tuple: List of translated vertices as (x, y) coordinates.

   .. method:: _draw_base(vertices)

      Draw the base of the equilateral triangle.

      :param list of tuple vertices: List of vertices as (x, y) coordinates.

   .. method:: _draw_edges(vertices)

      Draw the edges of the equilateral triangle.

      :param list of tuple vertices: List of vertices as (x, y) coordinates.

   .. method:: draw_3d_triangle_local(position, rotation_angle=0)

      Draw a 3D equilateral triangle in local space.

      :param tuple position: Position of the triangle as (x, y) coordinates.
      :param float rotation_angle: Rotation angle in degrees (default is 0).

   .. method:: show_image()

      Display the image with the drawn triangles.

.. function:: main()

   Main function to demonstrate the usage of EquilateralTriangle3D class.

   Constants:
      - width (int): Width of the image (800).
      - height (int): Height of the image (600).
      - triangle_side_length (int): Side length of the equilateral triangle (100).

   Usage:
      - Create an instance of EquilateralTriangle3D.
      - Draw three 3D triangles in global space with different positions and rotation angles.

   Example usage:
   
   .. code-block:: python

      if __name__ == "__main__":
          main()

