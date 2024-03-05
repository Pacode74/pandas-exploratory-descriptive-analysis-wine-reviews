import pandas as pd
import numpy as np

def percentage_remaining(df, column: str):
    total_records = len(df)
    total_missing = df[column].isnull().sum()
    percentage_ratio = f'{100 - ((total_missing / total_records) * 100): .2f}%'
    # Calculate the percentage of rows where 'Price' is NaN
    price_nan_percentage = df[column].isna().mean() * 100
    dic = {"Total records": total_records, 
           f"Missing {column.lower()}": total_missing, 
           f"Percent remaining {column.lower()}": percentage_ratio,
          f"% of rows where {column.lower()} is NaN": f"{price_nan_percentage:.2f}%"}
    return dic