def callLimit(limit: int):
    '''Decorator that limits the number of calls to a function'''
    count = 0

    def callLimiter(function):
        '''Decorator that limits the number of calls to a function'''

        def limit_function(*args, **kwds):
            '''Decorator that limits the number of calls to a function'''
            nonlocal count
            try:
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    raise AssertionError(
                        f"Error: {function} call too many times")
            except AssertionError as error:
                print(error)

        return limit_function

    return callLimiter
