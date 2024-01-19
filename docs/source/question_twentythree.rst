Question Twenty Three
=====================
Write a program that draws three black dots of radius 0.25 at x = 0, 1, 2 along the x-axis.
Then display instead three black dots at positions t, t + 1, and t + 2 (using t = 0. 25
initially). Make the display toggle back and forth between the two sets of dots, once every quarter-second. Do you tend to see the dots as moving? What if you increase t to 0.
5? Include a slider that lets you adjust t from 0 to 3. Does the illusion of the dots moving
ever weaken? When t = 1, you could interpret the motion as “the outer dot jumps back
and forth from the far left (x = 0) to the far right (x = 3) while the middle two dots remain
fixed.” Can you persuade yourself that this is what you’re seeing? The strong impression
that the dots are moving as a group is remarkably hard to abandon, supporting the Gestalt
theory.

OpenGLWidget Class
------------------

.. py:class:: OpenGLWidget

    It is a custom
    :class:`~PyQt5.QtWidgets.QOpenGLWidget` for rendering dynamic dots.

    :ivar t: Current time for dot animation.
    :ivar timer: :class:`~PyQt5.QtCore.QTimer` for periodic updates.
    
    .. method:: __init__(parent=None)
    
        Constructor for the :class:`OpenGLWidget` class.

        :param parent: The parent widget.

    .. method:: initializeGL()

        OpenGL initialization method.

    .. method:: resizeGL(w, h)

        Resize event handler for OpenGL.

        :param w: New width of the widget.
        :param h: New height of the widget.

    .. method:: paintGL()

        Paint event handler for OpenGL.

    .. method:: drawDot(x, y, radius, color)

        Draw a dot on the OpenGL canvas.

        :param x: X-coordinate of the center of the dot.
        :param y: Y-coordinate of the center of the dot.
        :param radius: Radius of the dot.
        :param color: RGBA color values of the dot.

    .. method:: updateDots()

        Update the position of the dots.

MainWindow Class
----------------

.. py:class:: MainWindow

    It is the main window for the application.

    :ivar centralWidget: The central widget of the main window.
    :ivar layout: QVBoxLayout for arranging widgets.
    :ivar openglWidget: Instance of :class:`OpenGLWidget` for rendering dots.
    :ivar slider: QSlider for controlling dot animation.

    .. method:: __init__()

        Constructor for the :class:`MainWindow` class.

    .. method:: updateT(value)

        Update the value of 't' based on the slider position.

        :param value: Slider position.

    .. method:: showMaximized()

        Show the window maximized.

    .. method:: main()

        Main function to demonstrate the :class:`MainWindow` class.

    Inherits from: :class:`~PyQt5.QtWidgets.QMainWindow`

