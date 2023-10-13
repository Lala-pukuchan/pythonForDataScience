def slice_me(family: list, start: int, end: int) -> list:
    '''
    If list is not a list, raise a ValueError.
    Slice a list of lists.
    
    '''
    try:
        if not isinstance(family, list):
            raise ValueError("The 'family' parameter must be a list.")

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
