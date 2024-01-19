import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QOpenGLWidget, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
from OpenGL.GL import glEnable, glBlendFunc, glClear, glClearColor, glColor4f, glBegin, glEnd, glVertex2f, GL_COLOR_BUFFER_BIT, GL_POLYGON
from OpenGL.GL import GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND
import math

class OpenGLWidget(QOpenGLWidget):
    """
    Custom QOpenGLWidget for rendering dynamic dots.
    """

    def __init__(self, parent=None):
        """
        Constructor for the OpenGLWidget class.

        Parameters:
        - parent (QWidget): The parent widget.
        """
        super(OpenGLWidget, self).__init__(parent)
        self.t = 0.25
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDots)
        self.timer.start(250)  # Update every 250 milliseconds

    def initializeGL(self):
        """
        OpenGL initialization method.
        """
        pass

    def resizeGL(self, w, h):
        """
        Resize event handler for OpenGL.
        
        Parameters:
        - w (int): New width of the widget.
        - h (int): New height of the widget.
        """
        pass

    def paintGL(self):
        """
        Paint event handler for OpenGL.
        """
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Set background color
        glClearColor(0.8, 0.8, 0.8, 1.0)  # Light gray background
        
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Set dot color to black
        glColor = [0.0, 0.0, 0.0, 1.0]

        # Draw three dots at initial positions
        self.drawDot(0.0, 0.0, 0.25, glColor)
        self.drawDot(1.0, 0.0, 0.25, glColor)
        self.drawDot(2.0, 0.0, 0.25, glColor)

        # Draw three dots at positions t, t + 1, and t + 2
        self.drawDot(self.t, 0.0, 0.25, glColor)
        self.drawDot(self.t + 1.0, 0.0, 0.25, glColor)
        self.drawDot(self.t + 2.0, 0.0, 0.25, glColor)

    def drawDot(self, x, y, radius, color):
        """
        Draw a dot on the OpenGL canvas.

        Parameters:
        - x (float): X-coordinate of the center of the dot.
        - y (float): Y-coordinate of the center of the dot.
        - radius (float): Radius of the dot.
        - color (list): RGBA color values of the dot.
        """
        num_segments = 100
        glBegin(GL_POLYGON)
        glColor4f(*color)
        for i in range(num_segments):
            theta = 2.0 * math.pi * i / num_segments
            dx = radius * math.cos(theta)
            dy = radius * math.sin(theta)
            glVertex2f(x + dx, y + dy)
        glEnd()

    def updateDots(self):
        """
        Update the position of the dots.
        """
        self.t += 0.25
        if self.t > 3.0:
            self.t = 0.25
        self.update()


class MainWindow(QMainWindow):
    """
    Main window for the application.
    """

    def __init__(self):
        """
        Constructor for the MainWindow class.
        """
        super(MainWindow, self).__init__()

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)

        self.openglWidget = OpenGLWidget(self)
        self.layout.addWidget(self.openglWidget)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(300)
        self.slider.setValue(25)  # Initial value for t
        self.slider.valueChanged.connect(self.updateT)
        self.layout.addWidget(self.slider)

        # Set the size policy for the OpenGLWidget
        self.openglWidget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

    def updateT(self, value):
        """
        Update the value of 't' based on the slider position.

        Parameters:
        - value (int): Slider position.
        """
        self.openglWidget.t = value / 100.0
        self.openglWidget.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()  # Show the window maximized
    sys.exit(app.exec_())

