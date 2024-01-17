"""
Using PIL for Python and docstrings and OOP:

23. Write a program that draws three black dots of radius 0.25 at x = 0, 1, 2 along the x-axis.
Then display instead three black dots at positions t, t + 1, and t + 2 (using t = 0. 25
initially). Make the display toggle back and forth between the two sets of dots, onceevery quarter-second. Do you tend to see the dots as moving? What if you increase t to 0.5? Include a slider that lets you adjust t from 0 to 3. Does the illusion of the dots moving ever weaken? When t = 1, you could interpret the motion as “the outer dot jumps back
and forth from the far left (x = 0) to the far right (x = 3) while the middle two dots remain
fixed.” Can you persuade yourself that this is what you’re seeing? The strong impression
that the dots are moving as a group is remarkably hard to abandon, supporting the Gestalt
theory.
"""

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import time


class MovingDotsApp(tk.Tk):
    def __init__(self):
        """
        GUI application for displaying moving dots along the x-axis.
        """
        super().__init__()

        self.size = 400
        self.dot_radius = 0.25
        self.dot_spacing = 1.0
        self.t = 0.25
        self.timer_interval = 250  # milliseconds

        self.canvas = tk.Canvas(self, width=self.size, height=self.size, background='white')
        self.canvas.pack()

        self.slider = tk.Scale(self, from_=0, to=3, resolution=0.01, orient=tk.HORIZONTAL, label="t", length=300,
                               command=self.update_t)
        self.slider.set(self.t)
        self.slider.pack()

        self.dots_positions = [(0, 0), (0, 0), (0, 0)]  # Initial positions
        self.is_set_1 = True  # Flag to toggle between two sets of dots

        self.timer_callback()

    def update_t(self, t):
        """
        Update the value of t based on the slider.

        Parameters:
        - t (float): The value of t from the slider.
        """
        self.t = float(t)
        self.update_dots_positions()
        self.draw_dots()

    def update_dots_positions(self):
        """
        Update the positions of the three dots based on the current value of t.
        """
        if self.is_set_1:
            self.dots_positions = [(self.t, 0), (self.t + 1, 0), (self.t + 2, 0)]
        else:
            self.dots_positions = [(0, 0), (1, 0), (2, 0)]

    def draw_dots(self):
        """
        Draw the three black dots on the canvas.
        """
        self.canvas.delete("dots")
        for position in self.dots_positions:
            x, y = position
            dot_x = x * self.size / 3
            dot_y = y * self.size / 3
            self.canvas.create_oval(dot_x - self.dot_radius * self.size,
                                    dot_y - self.dot_radius * self.size,
                                    dot_x + self.dot_radius * self.size,
                                    dot_y + self.dot_radius * self.size,
                                    fill='black', tags="dots")

    def timer_callback(self):
        """
        Callback function for the timer to toggle between two sets of dots.
        """
        self.is_set_1 = not self.is_set_1
        self.update_dots_positions()
        self.draw_dots()
        self.after(self.timer_interval, self.timer_callback)


if __name__ == '__main__':
    app = MovingDotsApp()
    app.title("Moving Dots")
    app.geometry("500x600")
    app.mainloop()
