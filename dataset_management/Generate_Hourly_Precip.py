import pandas as pd
import calendar
from datetime import datetime
pd.options.display.float_format = '{:.3f}'.format

df1 = pd.read_csv('hourly_precip_data/Hourly_Precip_1.csv')
df2 = pd.read_csv('hourly_precip_data/Hourly_Precip_2.csv')
df3 = pd.read_csv('hourly_precip_data/Hourly_Precip_3.csv')
df4 = pd.read_csv('hourly_precip_data/Hourly_Precip_4.csv')
df5 = pd.read_csv('hourly_precip_data/Hourly_Precip_5.csv')
df6 = pd.read_csv('hourly_precip_data/Hourly_Precip_6.csv')
df7 = pd.read_csv('hourly_precip_data/Hourly_Precip_7.csv')
df8 = pd.read_csv('hourly_precip_data/Hourly_Precip_8.csv')

frames = [df1, df2, df3, df4, df5, df6, df7, df8]
complete_df = pd.concat(frames, ignore_index=True)
complete_df.to_csv('test.csv')
complete_df = complete_df.rename(columns={"system:time_start": "datetime", 
                                          "total_precipitation_hourly": "total_precip"})

for index, row in complete_df.iterrows():
    # print(row["datetime"])
    # Process date string
    month, day, year = row["datetime"].split(" ")
    d = int(day.replace(',', ''))
    yr = int(year)
    # print(yr)
    # Get month number from abbreviated month name
    mn = list(calendar.month_abbr).index(month)
    hr = index % 24
    timestamp = datetime(yr, mn, d, hour=hr)
    # print(index)
    complete_df.loc[index, "datetime"] = timestamp

complete_df.reset_index(drop=True, inplace=True)

complete_df.to_csv('hourly_precipitation.csv', index=False)