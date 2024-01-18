from PIL import Image, ImageDraw

class ObjectWithShapes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_square(self, size, position):
        self.draw.rectangle([position, (position[0] + size, position[1] + size)], outline="black")

    def draw_circle(self, radius, position):
        self.draw.ellipse([position[0] - radius, position[1] - radius, position[0] + radius, position[1] + radius], outline="black")

    def draw_object(self):
        circle_radius = 10
        circle_center = (self.width // 2, self.height // 2)
        self.draw_circle(circle_radius, circle_center)
        square_size = 20
        square_top_left = (circle_center[0] - circle_radius * 2 - square_size, circle_center[1] - square_size // 2)
        self.draw_square(square_size, square_top_left)
        square_top_right = (circle_center[0] + circle_radius * 2, circle_center[1] - square_size // 2)
        self.draw_square(square_size, square_top_right)

    def show_image(self):
        self.image.show()

def main():
    width, height = 300, 200
    object_with_shapes = ObjectWithShapes(width, height)
    object_with_shapes.draw_object()
    object_with_shapes.show_image()

if __name__ == "__main__":
    main()

