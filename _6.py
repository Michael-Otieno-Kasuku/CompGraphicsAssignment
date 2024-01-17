"""
How are curves like the B ́ezier curve and the B-spline curve useful? 2 Marks. Give an
application where a curve can be used as a reference. Using PIL for Python
Write a program to carry out subdivision of triangular or quadrilateral meshes.
When the subdivision is working correctly, add the averaging step to form a smoother surface.
Use OOP and docstrings
"""

"""
1. Bezier Curve and B-spline Curve Utility (1 mark): Both Bézier curves and B-spline curves are widely used in computer graphics and computer-aided design. They provide a flexible and intuitive way to represent and manipulate curves and surfaces, making them valuable in various applications.

2. Application Example (1 mark): One application where curves can be used as a reference is in computer-aided design (CAD). In CAD systems, Bézier curves and B-spline curves are often employed to model and represent shapes of objects. Designers can control the shape of curves by adjusting control points, allowing for precise and smooth curve manipulation. This is crucial in designing anything from automotive parts to consumer products.
"""

from PIL import Image, ImageDraw
import random

class MeshSubdivision:
    def __init__(self, width, height, num_iterations):
        """
        Initialize the MeshSubdivision object.

        Parameters:
        - width (int): Width of the image.
        - height (int): Height of the image.
        - num_iterations (int): Number of subdivision iterations.

        Returns:
        None
        """
        self.width = width
        self.height = height
        self.num_iterations = num_iterations
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def generate_random_mesh(self, num_points, num_triangles):
        """
        Generate a random triangular mesh.

        Parameters:
        - num_points (int): Number of mesh points.
        - num_triangles (int): Number of triangles in the mesh.

        Returns:
        list: List of points and triangles forming the mesh.
        """
        points = [(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(num_points)]
        triangles = [(random.sample(range(num_points), 3)) for _ in range(num_triangles)]

        return points, triangles

    def draw_mesh(self, points, triangles):
        """
        Draw the triangular mesh.

        Parameters:
        - points (list): List of points.
        - triangles (list): List of triangles represented by point indices.

        Returns:
        None
        """
        for triangle in triangles:
            vertices = [points[i] for i in triangle]
            self.draw.polygon(vertices, outline="black")

    def subdivide_mesh(self, points, triangles):
        """
        Subdivide the triangular mesh.

        Parameters:
        - points (list): List of points.
        - triangles (list): List of triangles represented by point indices.

        Returns:
        list: List of points and triangles after subdivision.
        """
        new_points = points.copy()
        new_triangles = []

        for triangle in triangles:
            midpoints = [((points[i][0] + points[j][0]) // 2, (points[i][1] + points[j][1]) // 2)
                         for i, j in zip(triangle, triangle[1:] + [triangle[0]])]

            new_indices = list(range(len(new_points), len(new_points) + len(midpoints)))
            new_points.extend(midpoints)

            new_triangles.extend([
                (triangle[0], new_indices[0], new_indices[2]),
                (new_indices[0], triangle[1], new_indices[1]),
                (new_indices[2], new_indices[1], triangle[2]),
                (new_indices[0], new_indices[1], new_indices[2])
            ])

        return new_points, new_triangles

    def average_mesh(self, points, triangles):
        """
        Average the mesh to form a smoother surface.

        Parameters:
        - points (list): List of points.
        - triangles (list): List of triangles represented by point indices.

        Returns:
        list: List of points and triangles after averaging.
        """
        averaged_points = []

        for i in range(len(points)):
            connected_triangles = [triangle for triangle in triangles if i in triangle]
            connected_points = set(point for triangle in connected_triangles for point in triangle)
            connected_points.remove(i)  # Exclude the current point

            x_avg = sum(points[j][0] for j in connected_points) / len(connected_points)
            y_avg = sum(points[j][1] for j in connected_points) / len(connected_points)

            averaged_points.append((round(x_avg), round(y_avg)))

        return averaged_points, triangles

    def save_image(self, filename):
        """
        Save the image.

        Parameters:
        - filename (str): Filename to save the image.

        Returns:
        None
        """
        self.image.save(filename)

if __name__ == "__main__":
    width, height = 600, 600
    num_iterations = 4

    mesh_subdivision = MeshSubdivision(width, height, num_iterations)

    # Generate a random triangular mesh
    num_points = 10
    num_triangles = 15
    points, triangles = mesh_subdivision.generate_random_mesh(num_points, num_triangles)

    # Subdivide the mesh
    for _ in range(num_iterations):
        points, triangles = mesh_subdivision.subdivide_mesh(points, triangles)

    # Draw the subdivided mesh
    mesh_subdivision.draw_mesh(points, triangles)

    # Average the mesh for a smoother surface
    points, triangles = mesh_subdivision.average_mesh(points, triangles)

    # Draw the averaged mesh
    mesh_subdivision.draw_mesh(points, triangles)

    # Save the result
    mesh_subdivision.save_image("subdivided_mesh_oop.png")

"""
def subdivide_mesh(self, points, triangles):
    """
    Subdivide the triangular mesh.

    Parameters:
    - points (list): List of points.
    - triangles (list): List of triangles represented by point indices.

    Returns:
    list: List of points and triangles after subdivision.
    """
    new_points = points.copy()
    new_triangles = []

    for triangle in triangles:
        midpoints = [((points[i][0] + points[j][0]) // 2, (points[i][1] + points[j][1]) // 2)
                     for i, j in zip(triangle, triangle[1:] + [triangle[0]])]

        # Convert midpoints to lists
        midpoints = [list(point) for point in midpoints]

        new_indices = list(range(len(new_points), len(new_points) + len(midpoints)))
        new_points.extend(midpoints)

        new_triangles.extend([
            (triangle[0], new_indices[0], new_indices[2]),
            (new_indices[0], triangle[1], new_indices[1]),
            (new_indices[2], new_indices[1], triangle[2]),
            (new_indices[0], new_indices[1], new_indices[2])
        ])

    return new_points, new_triangles

"""