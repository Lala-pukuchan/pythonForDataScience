from abc import ABC, abstractmethod


class Character(ABC):
    """
    take first_name and is_alive as parameters
    first_name is a string
    is_alive is a boolean that defaults to True
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self, is_alive):
        pass


class Stark(Character):
    """Stark class is inherited from the Character class"""
    def __init__(self, first_name, is_alive=True):
        """if is_alive is not provided, it should be set to True by default"""
        super().__init__(first_name, is_alive)

    def die(self):
        """die method sets is_alive to False"""
        self.is_alive = False


def main():
    print("Hello World")


if __name__ == '__main__':
    main()
