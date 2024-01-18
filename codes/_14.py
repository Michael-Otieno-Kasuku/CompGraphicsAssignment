"""
The orientation of an airplane is described by a coordinate system as shown below. The
forward–backward motion of the joystick controls the up– down rotation with respect to
the axis running along the length of the airplane, called the pitch. The right–left motion of
the joystick controls the rotation about this axis, called the roll.Using PIL for Python and docstrings and OOP Write a program that uses
the mouse to control pitch and roll for the view seen by a pilot. You can do this exercise
in two dimensions by considering a set of objects to be located far from the airplane, then
having the mouse control the two-dimensional viewing of these objects.
"""

from PIL import Image, ImageDraw
import math
import tkinter as tk

class AirplaneView:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pitch = 0  # Initial pitch angle
        self.roll = 0   # Initial roll angle

        # Create an image to represent the scene
        self.scene_image = Image.new("RGB", (width, height), "white")
        self.draw_scene()

        # Create a Tkinter window to display the scene
        self.root = tk.Tk()
        self.root.title("Airplane View")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        # Bind mouse events to control pitch and roll
        self.canvas.bind("<B1-Motion>", self.handle_mouse_motion)

        # Run the Tkinter main loop
        self.root.after(0, self.update)
        self.root.mainloop()

    def draw_scene(self):
        draw = ImageDraw.Draw(self.scene_image)

        # Draw a simple scene with objects
        draw.rectangle((50, 50, 150, 150), fill="blue")   # Object 1
        draw.rectangle((200, 100, 300, 200), fill="green") # Object 2
        draw.rectangle((350, 50, 450, 150), fill="red")    # Object 3

    def update(self):
        # Update the scene based on pitch and roll angles
        rotated_scene = self.rotate_scene()

        # Display the rotated scene on the Tkinter canvas
        rotated_tk_image = self.convert_pil_to_tk(rotated_scene)
        self.canvas.create_image(self.width // 2, self.height // 2, image=rotated_tk_image)

        # Schedule the next update
        self.root.after(30, self.update)

    def rotate_scene(self):
        # Rotate the scene based on pitch and roll angles
        rotated_scene = self.scene_image.rotate(self.roll, resample=Image.BICUBIC)
        rotated_scene = rotated_scene.rotate(self.pitch, resample=Image.BICUBIC)

        return rotated_scene

    def handle_mouse_motion(self, event):
        # Calculate pitch and roll based on mouse movement
        center_x = self.width // 2
        center_y = self.height // 2

        # Calculate the displacement vector
        dx = event.x - center_x
        dy = event.y - center_y

        # Calculate the angles based on displacement
        self.roll = -math.degrees(math.atan2(dy, center_x))
        self.pitch = -math.degrees(math.atan2(dx, center_y))

    def convert_pil_to_tk(self, pil_image):
        # Convert a PIL image to Tkinter PhotoImage
        return tk.PhotoImage(data=pil_image.tobytes())

if __name__ == "__main__":
    airplane_view = AirplaneView(600, 400)
