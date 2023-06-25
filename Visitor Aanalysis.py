import pandas as pd
import numpy as np

combined_df.columns

combined_df[['visitor_code','visitor_type']].drop_duplicates()

# filter 'סכום'
combined_df = combined_df[lambda x: x['visitor_code'] != 105]

# Sum visits grouped by year
combined_df.groupby('year')['num_of_visitors'].sum()
