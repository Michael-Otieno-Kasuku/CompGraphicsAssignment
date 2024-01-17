"""
Circuit-layout programs are variants of paint programs. Consider the design of logical
circuits using the Boolean and, or, and not functions. Each of these functions is provided
by one of the three types of integrated circuits (gates),the symbols for which are shown in
Figure below.Using PIL for Python , PyQT5 and docstrings Write a program that allows the user to design a logical circuit by selecting
gates from a menu and positioning them on the screen. Consider methods for connecting
the outputs of one gate to the inputs of others.
"""

import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsLineItem, QGraphicsRectItem, QGraphicsTextItem, QMenu, QGraphicsSceneContextMenuEvent, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QPainter, QPixmap, QTransform
from PyQt5.QtCore import Qt

class Gate(QGraphicsRectItem):
    """
    Represents a logical gate in the circuit.

    Attributes:
    - gate_type (str): The type of the gate (AND, OR, NOT).
    - outputs (list): List of gates connected to the output of this gate.
    """

    def __init__(self, gate_type, x, y):
        """
        Initialize the Gate object.

        Parameters:
        - gate_type (str): The type of the gate (AND, OR, NOT).
        - x (int): X-coordinate for the initial position.
        - y (int): Y-coordinate for the initial position.
        """
        super().__init__(x, y, 50, 50)
        self.gate_type = gate_type
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        self.outputs = []

    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent):
        """
        Handle the context menu event for the gate.

        Parameters:
        - event (QGraphicsSceneContextMenuEvent): The context menu event.
        """
        menu = QMenu()
        delete_action = menu.addAction("Delete")
        action = menu.exec_(event.screenPos())

        if action == delete_action:
            self.scene().removeItem(self)

    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent):
        """
        Handle the double-click event for the gate.

        Parameters:
        - event (QGraphicsSceneMouseEvent): The double-click event.
        """
        # Double-click to toggle gate type
        if self.gate_type == "AND":
            self.gate_type = "OR"
        elif self.gate_type == "OR":
            self.gate_type = "NOT"
        else:
            self.gate_type = "AND"
        self.update()

    def paint(self, painter: QPainter, option, widget=None):
        """
        Custom paint method to draw gate based on type.

        Parameters:
        - painter (QPainter): The painter object for drawing.
        - option: Drawing options.
        - widget: The widget being painted.
        """
        painter.drawRect(self.rect())
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.gate_type)

    def add_output(self, output):
        """
        Add an output gate to the list of connected gates.

        Parameters:
        - output (Gate): The gate connected to the output of this gate.
        """
        self.outputs.append(output)

    def get_outputs(self):
        """
        Get the list of connected output gates.

        Returns:
        - list: List of connected output gates.
        """
        return self.outputs

class Connection(QGraphicsLineItem):
    """
    Represents a connection between two gates in the circuit.

    Attributes:
    - start_gate (Gate): The gate from which the connection starts.
    - end_gate (Gate): The gate to which the connection ends.
    """

    def __init__(self, start_gate, end_gate):
        """
        Initialize the Connection object.

        Parameters:
        - start_gate (Gate): The gate from which the connection starts.
        - end_gate (Gate): The gate to which the connection ends.
        """
        super().__init__()
        self.start_gate = start_gate
        self.end_gate = end_gate

    def paint(self, painter: QPainter, option, widget=None):
        """
        Paint the connection line between gates.

        Parameters:
        - painter (QPainter): The painter object for drawing.
        - option: Drawing options.
        - widget: The widget being painted.
        """
        painter.drawLine(self.start_gate.scenePos(), self.end_gate.scenePos())

class CircuitScene(QGraphicsScene):
    """
    Represents the overall circuit scene.

    Attributes:
    - selected_gate (Gate): The currently selected gate for connection.
    - connection_in_progress (Connection): The connection being created.
    """

    def __init__(self):
        """
        Initialize the CircuitScene object.
        """
        super().__init__()
        self.selected_gate = None
        self.connection_in_progress = None

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        """
        Handle the mouse press event in the circuit scene.

        Parameters:
        - event (QGraphicsSceneMouseEvent): The mouse press event.
        """
        item = self.itemAt(event.scenePos(), QTransform())
        if isinstance(item, Gate):
            self.selected_gate = item
            self.connection_in_progress = Connection(self.selected_gate, None)
            self.addItem(self.connection_in_progress)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        """
        Handle the mouse release event in the circuit scene.

        Parameters:
        - event (QGraphicsSceneMouseEvent): The mouse release event.
        """
        item = self.itemAt(event.scenePos(), QTransform())
        if isinstance(item, Gate) and item != self.selected_gate:
            self.selected_gate.add_output(item)
            item.add_input(self.connection_in_progress)
        self.removeItem(self.connection_in_progress)
        self.selected_gate = None
        self.connection_in_progress = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = CircuitScene()
    view = QGraphicsView(scene)
    view.show()
    sys.exit(app.exec_())
