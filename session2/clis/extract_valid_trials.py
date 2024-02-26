import sys
import pandas as pd
import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='ExtractValidTrials')

# Add an argument
parser.add_argument('InputLocation', type=int, help='Defines the location of the input.')
parser.add_argument('OutputLocation', type=int, help='Defines the location of the output.')

args = parser.parse_args()

# Load the csv file and extract active trials
df = pd.read_csv(args.InputLocation)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(args.OutputLocation, index=False)