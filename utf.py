import os
import chardet

folder_path = "/Users/sauravmanitripathi/Desktop/1/New-Files"

# Get a list of all txt files in the folder
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

for file in txt_files:
    file_path = os.path.join(folder_path, file)

    # Detect the encoding of the file
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    
    # Read the file in its original encoding
    with open(file_path, 'r', encoding=result['encoding']) as f:
        content = f.read()
    
    # Write the content back out in UTF-8
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
