class calculator:
    '''This is a calculator class'''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f"Dot product is: {sum(i*j for i, j in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Add Vector is : ["
              f"{' , '.join(f'{i+j:.1f}' for i, j in zip(V1, V2))}]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Sous Vector is : ["
              f"{' , '.join(f'{i-j:.1f}' for i, j in zip(V1, V2))}]")
