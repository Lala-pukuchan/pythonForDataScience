from load_csv import load
from matplotlib import pyplot as plt


def aff_life(df, country: str) -> None:
    '''
    This function prints the life expectancy of a country
    my campus located.
    '''
    try:
        # Get the data for the country
        country_data = df[df["country"] == country]

        # Get the years and life expectancy
        years = country_data.columns[1:].tolist()
        life_expectancy = country_data.iloc[0, 1:].tolist()

        # Plot the data
        plt.figure(figsize=(12, 6))
        plt.plot(years, life_expectancy)
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(f'{country} Life Expectancy Projection')
        plt.xticks(years[::40])
        plt.show()

    except KeyError:
        print("Country or year not found")


def main():
    aff_life(load("life_expectancy_years.csv"), "Japan")


if __name__ == "__main__":
    main()
