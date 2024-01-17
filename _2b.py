"""
b) Transpose three (3) object instances of the 3-dimensional triangle (defined in part
(a) above) to global space, along the same z-plane, so that the left object is tilted
30 degrees left of the y-axis, the center object is aligned vertically with the y-axis
and the right object is tilted 30 degrees right of the y-axis.
Hint: You may use a separate function to define the object in local space and call
that function in your display/render function to position the objects in world
space.
"""

from PIL import Image, ImageDraw
import math

class EquilateralTriangle3D:
    def __init__(self, width, height, triangle_side_length):
        """
        Initialize an EquilateralTriangle3D object.

        Parameters:
        - width (int): Width of the image.
        - height (int): Height of the image.
        - triangle_side_length (int): Side length of the equilateral triangle.
        """
        self.width = width
        self.height = height
        self.viewport_center = (width // 2, height // 2)
        self.triangle_side_length = triangle_side_length
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def _calculate_vertices_local(self):
        """
        Calculate the local coordinates of the vertices of the equilateral triangle.

        Returns:
        tuple: Tuple containing three vertices as (x, y) coordinates.
        """
        triangle_height = math.sqrt(3) / 2 * self.triangle_side_length
        vertex1 = (-self.triangle_side_length / 2, triangle_height / 2)
        vertex2 = (self.triangle_side_length / 2, triangle_height / 2)
        vertex3 = (0, -triangle_height / 2)
        return vertex1, vertex2, vertex3

    def _rotate_vertices(self, vertices, angle):
        """
        Rotate vertices around their centroid by a specified angle.

        Parameters:
        - vertices (list of tuple): List of vertices as (x, y) coordinates.
        - angle (float): Rotation angle in degrees.

        Returns:
        list of tuple: List of rotated vertices as (x, y) coordinates.
        """
        center = (
            sum(v[0] for v in vertices) / 3,
            sum(v[1] for v in vertices) / 3
        )

        angle_rad = math.radians(angle)
        rotated_vertices = [
            (
                center[0] + (vertex[0] - center[0]) * math.cos(angle_rad) - (vertex[1] - center[1]) * math.sin(angle_rad),
                center[1] + (vertex[0] - center[0]) * math.sin(angle_rad) + (vertex[1] - center[1]) * math.cos(angle_rad),
            )
            for vertex in vertices
        ]
        return rotated_vertices

    def _translate_vertices(self, vertices, translation):
        """
        Translate vertices by a specified translation vector.

        Parameters:
        - vertices (list of tuple): List of vertices as (x, y) coordinates.
        - translation (tuple): Translation vector as (dx, dy).

        Returns:
        list of tuple: List of translated vertices as (x, y) coordinates.
        """
        translated_vertices = [
            (
                vertex[0] + translation[0],
                vertex[1] + translation[1]
            )
            for vertex in vertices
        ]
        return translated_vertices

    def _draw_base(self, vertices):
        """
        Draw the base of the equilateral triangle.

        Parameters:
        - vertices (list of tuple): List of vertices as (x, y) coordinates.
        """
        base_color = (169, 169, 169)
        self.draw.polygon([vertices[0], vertices[1], self.viewport_center, vertices[0]], fill=base_color, outline="black")

    def _draw_edges(self, vertices):
        """
        Draw the edges of the equilateral triangle.

        Parameters:
        - vertices (list of tuple): List of vertices as (x, y) coordinates.
        """
        self.draw.line([vertices[0], vertices[1]], fill="black")
        self.draw.line([vertices[1], vertices[2]], fill="black")
        self.draw.line([vertices[2], vertices[0]], fill="black")

    def draw_3d_triangle_local(self, position, rotation_angle=0):
        """
        Draw a 3D equilateral triangle in local space.

        Parameters:
        - position (tuple): Position of the triangle as (x, y) coordinates.
        - rotation_angle (float): Rotation angle in degrees (default is 0).
        """
        vertices_local = self._calculate_vertices_local()
        vertices_rotated = self._rotate_vertices(vertices_local, rotation_angle)
        vertices_world = self._translate_vertices(vertices_rotated, position)

        self.draw.line([self.viewport_center, vertices_world[0]], fill="black")
        self.draw.line([self.viewport_center, vertices_world[1]], fill="black")
        self.draw.line([self.viewport_center, vertices_world[2]], fill="black")

        self._draw_base(vertices_world)
        self._draw_edges(vertices_world)

    def show_image(self):
        """
        Display the image with the drawn triangles.
        """
        self.image.show()

def main():
    """
    Main function to demonstrate the usage of EquilateralTriangle3D class.
    """
    width, height = 800, 600
    triangle_side_length = 100

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    triangle_3d = EquilateralTriangle3D(width, height, triangle_side_length)

    # Draw three 3D triangles in global space
    triangle_3d.draw_3d_triangle_local((200, 300), 30)  # Left object tilted 30 degrees left
    triangle_3d.draw_3d_triangle_local((400, 300), 0)   # Center object aligned vertically
    triangle_3d.draw_3d_triangle_local((600, 300), -30) # Right object tilted 30 degrees right

    triangle_3d.show_image()

if __name__ == "__main__":
    main()
