import pandas as pd
import calendar
from datetime import datetime
pd.options.display.float_format = '{:.2f}'.format

df1 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_1.csv')
df2 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_2.csv')
df3 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_3.csv')
df4 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_4.csv')
df5 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_5.csv')
df6 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_6.csv')
df7 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_7.csv')
df8 = pd.read_csv('hourly_soil_temp_4_data/Hourly_Soil_Temp_Lvl4_8.csv')

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

complete_df.to_csv('hourly_soil_temp_lvl4.csv', index=False)