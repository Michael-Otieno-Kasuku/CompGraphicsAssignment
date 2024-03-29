"""
Using PIL for Python and docstrings and OOP:

44. Write a particle systemthat simulates the sparks that are generated by welding or by
fireworks.
"""

import pygame
from pygame.locals import *
import random

class Particle:
    def __init__(self, position, velocity, color, lifetime):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.lifetime = lifetime
        self.age = 0

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.age += 1

class ParticleSystem:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.particles = []

    def generate_particle(self, position, velocity, color, lifetime):
        particle = Particle(position, velocity, color, lifetime)
        self.particles.append(particle)

    def update_particles(self):
        for particle in self.particles:
            particle.update()

        # Remove expired particles
        self.particles = [particle for particle in self.particles if particle.age < particle.lifetime]

    def draw_particles(self, surface):
        for particle in self.particles:
            pygame.draw.circle(surface, particle.color, (int(particle.position[0]), int(particle.position[1])), 2)

def main():
    pygame.init()

    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL)

    clock = pygame.time.Clock()

    particle_system = ParticleSystem(screen_size)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        particle_system.generate_particle(
            position=(screen_size[0] // 2, screen_size[1]),
            velocity=(random.uniform(-1, 1), random.uniform(-3, -1)),
            color=(255, 255, 0),
            lifetime=50
        )

        particle_system.update_particles()

        screen.fill((0, 0, 0))
        particle_system.draw_particles(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
