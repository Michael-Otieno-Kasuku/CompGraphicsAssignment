"""
Using PIL for Python and docstrings and OOP:

26. The goal of this assignment is to introduce you to mesh representation,
curve/surface smoothing, and modeling. You will be creating a basic interactive
modeling program for generating smooth surfaces that allows a user to drag
vertices of a coarse control mesh in 3D while displaying an associated smooth
surface. You will be asked to implement aspects of both the user interface and the
subdivision algorithm, and finally use your program to construct several models.
Specifically, you will write a program that reads a set of triangle from a. ray file,
builds a "control" mesh from these triangles (shown in green above), and displays
it in a window using PyGame. As the program executes, a user can subdivide the
control mesh (each press of the `S' key subdivides one level further) to produce a
smooth subdivision surface for display (shown in gray above). The user may also
drag vertices of the control mesh with the mouse while the corresponding finest
level of the subdivision surface is updated continuously in the display. To createthe smooth surface, we will be implementing the Loop subdivision scheme.
"""

import pygame
import sys
import math

class ControlMesh:
    def __init__(self, triangles):
        """
        Control mesh class for interactive modeling.

        Parameters:
        - triangles (list): List of triangles represented as vertices.
        """
        self.vertices = triangles  # Initialize control mesh vertices
        self.subdivision_level = 0  # Current subdivision level

    def draw(self, screen):
        """
        Draw the control mesh on the screen.

        Parameters:
        - screen: Pygame screen object.
        """
        # Implement drawing logic for the control mesh
        pass

    def subdivide(self):
        """
        Subdivide the control mesh using the Loop subdivision scheme.
        """
        # Implement the Loop subdivision algorithm
        pass

    def drag_vertex(self, index, dx, dy):
        """
        Drag a vertex of the control mesh.

        Parameters:
        - index (int): Index of the vertex to be dragged.
        - dx (float): Change in x-coordinate.
        - dy (float): Change in y-coordinate.
        """
        # Implement logic to update the position of the dragged vertex
        pass

class InteractiveModeling:
    def __init__(self, triangles):
        """
        Interactive modeling class using Pygame.

        Parameters:
        - triangles (list): List of triangles represented as vertices.
        """
        pygame.init()
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Interactive Modeling')

        self.clock = pygame.time.Clock()
        self.running = True
        self.control_mesh = ControlMesh(triangles)

    def handle_events(self):
        """
        Handle Pygame events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.control_mesh.subdivide()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    # Find the closest vertex and start dragging it
                    index = self.find_closest_vertex(x, y)
                    if index is not None:
                        self.drag_vertex_index = index

                elif event.button == 3:  # Right mouse button
                    # Stop dragging
                    self.drag_vertex_index = None

            elif event.type == pygame.MOUSEMOTION and self.drag_vertex_index is not None:
                x, y = event.pos
                dx = x - self.drag_start_pos[0]
                dy = y - self.drag_start_pos[1]
                self.control_mesh.drag_vertex(self.drag_vertex_index, dx, dy)
                self.drag_start_pos = (x, y)

    def find_closest_vertex(self, x, y):
        """
        Find the index of the closest vertex to the given coordinates.

        Parameters:
        - x (int): x-coordinate.
        - y (int): y-coordinate.

        Returns:
        - int or None: Index of the closest vertex or None if not found.
        """
        # Implement logic to find the closest vertex
        pass

    def run(self):
        """
        Run the interactive modeling program.
        """
        while self.running:
            self.handle_events()

            self.screen.fill((255, 255, 255))  # Clear the screen

            self.control_mesh.draw(self.screen)  # Draw the control mesh

            pygame.display.flip()
            self.clock.tick(60)  # Set the frame rate

        pygame.quit()

if __name__ == '__main__':
    # Example usage with a set of triangles
    triangles = [
        (0, 0),
        (100, 0),
        (50, 100),
    ]

    app = InteractiveModeling(triangles)
    app.run()
