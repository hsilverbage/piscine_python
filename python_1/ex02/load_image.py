import numpy as np
from PIL import Image
import sys

def ft_load(path: str):
    """Load an image file and return its pixel data as a NumPy array in RGB format.

    The image is opened using PIL, converted to RGB, and returned as a
    NumPy ndarray of shape (height, width, 3).

    Parameters:
        path (str): Path to the image file.

    Returns:
        np.ndarray: The image data in RGB format.

    Raises:
        SystemExit: If the image cannot be opened or converted."""
    try:
        if path is None:
            raise OSError("path is None")
        img = Image.open(path).convert("RGB")
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except OSError as e:
        print(f"Error loading image: {e}")
        sys.exit(1)

def main() -> None:
    print(ft_load("landscape.jpg"))

if __name__ == "__main__":
    main()
