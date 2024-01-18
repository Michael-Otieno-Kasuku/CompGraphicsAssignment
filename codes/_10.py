import pygame
import sys
import math

class BouncingBallSimulation:
    def __init__(self, width, height, ball_radius, initial_position, initial_velocity, gravity, elasticity):
        self.width = width
        self.height = height
        self.ball_radius = ball_radius
        self.position = list(initial_position)
        self.velocity = list(initial_velocity)
        self.gravity = gravity
        self.elasticity = elasticity

    def update_position(self, time_step):
        self.position[0] += self.velocity[0] * time_step
        self.position[1] += self.velocity[1] * time_step
        self.velocity[1] += self.gravity * time_step
        self.handle_wall_collisions()

    def handle_wall_collisions(self):
        if self.position[0] - self.ball_radius < 0 or self.position[0] + self.ball_radius > self.width:
            self.velocity[0] *= -self.elasticity
        if self.position[1] - self.ball_radius < 0 or self.position[1] + self.ball_radius > self.height:
            self.velocity[1] *= -self.elasticity

    def simulate_bouncing_ball(self, num_frames, frame_duration, output_file=None):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bouncing Ball Simulation")
        frames = []
        for _ in range(num_frames):
            self.handle_events()
            self.update_position(frame_duration / 1000.0)
            frame = self.draw_frame()
            frames.append(frame)
            screen.blit(frame, (0, 0))
            pygame.display.flip()
            clock.tick(60)
        if output_file:
            pygame.image.save(frames[0], output_file)
        pygame.quit()
        sys.exit()

    def draw_frame(self):
        surface = pygame.Surface((self.width, self.height))
        surface.fill((255, 255, 255))
        ball_points = self.calculate_ball_points()
        pygame.draw.polygon(surface, (0, 0, 255), ball_points)
        return surface

    def calculate_ball_points(self):
        num_sides = 32
        ball_points = []
        for i in range(num_sides):
            angle = 2 * math.pi * i / num_sides
            x = self.position[0] + self.ball_radius * math.cos(angle)
            y = self.position[1] + self.ball_radius * math.sin(angle)
            ball_points.append((int(x), int(y)))
        return ball_points

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

width = 600
height = 400
ball_radius = 20
initial_position = (width // 2, height // 2)
initial_velocity = (100, 0)
gravity = 300
elasticity = 0.8
num_frames = 100

simulation = BouncingBallSimulation(width, height, ball_radius, initial_position, initial_velocity, gravity, elasticity)
simulation.simulate_bouncing_ball(num_frames, frame_duration=50)
