import pandas as pd
from pathlib import Path

# Read all 4 CSV files from the raw directory
raw_dir = Path("raw")
csv_files = [
    "depths141 (2).csv",
    "depths188 (2).csv",
    "depths197 (2).csv",
    "depths211 (2).csv"
]

# Read and combine all files
dfs = []
for file in csv_files:
    df = pd.read_csv(raw_dir / file)
    # Keep only depth and origin_time columns
    df = df[['depth', 'origin_time']]
    dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Convert origin_time to datetime
combined_df['origin_time'] = pd.to_datetime(combined_df['origin_time'], format='mixed')

# Sort by origin_time
combined_df = combined_df.sort_values('origin_time')

# Get min and max time
min_time = combined_df['origin_time'].min()
max_time = combined_df['origin_time'].max()

# Create a complete time range with 1-minute intervals
time_range = pd.date_range(start=min_time.floor('min'), end=max_time.ceil('min'), freq='1min')

# Set origin_time as index for resampling
combined_df = combined_df.set_index('origin_time')

# Resample to count events per minute
resampled = combined_df.resample('1min').size()

# Reindex to include all minutes (even those with 0 events)
resampled = resampled.reindex(time_range, fill_value=0)

# Convert to dataframe
result_df = pd.DataFrame({
    'datetime': resampled.index,
    'count': resampled.values
})

# Save to CSV
result_df.to_csv('fractures.csv', index=False)

print(f"Processed {len(combined_df)} total events")
print(f"Time range: {min_time} to {max_time}")
print(f"Created fractures.csv with {len(result_df)} minute intervals")
