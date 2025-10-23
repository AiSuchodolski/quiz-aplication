import os
import glob
import docx


def docx_parser():
    docx_path = os.path.join("..", "upload", "*.docx")
    docx_files = glob.glob(docx_path)
    if not docx_files:
        print(f"No DOCX file found in {docx_path}")
        exit()
    data_path = os.path.join("..", "data", "data.txt")
    for docx_file in docx_files:
        doc = docx.Document(docx_file)
        with open(data_path, "a", encoding="utf-8") as data_file:
            for paragraph in doc.paragraphs:
               data_file.write(f'{paragraph.text}\n')

    
    print("DOCX file parsed successfully and saved to data.txt")

docx_parser()