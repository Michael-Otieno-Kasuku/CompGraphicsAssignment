import pygame
import sys
import math

class BouncingBallSimulation:
    def __init__(self, width, height, ball_radius, initial_position, initial_velocity, gravity, elasticity):
        """
        Initialize the bouncing ball simulation.

        Parameters:
        - width: Width of the simulation canvas.
        - height: Height of the simulation canvas.
        - ball_radius: Radius of the bouncing ball.
        - initial_position: Initial position of the ball as a tuple (x, y).
        - initial_velocity: Initial velocity of the ball as a tuple (vx, vy).
        - gravity: Acceleration due to gravity.
        - elasticity: Coefficient of restitution for elastic collisions.
        """
        self.width = width
        self.height = height
        self.ball_radius = ball_radius
        self.position = list(initial_position)
        self.velocity = list(initial_velocity)
        self.gravity = gravity
        self.elasticity = elasticity

    def update_position(self, time_step):
        """
        Update the position of the ball based on the current velocity and time step.

        Parameters:
        - time_step: Time step for the simulation.
        """
        # Update position using current velocity
        self.position[0] += self.velocity[0] * time_step
        self.position[1] += self.velocity[1] * time_step

        # Update velocity due to gravity
        self.velocity[1] += self.gravity * time_step

        # Check for collisions with walls and update velocity accordingly
        self.handle_wall_collisions()

    def handle_wall_collisions(self):
        """
        Check for collisions with the walls and update velocity accordingly.
        """
        if self.position[0] - self.ball_radius < 0 or self.position[0] + self.ball_radius > self.width:
            self.velocity[0] *= -self.elasticity  # Reflect horizontally

        if self.position[1] - self.ball_radius < 0 or self.position[1] + self.ball_radius > self.height:
            self.velocity[1] *= -self.elasticity  # Reflect vertically

    def simulate_bouncing_ball(self, num_frames, frame_duration, output_file=None):
        """
        Simulate the bouncing ball for a specified number of frames.

        Parameters:
        - num_frames: Number of frames to simulate.
        - frame_duration: Duration of each frame in milliseconds.
        - output_file: Output GIF file name (optional, None if not saving).
        """
        pygame.init()
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bouncing Ball Simulation")

        frames = []
        for _ in range(num_frames):
            self.handle_events()
            self.update_position(frame_duration / 1000.0)  # Convert frame duration to seconds
            frame = self.draw_frame()
            frames.append(frame)

            screen.blit(frame, (0, 0))
            pygame.display.flip()

            clock.tick(60)  # Cap the frame rate to 60 FPS

        if output_file:
            pygame.image.save(frames[0], output_file)

        pygame.quit()
        sys.exit()

    def draw_frame(self):
        """
        Draw the current frame with the bouncing ball.

        Returns:
        - Surface: Pygame Surface object representing the current frame.
        """
        surface = pygame.Surface((self.width, self.height))
        surface.fill((255, 255, 255))

        # Draw the bouncing ball as a filled polygon
        ball_points = self.calculate_ball_points()
        pygame.draw.polygon(surface, (0, 0, 255), ball_points)

        return surface

    def calculate_ball_points(self):
        """
        Calculate the points of the ball polygon based on the current position and radius.

        Returns:
        - List: List of tuples representing the points of the ball polygon.
        """
        num_sides = 32  # Number of sides for the ball polygon
        ball_points = []

        for i in range(num_sides):
            angle = 2 * math.pi * i / num_sides
            x = self.position[0] + self.ball_radius * math.cos(angle)
            y = self.position[1] + self.ball_radius * math.sin(angle)
            ball_points.append((int(x), int(y)))

        return ball_points

    def handle_events(self):
        """
        Handle events such as quitting the simulation.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
