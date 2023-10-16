from load_image import ft_load
from PIL import Image
from numpy import ndarray as array


def ft_invert(array) -> array:
    """
    This function takes an image as a parameter
    and inverts the colors of the image.
    """
    img = 255 - array
    Image.fromarray(img).show()
    return img


def ft_red(array) -> array:
    '''
    This function takes an image as a parameter
    and sets the red channel's value to 0.
    '''
    img = array.copy()
    img[:, :, 0] = 0
    Image.fromarray(img).show()
    return img


def ft_green(array) -> array:
    '''
    This function takes an image as a parameter
    and sets the green channel's value to 0.
    '''
    img = array.copy()
    img[:, :, 1] = 0
    Image.fromarray(img).show()
    return img


def ft_blue(array) -> array:
    '''
    This function takes an image as a parameter
    and sets the blue channel's value to 0.
    '''
    img = array.copy()
    img[:, :, 2] = 0
    Image.fromarray(img).show()
    return img


def ft_grey(array) -> array:
    '''
    This function takes an image as a parameter
    and sets the red, green and blue channel's value
    to the average of the three.
    '''
    img = array.copy()
    gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
    img[:, :, 0] = gray
    img[:, :, 1] = gray
    img[:, :, 2] = gray
    Image.fromarray(img).show()
    return img


def main():
    ft_grey(ft_load("landscape.jpg"))


if __name__ == '__main__':
    main()
