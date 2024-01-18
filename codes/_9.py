from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import ttk
import random

class GrayAdjustmentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gray Adjustment App")
        self.width = 600
        self.height = 400
        self.gray_level = 128
        self.stripe_orientation = random.choice(['horizontal', 'vertical'])
        self.image = self.create_striped_image()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack(pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.adjust_button = ttk.Button(self.master, text="Adjust Gray Level", command=self.adjust_gray_level)
        self.adjust_button.pack(pady=10)
        self.update_image()

    def create_striped_image(self):
        image = Image.new("RGB", (self.width, self.height), "white")
        draw = ImageDraw.Draw(image)
        stripe_width = 20
        for i in range(0, self.width, stripe_width * 2):
            if self.stripe_orientation == 'horizontal':
                draw.rectangle([i, 0, i + stripe_width, self.height], fill="red")
            else:
                draw.rectangle([0, i, self.width, i + stripe_width], fill="yellow")
        draw.rectangle([0, 0, self.width, self.height], fill=(self.gray_level, self.gray_level, self.gray_level))
        return image

    def update_image(self):
        self.image = self.create_striped_image()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(1, image=self.tk_image)  # Assuming canvas has only one item

    def adjust_gray_level(self):
        self.gray_level = random.randint(0, 255)
        self.stripe_orientation = random.choice(['horizontal', 'vertical'])
        self.update_image()

def main():
    root = tk.Tk()
    app = GrayAdjustmentApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
