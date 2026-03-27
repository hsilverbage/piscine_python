import sys

def odd_or_even(number : int) -> None:
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main() -> None:
    try:
        if len(sys.argv) < 2:
            raise AssertionError("no argument is provided")
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        num = int(sys.argv[1])
        odd_or_even(num)

    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
