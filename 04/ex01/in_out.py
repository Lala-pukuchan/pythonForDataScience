def square(x: int | float) -> int | float:
    '''
    Returns the square of the given number.
    '''
    return (x * x)


def pow(x: int | float) -> int | float:
    '''
    Returns the power of the given number.
    '''
    return (x ** x)


def outer(x: int | float, function) -> object:
    '''
    Returns a function that takes no arguments and returns the result of
    applying the given function to the given number.
    '''
    def inner() -> float:
        nonlocal x
        x = function(x)
        return (x)
    return (inner)


def main():
    print("This is the main function.")


if __name__ == "__main__":
    main()
