from load_csv import load
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def projection_life(df1: pd.DataFrame, df2: pd.DataFrame) -> None:
    '''
    create scatter diagram of gdp per person and life expectancy in 1900
    '''

    # retrieve 1900's data
    df1_1900 = df1.iloc[:, df1.columns.get_loc('1900')]
    df2_1900 = df2.iloc[:, df2.columns.get_loc('1900')]
    plt.scatter(df2_1900, df1_1900, color='blue', edgecolor='black')

    # scale setting
    plt.xscale("log")
    ticks = [300, 1000, 10000]
    labels = ['300', '1K', '10K']
    plt.xticks(ticks, labels)

    # label setting
    plt.title('1900')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.show()


def main():
    projection_life(
        load("life_expectancy_years.csv"),
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))


if __name__ == "__main__":
    main()
