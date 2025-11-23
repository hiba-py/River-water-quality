import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "data/river-water-quality-raw-data-by-nrwqn-site-1989-2013.csv"


def read_csv_data(filename: str, columns: list[str]) -> list[tuple]:
    """
    IMPORTANT NOTE:
      When completing Part one and Part Two of the project you do NOT need to understand how this function works.
    Reads in data from a list of csv files.
    Returns columns of data requested, in the order given in
    """
    df = pd.read_csv(filename)
    desired_columns = df[columns]
    return list(desired_columns.itertuples(index=False, name=None))


def menu_select(options: list[str]) -> int:
    """
    - Prints a list of enumerated options and collects the users
    - The user is prompted until they enter a valid menu index
    - returns valid user selection
    """
    prompt = f"0-{len(options) - 1}: "
    i = 0
    while i < len(options):
        print(f'[{i}] {options[i]}')
        i += 1

    selection = int(input(prompt))
    while selection < 0 or selection >= len(options):
        print(f'{selection} is not a valid option\nTry again')
        selection = int(input(prompt))
    return selection

def get_all_years_data(river_data):
    """ Combines yearly data for each river """
    for location in river_data:
            temp_dict = {'count': 0, 'total': 0, 'min': 1e6, 'max': -1e6}
            for year in river_data[location]:
                temp_dict['count'] += river_data[location][year]['count']
                temp_dict['total'] += river_data[location][year]['total']
                if temp_dict['min'] > river_data[location][year]['min']:
                    temp_dict['min'] = river_data[location][year]['min']
                if temp_dict['max'] < river_data[location][year]['max']:
                    temp_dict['max'] = river_data[location][year]['max']
            river_data[location]['All years'] = temp_dict
    return river_data

def extract_river_data(quality_data, river_names, year, period = None):
    """ Extracts water quality for given river(s)and year """
    # Initalise dictionary
    river_data = {name.strip(): {} for name in river_names}
    
    for river_name, date_str, reading, in quality_data:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        if year is not None and date.year != year: # continues loop as given year doesn't match
            continue
        if period is not None and (date.year < period[0] or date.year > period[1]):
            # continues loop as current year is not within period
            continue
        if river_name in river_data:
            # Creates new dictionary for given river and current year if not in dictionary
            if date.year not in river_data[river_name]:
                river_data[river_name][date.year] = {'count': 1, 'total': reading,
                                                     'min': reading, 'max': reading}
            else:
                year_data = river_data[river_name][date.year]
                year_data['count'] += 1
                year_data['total'] += reading
                if year_data['min'] > reading:
                    year_data['min'] = reading
                if year_data['max'] < reading:
                    year_data['max'] = reading
    # Create all years dictionary
    if year is None and period is None:
        river_data = get_all_years_data(river_data)
    return river_data

def print_water_quality_report(quality_data , river_names: list[str], year_of_interest: int = None) -> None:
    """Prints a table outlining the quality reading in a given year for a given location"""
    data = extract_river_data(quality_data, river_names, year_of_interest)
    if year_of_interest is None:
        year_of_interest = 'All years'
    print("Water Quality:", year_of_interest)
    print('-' * 56)
    print(f"{'Name':15}{'Avg (mg/m3)':^10}{'Readings':^15}{'Min':^8}{'Max':^8}")
    print('-' * 56)
    for location in data:
        river_data = data[location]
        count = river_data[year_of_interest]['count']
        total = river_data[year_of_interest]['total']
        min_val = river_data[year_of_interest]['min']
        max_val = river_data[year_of_interest]['max']
        print(f"{location:15}{total /  count:^10.2f}{count:^15}{min_val:^8}{max_val:^8}")

def extract_valid_year_and_river(quality_data):
    """ Reads data input and returns range for year and valid river names """
    years = []
    all_rivers = []

    for i in range(len(quality_data)):
        year = datetime.strptime(quality_data[i][1], "%d/%m/%Y").year
        if year not in years:
            years.append(year)
        if quality_data[i][0] not in all_rivers:
            all_rivers.append(quality_data[i][0])
    return (min(years), max(years)), all_rivers

def validate_river(all_rivers, user_input):
    """ Checks each user inputted river name in data. Returns True if all names are in data """
    for river in user_input:
        if river not in all_rivers:
            return False
    return True

def get_river_names(all_rivers):
    """ Prompts user for river names """
    while True:
        rivers_string = input("River Names: ")
        river_names = [r.strip() for r in rivers_string.split(",")]
        if validate_river(all_rivers, river_names):
            return river_names
        print(f"Sorry, no data available for {', '.join([str(river) for river in river_names])}. Please enter another river")

def get_plot_data(quality_data, rivers, start, end):
    """ Extracts x and y values for time plot as numpy arrays """
    data = extract_river_data(quality_data, rivers, None, (start, end))
    x_vals = np.arange(start, end + 1)
    y_vals = np.array([])
    for year in range(start, end + 1):
        for river in data:
            avg = data[river][year]['total'] / data[river][year]['count']
            y_vals = np.append(y_vals, avg)
    y_vals = y_vals.reshape((end - start + 1), len(data))
    return x_vals, y_vals

def plot_time_graph(quality_data, rivers, start, end):
    """ Plots time graph for specified period """
    # Get the data
    x, y = get_plot_data(quality_data, rivers, start, end)
    
    # plot data
    axes = plt.axes()
    axes.plot(x, y, label = rivers)
    axes.set_title(f"Water Quality for {start}-{end}")
    axes.set_ylabel("Average Water Quality (mg/m$^3$)")
    axes.set_xlabel("Year")
    axes.legend()
    plt.show()

def validate_year(prompt):
    """ Prompts user to enter year, and validates whether input is an integer"""
    while True:
        year = input(prompt)
        if year.isnumeric():
            return int(year.strip())
        print(f'Enter numeric year')

def get_valid_year(years, prompt):
    """ Validates whether year is within data range """
    year = validate_year(prompt)
    while year not in range(years[0], years[1] + 1):
        print(f'Sorry, no data available for the year {year}. Please enter a year between {years[0]} and {years[1]}')
        year = validate_year(prompt)
    return year

def get_time_period(years):
    """ Checks whether time period is logically valid 
        - start year must be earlier than end year """
    while True:
        start_year = get_valid_year(years, 'Start year: ')
        end_year = get_valid_year(years, 'End year: ')
        if start_year < end_year:
            return start_year, end_year
        print(f'Invalid time period, please enter again.\nStart year cannot be greater than or equal to end year.')

def main():
    """Small application that presents tables and graphs based on water quality data."""
    menu_options = [
        "Water Quality Report",
        'Water Quality Report - All years',
        "Water Quality Over Time Graph",
        "Exit"
    ]
    # loads data only once
    quality_data = read_csv_data(DATA_FILE, ["river", "sDate", "values"])
    years, rivers = extract_valid_year_and_river(quality_data)
    option = menu_select(menu_options)
    if option == 0:
        year = get_valid_year(years, "Year: ")
        river_names = get_river_names(rivers)
        print_water_quality_report(quality_data, river_names, year)
    elif option == 1:
        river_names = get_river_names(rivers)
        print_water_quality_report(quality_data, river_names)
    elif option == 2:
        start_year, end_year = get_time_period(years)
        river_names = get_river_names(rivers)
        plot_time_graph(quality_data, river_names, start_year, end_year)
    elif option == 3:
        print("Bye")


main()