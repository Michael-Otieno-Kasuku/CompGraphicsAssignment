"""
Using PIL for Python and docstrings and OOP:

19. Another CAD application that can be developed in PyQT5 is a paint program. You can
display the various objects that can be painted—lines, rectangles, circles, and triangles,
for example—and use picking to select which to draw. The mouse can then enter vertex
data and select attributes such as colors from a menu. Write such an application.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QPainter, QPen


class PaintItem(QGraphicsItem):
    def __init__(self, shape, start, end, pen):
        """
        Custom QGraphicsItem for drawing different shapes.

        Parameters:
        - shape (str): Shape to be drawn ('Line', 'Rect', 'Ellipse', 'Triangle').
        - start (QPoint): Starting point of the shape.
        - end (QPoint): Ending point of the shape.
        - pen (QPen): Pen settings for drawing.
        """
        super(PaintItem, self).__init__()
        self.shape = shape
        self.start = start
        self.end = end
        self.pen = pen

    def paint(self, painter, option, widget):
        """
        Paint the shape on the QGraphicsItem.

        Parameters:
        - painter (QPainter): Painter object for drawing.
        - option: Graphics options.
        - widget: Associated widget.
        """
        painter.setPen(self.pen)
        if self.shape == 'Line':
            painter.drawLine(self.start, self.end)
        elif self.shape == 'Rect':
            painter.drawRect(self.start.x(), self.start.y(), self.end.x() - self.start.x(), self.end.y() - self.start.y())
        elif self.shape == 'Ellipse':
            painter.drawEllipse(self.start.x(), self.start.y(), self.end.x() - self.start.x(), self.end.y() - self.start.y())
        elif self.shape == 'Triangle':
            points = [self.start, self.end, QPoint(self.start.x(), self.end.y())]
            painter.drawPolygon(points)

    def boundingRect(self):
        """
        Get the bounding rectangle of the shape.

        Returns:
        - QRectF: Bounding rectangle.
        """
        return QRectF(self.start, self.end)


class PaintApp(QMainWindow):
    def __init__(self):
        """
        Simple Paint Application using PyQt5.
        """
        super(PaintApp, self).__init__()

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.pen = QPen(Qt.black)
        self.shape = 'Line'
        self.start_point = None

        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        line_action = file_menu.addAction('Line')
        line_action.triggered.connect(lambda: self.set_shape('Line'))

        rect_action = file_menu.addAction('Rectangle')
        rect_action.triggered.connect(lambda: self.set_shape('Rect'))

        ellipse_action = file_menu.addAction('Ellipse')
        ellipse_action.triggered.connect(lambda: self.set_shape('Ellipse'))

        triangle_action = file_menu.addAction('Triangle')
        triangle_action.triggered.connect(lambda: self.set_shape('Triangle'))

        clear_action = file_menu.addAction('Clear')
        clear_action.triggered.connect(self.clear_scene)

        self.view.mousePressEvent = self.mouse_press_event
        self.view.mouseMoveEvent = self.mouse_move_event

    def set_shape(self, shape):
        """
        Set the current drawing shape.

        Parameters:
        - shape (str): Shape to be set.
        """
        self.shape = shape

    def clear_scene(self):
        """
        Clear the graphics scene.
        """
        self.scene.clear()

    def mouse_press_event(self, event):
        """
        Handle mouse press event to set the starting point.

        Parameters:
        - event: Mouse press event.
        """
        self.start_point = event.pos()

    def mouse_move_event(self, event):
        """
        Handle mouse move event to draw shapes.

        Parameters:
        - event: Mouse move event.
        """
        if self.start_point:
            end_point = event.pos()
            item = PaintItem(self.shape, self.start_point, end_point, self.pen)
            self.scene.addItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaintApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
