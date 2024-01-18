from PIL import Image

class ImageFlipper:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def flip_image(self):
        original_image = Image.open(self.input_path)
        flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
        flipped_image.save(self.output_path)
        print(f"Flipped image saved to {self.output_path}")

if __name__ == "__main__":
    input_image_path = "image.png"
    output_image_path = "flipped.png"
    image_flipper = ImageFlipper(input_image_path, output_image_path)
    image_flipper.flip_image()
