from flask import jsonify
import csv
from docx import Document
import PyPDF2


def processing_csv(file_path, open_data_file):
    try:
        with open(file_path, encoding="utf-8", errors="ignore") as file:
            reader = csv.reader(file)
            writer = csv.writer(open_data_file)
            for row in reader:
                writer.writerow(row)
            return jsonify({"status" : "success", "message": "Dane z pliku CSV zostały załadowane do pliku data.txt"}), 200
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


def processing_docx(file_path, open_data_file):
    try:   
        reader = Document(file_path)
        for paragraph in reader.paragraphs:
            open_data_file.write(f'{paragraph.text}\n')
        return jsonify({"status" : "success", "message": "Dane z pliku DOCX zostały załadowane do pliku data.txt"}), 200
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


def processing_pdf(file_path, open_data_file):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                open_data_file.write(f'{page.extract_text()}\n')                                    
        return jsonify({"status" : "success", "message": "Dane z pliku PDF zostały załadowane do pliku data.txt"}), 200
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


def processing_txt(file_path, open_data_file):
    try:
        with open(file_path, encoding="utf-8", errors="ignore") as file:
            reader = file.read()
            open_data_file.write(reader)
            return jsonify({"status" : "success", "message": "Dane z pliku TXT zostały załadowane do pliku data.txt"}), 200
    except Exception as e:  
        return jsonify({"status" : "error", "message": str(e)}), 500     


def processing_upload_files(file_path, open_data_file):
    global file_names
    try:
        if file_path.suffix == ".csv":
            return processing_csv(file_path, open_data_file)
        elif file_path.suffix == ".docx":
            return processing_docx(file_path, open_data_file)
        elif file_path.suffix == ".pdf":
            return processing_pdf(file_path, open_data_file)
        elif file_path.suffix == ".txt":
            return processing_txt(file_path, open_data_file)
        else:
            return jsonify({"status" : "error", "message": "Plik nie jest CSV, DOCX, PDF lub TXT"}), 400
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500



if __name__ == "__main__":
    processing_upload_files()