import pandas as pd
from datetime import datetime

DATA_FILE = "river-water-quality-raw-data-by-nrwqn-site-1989-2013.csv"


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


def print_water_quality_report(year_of_interest: int, river_names: list[str]) -> None:
    """Prints a table outlining the quality reading in a given year for a given location"""
    data = read_csv_data(DATA_FILE, ["river", "sDate", "values"])
    print("Water Quality")
    print('-' * 56)
    print(f"{'Name':15}{'Avg (mg/m3)':^10}{'Readings':^15}{'Min':^8}{'Max':^8}")
    print('-' * 56)
    for name in river_names:
        count = 0
        total = 0
        min_val = 0
        max_val = 0
        for river_name, date_str, reading in data:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            if name == river_name and year_of_interest == date.year:
                total = total + reading
                count += 1
                if reading < min_val:
                    min_val = reading
                if reading > max_val:
                    max_val = reading
        print(f"{name:15}{total /  count:^10.2f}{count:^15}{min_val:^8}{max_val:^8}")

def extract_valid_year_and_river():
    """ Reads data input and returns range for year and valid river names """
    data = read_csv_data(DATA_FILE, ["river", "sDate", "values"])
    years = []
    all_rivers = []

    for i in range(len(data)):
        year = datetime.strptime(data[i][1], "%d/%m/%Y").year
        if year not in years:
            years.append(year)
        if data[i][0] not in all_rivers:
            all_rivers.append(data[i][0])
    return (min(years), max(years)), all_rivers

def validate_river(all_rivers, user_input):
    """ Checks each user inputted river name in data. Returns True if all names are in data """
    for i in range(len(user_input)):
        if user_input[i].strip() not in all_rivers:
            return False
    return True

def main():
    """Small application that presents tables and graphs based on water quality data."""
    menu_options = [
        "Water Quality Report",
        "Water Quality Over Time Graph",
        "Exit"
    ]
    years, rivers = extract_valid_year_and_river()
    option = menu_select(menu_options)
    if option == 0:
        year = int(input("Year: "))
        while year not in range(years[0], years[1] + 1):
            print(f'Sorry, no data available for the year {year}. Please enter a year between {years[0]} and {years[1]}')
            year = int(input('Year: '))
        rivers_string = input("River Names: ")
        river_names = rivers_string.split(",")
        while not validate_river(rivers, river_names):
            print(f'Sorry, no data available for {', '.join([str(river) for river in river_names])}. Please enter another river')
            rivers_string = input("River Names: ")
            river_names = rivers_string.split(",")
        print_water_quality_report(year, river_names)
    elif option == 1:
        print("Not Implemented Yet")
    elif option == 2:
        print("Bye")


main()