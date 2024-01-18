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

    def _calculate_vertices(self):
        triangle_height = math.sqrt(3) / 2 * self.triangle_side_length
        vertex1 = (self.viewport_center[0] - self.triangle_side_length / 2, self.viewport_center[1] + triangle_height / 2)
        vertex2 = (self.viewport_center[0] + self.triangle_side_length / 2, self.viewport_center[1] + triangle_height / 2)
        vertex3 = (self.viewport_center[0], self.viewport_center[1] - triangle_height / 2)
        return vertex1, vertex2, vertex3

    def _draw_base(self, vertices):
        base_color = (169, 169, 169)
        self.draw.polygon([vertices[0], vertices[1], self.viewport_center, vertices[0]], fill=base_color, outline="black")

    def _draw_edges(self, vertices):
        self.draw.line([vertices[0], vertices[1]], fill="black")
        self.draw.line([vertices[1], vertices[2]], fill="black")
        self.draw.line([vertices[2], vertices[0]], fill="black")

    def draw_3d_triangle(self):
        vertices = self._calculate_vertices()
        self.draw.line([self.viewport_center, vertices[0]], fill="black")
        self.draw.line([self.viewport_center, vertices[1]], fill="black")
        self.draw.line([self.viewport_center, vertices[2]], fill="black")
        self._draw_base(vertices)
        self._draw_edges(vertices)

    def show_image(self):
        self.image.show()

def main():
    width, height = 800, 600
    triangle_side_length = 100
    triangle_3d = EquilateralTriangle3D(width, height, triangle_side_length)
    triangle_3d.draw_3d_triangle()
    triangle_3d.show_image()

if __name__ == "__main__":
    main()
