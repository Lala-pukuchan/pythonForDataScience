from PIL import Image
from numpy import ndarray
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_rotate(image_path: str) -> ndarray:
    '''
        rotate an image
    '''
    try:
        img = Image.open(image_path)
        width, height = img.size
        transposed_image = Image.new("RGB", (height, width))

        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                transposed_image.putpixel((y, x), pixel)

        transposed_image.save("rotated_img.jpg")
        im = Image.open("rotated_img.jpg")
        plt.imshow(im)
        plt.show()
        rotated_img_array = np.array(im)
        if len(rotated_img_array.shape) == 3:
            print(f"New shape after slicing: {rotated_img_array.shape}")
        else:
            print(f"New shape after slicing: {rotated_img_array.shape} or "
                  f"({rotated_img_array.shape[0]}, "
                  f"{rotated_img_array.shape[1]})")
        return rotated_img_array

    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
    except OSError:
        print(f"Error: {image_path} is not a valid image file.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print(ft_load("animal.jpeg"))
    print(ft_rotate("animal.jpeg"))


if __name__ == "__main__":
    main()
