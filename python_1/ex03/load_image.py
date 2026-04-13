import numpy as np
from PIL import Image
import sys

def ft_load(path: str) -> np.ndarray:
    """Load an image file and return its pixel data as a NumPy array.

    Opens the image using PIL, converts it to RGB, prints its shape
    and pixel content, then returns it as a NumPy ndarray of shape
    (height, width, 3).

    Parameters:
        path (str): Path to the image file (JPG or JPEG).

    Returns:
        np.ndarray: The image data in RGB format, or None on error.
    """
    try:
        img = Image.open(path).convert("RGB")
        array = np.array(img)
        print(f"The shape of image is: {array.shape}")
        print(array)
        return array
    except Exception as e:
        print(f"Error loading image: {e}")
    return None


def main() -> None:
    """Entry point for testing ft_load."""
    print(ft_load("animal.jpeg"))


if __name__ == "__main__":
    main()
