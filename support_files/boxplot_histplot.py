import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_boxplot_series(series, plot=True, swarmplot=False, histogram=True):
    """
    Analyzes categorical data using the direct method on series approach.

    Parameters:
        series (Series): The input dataset with numerical values.
        plot (bool): Whether to plot the box plot. Default is False.
        swarmplot (bool): Whether to include a swarmplot. Default is False.
        return_dataframe (bool): Whether to return the result as a DataFrame. Default is False.
        histogram (bool): Whether to include a histogram. Default is True.

    """
    # Create a temporary figure with adjusted size
    fig, ax_box = plt.subplots(figsize=(15, 8))
    
    # Create a twin Axes for the histogram if enabled
    if histogram:
        ax_hist = ax_box.twinx()

    # Calculate statistics and round to two decimal places
    mean_value = round(series.mean(), 2)
    q1_value = round(series.quantile(0.25), 2)
    median_value = round(series.median(), 2)
    q3_value = round(series.quantile(0.75), 2)

    # Calculate IQR and round to two decimal places
    iqr = q3_value - q1_value
    iqr_value = round(iqr, 2)

    # Calculate whisker values and round to two decimal places
    whisker_bottom = round(series[series >= q1_value - 1.5 * iqr].min(), 2)
    whisker_top = round(series[series <= q3_value + 1.5 * iqr].max(), 2)

    # Calculate minimum, maximum, and range that includes Outliers values
    min_value = series.min()
    max_value = series.max()
    range_incl_outliers = max_value - min_value

    # Calculate midpoint between Q1 and Q3
    midpoint_q1_q3 = round((q1_value + q3_value) / 2, 2)
    
    # Calculate midpoint between Whisker Bottom and Whisker Top
    midpoint_whiskers = round((whisker_bottom + whisker_top) / 2, 2)

    # Extract outliers
    outliers = series[(series < whisker_bottom) | (series > whisker_top)]

    # Set y-axis limits
    ax_box.set_ylim([series.min() - 1, series.max() + 1])

    # Plot the boxplot
    sns.boxplot(x=series, data=pd.DataFrame(series), width=0.5, ax=ax_box)
    if swarmplot:
        sns.swarmplot(x=series, color='black', alpha=0.2, ax=ax_box)
    # Drawing a midpoint line
    ax_box.axvline(x=midpoint_q1_q3, color='red', linestyle='--', label='IQR Midpoint')
    ax_box.axvline(x=midpoint_whiskers, color='blue', linestyle='--', label='Whiskers Midpoint')
    # Draw a red dot for the mean
    ax_box.plot(mean_value, 0, 'ro', label='Mean')
    # Place legend inside the boxplot
    ax_box.legend(loc='upper left')

    # Plot the histogram if enabled
    if histogram:
        sns.histplot(series, bins=20, kde=True, ax=ax_hist, color='green', stat='count', alpha=0.1)

    # Show the plot if requested
    if plot:
        plt.show()

