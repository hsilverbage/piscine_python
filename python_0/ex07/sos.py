import sys

def encode_into_morse(s: str):
    """Convert the given string into Morse code and print the encoded sequence.
    Raise an AssertionError if the string contains unsupported characters."""

    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    s_to_morse = []
    for c in s.upper():
        if c in morse_code_dict:
            s_to_morse.append(morse_code_dict[c])
        else:
            raise AssertionError("The program only supports spaces and alphanumeric characters")
    print(*s_to_morse)

def main():
    """Validate the command-line arguments, pass the input string to the Morse
    encoder, and display an error message if the input is invalid."""

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong number of arguments, a string is required")
        encode_into_morse(sys.argv[1])

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return

if __name__ == "__main__":
    main()
