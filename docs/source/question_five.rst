Question five
=============
A quadratic B ́ezier curve is defined by three points, P1, P2, P3, and a parameter, t:
P(t) = (1−t) 2 P 1 + 2t(1−t)P 2 + t 2 P 3 , 0 ≤ t ≤ 1
Describe an algorithm that draws the quadratic B ́ezier curve, using straight lines only, to
within a tolerance τ. You may use the algorithm from part (a) and you may assume that
you already have an algorithm for drawing a straight line.

An algorithm that draws the quadratic B ́ezier curve, using straight lines only, to within a tolerance τ
--------------------------------------------------------------------------------------------------------
To draw a quadratic Bézier curve using straight lines within a given tolerance τ, you can use a recursive approach to approximate the curve with line segments. Here's a high-level description of the algorithm:

    Input: Three control points P1, P2, and P3, and a tolerance τ.
    Initialize: Set t = 0 and create an empty list to store line segments.
    Recursive Function: Implement a recursive function that takes the control points, the current parameter t, and the tolerance τ as parameters. The function should do the following:
    a. Calculate the Bézier curve point P(t) using the given formula.
    b. Check if the distance between P(t) and the line segment connecting P1 and P3 is less than τ. If true, add the line segment (P1, P3) to the list and return.
    c. If not, calculate midpoints P12 and P23 of the line segments (P1, P2) and (P2, P3).
    d. Recursively call the function for the control points (P1, P12, P(t)), (P(t), P23, P3).
    Initialize: Call the recursive function with the initial control points P1, P2, P3, t=0, and τ.
    Output: The list of line segments approximating the quadratic Bézier curve.

QuadraticBezierDrawer Class
---------------------------

.. py:class:: QuadraticBezierDrawer

   A class for drawing a quadratic Bézier curve using straight lines within a given tolerance τ.

   :ivar int width: Width of the image.
   :ivar int height: Height of the image.
   :ivar PIL.Image.Image image: The image object used for drawing the Bézier curve.
   :ivar PIL.ImageDraw.ImageDraw draw: The drawing context for the image.

   .. method:: __init__(width, height)

      Initialize the QuadraticBezierDrawer object.

      :param int width: Width of the image.
      :param int height: Height of the image.

   .. method:: interpolate(point1, point2, t)

      Interpolate between two points.

      :param tuple point1: First point (x, y).
      :param tuple point2: Second point (x, y).
      :param float t: Interpolation parameter.

      :returns: Interpolated point (x, y).

   .. method:: draw_line(point1, point2)

      Draw a line between two points.

      :param tuple point1: First point (x, y).
      :param tuple point2: Second point (x, y).

   .. method:: draw_quadratic_bezier(P1, P2, P3, t, tolerance)

      Draw a quadratic Bézier curve using straight lines.

      :param tuple P1: First control point (x, y).
      :param tuple P2: Second control point (x, y).
      :param tuple P3: Third control point (x, y).
      :param float t: Interpolation parameter.
      :param float tolerance: Tolerance for approximation.

   .. method:: line_segment(point1, point2)

      Define a line segment by two points.

      :param tuple point1: First point (x, y).
      :param tuple point2: Second point (x, y).

      :returns: Line segment represented by two points.

   .. method:: distance(point, line_segment)

      Calculate the distance between a point and a line segment.

      :param tuple point: Point (x, y).
      :param list line_segment: Line segment represented by two points.

      :returns: Distance between the point and the line segment.

   .. method:: save_image(filename)

      Save the image.

      :param str filename: Filename to save the image.

   .. function:: main()

      Main function to demonstrate the QuadraticBezierDrawer class.

      Constants:
         - P1 (tuple): First control point (50, 250).
         - P2 (tuple): Second control point (150, 50).
         - P3 (tuple): Third control point (250, 250).
         - t (float): Interpolation parameter (0).
         - tolerance (float): Tolerance for approximation (2).

      Usage:
         - Create an instance of QuadraticBezierDrawer.
         - Draw a quadratic Bézier curve using draw_quadratic_bezier.
         - Save the image.

      Example usage:
      
      .. code-block:: python

         if __name__ == "__main__":
             bezier_drawer = QuadraticBezierDrawer(width=300, height=300)

             P1 = (50, 250)
             P2 = (150, 50)
             P3 = (250, 250)

             t = 0
             tolerance = 2

             bezier_drawer.draw_quadratic_bezier(P1, P2, P3, t, tolerance)
             bezier_drawer.save_image("quadratic_bezier_oop.png")

