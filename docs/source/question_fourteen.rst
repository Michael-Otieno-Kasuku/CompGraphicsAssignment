Question Fourteen
=================
The orientation of an airplane is described by a coordinate system as shown below. The
forward–backward motion of the joystick controls the up– down rotation with respect to
the axis running along the length of the airplane, called the pitch. The right–left motion of
the joystick controls the rotation about this axis, called the roll. Write a program that uses
the mouse to control pitch and roll for the view seen by a pilot. You can do this exercise
in two dimensions by considering a set of objects to be located far from the airplane, then
having the mouse control the two-dimensional viewing of these objects.

AirplaneView Class
------------------

.. py:class:: AirplaneView

   A class for displaying an airplane view using Pygame and PIL.

   :ivar float pitch_angle: Pitch angle of the airplane.
   :ivar float roll_angle: Roll angle of the airplane.
   :ivar int mouse_x: X-coordinate of the mouse position.
   :ivar int mouse_y: Y-coordinate of the mouse position.

   .. method:: __init__()

      Initialize the AirplaneView object.

   .. method:: update_view()

      Update the view of the airplane based on pitch and roll angles.

      :returns: Pygame surface representing the updated view.

   .. method:: draw_airplane(draw)

      Draw the airplane on the PIL ImageDraw object.

      :param draw: PIL ImageDraw object.

   .. method:: draw_distant_objects(draw)

      Draw distant objects on the PIL ImageDraw object.

      :param draw: PIL ImageDraw object.

   .. method:: handle_mouse_event(event)

      Handle mouse events to update mouse coordinates.

      :param event: Pygame mouse event.

   .. method:: update_angles()

      Update pitch and roll angles based on mouse position.

      :returns: None

.. method:: main()

   Main function to demonstrate the AirplaneView class.

   Constants:
      - SCREEN_WIDTH (int): Width of the Pygame window (800).
      - SCREEN_HEIGHT (int): Height of the Pygame window (600).
      - AIRPLANE_WIDTH (int): Width of the airplane representation (100).
      - AIRPLANE_HEIGHT (int): Height of the airplane representation (150).
      - AIRPLANE_COLOR (tuple): RGB color tuple for the airplane (255, 0, 0).
      - OBJECTS_COLOR (tuple): RGB color tuple for distant objects (0, 0, 255).

   Usage:
      - Create an instance of AirplaneView.
      - Move the mouse to control the pitch and roll angles.
      - Observe the updated view of the airplane.

   Example usage:

   .. code-block:: python

      if __name__ == "__main__":
          main()

