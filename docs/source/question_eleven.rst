Question Eleven
===============
Creating simple games is a good way to become familiar with interactive graphics
programming. Program the game of checkers. You can look at each square as an object
that can be picked by the user. You can start with a program in which the user plays both
sides.

CheckersGame Class
------------------

.. py:class:: CheckersGame

   A class representing a simple Checkers game using Pygame.

   :ivar int board_size: Size of the game board (number of squares per row and column).
   :ivar int square_size: Size of each square on the board.
   :ivar list[list[int]] board: 2D list representing the game board, where 0 represents an empty square.
   :ivar int current_player: Current player (1 or 2).
   
   .. method:: __init__(board_size, square_size)

      Initialize the CheckersGame object.

      :param int board_size: Size of the game board.
      :param int square_size: Size of each square on the board.

   .. method:: draw_board()

      Draw the current state of the Checkers board using Pygame.

      :returns: Pygame Surface object representing the current state of the board.

   .. method:: move_piece(start_row, start_col, end_row, end_col)

      Move a piece on the board.

      :param int start_row: Starting row of the piece.
      :param int start_col: Starting column of the piece.
      :param int end_row: Ending row of the piece.
      :param int end_col: Ending column of the piece.

      :returns: bool - True if the move is valid and executed, False otherwise.

   .. method:: is_valid_move(start_row, start_col, end_row, end_col)

      Check if a move is valid.

      :param int start_row: Starting row of the piece.
      :param int start_col: Starting column of the piece.
      :param int end_row: Ending row of the piece.
      :param int end_col: Ending column of the piece.

      :returns: bool - True if the move is valid, False otherwise.

   .. method:: switch_player()

      Switch the current player.

   .. method:: run_game()

      Run the Checkers game using Pygame.

   .. method:: is_valid_square(row, col)

      Check if the clicked square is a valid square.

      :param int row: Row index of the clicked square.
      :param int col: Column index of the clicked square.

      :returns: bool - True if the square is valid, False otherwise.

   .. method:: handle_square_click(row, col)

      Handle a click on a valid square.

      :param int row: Row index of the clicked square.
      :param int col: Column index of the clicked square.

   .. warning::

      Ensure that Pygame is installed before running the game.

Example Usage
-------------

.. code-block:: python

   board_size = 8
   square_size = 60

   checkers_game = CheckersGame(board_size, square_size)
   checkers_game.run_game()

