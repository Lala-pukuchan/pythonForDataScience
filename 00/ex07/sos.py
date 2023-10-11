import sys


NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', " ": "/"
}


def main():
    '''
    covert char to Morse sign and print
    '''
    try:
        if (len(sys.argv) != 2):
            raise AssertionError()
        all_morse = ''
        for char in sys.argv[1]:
            morse = NESTED_MORSE.get(char.upper())
            if morse is None:
                raise AssertionError
            all_morse += " "
            all_morse += morse
        print(all_morse)
    except AssertionError:
        print(AssertionError.__name__ + ":the arguments are bad")


if __name__ == "__main__":
    main()
