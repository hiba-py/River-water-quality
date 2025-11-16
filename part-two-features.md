# Part Two Features
## 1. User Input Validation: Water Quality Report
Added a helper function to validate year entered by input. `validate_year()` prompts user for input and checks whether user entered year is an integer before continuing. This is implemented to prevent any premature crashes due to invalid types such as symbols or letters.

### Design choices
1. Prompt message can be changed, by specifying message.
2. `while` loop is used to repeatedly prompt user if input is not an integer.
3. Displays a message if user enter invalid input.
4. Uses `.isnumeric()` to check if string contains integer, and `.strip()` to remove any whitespaces.

## 2. Include Count, High, and Low Readings: Water Quality Report
Added three columns to the `print_water_quality_report()` function to calculate and display additional information for each river:
- Readings: Total count of measurements
- Min: Minimum reading value
- Max: Maximum reading value

The function was then modified into two parts of the programme:
- `extract_river_data()`: reads csv data and aggregates yearly statistics for each river
- `print_water_quality_report()`: prints the final results as a table

### Design choices
1. Utilised nested dictionaries to store each rivers data
    - Data is stored in the form:
    `{river: 
        {year: {
            'count': ...,
            'total': ...,
            'min': ...,
            'max': ...}}}`
    - This data structure was chosen as:
        - It allows easy access to any river/year combination as the results are mapped
        - Groups readings by year
        - Can be updated in each iteration so relevant data is collected through one pass rather than multiple
        - Can be used for other features such as implementing statistics for all years and creating time series of results
2. `extract_river_data()` processes each data row once while simultaneoulsy updating counter variables in dictionary, `continue` statements are used to skip the rest of the loop when relevant conditions are not met.
3. Included two new (counter) variables (`min_val`, `max_val`) inside loop to improve efficiency and avoid multiple passes over the data.
4. Initialised `min_val` and `max_val` within each loop to get accurate statistical values for each river.
5. Improved table format to include new statistics and display the year of interest.
6. Used centre alignment for columns using f-string formatting for improved readability. This ensures output is well-aligned regardless of the varying number of digits between readings.

## 3. Warn the User if No Records Found
This feature has been implemented in two pipelines:
1. Pre-processing the dataset
2. Validation functions that compare user input to pre-processed values

#### 1. Pre-processing the dataset
Data is first read through `extract_valid_year_and_river()` which collects all unique years and river names. Function returns two values: a tuple of the earliest and latest year, and the list of all valid river names in dataset.

Function loops through `quality_data` using `datetime.strptime(date_str, %d/%m/%Y%).year` to extract year from strings. In the same iteration, it appends the year and river if it's not already in list.

#### 2. Validation functions
Secondly user input is validated against the results of the former function in `validate_river()`, `get_river_names()`, and `get_valid_year()`. The purpose of each functions are as follows:
- `validate_river()`: Validates each user entered river against the list of valid river names returned from extracting function. If the immediate river is not in the reference list, it immediately returns `False`.
- `get_river_names()`: Prompts user for river names.
- `get_valid_year()`: Uses earliest and latest year returned from `extract_valid_year_and_river()` to check whether entered year is within valid range.

### Design choices
1. `extract_valid_year_and_river()` is read at the beginning of user prompt to efficiently validate user input.
2. Helpful error message which shows valid year range.
3. Reduces redudant code in `main()` by centralising validation
4. Ensures programme does not prematurely crash if no result found for entered year and river.

## 4. Add all years: Water Quality Report
To allow user to view aggregated statistics across the entire dataset, I added the ability to generate a report for all years combined. This is implemented in an additional function `get_all_years_data()`.

Firstly, `extract_river_data()` calculates yearly statistics, which is then passed on to the function. The function then iterates over each river's yearly data and creates a new entry called 'All years' which sums `count` and `total` and updates `min` and `max`.

Lastly, the results are then printed through existing function `print_water_quality_report()`.

### Design choices
1. Reusing existing nested dictionary structure to keep data in consistent stucture.
2. Initalised `min` and `max` to `1e6` and `-1e6` respectively, so the values are replaced by first reading and accurate minimum and maximum value is found.
3. Added an additional menu option for user
4. Added an conditional call to function inside `extract_river_data()` to ensure functions perform one task.

## 5. Line Graph of Water Quality Over Time
Implemented a time series graphing option that visualises the water quality across rivers for chosen time periods using `matplotlib.pyplot`.

Programme calls `extract_river_data()` with `period` parameter to get yearly data, then loops over dictionary to get yearly average data. Y values are stored in a dictionary of lists, and `np.arange()` is used to gain x-values (the years).

Time periods are validated by `get_time_period()` function which prompts user for start and end years. The function ensures the entered value is of valid year by `get_valid_year()`, and start year is earlier than later year.

### Design choices:
1. Utlises existing functions to reduce redudant code and maximise efficiency.
2. Uses colour cycling so that each river is of different colour, this ensures easy readablity. This is done by creating a list of valid colours in `matplotlib.pyplot`, where colour is chosen by index from using the modulo of the iteration step and the length of valid colour.
3. Helpful error message is displayed if time period is not logically valid.
4. Additional condition added to `extract_river_data()` to only get yearly data for chosen time period.