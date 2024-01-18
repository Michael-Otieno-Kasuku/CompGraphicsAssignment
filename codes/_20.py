"""
Using PIL for Python and docstrings and OOP:

20. Write a library of functions that will allow you to do geometric programming. Your
library should contain functions for manipulating the basic geometric types (points, lines,
vectors) and operations on those types, including dot and cross products. It should allow
you to change frames. You can also create functions to interface with PyQT5 so that you
can display the results of geometric calculations.
"""

from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QApplication
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtGui import QPainter, QPen
import sys


class Point:
    def __init__(self, x, y):
        """
        Represents a point in 2D space.

        Parameters:
        - x (float): x-coordinate.
        - y (float): y-coordinate.
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, x, y):
        """
        Represents a 2D vector.

        Parameters:
        - x (float): x-component.
        - y (float): y-component.
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


class Line:
    def __init__(self, point1, point2):
        """
        Represents a line segment connecting two points.

        Parameters:
        - point1 (Point): Starting point.
        - point2 (Point): Ending point.
        """
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f"Line({self.point1}, {self.point2})"


class GeometricOperations:
    @staticmethod
    def dot_product(vector1, vector2):
        """
        Calculate the dot product of two vectors.

        Parameters:
        - vector1 (Vector): First vector.
        - vector2 (Vector): Second vector.

        Returns:
        - float: Dot product.
        """
        return vector1.x * vector2.x + vector1.y * vector2.y

    @staticmethod
    def cross_product(vector1, vector2):
        """
        Calculate the cross product of two vectors.

        Parameters:
        - vector1 (Vector): First vector.
        - vector2 (Vector): Second vector.

        Returns:
        - float: Cross product.
        """
        return vector1.x * vector2.y - vector1.y * vector2.x


class GeometricDisplay:
    @staticmethod
    def display_point(scene, point, color=Qt.black):
        """
        Display a point on the PyQt5 graphics scene.

        Parameters:
        - scene (QGraphicsScene): Graphics scene.
        - point (Point): Point to be displayed.
        - color (Qt.Color): Color of the point.
        """
        graphics_point = QPointF(point.x, point.y)
        scene.addEllipse(graphics_point, 2, 2, QPen(color), Qt.NoBrush)

    @staticmethod
    def display_line(scene, line, color=Qt.black):
        """
        Display a line on the PyQt5 graphics scene.

        Parameters:
        - scene (QGraphicsScene): Graphics scene.
        - line (Line): Line to be displayed.
        - color (Qt.Color): Color of the line.
        """
        graphics_line = QGraphicsItem()
        graphics_line.setLine(line.point1.x, line.point1.y, line.point2.x, line.point2.y)
        scene.addItem(graphics_line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene()

    # Example usage
    point_a = Point(0, 0)
    point_b = Point(5, 5)
    vector_ab = Vector(point_b.x - point_a.x, point_b.y - point_a.y)

    GeometricDisplay.display_point(scene, point_a, Qt.red)
    GeometricDisplay.display_point(scene, point_b, Qt.blue)
    GeometricDisplay.display_line(scene, Line(point_a, point_b), Qt.black)

    dot_product_result = GeometricOperations.dot_product(vector_ab, Vector(1, 1))
    cross_product_result = GeometricOperations.cross_product(vector_ab, Vector(1, -1))

    print(f"Dot Product: {dot_product_result}")
    print(f"Cross Product: {cross_product_result}")

    view = QGraphicsView(scene)
    view.show()
    sys.exit(app.exec_())
