import cv2
import numpy as np

def black_and_white(image):
    """
    Applies a black and white filter to the image.
    
    Args:
        image: The input image to process with black-and-white filter.
    
    Returns:
        The image in black and white format.
    
    Example:
        https://ibb.co/w68P2SR
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray_image
