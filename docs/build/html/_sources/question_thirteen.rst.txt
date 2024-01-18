Question Thirteen
=================
Write a program that allows a user to play a simple version of solitaire. First, design a
simple set of cards using only our basic primitives. Your program can be written in terms
of picking rectangular objects.

Card Class
----------
.. py:class:: Card

   Represents a playing card with a suit and rank.

   :ivar str suit: The suit of the card ('♠', '♥', '♦', '♣').
   :ivar str rank: The rank of the card ('A', '2', ..., '10', 'J', 'Q', 'K').

   .. method:: __init__(suit, rank)

      Initialize a Card object.

      :param str suit: The suit of the card ('♠', '♥', '♦', '♣').
      :param str rank: The rank of the card ('A', '2', ..., '10', 'J', 'Q', 'K').

Deck Class
----------

.. py:class:: Deck

   Represents a deck of playing cards.

   :ivar list cards: List of Card objects in the deck.

   .. method:: __init__()

      Initialize a Deck object with a list of Card objects.

   .. method:: create_deck()

      Create a standard deck of 52 playing cards.

   .. method:: shuffle()

      Shuffle the deck of cards.

SolitaireGame Class
-------------------

.. py:class:: SolitaireGame

   Represents the main Solitaire game logic.

   :ivar Deck deck: Deck object representing the playing cards.
   :ivar int card_x: X-coordinate for card positions.
   :ivar int card_y: Y-coordinate for card positions.
   :ivar Image background: Background image using PIL.
   :ivar ImageDraw draw: ImageDraw object for drawing on the background.
   :ivar Surface background_image: Pygame Surface object representing the background image.

   .. method:: __init__()

      Initialize a SolitaireGame object.

   .. method:: create_window()

      Create the game window and draw the initial cards.

   .. method:: run_game()

      Run the main game loop.

   .. method:: load_image(file_path)

      Load an image using PIL and convert it to a Pygame surface.

      :param str file_path: Path to the image file.

      :returns: Pygame Surface object representing the loaded image.

   .. method:: draw_card(position, card)

      Draw a card on the background image.

      :param tuple position: Tuple representing the position of the card (x1, y1, x2, y2).
      :param Card card: Card object to be drawn.

   Example Usage:
      - Create an instance of SolitaireGame.
      - Run the main game loop.

