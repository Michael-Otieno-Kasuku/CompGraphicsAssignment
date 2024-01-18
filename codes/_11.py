import pygame
from pygame.locals import *
from PIL import Image, ImageDraw

class CheckersGame:
    def __init__(self, board_size, square_size):
        self.board_size = board_size
        self.square_size = square_size
        self.board = [[0] * board_size for _ in range(board_size)]  # 0 represents an empty square
        self.current_player = 1  # Player 1 starts

    def draw_board(self):
        surface = pygame.Surface((self.board_size * self.square_size, self.board_size * self.square_size))
        surface.fill((255, 255, 255))
        for row in range(self.board_size):
            for col in range(self.board_size):
                square_color = (0, 0, 0) if (row + col) % 2 == 0 else (255, 255, 255)
                pygame.draw.rect(surface, square_color,
                                 (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
                piece = self.board[row][col]
                if piece != 0:
                    piece_color = (255, 0, 0) if piece == 1 else (0, 0, 0)
                    pygame.draw.ellipse(surface, piece_color,
                                        (col * self.square_size + 5, row * self.square_size + 5,
                                         self.square_size - 10, self.square_size - 10))
        return surface

    def move_piece(self, start_row, start_col, end_row, end_col):
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            return False
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = 0
        if abs(end_row - start_row) == 2:
            captured_row = (start_row + end_row) // 2
            captured_col = (start_col + end_col) // 2
            self.board[captured_row][captured_col] = 0
        return True

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        if not (0 <= start_row < self.board_size and 0 <= start_col < self.board_size
                and 0 <= end_row < self.board_size and 0 <= end_col < self.board_size):
            return False
        if piece == 0 or (piece == 1 and self.current_player != 1) or (piece == 2 and self.current_player != 2):
            return False
        if self.board[end_row][end_col] != 0:
            return False
        if abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1:
            return True
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            captured_row = (start_row + end_row) // 2
            captured_col = (start_col + end_col) // 2
            if self.board[captured_row][captured_col] == 3 - self.current_player:
                return True
        return False

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def run_game(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen_size = (self.board_size * self.square_size, self.board_size * self.square_size)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Checkers Game")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    clicked_col = mouse_x // self.square_size
                    clicked_row = mouse_y // self.square_size
                    if self.is_valid_square(clicked_row, clicked_col):
                        self.handle_square_click(clicked_row, clicked_col)
            board_surface = self.draw_board()
            screen.blit(board_surface, (0, 0))
            pygame.display.flip()
            clock.tick(60)

    def is_valid_square(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] != 0

    def handle_square_click(self, row, col):
        if self.board[row][col] == self.current_player:
            self.selected_piece = (row, col)
        elif hasattr(self, 'selected_piece'):
            if self.move_piece(self.selected_piece[0], self.selected_piece[1], row, col):
                self.switch_player()
                delattr(self, 'selected_piece')

board_size = 8
square_size = 60
checkers_game = CheckersGame(board_size, square_size)
checkers_game.run_game()

