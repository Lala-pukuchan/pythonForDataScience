from load_csv import load
from matplotlib import pyplot as plt


def aff_life(df, country: str) -> None:
    '''
    This function prints the life expectancy of a country
    my campus located.
    '''
    try:
        print(df.head())
        print(df.head(0))
        plt.plot()
    except KeyError:
        print("Country or year not found")


def main():
    aff_life(load("life_expectancy_years.csv"), "Japan")


if __name__ == "__main__":
    main()
