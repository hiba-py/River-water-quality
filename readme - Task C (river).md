# Water Data Analysis
## Initial Program Behaviour
The input data is in a comma separated values (.CSV) file, with 13 columns including (river) name, location, sDate - sample date, npID - NIWA parameter ID, and (parameter) values

The user is then prompted to input numbers 0-2:
- 0: Generate the water quality report
- 1: Displacy time graph of the water quality report (not yet implemented)
- 2: Exit the programme

When 0 is inputted, the user is then prompted to give a year and river name for water quality report. The programme outputs the average of all measured parameters for the specified year and river. Currently if user inputs 1, the output is 'Not implemented yet'.

## Dependencies
This program requires the following Python libraries:
- pandas
- matplotlib
- datetime (Python standard library)

Data sources:
- Data (NIWA) CC BY 3.0
- Data (PHF) CC BY 4.0

## How to Run
To execute this program run following command from a terminal:

`python3 main.py`

## Future Development
### Basic Analysis Feature
**Water Quality and Health Connections**

I will analyse the water quality over time and the waterborne diseases. This will involve:
- Calculating annual average water quality indicators by region
- Aggregating waterborne disease cases (Campylobacteriosis, Cryptosporidiosis, Salmonellosis) by region and year
- Creating plots for:
  - Scatter plots showing correlation between water quality metrics and disease rates by region
  - Time series line graphs comparing regional water quality trends with disease notification trends
  - Bar charts analysing disease susceptibility by age group and ethnicity in regions with varying water quality

**Additional data source:** Notifiable disease data from the Institute of Environmental Science and Research (ESR) Public Health and Forensic Science Notifiable Diseases Intelligence Dashboard (2006-2013).

### Student Lead Features
**Interactive Regional Health and Water Quality Dashboard**

I will develop an interactive dashboard using Streamlit or Dash that allows users to:
- Select specific regions and time periods to view water quality and disease data
- Generate dynamic visualisations showing correlations between water quality parameters and disease rates
- Filter by demographic groups (age, ethnicity) to explore vulnerability patterns
- Display geographic visualisations using Plotly choropleth maps to show regional water quality and disease rates across New Zealand

**Additional feature:** Integration of live water quality data using the requests library to pull current monitoring data via API for real-time monitoring capabilities.

## Citations
- NIWA. _River water quality, raw data by NRWQN site, 1989-2013_. Retrieved January 13, 2025, from https://data.mfe.govt.nz/table/52532-river-water-quality-raw-data-by-nrwqn-site-1989-2013/
- New Zealand Institute for Public Health and Forensic Science. _Notifiable Diseases Intelligence Dashboard, 2006-2023_. Retrived October 18, 2025, from https://github.com/ESR-NZ/Notifiable-Diseases-Annual-Dashboard-/blob/main/README.md