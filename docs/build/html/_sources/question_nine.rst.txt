Question nine
=============
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

GrayAdjustmentApp Class
-----------------------

.. py:class:: GrayAdjustmentApp

   A professional application for adjusting the gray level of a gray rectangle
   in the presence of parallel stripes.

   :ivar tk.Tk master: The main Tkinter window.
   :ivar int width: Width of the image.
   :ivar int height: Height of the image.
   :ivar Image.Image image: The current image with parallel stripes and a gray rectangle.
   :ivar ImageTk.PhotoImage tk_image: Tkinter-compatible image.
   :ivar tk.Canvas canvas: The canvas to display the image.
   :ivar ttk.Button adjust_button: Button to adjust the gray level.
   :ivar int gray_level: Current gray level of the rectangle.
   :ivar str stripe_orientation: Orientation of parallel stripes ('horizontal' or 'vertical').

   .. method:: __init__(master)

      Initializes the GrayAdjustmentApp.

      :param tk.Tk master: The main tkinter window.

   .. method:: create_striped_image()

      Creates an image with parallel stripes and a gray rectangle.

      :returns: Image.Image - The generated image.

   .. method:: update_image()

      Updates the image on the canvas with the current gray level.

      :returns: None

   .. method:: adjust_gray_level()

      Adjusts the gray level randomly and updates the image.

      :returns: None

   .. function:: main()

      Main function to create and run the GrayAdjustmentApp.

      Usage:
         - Create an instance of GrayAdjustmentApp.
         - Adjust the gray level using the button.
         - Observe the changes in the displayed image.

      Example usage:

      .. code-block:: python

         if __name__ == "__main__":
             root = tk.Tk()
             app = GrayAdjustmentApp(root)
             root.mainloop()

