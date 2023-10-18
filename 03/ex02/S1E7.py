from S1E9 import Character


class Baratheon(Character):
    '''
    families that inherit from the Character class, that we can instantiate
    '''

    def __init__(self, first_name, is_alive=True):
        '''
        if is_alive is not provided, it should be set to True by default
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        '''
        die method sets is_alive to False
        '''
        self.is_alive = False

    def __str__(self):
        return (f"Vector: ('{self.family_name}', '{self.eyes}',"
                f"'{self.hairs}')")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"('{self.first_name}', {self.is_alive})")


class Lannister(Character):
    '''
    families that inherit from the Character class, that we can instantiate
    '''

    def __init__(self, first_name, is_alive=True):
        '''
        if is_alive is not provided, it should be set to True by default
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''
        die method sets is_alive to False
        '''
        self.is_alive = False

    def __str__(self):
        return (f"('{self.family_name}', '{self.eyes}',"
                f"'{self.hairs}')")

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"('{self.first_name}', {self.is_alive})")

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        '''
        create_lannister method that returns a Lannister object
        '''
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)


if __name__ == '__main__':
    main()
