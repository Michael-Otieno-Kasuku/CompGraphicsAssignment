Question ten
============
We can simulate many realistic effects using computer graphics by incorporating simple
physics in the model. Simulate a bouncing ball in two dimensions incorporating both
gravity and elastic collisions with a surface. You can model the ball with a closed
polygon that has a sufficient number of sides to look smooth.

BouncingBallSimulation Class
----------------------------

.. py:class:: BouncingBallSimulation

   A class for simulating the motion of a bouncing ball using Pygame.

   :ivar int width: Width of the simulation canvas.
   :ivar int height: Height of the simulation canvas.
   :ivar int ball_radius: Radius of the bouncing ball.
   :ivar list position: Current position of the ball as a tuple (x, y).
   :ivar list velocity: Current velocity of the ball as a tuple (vx, vy).
   :ivar float gravity: Acceleration due to gravity.
   :ivar float elasticity: Coefficient of restitution for elastic collisions.

   .. method:: __init__(width, height, ball_radius, initial_position, initial_velocity, gravity, elasticity)

      Initialize the bouncing ball simulation.

      :param int width: Width of the simulation canvas.
      :param int height: Height of the simulation canvas.
      :param int ball_radius: Radius of the bouncing ball.
      :param tuple initial_position: Initial position of the ball as a tuple (x, y).
      :param tuple initial_velocity: Initial velocity of the ball as a tuple (vx, vy).
      :param float gravity: Acceleration due to gravity.
      :param float elasticity: Coefficient of restitution for elastic collisions.

   .. method:: update_position(time_step)

      Update the position of the ball based on the current velocity and time step.

      :param float time_step: Time step for the simulation.

   .. method:: handle_wall_collisions()

      Check for collisions with the walls and update velocity accordingly.

   .. method:: simulate_bouncing_ball(num_frames, frame_duration, output_file=None)

      Simulate the bouncing ball for a specified number of frames.

      :param int num_frames: Number of frames to simulate.
      :param int frame_duration: Duration of each frame in milliseconds.
      :param str output_file: Output GIF file name (optional, None if not saving).

   .. method:: draw_frame()

      Draw the current frame with the bouncing ball.

      :returns: pygame.Surface - Pygame Surface object representing the current frame.

   .. method:: calculate_ball_points()

      Calculate the points of the ball polygon based on the current position and radius.

      :returns: list - List of tuples representing the points of the ball polygon.

   .. method:: handle_events()

      Handle events such as quitting the simulation.

   .. function:: main()

      Example usage:

      .. code-block:: python

         # Example usage
         width = 600
         height = 400
         ball_radius = 20
         initial_position = (width // 2, height // 2)
         initial_velocity = (100, 0)
         gravity = 300
         elasticity = 0.8
         num_frames = 100

         # Create and simulate bouncing ball
         simulation = BouncingBallSimulation(width, height, ball_radius, initial_position, initial_velocity, gravity, elasticity)
         simulation.simulate_bouncing_ball(num_frames, frame_duration=50)  # milliseconds

