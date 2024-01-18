from PIL import Image, ImageDraw
import math

class EquilateralTriangle3D:
    def __init__(self, width, height, triangle_side_length):
        self.width = width
        self.height = height
        self.viewport_center = (width // 2, height // 2)
        self.triangle_side_length = triangle_side_length
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def _calculate_vertices_local(self):
        triangle_height = math.sqrt(3) / 2 * self.triangle_side_length
        vertex1 = (-self.triangle_side_length / 2, triangle_height / 2)
        vertex2 = (self.triangle_side_length / 2, triangle_height / 2)
        vertex3 = (0, -triangle_height / 2)
        return vertex1, vertex2, vertex3

    def _rotate_vertices(self, vertices, angle):
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
        translated_vertices = [
            (
                vertex[0] + translation[0],
                vertex[1] + translation[1]
            )
            for vertex in vertices
        ]
        return translated_vertices

    def _draw_base(self, vertices):
        base_color = (169, 169, 169)
        self.draw.polygon([vertices[0], vertices[1], self.viewport_center, vertices[0]], fill=base_color, outline="black")

    def _draw_edges(self, vertices):
        self.draw.line([vertices[0], vertices[1]], fill="black")
        self.draw.line([vertices[1], vertices[2]], fill="black")
        self.draw.line([vertices[2], vertices[0]], fill="black")

    def draw_3d_triangle_local(self, position, rotation_angle=0):
        vertices_local = self._calculate_vertices_local()
        vertices_rotated = self._rotate_vertices(vertices_local, rotation_angle)
        vertices_world = self._translate_vertices(vertices_rotated, position)
        self.draw.line([self.viewport_center, vertices_world[0]], fill="black")
        self.draw.line([self.viewport_center, vertices_world[1]], fill="black")
        self.draw.line([self.viewport_center, vertices_world[2]], fill="black")
        self._draw_base(vertices_world)
        self._draw_edges(vertices_world)

    def show_image(self):
        self.image.show()

def main():
    width, height = 800, 600
    triangle_side_length = 100
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    triangle_3d = EquilateralTriangle3D(width, height, triangle_side_length)
    triangle_3d.draw_3d_triangle_local((200, 300), 30)
    triangle_3d.draw_3d_triangle_local((400, 300), 0)
    triangle_3d.draw_3d_triangle_local((600, 300), -30)
    triangle_3d.show_image()

if __name__ == "__main__":
    main()

