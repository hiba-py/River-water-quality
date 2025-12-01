# Water Data Analysis
## Initial Program Behaviour
The input data is in a comma separated values (.CSV) file, with 13 columns including river name, location, sDate (sample date), npID (NIWA parameter ID), and parameter values

The user is then prompted to input numbers 0-4:
- 0: Generate the water quality report for specified year
- 1: Generate the water quality report for all years
- 2: Display time graph of the water quality report
- 3: Generate E. coli choropleth map visualisation
- 4: Exit the programme

When 0 is inputted, the user is then prompted to give a year and river name for water quality report. The programme outputs the average of all measured parameters for the specified year and river. If user inputs 1, the programme outputs the average of all measured parameters for all years and specified river. When 2 is inputted, a time graph for specified time period and river is generated. Lastly, when 3 is inputted an interactive animated choropleth map across New Zealand regions is generated.

## Dependencies
This program requires the following Python libraries:
- pandas
- matplotlib
- datetime (Python standard library)
- numpy
- geopandas
- plotly
- pyproj

Data source:
- Data (NIWA) CC BY 3.0

## How to Run
To execute this program run following command from a terminal:

`python3 main.py`

## Future Development
### Basic Analysis Feature
**Water Quality and Health Connections**

I will analyse the relationship between water contamination levels and public health outcomes using E.coli readings as the primary indicator of fecal contamination. This involves:
- Converting easting and northing coordinates to longitude and latitude using pyproj's Transformer
- Perform spatial joins using GeoPandas to match monitoring site coordinates with regional boundary polygons from GeoJSON data
- Calculate regional statistics (mean, median, minimum, maximum, and count) for E.coli readings across all monitoring sites within each region
- Display geographic visualisations using Plotly choropleth maps to show regional water quality across New Zealand for each year

### Student Lead Features
**Interactive Regional Water Quality Choropleth Map**

I developed an interactive choropleth map using Plotly that provides:
- Year selection interface - users can select specific years or use animated timeline slider
- Regional statistics - shown when user hovers over a region

## Citations
- NIWA. _River water quality, raw data by NRWQN site, 1989-2013_. Retrieved January 13, 2025, from https://data.mfe.govt.nz/table/52532-river-water-quality-raw-data-by-nrwqn-site-1989-2013/