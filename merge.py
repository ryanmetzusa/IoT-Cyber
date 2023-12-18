import pandas as pd
import glob
import os

# Set the path to your folder containing CSV files
folder_path = r'C:\Users\RyanM\OneDrive\Desktop\wataiData\csv\CICIoT2023'

# Create the pattern for file names (assuming all files end with '.csv')
pattern = os.path.join(folder_path, '*.csv')

# Get a list of all CSV files using the pattern
csv_files = glob.glob(pattern)

# Concatenate all files into a single DataFrame
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)

# Save the merged DataFrame to a new CSV file
output_path = r'C:\Users\RyanM\OneDrive\Desktop\wataiData\merged_output.csv'
df.to_csv(output_path, index=False)

# Display the merged DataFrame
print(df)

