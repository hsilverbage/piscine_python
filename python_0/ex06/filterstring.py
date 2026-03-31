import sys
from ft_filter import ft_filter


def main() -> None:
    """Read a string and an integer from the command line, keep only the words
    longer than the integer value, and print the filtered list."""

    try:
        if len(sys.argv) != 3:
            raise AssertionError("Program requires 2 args")
        words = sys.argv[1]
        num = int(sys.argv[2])

        filterstring = list(ft_filter(lambda x: len(x) > num, words.split()))

        print(filterstring)

    except ValueError:
        print("AssertionError: Second argument must be an Int")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return


if __name__ == "__main__":
    main()
