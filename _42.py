"""
Using PIL for Python and docstrings and OOP:

42. Write a program that, given two polygons with the same number of vertices, will generate
a sequence of images that converts one polygon into the other.
"""

from PIL import Image, ImageDraw
import numpy as np

class PolygonMorpher:
    def __init__(self, vertices1, vertices2, num_frames):
        self.vertices1 = np.array(vertices1)
        self.vertices2 = np.array(vertices2)
        self.num_frames = num_frames
        self.frames = []

    def generate_frames(self):
        for i in range(self.num_frames):
            t = i / (self.num_frames - 1)  # Interpolation factor

            morphed_vertices = self.lerp_vertices(t)
            frame = self.draw_polygon(morphed_vertices)
            self.frames.append(frame)

    def lerp_vertices(self, t):
        morphed_vertices = (1 - t) * self.vertices1 + t * self.vertices2
        return morphed_vertices.astype(int)

    def draw_polygon(self, vertices):
        image_size = (400, 400)
        image = Image.new("RGB", image_size, "white")
        draw = ImageDraw.Draw(image)

        # Draw the polygon
        draw.polygon(vertices.flatten().tolist(), outline="black")

        return image

    def save_frames(self, output_folder="./morph_frames"):
        for i, frame in enumerate(self.frames):
            frame.save(f"{output_folder}/frame_{i:03d}.png")

if __name__ == "__main__":
    # Example polygons (replace with your own vertices)
    polygon1 = np.array([[50, 50], [150, 50], [150, 150], [50, 150]])
    polygon2 = np.array([[200, 50], [300, 50], [300, 150], [200, 150]])

    num_frames = 30
    morpher = PolygonMorpher(polygon1, polygon2, num_frames)
    morpher.generate_frames()
    morpher.save_frames()
