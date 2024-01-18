from PIL import Image, ImageDraw

class PNGWriter:
    def __init__(self, width, height):
        self.image = Image.new("RGB", (width, height), color="white")
        self.draw = ImageDraw.Draw(self.image)

    def save(self, filename):
        self.image.save(filename)

    def draw_primary_diagonal(self, color):
        for i in range(min(self.image.width, self.image.height)):
            self.draw.point((i, i), fill=color)

    def draw_secondary_diagonal(self, color):
        for i in range(min(self.image.width, self.image.height)):
            self.draw.point((i, self.image.height - 1 - i), fill=color)

    def fill_quadrant(self, color, quadrant):
        width, height = self.image.size
        x_range = range(width // 2) if quadrant % 2 == 0 else range(width // 2, width)
        y_range = range(height // 2) if quadrant < 2 else range(height // 2, height)
        for x in x_range:
            for y in y_range:
                self.draw.point((x, y), fill=color)

png_writer = PNGWriter(300, 300)
png_writer.draw_primary_diagonal("red")
png_writer.draw_secondary_diagonal("green")
png_writer.fill_quadrant("blue", 3)
png_writer.save("image.png")
