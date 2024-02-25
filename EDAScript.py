"""
In this script, we first import the pandas, library which provides data structures and data analysis tools. We then define our data as a dictionary( since i have to copy from  your website) where each key-balue pair represents a column in our dataset.
The keys are our column names and the values are lists of data points. We convert this dictionary into a pandas Data Frame, which is a 2D labeled data structure.
Next, we calculate the crude death rate for each country by summing the death rates across all age groups. This gives the total death rate per 100,000 people for the entire population.
We then calculate the age-standardized death rate. This is done by multiplying the death rate for each age group by the proportion of people in that age group (assuming a uniform age distribution for simplicity), and then summing these values.
This gives us a death rate that accounts for differences in age distributions between the two countries.
FINALLY, we print the results for the crude death rate and the age-standardized death rate for each country, rounded to one decimal place.
"""

import pandas as pd

# Define the data as a dictionary
data = {
    'Age_group(years)': ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85+'],
    'Death_rate_United_States_2019': [0.04, 0.02, 0.02, 0.02, 0.06, 0.11, 0.29, 0.56, 1.42, 4.00, 14.13, 37.22, 66.48, 108.66, 213.10, 333.06, 491.10, 894.45],
    'Death_rate_Uganda_2019': [0.40, 0.17, 0.07, 0.23, 0.38, 0.40, 0.75, 1.11, 2.04, 5.51, 13.26, 33.25, 69.62, 120.78, 229.88, 341.06, 529.31, 710.40]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Calculate the crude death rate for each country
crude_death_rate_us = df['Death_rate_United_States_2019'].sum()
crude_death_rate_uganda = df['Death_rate_Uganda_2019'].sum()

# Calculate the age-standardized death rate for each country
# Assume a uniform age distribution for simplicity
age_standardized_death_rate_us = (df['Death_rate_United_States_2019'] * (1 / len(df))).sum()
age_standardized_death_rate_uganda = (df['Death_rate_Uganda_2019'] * (1 / len(df))).sum()

# Print the results
print(f"Crude death rate in the US: {crude_death_rate_us:.1f}")
print(f"Crude death rate in Uganda: {crude_death_rate_uganda:.1f}")
print(f"Age-standardized death rate in the US: {age_standardized_death_rate_us:.1f}")
print(f"Age-standardized death rate in Uganda: {age_standardized_death_rate_uganda:.1f}")