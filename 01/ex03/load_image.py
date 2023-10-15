from PIL import Image
import numpy as np
from numpy import ndarray


def ft_load(image_path: str) -> ndarray:
    '''
    This function loads an image into a numpy array.
    If you don't have numpy installed, run this command:
        pip3 install numpy
    If you don't have Pillow installed, run this command:
        pip3 install Pillow
    '''
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array
    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
    except OSError:
        print(f"Error: {image_path} is not a valid image file.")
