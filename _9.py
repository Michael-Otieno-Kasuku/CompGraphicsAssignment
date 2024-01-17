"""
Using PIL for Python and docstrings:
Write a program that displays an image consisting of parallel stripes, sitting above
another image that’s pure gray. Make the gray level adjustable (by slider, buttons,
keystrokes, or any other means you like). Stand far enough away that the stripes are
indistinguishable from one another, and adjust (or have a friend adjust) the gray level of
the solid rectangle until you say it matches the apparent gray of the stripes. Now move
toward the display screen until you can detect the stripes individually; measure your
distance from the display, and compute the angle subtended at your eye by a pair of
parallel stripes. You should make sure that you’re not fooling yourself by having the
display (after the press/click of a button) show either vertical or horizontal stripes next tothe gray rectangle (at random) and have the position of the stripes and the solid rectangle
exchanged or not (at random).
"""

from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import ttk
import random

class GrayAdjustmentApp:
    """
    A professional application for adjusting the gray level of a gray rectangle
    in the presence of parallel stripes.

    Attributes:
        master (tk.Tk): The main tkinter window.
        width (int): Width of the image.
        height (int): Height of the image.
        image (Image.Image): The current image with parallel stripes and a gray rectangle.
        tk_image (ImageTk.PhotoImage): Tkinter-compatible image.
        canvas (tk.Canvas): The canvas to display the image.
        adjust_button (ttk.Button): Button to adjust the gray level.
        gray_level (int): Current gray level of the rectangle.
    """

    def __init__(self, master):
        """
        Initializes the GrayAdjustmentApp.

        Parameters:
            master (tk.Tk): The main tkinter window.
        """
        self.master = master
        self.master.title("Gray Adjustment App")

        # Initialize image dimensions
        self.width = 600
        self.height = 400

        # Initialize gray level variable
        self.gray_level = 128

        # Initialize stripe orientation variable
        self.stripe_orientation = random.choice(['horizontal', 'vertical'])

        # Create a blank image with parallel stripes and a gray rectangle
        self.image = self.create_striped_image()

        # Create Tkinter PhotoImage from PIL Image
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Configure style for a modern look
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Display the image on a canvas
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack(pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        # Create a button to adjust gray level
        self.adjust_button = ttk.Button(self.master, text="Adjust Gray Level", command=self.adjust_gray_level)
        self.adjust_button.pack(pady=10)

        # Update the image with the initial gray level
        self.update_image()

    def create_striped_image(self):
        """
        Creates an image with parallel stripes and a gray rectangle.

        Returns:
            Image.Image: The generated image.
        """
        # Create a blank image
        image = Image.new("RGB", (self.width, self.height), "white")
        draw = ImageDraw.Draw(image)

        # Draw parallel stripes
        stripe_width = 20
        for i in range(0, self.width, stripe_width * 2):
            if self.stripe_orientation == 'horizontal':
                draw.rectangle([i, 0, i + stripe_width, self.height], fill="black")
            else:
                draw.rectangle([0, i, self.width, i + stripe_width], fill="black")

        # Draw a gray rectangle
        draw.rectangle([0, 0, self.width, self.height], fill=(self.gray_level, self.gray_level, self.gray_level))

        return image

    def update_image(self):
        """
        Updates the image on the canvas with the current gray level.
        """
        # Update the image with the current gray level
        self.image = self.create_striped_image()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(1, image=self.tk_image)  # Assuming canvas has only one item

    def adjust_gray_level(self):
        """
        Adjusts the gray level randomly and updates the image.
        """
        # Adjust the gray level randomly
        self.gray_level = random.randint(0, 255)
        
        # Randomize stripe orientation
        self.stripe_orientation = random.choice(['horizontal', 'vertical'])
        
        self.update_image()

def main():
    """
    Main function to create and run the GrayAdjustmentApp.
    """
    root = tk.Tk()
    app = GrayAdjustmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
