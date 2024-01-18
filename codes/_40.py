"""
Using PIL for Python and docstrings and OOP:

40. Robotics is only one example in which the parts of the scene show compound motion,
where the movement of some objects depends on the movement of other objects. Other
examples include bicycles (with wheels), airplanes (with propellers), and merry-go-
rounds (with horses). Pick an example of compound motion. Write a graphics program to
simulate your selection.
"""

import pygame
from pygame.locals import *
from PIL import Image, ImageDraw, ImageOps
import math

class BicycleSimulator:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.bicycle_length = 80
        self.wheel_radius = 20
        self.angle = 0
        self.speed = 5
        self.create_bicycle_image()

    def create_bicycle_image(self):
        self.bicycle_image = Image.new("RGB", (self.width, self.height), "white")
        draw = ImageDraw.Draw(self.bicycle_image)
        self.draw_bicycle(draw)
        self.bicycle_image = ImageOps.mirror(self.bicycle_image)

    def draw_bicycle(self, draw):
        # Draw bicycle body
        draw.rectangle([self.width // 2 - 10, self.height // 2 - 20,
                        self.width // 2 + 10, self.height // 2 + self.bicycle_length], fill="blue")

        # Draw wheels
        wheel1_x = self.width // 2 - 20
        wheel2_x = self.width // 2 + 20
        wheel_y = self.height // 2 + self.bicycle_length
        draw.ellipse([wheel1_x - self.wheel_radius, wheel_y - self.wheel_radius,
                      wheel1_x + self.wheel_radius, wheel_y + self.wheel_radius], fill="black")
        draw.ellipse([wheel2_x - self.wheel_radius, wheel_y - self.wheel_radius,
                      wheel2_x + self.wheel_radius, wheel_y + self.wheel_radius], fill="black")

    def update_bicycle_position(self):
        self.angle += math.radians(self.speed)
        self.angle %= 2 * math.pi

    def draw(self):
        self.update_bicycle_position()
        rotated_bicycle = self.bicycle_image.rotate(math.degrees(self.angle))
        pygame_image = pygame.image.fromstring(rotated_bicycle.tobytes(), rotated_bicycle.size, rotated_bicycle.mode)
        pygame_surface = pygame.image.tostring(pygame_image, 'RGBA')
        pygame_surface = pygame.image.fromstring(pygame_surface, rotated_bicycle.size, 'RGBA')

        pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        pygame.display.get_surface().blit(pygame_surface, (0, 0))
        pygame.display.flip()

    def run_simulation(self):
        pygame.init()
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            self.draw()
            clock.tick(60)

if __name__ == "__main__":
    simulator = BicycleSimulator()
    simulator.run_simulation()
