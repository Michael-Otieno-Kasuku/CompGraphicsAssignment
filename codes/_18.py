from PIL import Image

class BresenhamLine:
    def __init__(self, start, end):
        """
        Bresenham's Line Drawing Algorithm

        Parameters:
        - start (tuple): (x, y) coordinates of the starting point
        - end (tuple): (x, y) coordinates of the ending point
        """
        self.start = start
        self.end = end
        self.points = []

    def draw_line(self):
        """
        Generate the locations of pixels along the rasterized line segment using Bresenham's algorithm.
        """
        x1, y1 = self.start
        x2, y2 = self.end

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        slope = dy > dx

        if slope:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        p = 2 * dy - dx

        inc1 = 2 * dy
        inc2 = 2 * (dy - dx)

        x, y = x1, y1

        while x <= x2:
            if slope:
                self.points.append((y, x))
            else:
                self.points.append((x, y))

            x += 1

            if p < 0:
                p += inc1
            else:
                y += 1
                p += inc2

    def create_image(self, filename='line_image.png'):
        """
        Create an image and draw the line on it.

        Parameters:
        - filename (str): Name of the output image file.
        """
        img = Image.new('RGB', (800, 600), color='white')
        pixels = img.load()

        for point in self.points:
            pixels[point[0], point[1]] = (0, 0, 0)  # Black color for line

        img.save(filename)

if __name__ == "__main__":
    # Example usage
    start_point = (10, 20)
    end_point = (100, 80)

    bresenham_line = BresenhamLine(start_point, end_point)
    bresenham_line.draw_line()
    bresenham_line.create_image('output_line.png')
