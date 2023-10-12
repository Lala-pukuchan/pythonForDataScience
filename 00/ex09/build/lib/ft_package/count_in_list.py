def count_in_list(iterable, str) -> int:
    '''
    Count the number of elements in the given list.
    '''
    return sum(1 for word in iterable if word == str)
