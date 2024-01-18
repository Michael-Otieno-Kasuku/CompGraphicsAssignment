Question seven
==============
You can generate a simple maze starting with a rectangular array of cells. Each cell has
four sides. You remove sides (except from the perimeter of all the cells) until all the cellsare connected. Then you create an entrance and an exit by removing two sides from the
perimeter. A simple example is shown in Figure below. Write a program using WebGL
or OPENGL or JAVA or any other programming language of your choice and
understanding that takes as input the two integers N and M and then draws an N × M maze.

MazeGenerator Class
-------------------

.. py:class:: MazeGenerator

   The MazeGenerator class provides functionality for generating and visualizing mazes using a randomized Prim's algorithm.

   :ivar int N: Number of rows in the maze.
   :ivar int M: Number of columns in the maze.
   :ivar list maze: The generated maze represented as a 2D list.
   :ivar set visited: Set of visited cells during maze generation.

   .. method:: __init__(N, M)

      Initialize the MazeGenerator object.

      :param int N: Number of rows.
      :param int M: Number of columns.

   .. method:: generate_maze()

      Generate a connected maze using a randomized Prim's algorithm.

      :returns: The generated maze as a 2D list.

   .. method:: _visit(cell)

      Helper method for randomized Prim's algorithm.

      :param tuple cell: Current cell coordinates.

      :returns: None

   .. method:: draw_maze(cell_size=20)

      Draw the generated maze with color.

      :param int cell_size: Size of each cell in pixels.

      :returns: None

