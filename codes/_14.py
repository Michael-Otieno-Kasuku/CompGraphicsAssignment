import pygame
from pygame.locals import *
from PIL import Image, ImageDraw
import sys
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
AIRPLANE_WIDTH, AIRPLANE_HEIGHT = 100, 150
AIRPLANE_COLOR = (255, 0, 0)  # Red color for the airplane
OBJECTS_COLOR = (0, 0, 255)   # Blue color for distant objects

class AirplaneView:
    def __init__(self):
        self.pitch_angle = 0
        self.roll_angle = 0
        self.mouse_x, self.mouse_y = 0, 0

    def update_view(self):
        # Create a blank image using PIL
        image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), "white")
        draw = ImageDraw.Draw(image)

        # Draw the airplane
        self.draw_airplane(draw)

        # Draw distant objects
        self.draw_distant_objects(draw)

        # Convert PIL image to Pygame surface
        pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
        return pygame_image

    def draw_airplane(self, draw):
        # Draw the airplane based on pitch and roll angles
        airplane_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        airplane_rect = (
            airplane_center[0] - AIRPLANE_WIDTH // 2,
            airplane_center[1] - AIRPLANE_HEIGHT // 2,
            airplane_center[0] + AIRPLANE_WIDTH // 2,
            airplane_center[1] + AIRPLANE_HEIGHT // 2
        )
        draw.rectangle(airplane_rect, fill=AIRPLANE_COLOR)

    def draw_distant_objects(self, draw):
        # Draw distant objects (simple representation)
        # In a real application, you would have a more complex scene with depth and perspective
        for _ in range(10):
            object_x = SCREEN_WIDTH // 2 + 100 * (random.random() - 0.5)
            object_y = SCREEN_HEIGHT // 2 + 100 * (random.random() - 0.5)
            object_rect = (
                object_x - 5, object_y - 5,
                object_x + 5, object_y + 5
            )
            draw.rectangle(object_rect, fill=OBJECTS_COLOR)

    def handle_mouse_event(self, event):
        if event.type == MOUSEMOTION:
            self.mouse_x, self.mouse_y = event.pos
            self.update_angles()

    def update_angles(self):
        # Update pitch and roll angles based on mouse position
        self.pitch_angle = (self.mouse_y - SCREEN_HEIGHT // 2) / SCREEN_HEIGHT * 90
        self.roll_angle = (self.mouse_x - SCREEN_WIDTH // 2) / SCREEN_WIDTH * 90

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Airplane View")

    airplane_view = AirplaneView()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEMOTION:
                airplane_view.handle_mouse_event(event)

        # Update the view and display
        screen.fill((255, 255, 255))
        airplane_image = airplane_view.update_view()
        screen.blit(airplane_image, (0, 0))
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

