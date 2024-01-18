from PIL import Image, ImageDraw

class MaxwellTriangle:
    def __init__(self, size):
        self.size = size
        self.image = Image.new("RGB", (size, size), "white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_triangle(self):
        cube_vertices = [
            (0, 0, 0),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (255, 255, 255)
        ]
        triangle_vertices = [
            (255, 0, 0),  
            (0, 255, 0),  
            (0, 0, 255)   
        ]
        for i in range(4):
            self.draw.line([self.rgb_to_xy(cube_vertices[i]), self.rgb_to_xy(cube_vertices[(i+1)%4])], fill="black")
        for i in range(4, 8):
            self.draw.line([self.rgb_to_xy(cube_vertices[i]), self.rgb_to_xy(cube_vertices[i-4])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[0]), self.rgb_to_xy(cube_vertices[4])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[1]), self.rgb_to_xy(cube_vertices[5])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[2]), self.rgb_to_xy(cube_vertices[6])], fill="black")
        self.draw.line([self.rgb_to_xy(cube_vertices[3]), self.rgb_to_xy(cube_vertices[7])], fill="black")
        self.draw.polygon([self.rgb_to_xy(v) for v in triangle_vertices], outline="black")

    def rgb_to_xy(self, rgb):
        x = int(rgb[0] / 255 * (self.size - 1))
        y = self.size - 1 - int(rgb[1] / 255 * (self.size - 1))
        return x, y

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename)

if __name__ == "__main__":
    image_size = 500
    maxwell_triangle = MaxwellTriangle(image_size)
    maxwell_triangle.draw_triangle()
    maxwell_triangle.show()
    maxwell_triangle.save("maxwell_triangle_oop.png")

