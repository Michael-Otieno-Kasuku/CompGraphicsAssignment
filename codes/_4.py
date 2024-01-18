"""
Using the PNGWriter class, use PIL for Python to write a program which takes an existing image called
image.png and creates a second image called flipped.png , where
flipped.png is the result of flipping image.png both horizontally and vertically.
"""

from PIL import Image

class ImageFlipper:
    def __init__(self, input_path, output_path):
        """
        Initialize the ImageFlipper object.

        Parameters:
        - input_path (str): The path to the input image file.
        - output_path (str): The path to save the flipped image.

        Returns:
        None
        """
        self.input_path = input_path
        self.output_path = output_path

    def flip_image(self):
        """
        Open the original image, flip it both horizontally and vertically, and save the result.

        Parameters:
        None

        Returns:
        None
        """
        # Open the original image
        original_image = Image.open(self.input_path)

        # Flip the image both horizontally and vertically
        flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)

        # Save the flipped image
        flipped_image.save(self.output_path)

        print(f"Flipped image saved to {self.output_path}")

if __name__ == "__main__":
    input_image_path = "image.png"
    output_image_path = "flipped.png"

    # Create an instance of ImageFlipper
    image_flipper = ImageFlipper(input_image_path, output_image_path)

    # Call the flip_image method
    image_flipper.flip_image()
