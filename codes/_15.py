import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QVBoxLayout, QWidget, QPushButton, QMenu, QGraphicsSceneContextMenuEvent
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor, QPainterPath, QFont
from PyQt5.QtCore import Qt, QRectF

class Gate(QGraphicsItem):
    def __init__(self, gate_type, x, y):
        super(Gate, self).__init__()
        self.gate_type = gate_type
        self.width = 60
        self.height = 60
        self.inputs = []
        self.outputs = []
        self.setPos(x, y)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.darkGray))
        painter.drawRoundedRect(self.boundingRect(), 10, 10)

        font = QFont()
        font.setPointSize(8)
        painter.setFont(font)

        text = painter.drawText(self.boundingRect(), Qt.AlignCenter, self.gate_type)
        self.bounding_rect = text.boundingRect()

    def contextMenuEvent(self, event):
        menu = QMenu()
        add_input_action = menu.addAction("Add Input")
        add_output_action = menu.addAction("Add Output")

        action = menu.exec_(event.scenePos().toPoint())

        if action == add_input_action:
            self.add_input(event.scenePos().x(), event.scenePos().y())
        elif action == add_output_action:
            self.add_output(event.scenePos().x(), event.scenePos().y())

    def hoverEnterEvent(self, event):
        self.setOpacity(0.7)

    def hoverLeaveEvent(self, event):
        self.setOpacity(1.0)

    def add_input(self, x, y):
        input_gate = GateInput(self, x, y)
        self.inputs.append(input_gate.scenePos())
        self.scene().addItem(input_gate)
        self.update_connections()

    def add_output(self, x, y):
        output_gate = GateOutput(self, x, y)
        self.outputs.append(output_gate.scenePos())
        self.scene().addItem(output_gate)
        self.update_connections()

    def update_connections(self):
        self.scene().update()

class GateInput(Gate):
    def __init__(self, parent_gate, x, y):
        super(GateInput, self).__init__("Input", x, y)
        self.setParentItem(parent_gate)

class GateOutput(Gate):
    def __init__(self, parent_gate, x, y):
        super(GateOutput, self).__init__("Output", x, y)
        self.setParentItem(parent_gate)

class Connection(QGraphicsLineItem):
    def __init__(self, start, end):
        super(Connection, self).__init__()
        self.start = start
        self.end = end
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def update_path(self):
        self.setLine(self.start.x(), self.start.y(), self.end.x(), self.end.y())

class CircuitScene(QGraphicsScene):
    def __init__(self):
        super(CircuitScene, self).__init__()
        self.connections = []

    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent):
        menu = QMenu()
        add_and_gate_action = menu.addAction("Add AND Gate")
        add_or_gate_action = menu.addAction("Add OR Gate")
        add_not_gate_action = menu.addAction("Add NOT Gate")

        action = menu.exec_(event.scenePos().toPoint())

        if action == add_and_gate_action:
            self.add_gate("AND", event.scenePos().x(), event.scenePos().y())
        elif action == add_or_gate_action:
            self.add_gate("OR", event.scenePos().x(), event.scenePos().y())
        elif action == add_not_gate_action:
            self.add_gate("NOT", event.scenePos().x(), event.scenePos().y())

    def add_gate(self, gate_type, x, y):
        gate = Gate(gate_type, x, y)
        self.addItem(gate)

    def mousePressEvent(self, event):
        selected_items = self.selectedItems()

        if len(selected_items) == 2 and isinstance(selected_items[0], GateOutput) and isinstance(selected_items[1], GateInput):
            connection = Connection(selected_items[0].scenePos(), selected_items[1].scenePos())
            self.addItem(connection)
            self.connections.append(connection)

        super(CircuitScene, self).mousePressEvent(event)

class CircuitDesigner(QWidget):
    def __init__(self):
        super(CircuitDesigner, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Advanced Logical Circuit Designer')

        self.view = QGraphicsView(self)
        self.view.setScene(CircuitScene())

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    designer = CircuitDesigner()
    designer.show()
    sys.exit(app.exec_())

