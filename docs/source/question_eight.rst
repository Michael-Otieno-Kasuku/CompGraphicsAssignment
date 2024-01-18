Question eight
==============
Implement the suggestion about displaying a rotating cube in the program. Add a button
that, when the cube is loaded, can update the locations of the cube vertices by computing
them with a new value of t, the amount to rotate. To make the animation look smooth, try
changing t by .05 radians per button click.

RotatingCube Class
------------------

.. py:class:: RotatingCube

   A class for displaying a rotating cube using Tkinter.

   :ivar tk.Tk master: The main Tkinter window.
   :ivar int width: Width of the canvas.
   :ivar int height: Height of the canvas.
   :ivar float t: Current rotation angle.
   :ivar int cube_size: Size of the cube.
   :ivar list vertices: List of cube vertices.
   :ivar tk.Canvas canvas: Tkinter canvas for drawing the cube.
   :ivar tk.Button update_button: Tkinter button for updating the rotation.
   
   .. method:: __init__(master)

      Initialize the RotatingCube object.

      :param tk.Tk master: The main Tkinter window.

   .. method:: calculate_cube_vertices()

      Calculate the vertices of the cube based on the current rotation angle.

      :returns: List of cube vertices.

   .. method:: draw_cube()

      Draw the cube on the canvas.

      :returns: None

   .. method:: update_rotation()

      Update the rotation angle and redraw the cube with smooth transitions.

      :returns: None

   .. method:: draw_polygon(face, color)

      Draw a polygon on the canvas.

      :param list face: List of vertices forming the polygon.
      :param str color: Fill color of the polygon.

      :returns: None

   .. method:: main()

      Main function to demonstrate the RotatingCube class.

      Constants:
         - width (int): Width of the canvas (400).
         - height (int): Height of the canvas (400).
         - t (float): Initial rotation angle (0).
         - cube_size (int): Size of the cube (100).

      Usage:
         - Create an instance of RotatingCube.
         - Draw the rotating cube on the canvas.
         - Use the button to update the rotation.

      Example usage:

      .. code-block:: python

         if __name__ == "__main__":
             root = tk.Tk()
             rotating_cube = RotatingCube(root)
             root.mainloop()

