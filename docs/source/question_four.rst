Question four
=============
Using the PNGWriter class, write a program which takes an existing image called
image.png and creates a second image called flipped.png as shown below, where
flipped.png is the result of flipping image.png both horizontally and vertically.

ImageFlipper Class
------------------

.. py:class:: ImageFlipper

   A class for flipping an image both horizontally and vertically.

   :ivar str input_path: The path to the input image file.
   :ivar str output_path: The path to save the flipped image.

   .. method:: __init__(input_path, output_path)

      Initialize the ImageFlipper object.

      :param str input_path: The path to the input image file.
      :param str output_path: The path to save the flipped image.

   .. method:: flip_image()

      Open the original image, flip it both horizontally and vertically, and save the result.

      :returns: None

.. function:: main()

   Main function to demonstrate the usage of ImageFlipper class.

   Constants:
      - input_image_path (str): The path to the input image file ("image.png").
      - output_image_path (str): The path to save the flipped image ("flipped.png").

   Usage:
      - Create an instance of ImageFlipper.
      - Call the flip_image method.

   Example usage:
   
   .. code-block:: python

      if __name__ == "__main__":
          input_image_path = "image.png"
          output_image_path = "flipped.png"

          # Create an instance of ImageFlipper
          image_flipper = ImageFlipper(input_image_path, output_image_path)

          # Call the flip_image method
          image_flipper.flip_image()

