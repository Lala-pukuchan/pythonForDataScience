def slice_me(family: list, start: int, end: int) -> list:
    '''
    If list is not a list, raise a ValueError.
    Slice a list of lists.
    '''
    try:
        if not isinstance(family, list):
            raise AssertionError("The 'family' parameter must be a list.")
        for item in family:
            if not isinstance(item, list):
                raise AssertionError(
                    "The 'family' parameter must be a list of lists.")
            if len(item) != len(family[0]):
                raise AssertionError(
                    "All lists in the 'family' parameter must have " +
                    "the same length.")
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        sliced = family[start:end]
        print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")
        return family[start:end]

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
