"""
Using PIL for Python and docstrings and OOP:

43. If we use the basic formula that we used for the Mandelbrot set, but this time fix the
value of the complex number c and find the set of initial points for which we obtain
convergence, we have the Julia set for that c. Write a program to display Julia sets. Hint:
Use values of c near the edges of the Mandelbrot set.
"""
from PIL import Image

class JuliaSet:
    def __init__(self, width, height, c, max_iterations=1000):
        self.width = width
        self.height = height
        self.c = c
        self.max_iterations = max_iterations
        self.image = Image.new("RGB", (width, height), "black")

    def generate_julia_set(self):
        for x in range(self.width):
            for y in range(self.height):
                zx = 1.5 * (x - self.width / 2) / (0.5 * self.width)
                zy = (y - self.height / 2) / (0.5 * self.height)

                iterations = self.calculate_iterations(zx, zy)
                color = self.calculate_color(iterations)
                self.image.putpixel((x, y), color)

    def calculate_iterations(self, zx, zy):
        for i in range(self.max_iterations):
            if zx * zx + zy * zy > 4:
                return i
            zx, zy = zx * zx - zy * zy + self.c.real, 2 * zx * zy + self.c.imag
        return self.max_iterations

    def calculate_color(self, iterations):
        color_value = int(iterations / self.max_iterations * 255)
        return (color_value, color_value, color_value)

    def save_image(self, filename="julia_set.png"):
        self.image.save(filename)

if __name__ == "__main__":
    # Example: Generate a Julia set with c = -0.7 + 0.27015j
    julia_set = JuliaSet(800, 600, -0.7 + 0.27015j)
    julia_set.generate_julia_set()
    julia_set.save_image()
