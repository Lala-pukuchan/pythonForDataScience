from PIL import Image
from numpy import ndarray
import numpy as np


def ft_zoom(image_path: str) -> ndarray:
    '''
    This function zooms an image.
    '''
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        start_x = 300
        start_y = 200
        end_x = 700
        end_y = 700
        zoomed_img_array = img_array[start_x:end_x, start_y:end_y]
        zoomed_img = Image.fromarray(zoomed_img_array)
        zoomed_img.save("zoomed_img.jpg")
        if len(zoomed_img_array.shape) == 3:
            print(f"New shape after slicing: {zoomed_img_array.shape}")
        else:
            print(f"New shape after slicing: {zoomed_img_array.shape} or ({zoomed_img_array.shape[0]}, {zoomed_img_array.shape[1]})")
        return zoomed_img_array
    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
    except OSError:
        print(f"Error: {image_path} is not a valid image file.")


def main():
    img = ft_zoom("animal.jpeg")
    print(img)


if __name__ == "__main__":
    main()
