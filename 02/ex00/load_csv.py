import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    If you don't have pandas installed,
    pip3 install pandas
    This function loads a csv file and returns a numpy.ndarray.
    '''
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print("File not found")
        return None
    except OSError:
        print("OS error")
        return None
    except ValueError:
        print("Value error")
        return None


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
