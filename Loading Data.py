import os
import pandas as pd
import re
import numpy as np
from datetime import datetime

folder_path = "Data" #"path/to/your/folder"

filepath = os.path.join(folder_path, 'פילוחי אתרים - להשלים מידע.xlsx')
df_sites = pd.read_excel(filepath)
df_sites = df_sites.rename(columns={'מחוז':'district',
                                    'שם אתר':'site_name',
                                    'גן או שמורה': 'park_or_reserve',
                                    'סוג אתר': 'site_type',
                                    'פנייה לדת מסוימת': 'religion',
                                    'ים / בריכה / נחל / שכשוך': 'water_source',
                                    'חניון לילה באתר': 'campsite',
                                    'פעילויות מיוחדות': 'special_activity',
                                    'עמוסים יחסית בסופי שבוע' : 'isWeekendPacked',
                                    'משך ביקור ממוצע. קצר (עד שעתיים) בינוני (2-5) ארוך (5+)': 'Average_visit_time'
                                    })

print ('Site data imported')


# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Initialize an empty list to store the dataframes
dataframes = []

for i, filename in enumerate(file_list):
    if filename.endswith('.xlsx') and filename != 'פילוחי אתרים - להשלים מידע.xlsx':
        # Read the Excel file into a dataframe
        filepath = os.path.join(folder_path, filename)
        df = pd.read_excel(filepath)

        # Extract the year from the filename and add it as a new column
        year = filename.split(' - ')[0].split('.')[-1]
        df['Year'] = year

        # Append the dataframe to the list
        dataframes.append(df)

        print(f'{100 * i / len(file_list)-1} %')

df_visits = pd.concat(dataframes, ignore_index=True)


# Rename columns combined data frame
df_visits = df_visits.rename(columns={'אתר(ID)': 'site_id',
                                          'אתרים': 'site_type',
                                          'תאור אתרים': 'site_name',
                                          'SPEC6': 'visitor_code',
                                          'SPEC7': 'visitor_type',
                                          'כמות': 'num_of_visitors',
                                          'תאריך': 'visit_date'})

# Add Formatted column
df_visits['visit_date_fmt'] = pd.to_datetime(df_visits['visit_date'])

# Extract month as a new column
df_visits['Month'] = df_visits['visit_date_fmt'].dt.month

# Extract day of the week as a new column
df_visits['DayOfWeek'] = df_visits['visit_date_fmt'].dt.day_name()



print ('visit data imported')
