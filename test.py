import nbformat as nbf
import os
import chardet
import re

# Ask for the path of the notebook
notebook_path = input("Please enter the path of the notebook: ")

# Ask for the path of the folder containing the text files
folder_path = input("Please enter the path of the folder containing the text files: ")

# Read the notebook
with open(notebook_path, 'r') as f:
    notebook = nbf.read(f, as_version=4)

# Get a list of all text files
text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Function to sort the files numerically
def sort_numerically(text_file):
    numbers = re.findall(r'\d+', text_file)
    return int(numbers[0]) if numbers else text_file

# Sort text files in ascending order
text_files.sort(key=sort_numerically)

# Initialize a markdown cell counter
md_cell_counter = 0

for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'markdown':
        # Get the text file path
        txt_file_path = os.path.join(folder_path, text_files[md_cell_counter])

        # Detect the encoding of the text file
        with open(txt_file_path, 'rb') as f:
            result = chardet.detect(f.read())

        # Read the content of the text file with the detected encoding
        with open(txt_file_path, 'r', encoding=result['encoding']) as txt_file:
            cell_content = txt_file.read()

        # Replace the content of the markdown cell with the content of the text file
        notebook['cells'][i]['source'] = cell_content

        print(f"Replaced content of markdown cell {md_cell_counter + 1} with content of text file {text_files[md_cell_counter]}")

        md_cell_counter += 1

        # Stop replacing when we've replaced all the markdown cells
        if md_cell_counter >= len(text_files):
            break

# Save the updated notebook to a new file in the same directory as this script
script_directory = os.path.dirname(os.path.abspath(__file__))
new_notebook_name = "Updated_" + os.path.basename(notebook_path)
new_notebook_path = os.path.join(script_directory, new_notebook_name)

with open(new_notebook_path, 'w') as f:
    nbf.write(notebook, f)

print(f"Updated notebook saved to {new_notebook_path}")
