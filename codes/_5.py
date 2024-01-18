from PIL import Image, ImageDraw

class QuadraticBezierDrawer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def interpolate(self, point1, point2, t):
        return tuple((1 - t) * p1 + t * p2 for p1, p2 in zip(point1, point2))

    def draw_line(self, point1, point2):
        self.draw.line([point1, point2], fill="black", width=1)

    def draw_quadratic_bezier(self, P1, P2, P3, t, tolerance):
        def draw_curve_recursively(P1, P2, P3, t):
            P12 = self.interpolate(P1, P2, t)
            P23 = self.interpolate(P2, P3, t)
            P = self.interpolate(P12, P23, t)
            if self.distance(P, self.line_segment(P1, P3)) < tolerance:
                self.draw_line(P1, P3)
                return
            else:
                draw_curve_recursively(P1, P12, P, t)
                draw_curve_recursively(P, P23, P3, t)
        draw_curve_recursively(P1, P2, P3, t)

    def line_segment(self, point1, point2):
        return [point1, point2]

    def distance(self, point, line_segment):
        x1, y1 = line_segment[0]
        x2, y2 = line_segment[1]
        return abs((y2 - y1) * point[0] - (x2 - x1) * point[1] + x2 * y1 - y2 * x1) / ((y2 - y1)**2 + (x2 - x1)**2)**0.5

    def save_image(self, filename):
        self.image.save(filename)

if __name__ == "__main__":
    bezier_drawer = QuadraticBezierDrawer(width=300, height=300)
    P1 = (50, 250)
    P2 = (150, 50)
    P3 = (250, 250)
    t = 0
    tolerance = 2
    bezier_drawer.draw_quadratic_bezier(P1, P2, P3, t, tolerance)
    bezier_drawer.save_image("quadratic_bezier_oop.png")

