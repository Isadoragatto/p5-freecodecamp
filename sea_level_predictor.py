import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

        # Create scatter plot

    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
        # Create first line of best fit

    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = pd.Series(range(1880, 2051))
    line1 = intercept1 + slope1 * years_extended1
    plt.plot(years_extended1, line1, 'r', label='Best fit line (1880-2050)')
        # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended2 = pd.Series(range(2000, 2051))
    line2 = intercept2 + slope2 * years_extended2
    plt.plot(years_extended2, line2, 'green', label='Best fit line (2000-2050)')

        # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

        # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()