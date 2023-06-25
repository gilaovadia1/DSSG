import os
import pandas as pd
import re
import numpy as np

df_sites = pd.read_excel('Data/פילוחי אתרים - להשלים מידע.xlsx')
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

folder_path = "Data" #"path/to/your/folder"

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Create a DataFrame from the file list
file_df = pd.DataFrame(file_list, columns=["file_name"])

# Add columns with year list
file_df['file_year'] = file_df['file_name'].apply(lambda x: re.search(r'\d{4}',x).group() if re.search(r"\d{4}", x) else "N/A")
file_df = file_df[lambda x: x['file_year'] != 'N/A']


df_year = {}

print('importing visit data')
# Import the files from the folder
for i,file_name in enumerate(file_df["file_name"]):
    file_path = folder_path + "/" + file_name
    year = re.search(r"\d{4}", file_name).group()
    df_year[year] = pd.read_excel(file_path)
    print(f'{100*i/len(file_df["file_name"])} %')


# Combine data frames and add a "Year" column
df_visits = pd.concat(df_year.values())
df_visits['year'] = pd.concat([pd.Series([year]*len(df)) for year, df in df_year.items()])

# Reset the index of the combined data frame
df_visits = df_visits.reset_index(drop=True)

# Rename columns combined data frame
df_visits = df_visits.rename(columns={'אתר(ID)': 'site_id',
                                          'אתרים': 'site_type',
                                          'תאור אתרים': 'site_name',
                                          'SPEC6': 'visitor_code',
                                          'SPEC7': 'visitor_type',
                                          'כמות': 'num_of_visitors',
                                          'תאריך': 'visit_date'})


print ('visit data imported')
