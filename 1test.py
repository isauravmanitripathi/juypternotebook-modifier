import nbformat as nbf
import os
import shutil

notebook_path = "/Users/sauravmanitripathi/Desktop/1/20200520_Predictions_using_ML_Algorithms(SVM,RF,LogReg).ipynb"
folder_path = "/Users/sauravmanitripathi/Desktop/1/New-Files"

# Read the notebook
with open(notebook_path, 'r') as f:
    notebook = nbf.read(f, as_version=4)

# Sort text files in ascending order
text_files = sorted(os.listdir(folder_path))

# Initialize a markdown cell counter
md_cell_counter = 0

for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'markdown':
        # Read the content of the text file
        with open(os.path.join(folder_path, text_files[md_cell_counter]), 'r') as txt_file:
            cell_content = txt_file.read()

        # Replace the content of the markdown cell with the content of the text file
        notebook['cells'][i]['source'] = cell_content

        md_cell_counter += 1

        # Stop replacing when we've replaced all the markdown cells
        if md_cell_counter >= len(text_files):
            break

# Save the updated notebook to a new file
new_notebook_path = os.path.join(folder_path, "Updated_Predictions_using_ML_Algorithms(SVM,RF,LogReg).ipynb")
with open(new_notebook_path, 'w') as f:
    nbf.write(notebook, f)
