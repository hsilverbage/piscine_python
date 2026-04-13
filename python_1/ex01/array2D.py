import numpy as np
import sys

def slice_me(family: list, start: int, end: int) -> list:
    """Write a function that takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.

    You must use the slicing method.

    You have to handle error cases if the lists are not the same size, are not a list ...

    The prototype of function is:

        def slice_me(family: list, start: int, end: int) -> list:

         #your code here"""
    if family is None or type(family) is not list:
        print("Assertion error: Invalid argument")
        sys.exit(1)
    try:
        family = np.array(family)
        print(f"My shape is : {family.shape}")

        new_fam = family[start:end]
        print(f"My new shape is : {new_fam.shape}")

        return new_fam.tolist()

    except ValueError as e:
        print(f"Value error: {e}")
        sys.exit(1)
    except AssertionError as e:
        print(f"Assertion error: {e}")
        sys.exit(1)

def main() -> None:

    family = [[1.8, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]

    # family = ["salut"]
    print(type(family))

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    # Expected output:
    # $> python test_array2D.py
    # My shape is : (4, 2)
    # My new shape is : (2, 2)
    # [[1.8, 78.4], [2.15, 102.7]]
    # My shape is : (4, 2)
    # My new shape is : (1, 2)
    # [[2.15, 102.7]]

if __name__ == "__main__":
    main()
