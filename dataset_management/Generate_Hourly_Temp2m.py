import pandas as pd
import calendar
from datetime import datetime
pd.options.display.float_format = '{:.2f}'.format

df1 = pd.read_csv('hourly_temp2m_data/Temp2m_1.csv', dtype={"temperature_2m": "float64"})
df2 = pd.read_csv('hourly_temp2m_data/Temp2m_2.csv', dtype={"temperature_2m": "float64"})
df3 = pd.read_csv('hourly_temp2m_data/Temp2m_3.csv', dtype={"temperature_2m": "float64"})
df4 = pd.read_csv('hourly_temp2m_data/Temp2m_4.csv', dtype={"temperature_2m": "float64"})
df5 = pd.read_csv('hourly_temp2m_data/Temp2m_5.csv', dtype={"temperature_2m": "float64"})
df6 = pd.read_csv('hourly_temp2m_data/Temp2m_6.csv', dtype={"temperature_2m": "float64"})
df7 = pd.read_csv('hourly_temp2m_data/Temp2m_7.csv', dtype={"temperature_2m": "float64"})
df8 = pd.read_csv('hourly_temp2m_data/Temp2m_8.csv', dtype={"temperature_2m": "float64"})

frames = [df1, df2, df3, df4, df5, df6, df7, df8]
complete_df = pd.concat(frames, ignore_index=True)
complete_df = complete_df.rename(columns={"system:time_start": "datetime"})

for index, row in complete_df.iterrows():
    # Process date string
    month, day, year = row["datetime"].split(" ")
    d = int(day.replace(',', ''))
    yr = int(year)
    # Get month number from abbreviated month name
    mn = list(calendar.month_abbr).index(month)
    hr = index % 24
    timestamp = datetime(yr, mn, d, hour=hr)
    complete_df.loc[index, "datetime"] = timestamp

complete_df.reset_index(drop=True, inplace=True)

complete_df.to_csv('hourly_temp2m.csv', index=False)