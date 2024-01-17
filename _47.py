"""
Using PIL for Python and docstrings and OOP:

47. Write a program to carry out subdivision of triangular or quadrilateral meshes. When the
subdivision is working correctly, add the averaging step to form a smoother surface.
"""

import pygame
from pygame.locals import *
import numpy as np

class MeshSubdivision:
    def __init__(self, vertices, faces):
        self.vertices = np.array(vertices)
        self.faces = np.array(faces)
        self.subdivide()

    def subdivide(self):
        new_vertices = self.vertices.copy()
        new_faces = []

        for face in self.faces:
            v1, v2, v3 = face
            midpoints = [(self.vertices[v1] + self.vertices[v2]) / 2,
                          (self.vertices[v2] + self.vertices[v3]) / 2,
                          (self.vertices[v3] + self.vertices[v1]) / 2]

            new_indices = [len(new_vertices), len(new_vertices) + 1, len(new_vertices) + 2]

            new_vertices = np.vstack([new_vertices, midpoints])
            new_faces.append([v1, new_indices[0], new_indices[2]])
            new_faces.append([new_indices[0], v2, new_indices[1]])
            new_faces.append([new_indices[2], new_indices[1], v3])
            new_faces.append([new_indices[0], new_indices[1], new_indices[2]])

        self.vertices = new_vertices
        self.faces = np.array(new_faces)

    def average_vertices(self):
        new_vertices = self.vertices.copy()

        for i in range(len(self.vertices)):
            neighbors = self.find_neighbors(i)
            num_neighbors = len(neighbors)
            average_position = np.sum(self.vertices[neighbors], axis=0) / num_neighbors
            new_vertices[i] = average_position

        self.vertices = new_vertices

    def find_neighbors(self, vertex_index):
        neighbors = set()

        for face in self.faces:
            if vertex_index in face:
                neighbors.update(face)

        neighbors.remove(vertex_index)
        return list(neighbors)

    def draw(self, surface):
        for face in self.faces:
            points = [tuple(self.vertices[v]) for v in face]
            pygame.draw.polygon(surface, (255, 255, 255), points, 0)

def main():
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Mesh Subdivision")

    vertices = [
        [-1, -1, 0],
        [1, -1, 0],
        [1, 1, 0],
        [-1, 1, 0]
    ]

    faces = [
        [0, 1, 2],
        [0, 2, 3]
    ]

    subdivision = MeshSubdivision(vertices, faces)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((0, 0, 0))
        subdivision.draw(screen)
        pygame.display.flip()

        pygame.time.delay(1000)  # Add a delay for better visualization
        subdivision.subdivide()
        subdivision.average_vertices()

        clock.tick(1)  # Set a low frame rate for better visualization

    pygame.quit()

if __name__ == "__main__":
    main()
