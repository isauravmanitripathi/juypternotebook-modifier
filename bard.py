import os
import io

def copy_text_to_markdown_cell(txt_file, notebook):
    if not os.path.exists(txt_file):
        print("File not found: " + txt_file)
        return

    with open(txt_file, "r") as f:
        text = f.read()

    with notebook.as_default():
        cell = notebook.cells[-1]
        cell.cell_type = "markdown"
        cell.source = text

def main():
    txt_files = os.listdir("/Users/sauravmanitripathi/Desktop/1/New-Files")
    notebook = open("/Users/sauravmanitripathi/Desktop/1/20200520_Predictions_using_ML_Algorithms(SVM,RF,LogReg).ipynb", "r")

    for txt_file in txt_files:
        copy_text_to_markdown_cell(txt_file, notebook)

    notebook.close()

if __name__ == "__main__":
    main()
