from load_csv import load
from matplotlib import pyplot as plt


def aff_pop(df, country: str, another: str) -> None:
    '''
    This function prints the population of two countries
    '''
    try:
        # Get the data for the country
        country_data = df[df["country"] == country]
        another_country_data = df[df["country"] == another]

        # Get the years and population for the range 1800 to 2050
        start_col = country_data.columns.get_loc("1800")
        end_col = country_data.columns.get_loc("2050") + 1
        years = country_data.columns[start_col:end_col].tolist()
        pop = country_data.iloc[0, start_col:end_col] \
            .apply(lambda x: float(x.replace("M", ""))).tolist()
        another_start_col = another_country_data.columns.get_loc("1800")
        another_end_col = another_country_data.columns.get_loc("2050") + 1
        another_years = another_country_data \
            .columns[another_start_col:another_end_col].tolist()
        another_pop = another_country_data \
            .iloc[0, another_start_col:another_end_col] \
            .apply(lambda x: float(x.replace("M", ""))).tolist()

        # Plot the data
        plt.figure(figsize=(12, 6))
        plt.plot(years, pop, label=country)
        plt.plot(another_years, another_pop, label=another)
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projection')
        plt.xticks(years[::40])
        yticks = [20, 40, 60, 80, 100, 120]
        plt.yticks(yticks, [f'{y}M' for y in yticks])
        plt.legend()
        plt.show()

    except KeyError:
        print("Country or year not found")


def main():
    aff_pop(load("population_total.csv"), "Japan", "France")


if __name__ == "__main__":
    main()
