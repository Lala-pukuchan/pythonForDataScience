class calculator:
    '''
    This is a calculator class
    '''
    def __init__(self, values) -> None:
        '''
        set the vector values
        '''
        self.values = values

    def __add__(self, object) -> None:
        '''
        add function
        '''
        self.values = [x + object for x in self.values]
        print(self.values)
        return (self.values)

    def __mul__(self, object) -> None:
        '''
        multiply function
        '''
        self.values = [x * object for x in self.values]
        print(self.values)
        return (self.values)

    def __sub__(self, object) -> None:
        '''
        subtract function
        '''
        self.values = [x - object for x in self.values]
        print(self.values)
        return (self.values)

    def __truediv__(self, object) -> None:
        '''
        divide function
        '''
        if object == 0:
            print("ERROR (div by zero)")
            return (None)
        self.values = [x / object for x in self.values]
        print(self.values)
        return (self.values)
