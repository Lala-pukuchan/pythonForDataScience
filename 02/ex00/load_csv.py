import numpy as np
import csv
import pandas as pd


def load(path: str) -> np.ndarray:
    '''
    If you don't have pandas installed,
    pip3 install pandas
    This function loads a csv file and returns a numpy.ndarray.
    '''
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions"
              f" {df.shape[0]} rows x {df.shape[1]} columns")
        with open(path) as csvfile:
            data = list(csv.reader(csvfile)).pop(1)
        return data
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
