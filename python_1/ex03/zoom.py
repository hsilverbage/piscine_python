import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(array: np.ndarray) -> np.ndarray:
    """Extract a 400x400 single-channel region from the center of the image.

    Slices a 400x400 crop from the center of the image and keeps only
    the green channel (index 1), preserving the channel dimension.

    Parameters:
        array (np.ndarray): Original image array of shape (H, W, 3).

    Returns:
        np.ndarray: Cropped array of shape (400, 400, 1).
    """
    h, w = array.shape[:2]
    if h < 400 or w < 400:
        print(f"Error: image too small ({w}x{h}), minimum size is 400x400.")
        return None
    start_y = (h - 400) // 2
    start_x = ((w - 400) // 2)
    zoomed = array[start_y:start_y + 400, start_x:start_x + 400, 1:2]
    return zoomed


def main() -> None:
    """Load animal.jpeg, zoom into it and display the result."""
    try:
        array = ft_load("animal.jpeg")
        if array is None:
            return

        zoomed = ft_zoom(array)

        print(f"\nNew shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.figure()
        plt.imshow(zoomed[:, :, 0], cmap="gray")
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
