from pathlib import Path
import PyPDF2


def pdf_txt_parser():
    pdf_path = list(Path("..", "upload").glob("*.pdf"))
    if not pdf_path:
        print("No PDF files found in uploads folder")
        exit()
    data_path = Path("..", "data", "data.txt")
    data_path.parent.mkdir(exist_ok=True)
    with data_path.open("a", encoding="utf-8", errors="ignore") as open_data_file:
        for pdf_file in pdf_path:
            with pdf_file.open("rb") as open_pdf_file:
                reader = PyPDF2.PdfReader(open_pdf_file)
                for page in reader.pages:
                    open_data_file.write(page.extract_text())
    print(f"PDF files parsed successfully and saved to {data_path}")


pdf_txt_parser()




#     pdf_path = os.path.join("..", "upload", "*.pdf")
#     pdf_files = glob.glob(pdf_path)
#     if not pdf_files:
#         print(f"No PDF files found in {pdf_path}")
#         exit()
#     data_path = os.path.join("..", "data", "data.txt")
#     with open(data_path, "w", encoding="utf-8") as txt_file:
#         for pdf_file in pdf_files:
#             with open(pdf_file, "rb") as open_pdf_file:
#                 reader = PyPDF2.PdfReader(open_pdf_file)
#                 for page in reader.pages:
#                     txt_file.write(page.extract_text())
#     print(f"Data saved to {data_path}")


# pdf_txt_parser()