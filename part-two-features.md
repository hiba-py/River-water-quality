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

### Design choices
1. Included three new (counter) variables (`count`, `min_val`, `max_val`) inside the existing loop to improve efficiency and avoid multiple passes over the data.
2. Initialised `min_val` and `max_val` within each loop to get accurate statistical values for each river.
3. Improved table format to include new statistics.
4. Used centre alignment for columns using f-string formatting for improved readability. This ensures output is well-aligned regardless of the varying number of digits between readings.

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