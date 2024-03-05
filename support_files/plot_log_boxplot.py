import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_log_boxplot(series, title='Boxplot on Logarithmic Scale', xlabel='Value (Log Scale)'):
    """
    Plots an enhanced boxplot of a given pandas Series on a logarithmic scale, including lines for the midpoint of the IQR,
    midpoint of the whiskers, and a dot for the mean. Ensures accurate labeling of midpoints on the x-axis according to the log scale.

    Parameters:
    - series (pd.Series): The pandas Series for which the boxplot is to be plotted.
    - title (str, optional): The title of the plot. Defaults to 'Enhanced Boxplot on Logarithmic Scale'.
    - xlabel (str, optional): The label for the x-axis. Defaults to 'Value (Log Scale)'.

    Returns:
    None
    """
    # Prepare the data, removing NaN values
    # data = series.dropna()
    data = series
    
    # Plotting the boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=data)
    plt.xscale('log')
    plt.title(title)
    plt.xlabel(xlabel)

    # Calculating statistics
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    median = data.median()
    mean = data.mean()

    # Whiskers
    whisker_low = data[data >= q1 - 1.5 * iqr].min()
    whisker_high = data[data <= q3 + 1.5 * iqr].max()

    # Midpoints
    iqr_midpoint = (q1 + q3) / 2
    whisker_midpoint = (whisker_low + whisker_high) / 2

    # Adding lines for midpoints
    plt.axvline(x=iqr_midpoint, color='green', linestyle='--', label='IQR Midpoint')
    plt.axvline(x=whisker_midpoint, color='blue', linestyle='--', label='Whisker Midpoint')

    # Adding a dot for the mean
    plt.scatter(mean, 0, color='yellow', s=50, label='Mean', zorder=5)

    # Placing labels for midpoints accurately according to the log scale
    plt.text(iqr_midpoint, plt.gca().get_ylim()[0], f'{iqr_midpoint:.1f}', color='green', ha='center', va='top', rotation=45)
    plt.text(whisker_midpoint, plt.gca().get_ylim()[0], f'{whisker_midpoint:.1f}', color='blue', ha='center', va='top', rotation=45)

    plt.legend()

    plt.show()
