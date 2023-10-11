import sys
from ft_filter import ft_filter


def main():
    try:
        if (len(sys.argv) > 3):
            raise AssertionError("more than one argument is provided\n")
        elif len(sys.argv) == 1:
            str = input("What is the text to count?\n")
            str += "\n"
        else:
            str = sys.argv[1]
        length = int(sys.argv[2])
        words = str.split()
        ft_filter(lambda word: len(word) < length, words)
        print(list(filter(lambda word: len(word) > length, words)))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
