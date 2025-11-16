# Part Two Features
Below are a list of features that are to be completed for the second part of the assignment. Refer to the Project section of the course page for more detail on each feature.

Please fill in the section for each feature, replace all text below each heading.

## 1. User Input Validation: Water Quality Report
Replace me with an outline of:

- how you implemented this feature
- choices you made and why

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
Replace me with an outline of:

- how you implemented this feature
- choices you made and why

## 4. Add all years: Water Quality Report
Replace me with an outline of:

- how you implemented this feature
- choices you made and why

## 5. Line Graph of Water Quality Over Time
Replace me with an outline of:

- how you implemented this feature
- choices you made and why