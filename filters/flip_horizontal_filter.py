import cv2  

def flip_horizontal(image):
    """
    Flips an image horizontally.

    Args:
        image: The input image to flip.

    Returns:
        The flipped image.

    Example:
        flipped_image = flip_horizontal(image)
    """
    flipped_image = cv2.flip(image, 1)  
    return flipped_image 
