from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QSlider
from PyQt5.QtGui import QPainter, QPolygonF
from PyQt5.QtCore import Qt, QPointF
import sys
import webbrowser
import numpy as np

class GeometricLibrary:
    def __init__(self):
        self.current_frame = np.identity(3)

    def translate(self, dx, dy):
        translation_matrix = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ])
        self.current_frame = np.dot(translation_matrix, self.current_frame)

    def rotate(self, angle):
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 1]
        ])
        self.current_frame = np.dot(rotation_matrix, self.current_frame)

    def scale(self, sx, sy):
        scale_matrix = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ])
        self.current_frame = np.dot(scale_matrix, self.current_frame)

    def transform_point(self, point):
        homogeneous_point = np.array([point[0], point[1], 1])
        transformed_point = np.dot(self.current_frame, homogeneous_point)
        return transformed_point[:2]

class Canvas(QWidget):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.point = [100, 100]
        self.initUI()

    def initUI(self):
        self.setMinimumSize(400, 400)
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        transformed_point = self.library.transform_point(self.point)
    
        # Convert coordinates to integers for drawing
        x, y = int(transformed_point[0]), int(transformed_point[1])

        # Draw transformed point
        painter.drawEllipse(x, y, 10, 10)

        # Draw transformed line
        painter.drawLine(50, 50, x, y)

        # Draw transformed polygon
        polygon = QPolygonF([QPointF(200, 200), QPointF(300, 200), QPointF(x, y)])
        painter.drawPolygon(polygon)


class WebGLViewer(QWidget):
    def __init__(self, vertex_shader, fragment_shader):
        super().__init__()
        self.setup_ui()
        self.create_webgl_page(vertex_shader, fragment_shader)

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.webgl_button = QPushButton("Open WebGL Viewer", self)
        self.webgl_button.clicked.connect(self.open_webgl_viewer)
        layout.addWidget(self.webgl_button)
        self.webgl_url_label = QLabel("", self)
        layout.addWidget(self.webgl_url_label)
        self.setLayout(layout)

    def open_webgl_viewer(self):
        webbrowser.open("webgl_display.html")

    def create_webgl_page(self, vertex_shader, fragment_shader):
        with open('webgl_display.html', 'w') as f:
            f.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebGL Display</title>
    <script src="https://unpkg.com/gl-matrix@2.4.0/dist/gl-matrix.js"></script>
    <script type="x-shader/x-vertex" id="vertex-shader">
        {vertex_shader}
    </script>
    <script type="x-shader/x-fragment" id="fragment-shader">
        {fragment_shader}
    </script>
</head>
<body>
    <canvas id="webgl-canvas" width="500" height="500"></canvas>
    <script src="your_webgl_script.js"></script>
</body>
</html>
''')
        self.webgl_url_label.setText("WebGL Viewer URL: webgl_display.html")

def main():
    app = QApplication(sys.argv)

    library = GeometricLibrary()

    # PyQt5 Window
    main_window = QWidget()
    main_layout = QVBoxLayout(main_window)

    canvas = Canvas(library)
    main_layout.addWidget(canvas)

    control_layout = QHBoxLayout()
    control_layout.setAlignment(Qt.AlignTop)

    # Add sliders for translation, rotation, and scaling
    translation_slider = QSlider(Qt.Horizontal)
    rotation_slider = QSlider(Qt.Horizontal)
    scaling_slider = QSlider(Qt.Horizontal)

    translation_slider.valueChanged.connect(lambda value: handle_slider_change(value, 'translation', library, canvas))
    rotation_slider.valueChanged.connect(lambda value: handle_slider_change(value, 'rotation', library, canvas))
    scaling_slider.valueChanged.connect(lambda value: handle_slider_change(value, 'scaling', library, canvas))

    control_layout.addWidget(create_slider_group(translation_slider, "Translation", -100, 100))
    control_layout.addWidget(create_slider_group(rotation_slider, "Rotation", 0, 360))
    control_layout.addWidget(create_slider_group(scaling_slider, "Scaling", 1, 3))

    main_layout.addLayout(control_layout)

    # WebGL Viewer
    webgl_viewer = WebGLViewer('vertex_shader_code_here', 'fragment_shader_code_here')
    main_layout.addWidget(webgl_viewer)

    main_window.setLayout(main_layout)
    main_window.show()

    sys.exit(app.exec_())

def create_slider_group(slider, label_text, min_value, max_value):
    group_box = QWidget()
    layout = QVBoxLayout(group_box)
    label = QLabel(label_text)
    label.setAlignment(Qt.AlignCenter)
    slider.setRange(min_value, max_value)
    layout.addWidget(label)
    layout.addWidget(slider)
    return group_box

def handle_slider_change(value, transformation_type, library, canvas):
    if transformation_type == 'translation':
        library.translate(value, value)
    elif transformation_type == 'rotation':
        library.rotate(value)
    elif transformation_type == 'scaling':
        library.scale(value / 100.0, value / 100.0)

    canvas.update()

if __name__ == "__main__":
    main()

