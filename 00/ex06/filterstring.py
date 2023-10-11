import sys
from ft_filter import ft_filter


def main():
    '''
    split the args into the array of string
    if length of string is longer than specified len, retrieve it
    '''
    try:
        if (len(sys.argv) != 3):
            raise AssertionError()
        if not sys.argv[2].isdigit():
            raise AssertionError()
        s = sys.argv[1]
        n = int(sys.argv[2])
        array = s.split()
        ft_filter(lambda w: len(array) < n, array)
        print(list(filter(lambda w: len(w) > n, array)))
    except AssertionError:
        print(AssertionError.__name__ + ":the arguments are bad")


if __name__ == "__main__":
    main()
