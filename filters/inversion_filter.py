import cv2 

def inversion(image):
    """
    Flips pixel values to black & white colors:

    1. if pixel > 0 -> 0 (black)
    2. if pixel == 0 -> 255 (white)

    Args:
        image: The input image to which bitwise inversion will be performed.

    Returns:
        The balck & white inversion of an image.

    Example:
        https://pyimagesearch.com/wp-content/uploads/2021/01/opencv_bitwise_not.png
    """
    inversed_image = cv2.bitwise_not(image)  
    return finversed_image
