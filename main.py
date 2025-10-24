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
    prompt = f"0-{len(options) - 1}:: "
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
    """Prints a table outlining the number of crashes in a given year for a given speed limit"""
    data = read_csv_data(DATA_FILE, ["river", "sDate", "values"])
    print("Water Quality")
    print("Name   Reading (mg/m3)")
    for name in river_names:
        count = 0
        total = 0
        for river_name, date_str, reading in data:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            if name == river_name and year_of_interest == date.year:
                total = total + reading
                count += 1
        print(f"{name:15}{total /  count:6.2f}")


def main():
    """Small application that presents tables and graphs based on water quality data."""
    menu_options = [
        "Water Quality Report",
        "Water Quality Over Time Graph",
        "Exit"
    ]
    option = menu_select(menu_options)
    if option == 0:
        year = int(input("Year: "))
        rivers_string = input("River Names: ")
        river_names = rivers_string.split(",")
        print_water_quality_report(year, river_names)
    elif option == 1:
        print("Not Implemented Yet")
    elif option == 2:
        print("Bye")


main()
