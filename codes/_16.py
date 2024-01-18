from PIL import Image, ImageDraw

class SierpinskiGasket:
    def __init__(self, size, depth):
        self.size = size
        self.depth = depth
        self.image = Image.new("RGB", (size, size), "white")
        self.draw = ImageDraw.Draw(self.image)

    def draw_triangle(self, p1, p2, p3, depth):
        if depth == 0:
            self.draw.polygon([p1, p2, p3], fill="black")
        else:
            mid1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            mid2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
            mid3 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
            self.draw_triangle(p1, mid1, mid3, depth - 1)
            self.draw_triangle(mid1, p2, mid2, depth - 1)
            self.draw_triangle(mid3, mid2, p3, depth - 1)

    def generate(self):
        p1 = (self.size // 2, 0)
        p2 = (0, self.size)
        p3 = (self.size, self.size)
        self.draw_triangle(p1, p2, p3, self.depth)

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename)

if __name__ == "__main__":
    image_size = 500
    recursion_depth = 5
    sierpinski_gasket = SierpinskiGasket(image_size, recursion_depth)
    sierpinski_gasket.generate()
    sierpinski_gasket.show()
    sierpinski_gasket.save("sierpinski_gasket_oop.png")

