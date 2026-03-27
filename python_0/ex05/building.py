import sys
import string


def analyze_string(s: str) -> None:
    """Count and display the number of uppercase letters, lowercase letters,
    punctuation marks, spaces, and digits in the given string."""
    result = {
        'upper_letters': sum(1 for c in s if c.isupper()),
        'lower_letters': sum(1 for c in s if c.islower()),
        'punctuation_marks': sum(1 for c in s if c in string.punctuation),
        'spaces': sum(1 for c in s if c.isspace()),
        'digits': sum(1 for c in s if c.isdigit())
    }
    print(f"The text contains {len(s)} characters:")
    for key, value in result.items():
        print(f"{value} {key}")


def main() -> None:
    """Parse the command-line argument or prompt the user for input, then analyze
    the given string and display the count of its character types."""
    
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            print("What is the text to count?")
            str_to_parse = sys.stdin.readline()
            if str_to_parse != "" and not str_to_parse.endswith('\n'):
                print()
        else :
            str_to_parse = sys.argv[1]
        analyze_string(str_to_parse)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
