Question Fifteen
================
Circuit-layout programs are variants of paint programs. Consider the design of logical
circuits using the Boolean and, or, and not functions. Each of these functions is provided
by one of the three types of integrated circuits (gates),the symbols for which are shown in
Figure below. Write a program that allows the user to design a logical circuit by selecting
gates from a menu and positioning them on the screen. Consider methods for connecting
the outputs of one gate to the inputs of others.

.. _advanced-logical-circuit-designer:

Introduction
------------

This code demonstrates an advanced logical circuit designer using PyQt5. The designer allows users to create and connect various logic gates.

Class Structure
---------------

1. **Gate:** Represents a generic logic gate with a specified type (AND, OR, NOT).
2. **GateInput:** Represents an input terminal of a gate.
3. **GateOutput:** Represents an output terminal of a gate.
4. **Connection:** Represents a connection between the output of one gate to the input of another gate.
5. **CircuitScene:** QGraphicsScene subclass responsible for managing gates and connections.
6. **CircuitDesigner:** Main QWidget for the application, containing the QGraphicsView and the CircuitScene.

Gate Class
----------

.. py:class:: Gate

   Represents a generic logic gate in the circuit.

   :ivar str gate_type: Type of the gate (e.g., "AND", "OR", "NOT").
   :ivar int width: Width of the gate.
   :ivar int height: Height of the gate.
   :ivar list inputs: List of input terminals.
   :ivar list outputs: List of output terminals.
   :ivar QPointF bounding_rect: Bounding rectangle for the gate.
   :ivar float opacity: Opacity of the gate.
   :ivar QGraphicsItem parent: Parent item of the gate.

   .. method:: __init__(gate_type, x, y)

      Initializes a new Gate instance.

      :param str gate_type: Type of the gate.
      :param float x: X-coordinate of the gate's position.
      :param float y: Y-coordinate of the gate's position.

   .. method:: boundingRect()

      Returns the bounding rectangle of the gate.

      :returns: QRectF

   .. method:: paint(painter, option, widget)

      Paints the gate on the QGraphicsView.

      :param QPainter painter: QPainter instance.
      :param QStyleOptionGraphicsItem option: Style options.
      :param QWidget widget: QWidget being painted.

      :returns: None

   .. method:: contextMenuEvent(event)

      Handles the context menu event for the gate.

      :param QGraphicsSceneContextMenuEvent event: Context menu event.

      :returns: None

   .. method:: hoverEnterEvent(event)

      Handles the hover enter event for the gate.

      :param QGraphicsSceneHoverEvent event: Hover event.

      :returns: None

   .. method:: hoverLeaveEvent(event)

      Handles the hover leave event for the gate.

      :param QGraphicsSceneHoverEvent event: Hover event.

      :returns: None

   .. method:: add_input(x, y)

      Adds an input terminal to the gate.

      :param float x: X-coordinate of the input terminal's position.
      :param float y: Y-coordinate of the input terminal's position.

      :returns: None

   .. method:: add_output(x, y)

      Adds an output terminal to the gate.

      :param float x: X-coordinate of the output terminal's position.
      :param float y: Y-coordinate of the output terminal's position.

      :returns: None

   .. method:: update_connections()

      Updates the connections between gates.

      :returns: None

GateInput Class
---------------

.. py:class:: GateInput

   Represents an input terminal of a gate.

   :ivar QGraphicsItem parent_gate: Parent gate to which the input belongs.

   .. method:: __init__(parent_gate, x, y)

      Initializes a new GateInput instance.

      :param Gate parent_gate: Parent gate.
      :param float x: X-coordinate of the input terminal's position.
      :param float y: Y-coordinate of the input terminal's position.

GateOutput Class
----------------

.. py:class:: GateOutput

   Represents an output terminal of a gate.

   :ivar QGraphicsItem parent_gate: Parent gate to which the output belongs.

   .. method:: __init__(parent_gate, x, y)

      Initializes a new GateOutput instance.

      :param Gate parent_gate: Parent gate.
      :param float x: X-coordinate of the output terminal's position.
      :param float y: Y-coordinate of the output terminal's position.

Connection Class
----------------

.. py:class:: Connection

   Represents a connection between the output of one gate to the input of another gate.

   :ivar QPointF start: Start point of the connection.
   :ivar QPointF end: End point of the connection.

   .. method:: __init__(start, end)

      Initializes a new Connection instance.

      :param QPointF start: Start point of the connection.
      :param QPointF end: End point of the connection.

   .. method:: update_path()

      Updates the path of the connection.

      :returns: None

CircuitScene Class
------------------

.. py:class:: CircuitScene

   QGraphicsScene subclass responsible for managing gates and connections.

   :ivar list connections: List of connections in the scene.

   .. method:: __init__()

      Initializes a new CircuitScene instance.

   .. method:: contextMenuEvent(event)

      Handles the context menu event for the scene.

      :param QGraphicsSceneContextMenuEvent event: Context menu event.

      :returns: None

   .. method:: add_gate(gate_type, x, y)

      Adds a gate to the scene.

      :param str gate_type: Type of the gate.
      :param float x: X-coordinate of the gate's position.
      :param float y: Y-coordinate of the gate's position.

      :returns: None

   .. method:: mousePressEvent(event)

      Handles the mouse press event for the scene.

      :param QMouseEvent event: Mouse press event.

      :returns: None

CircuitDesigner Class
---------------------

.. py:class:: CircuitDesigner

   Main QWidget for the application, containing the QGraphicsView and the CircuitScene.

   .. method:: __init__()

      Initializes a new CircuitDesigner instance.

      :returns: None

   .. method:: initUI()

      Initializes the user interface.

      :returns: None

