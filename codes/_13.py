import pygame
from PIL import Image, ImageDraw
import os
import random

class Card:
    """Represents a playing card with a suit and rank."""

    def __init__(self, suit, rank):
        """
        Initialize a Card object.

        Parameters:
        - suit (str): The suit of the card ('♠', '♥', '♦', '♣').
        - rank (str): The rank of the card ('A', '2', ..., '10', 'J', 'Q', 'K').
        """
        self.suit = suit
        self.rank = rank

class Deck:
    """Represents a deck of playing cards."""

    def __init__(self):
        """Initialize a Deck object with a list of Card objects."""
        self.cards = []
        self.create_deck()

    def create_deck(self):
        """Create a standard deck of 52 playing cards."""
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)

class SolitaireGame:
    """Represents the main Solitaire game logic."""

    def __init__(self):
        """Initialize a SolitaireGame object."""
        self.deck = Deck()
        self.deck.shuffle()

        # Initialize card positions
        self.card_x = CARD_SPACING
        self.card_y = CARD_SPACING

        # Create a background image using PIL
        self.background = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), "green")
        self.draw = ImageDraw.Draw(self.background)

        self.create_window()

    def create_window(self):
        """Create the game window and draw the initial cards."""
        # Draw cards on the background
        for card in self.deck.cards:
            self.draw_card((self.card_x, self.card_y, self.card_x + CARD_WIDTH, self.card_y + CARD_HEIGHT), card)
            self.card_x += CARD_WIDTH + CARD_SPACING

            if self.card_x + CARD_WIDTH + CARD_SPACING > SCREEN_WIDTH:
                self.card_x = CARD_SPACING
                self.card_y += CARD_HEIGHT + CARD_SPACING

        # Save the background image as a temporary file
        self.background.save("background.png")

        # Load the background image using Pygame
        self.background_image = self.load_image("background.png")

        self.run_game()

    def run_game(self):
        """Run the main game loop."""
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simple Solitaire")

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Display the background image
            screen.blit(self.background_image, (0, 0))

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
        # Remove the temporary background image file
        os.remove("background.png")

    def load_image(self, file_path):
        """Load an image using PIL and convert it to a Pygame surface."""
        image = Image.open(file_path)
        return pygame.image.fromstring(image.tobytes(), image.size, image.mode)

    def draw_card(self, position, card):
        """Draw a card on the background image."""
        # Draw card background
        self.draw.rectangle(position, fill="white", outline="black")

        # Draw suit and rank
        self.draw.text((position[0] + 10, position[1] + 10), card.suit, fill="black")
        self.draw.text((position[0] + 10, position[1] + 40), card.rank, fill="black")

if __name__ == "__main__":
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    CARD_WIDTH, CARD_HEIGHT = 100, 150
    CARD_SPACING = 10

    solitaire_game = SolitaireGame()
