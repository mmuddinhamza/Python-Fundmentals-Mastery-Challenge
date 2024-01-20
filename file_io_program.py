# Import necessary module
import os

# Define the path to the files
input_file_path = 'product_descriptions.txt'
output_file_path = 'formatted_descriptions.txt'

# Check if the input file exists
if not os.path.exists(input_file_path):
    print(f"Input file {input_file_path} does not exist.")
else:
    # Open the input file and output file
    with open(input_file_path, 'r') as in_file, open(output_file_path, 'w') as out_file:
        # Read each line from the input file
        for line in in_file:
            # Capitalize the first letter of each word in the line
            formatted_line = line.title()
            # Write the formatted line to the output file
            out_file.write(formatted_line)
    print(f"Formatted descriptions have been written to {output_file_path}.")

