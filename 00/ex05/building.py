import sys


def count(text):
    print(f"The text contains {sum(1 for c in text)} characters:")
    print(f"{sum(1 for c in text if c.isupper())} upper letters")
    print(f"{sum(1 for c in text if c.islower())} lower letters")
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f"{sum(1 for c in text if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in text if c.isspace())} spaces")
    print(f"{sum(1 for c in text if c.isdigit())} digits")


def main():
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided\n")
        elif len(sys.argv) == 1:
            str = input("What is the text to count?\n")
            str += "\n"
        else:
            str = sys.argv[1]
        count(str)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)

if __name__ == "__main__":
    main()
