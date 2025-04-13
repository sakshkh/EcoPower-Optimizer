import pandas as pd
import os

# Corrected file paths using raw string literals (r'...')
energy_mix_file = r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\energy_mix_raw.csv"
emissions_file = r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\emissions_raw.csv"
renewable_potential_files = [
    r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\renewable_potential_raw1.csv",
    r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\renewable_potential_raw2.csv",
    r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\renewable_potential_raw3.csv",
    r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\renewable_potential_raw4.csv"
]
solarenergy = r"D:\Sakshham\prjt\clean-energy-optimizer\data\raw\solarenergy.csv"

# Directory to save cleaned data
cleaned_dir = r"D:/Sakshham/prjt/clean-energy-optimizer/data/processed"

# Ensure the cleaned directory exists
if not os.path.exists(cleaned_dir):
    os.makedirs(cleaned_dir)
    print(f"Created directory: {cleaned_dir}")

# Function to load and save data
def load_and_save_data(file_path, output_file):
    try:
        # Try to read the file
        df = pd.read_csv(file_path)
        print(f"--- {os.path.basename(file_path)} ---")
        print(df.info())
        df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Process energy mix and emissions data
load_and_save_data(energy_mix_file, os.path.join(cleaned_dir, 'energy_mix_raw.csv'))
load_and_save_data(emissions_file, os.path.join(cleaned_dir, 'emissions_raw.csv'))

# Process renewable potential files with flexible delimiter handling
for renewable_file in renewable_potential_files:
    try:
        # Try different delimiters, e.g., comma, semicolon, or tab
        df = pd.read_csv(renewable_file, delimiter=';', engine='python')  # Change delimiter as needed
        print(f"--- {os.path.basename(renewable_file)} ---")
        print(df.info())
        
        # Create output file path by replacing 'raw' with 'cleaned' in file name
        output_file = os.path.join(cleaned_dir, os.path.basename(renewable_file).replace('raw', 'cleaned'))
        
        # Save the cleaned data
        df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")
    except pd.errors.ParserError as e:
        print(f"Skipping file {renewable_file}: Error tokenizing data. {e}")
    except Exception as e:
        print(f"Error processing {renewable_file}: {e}")

# Process solar energy data
load_and_save_data(solarenergy, os.path.join(cleaned_dir, 'solarenergy.csv'))
