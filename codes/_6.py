from PIL import Image, ImageDraw
import random

class MeshSubdivision:
    def __init__(self, width, height, num_iterations):
        self.width = width
        self.height = height
        self.num_iterations = num_iterations
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def generate_random_mesh(self, num_points, num_triangles):
        points = [(random.randint(0, self.width), random.randint(0, self.height)) for _ in range(num_points)]
        triangles = [(random.sample(range(num_points), 3)) for _ in range(num_triangles)]

        return points, triangles

    def draw_mesh(self, points, triangles):
        for triangle in triangles:
            vertices = [points[i] for i in triangle]
            self.draw.polygon(vertices, outline="black")

    def subdivide_mesh(self, points, triangles):
        new_points = points.copy()
        new_triangles = []
        for triangle in triangles:
            midpoints = [((points[i][0] + points[j][0]) // 2, (points[i][1] + points[j][1]) // 2)
            for i, j in zip(triangle, tuple(triangle[1:]) + (triangle[0],))]
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
        averaged_points = []
        for i in range(len(points)):
            connected_triangles = [triangle for triangle in triangles if i in triangle]
            connected_points = set(point for triangle in connected_triangles for point in triangle)
            connected_points.remove(i)
            x_avg = sum(points[j][0] for j in connected_points) / len(connected_points)
            y_avg = sum(points[j][1] for j in connected_points) / len(connected_points)
            averaged_points.append((round(x_avg), round(y_avg)))
        return averaged_points, triangles

    def save_image(self, filename):
        self.image.save(filename)

if __name__ == "__main__":
    width, height = 600, 600
    num_iterations = 4
    mesh_subdivision = MeshSubdivision(width, height, num_iterations)
    num_points = 10
    num_triangles = 15
    points, triangles = mesh_subdivision.generate_random_mesh(num_points, num_triangles)
    for _ in range(num_iterations):
        points, triangles = mesh_subdivision.subdivide_mesh(points, triangles)
    mesh_subdivision.draw_mesh(points, triangles)
    points, triangles = mesh_subdivision.average_mesh(points, triangles)
    mesh_subdivision.draw_mesh(points, triangles)
    mesh_subdivision.save_image("subdivided_mesh_oop.png")

