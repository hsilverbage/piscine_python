import numpy as np
import sys

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """BMI = mass / height * height
    Je dois bloqué
    - si un elem height est 0

    deja dans le catch:
    - si un elem n'est pas int ou float
    - taille de list pas egale"""
    try:
        np_height = np.array(height)
        np_weight = np.array(weight)

        if np.min(np_height) <= 0:
            raise ValueError("Value cannot be 0")

        bmi = (np_weight / (np_height ** 2))

        return bmi.tolist()

    except TypeError:
        print(f"Type error: only int and float allowed")
        sys.exit(1)
    except ValueError as e:
        print(f"Value error: {e}")
        sys.exit(1)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        np_bmi = np.array(bmi)
        bmi_bool = np_bmi > limit

        return bmi_bool.tolist()

    except ValueError as e:
        print("Value error: {e}")
        sys.exit(1)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


def main() -> None:

    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()


# Expected output:
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]
