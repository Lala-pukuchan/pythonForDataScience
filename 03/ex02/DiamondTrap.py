from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''
    King class
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        if is_alive is not provided, it should be set to True by default
        '''
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        '''
        set the eyes color
        '''
        self.eyes = color

    def set_hairs(self, color):
        '''
        set the hairs color
        '''
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)


if __name__ == '__main__':
    main()
