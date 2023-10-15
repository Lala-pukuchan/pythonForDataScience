from PIL import Image
from numpy import ndarray
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(image_path: str) -> ndarray:
    '''
    If you don't have matplotlib, run this command in your terminal:
        pip3 install matplotlib

    This function zooms an image.
    '''
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        start_x = 300
        start_y = 200
        end_x = 700
        end_y = 600
        zoomed_img_array = img_array[start_x:end_x, start_y:end_y]
        zoomed_img = Image.fromarray(zoomed_img_array)
        zoomed_img.save("zoomed_img.jpg")
        im = Image.open("zoomed_img.jpg")
        plt.imshow(im)
        plt.show()
        if len(zoomed_img_array.shape) == 3:
            print(f"New shape after slicing: {zoomed_img_array.shape}")
        else:
            print(f"New shape after slicing: {zoomed_img_array.shape} or ({zoomed_img_array.shape[0]}, {zoomed_img_array.shape[1]})")
        return zoomed_img_array
    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
    except OSError:
        print(f"Error: {image_path} is not a valid image file.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print(ft_load("animal.jpeg"))
    print(ft_zoom("animal.jpeg"))


if __name__ == "__main__":
    main()
