import numpy as np  # Import the NumPy library for numerical operations.
import cv2  # Import the OpenCV library for image processing.


def erosion(image):
    """
    Erodes an image using a 3x3 kernel.

    Args:
        image: The input image to erode.

    Returns:
        The eroded image.

    Example:
        See: [https://imgur.com/a/l3ELN5J]
    """
    kernel = np.ones((3, 3), np.uint8)  # Define a 3x3 kernel filled with ones, using the uint8 data type for integer values.
    eroded_image = cv2.erode(image, kernel, iterations=1)  # Perform erosion on the image using the defined kernel.
    return eroded_image  # Return the eroded image.
