import pandas as pd
import numpy as np

def stat(series, df=True):
    """
    Calculate and return various descriptive statistics for a given Pandas Series.

    Parameters:
    - series (Pandas Series): The data series for which statistics are calculated.
    - df (bool): If True, results are returned as a Pandas DataFrame; otherwise, as a 
      dictionary.

    Returns:
    - Pandas DataFrame or dictionary containing the following statistics:
        - Count: Number of non-NA/null entries in the series.
        - Mean: Average value of the series.
        - Standard Deviation: Measures the dispersion of data points from the mean. Higher 
          values indicate greater spread.
        - Variance: Square of the standard deviation, indicating the spread of the series 
          values.
        - Q1 (25th percentile): Value below which 25% of the data falls.
        - Median (50th percentile): The range between Q1 and Q3. Middle value of the series, 
          dividing the data into two equal halves.
        - Q3 (75th percentile): Value below which 75% of the data falls.
        - IQR: Interquartile range, difference between Q3 and Q1, measuring the statistical 
          dispersion.
        - Range (including/excluding outliers): The difference between the maximum and 
          minimum values, with or without considering outliers.
        - Whisker Bottom/Top: Lower and upper bounds of the data excluding outliers, used in 
          box plots.
        - Max/Min value: Highest and lowest values in the series, including outliers.
        - Sum: Total sum of all values in the series.
        - Skewness: Indicates asymmetry of the distribution. A value of 0 suggests a 
          symmetrical distribution.
        - Kurtosis: Measures the tailedness of the distribution - how sharp the peak is. A 
          higher kurtosis indicates more outliers.
        - Coefficient of Variation: The ratio of the standard deviation to the mean, showing 
          relative variability.
        - Mode: The value that appears most frequently in the series.
        - Outliers: Values that fall outside of the expected range (beyond whiskers).
        
        
    - Interprets skewness value as:
    - 'Symmetric': Skewness close to 0, indicating a symmetric distribution. This 
       implies that the mean, median, and mode of the distribution are approximately equal.
       
    - 'Moderately skewed': Skewness between -1 and -0.5 (left) or 0.5 and 1 (right), 
       indicating a moderate shift from symmetry.
         - **Positive Skewness (Greater than 0 but less than 1)**: Indicates that the 
           distribution is moderately skewed to the right (right-tailed). This means that the 
           right tail of the distribution is longer or fatter than the left tail. In a 
           positively skewed distribution, the mean is typically greater than the median.
        - **Negative Skewness (Less than 0 but greater than -1)**: Indicates that the 
           distribution is moderately skewed to the left (left-tailed). This means that the 
           left tail of the distribution is longer or fatter than the right tail. In a 
           negatively skewed distribution, the mean is typically less than the median.
           
    - 'Highly skewed': Skewness less than -1 (left) or greater than 1 (right), indicating a 
       significant asymmetry in the distribution.
        - **Positive Skewness (Greater than 1)**: Indicates that the distribution is highly 
          skewed to the right. This extreme skewness suggests a significant stretching or 
          elongation on the right side of the histogram. In a positively skewed distribution, 
          the mean is typically greater than the median
        - **Negative Skewness (Less than -1)**: Indicates that the distribution is highly 
          skewed to the left. This extreme skewness suggests a significant stretching or 
          elongation on the left side of the histogram.

    - Interprets kurtosis value as:
      Kurtosis is a statistical measure that describes the shape of a distribution's tails 
      in relation to its overall shape. Specifically, it assesses the "tailedness" of the 
      probability distribution of a real-valued random variable. The concept of kurtosis is
      particularly useful in the context of understanding the extremity of outliers or the 
      likelihood of extreme outcomes in a dataset. Here's how to interpret kurtosis:
      
      - Normal Distribution (Mesokurtic): If the kurtosis is close to 0, it indicates that
        the distribution has tails similar to the normal distribution. Such a distribution is
        referred to as mesokurtic. The tails of a mesokurtic distribution are neither too 
        thick nor too thin compared to a normal distribution.

      - High Kurtosis (Leptokurtic): A positive kurtosis value indicates that the distribution 
        has heavier tails and a sharper peak compared to the normal distribution. This is known 
        as leptokurtic. High kurtosis means that outlier values are more likely to occur, which 
        can significantly affect the mean and variance of the data set.

      - Low Kurtosis (Platykurtic): A negative kurtosis value suggests that the distribution has
        lighter tails and a flatter peak than the normal distribution, termed platykurtic. In this
        case, the distribution tends to have fewer extreme outliers, and data points are more moderately
        spread out.
        
    Usage:
    - For exploratory data analysis to understand the distribution, central tendency, and 
      variability of the data.
    - To identify outliers and assess the shape of the data distribution.
    """
    # Calculate basic statistics and round to two decimal places
    mean_value = round(series.mean(), 2)
    q1_value = round(series.quantile(0.25), 2)
    median_value = round(series.median(), 2)
    q3_value = round(series.quantile(0.75), 2)
    count = series.count()  # Count of non-NA/null observations
    missing_values = series.isnull().sum()  # Number of missing values
    std_dev = round(series.std(), 2)  # Standard deviation of observations
    variance = round(series.var(), 2)  # Variance of observations
    skewness = round(series.skew(), 2)  # Skewness of the distribution
    kurtosis = round(series.kurtosis(), 2)  # Kurtosis of the distribution
    cv = round(std_dev / mean_value if mean_value != 0 else 0, 2)  # Coefficient of Variation
    mode_value = round(series.mode()[0], 2) if not series.mode().empty else "No mode"  # Mode of the series
    sum_value = round(series.sum(), 2)  # Sum of all values

    # Calculate IQR and round to two decimal places
    iqr = q3_value - q1_value
    iqr_value = round(iqr, 2)

    # Calculate whisker values and round to two decimal places
    whisker_bottom = round(series[series >= q1_value - 1.5 * iqr].min(), 2)
    whisker_top = round(series[series <= q3_value + 1.5 * iqr].max(), 2)

    # Calculate minimum, maximum, and range that includes outliers
    min_value = series.min()
    max_value = series.max()
    range_incl_outliers = max_value - min_value

    # Calculate midpoint between Q1 and Q3
    midpoint_q1_q3 = round((q1_value + q3_value) / 2, 2)

    # Calculate midpoint between whisker bottom and whisker top
    midpoint_whiskers = round((whisker_bottom + whisker_top) / 2, 2)

    # Extract outliers
    outliers = series[(series < whisker_bottom) | (series > whisker_top)]

    # Displaying the collected statistics as a dictionary
    result_dict = {
        "Count": count,
        "Number of Missing Values": missing_values,
        "Mean": mean_value,
        "Standard Deviation": std_dev,
        "Variance": variance,
        "Skewness": skewness,
        "Kurtosis": kurtosis,
        "Coefficient of Variation": cv,
        "Mode": mode_value,
        "Sum": sum_value,
        "Q1 (25th percentile)": q1_value,
        "Median (50th percentile)": median_value,
        "Q3 (75th percentile)": q3_value,
        "IQR": iqr_value,
        "Range, excl outliers": round(whisker_top - whisker_bottom, 2),
        "Whisker Bottom": whisker_bottom,
        "Whisker Top": whisker_top,
        'Max value': round(max_value, 2),
        'Min value': round(min_value, 2),
        'Range, incl. outliers': round(range_incl_outliers, 2),
        "Outliers": outliers.tolist(),
        "Number of Outliers": len(outliers),
        "IQR midpoint": midpoint_q1_q3,
        "Whiskers midpoint": midpoint_whiskers
    }
    
    # Return the result as a DataFrame if specified
    if df:
        result_df = pd.DataFrame([result_dict]).T
        result_df.columns = ['Value']
        return result_df
    else:
        return result_dict
