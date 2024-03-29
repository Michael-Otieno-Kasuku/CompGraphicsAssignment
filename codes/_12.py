import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw

class PlottingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Interactive Plotting App')
        self.setGeometry(100, 100, 800, 600)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.mode_combobox = QComboBox(self)
        self.mode_combobox.addItems(['Line Strip', 'Polyline', 'Bar Chart', 'Pie Chart'])
        self.mode_combobox.currentIndexChanged.connect(self.update_plot)
        self.color_combobox = QComboBox(self)
        self.color_combobox.addItems(['Red', 'Green', 'Blue', 'Black'])
        self.color_combobox.currentIndexChanged.connect(self.update_plot)
        self.line_style_combobox = QComboBox(self)
        self.line_style_combobox.addItems(['Solid', 'Dashed', 'Dotted'])
        self.line_style_combobox.currentIndexChanged.connect(self.update_plot)
        self.generate_button = QPushButton('Generate Plot', self)
        self.generate_button.clicked.connect(self.generate_plot)
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label, 1)
        layout.addWidget(self.mode_combobox)
        layout.addWidget(self.color_combobox)
        layout.addWidget(self.line_style_combobox)
        layout.addWidget(self.generate_button)
        self.setStyleSheet("background-color: lightGray;")

    def update_plot(self):
        self.generate_plot()

    def generate_plot(self):
        width, height = 600, 400
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        mode = self.mode_combobox.currentText()
        color = self.color_combobox.currentText().lower()
        line_style = self.line_style_combobox.currentText()
        if mode == 'Line Strip':
            draw.line([(50, 50), (550, 350)], fill=color, width=2)
        elif mode == 'Polyline':
            draw.line([(50, 50), (250, 350), (550, 50)], fill=color, width=2)
        elif mode == 'Bar Chart':
            draw.rectangle([(50, 50), (150, 350)], fill=color, outline='black', width=2)
            draw.rectangle([(250, 50), (350, 250)], fill=color, outline='black', width=2)
            draw.rectangle([(450, 50), (550, 200)], fill=color, outline='black', width=2)
        elif mode == 'Pie Chart':
            draw.pieslice([(50, 50), (550, 350)], start=0, end=90, fill=color, outline='black', width=2)
        img.save('plot.png')
        pixmap = QPixmap('plot.png')
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotting_app = PlottingApp()
    plotting_app.show()
    sys.exit(app.exec_())

