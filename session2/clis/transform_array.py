import argparse
import numpy as np

# Create a parser object
parser = argparse.ArgumentParser(description='Transform an array file')

# Add an argument
parser.add_argument('InputFile', type=str, help='.npy file to work on')
parser.add_argument('OutputFile', type=str, help='OutputLocation')
parser.add_argument('Operation', type=str, choices = ['normalize', 'standardize'])

args = parser.parse_args()

input_array_path = args.InputFile
input_array = np.load(input_array_path)
output_array_path = args.OutputFile

if args.Operation == "normalize":
# Load the input and normalize it
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)

     # Save the normalized array
    np.save(output_array_path, output_array)
elif args.Operation == "standardize":
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)

    # Save the standardized array
    np.save(output_array_path, output_array)
else:
    raise ValueError("False Argument.")