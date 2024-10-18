import pandas as pd
import calendar
from datetime import datetime
pd.options.display.float_format = '{:,.2f}'.format

df1 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_1.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df2 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_2.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df3 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_3.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df4 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_4.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df5 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_5.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df6 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_6.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df7 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_7.csv', dtype={"surface_pressure": "float64"}, thousands=',')
df8 = pd.read_csv('hourly_surface_pressure_data/Hourly_Surface_Pressure_8.csv', dtype={"surface_pressure": "float64"}, thousands=',')

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

complete_df.to_csv('hourly_surface_pressure.csv', index=False)