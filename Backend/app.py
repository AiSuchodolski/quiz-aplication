from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import shutil
from pathlib import Path
from quiz_main import (existing_questions, 
                        reset_quiz, 
                        get_quiz_question, 
                        check_answer, 
                        get_current_question, 
                        get_current_result, 
                        number_of_questions, 
                        get_current_correct_answer)
from parsers.csv_parser import csv_parser
from parsers.docx_parser import docx_parser
from parsers.pdf_txt_parser import pdf_txt_parser
from parsers.text_parser import text_parser

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return "Witaj w aplikacji QUIZ!"

@app.route('/quiz')
def quiz():
    return jsonify({
        "message" : "Witaj w quizie!",
        "status" : "success",
        "version" : "1.0.0"
    })

@app.route('/quiz/start')
def quiz_start():
    reset_quiz()
    return jsonify({
        "message" : "Witaj w quizie! Powodzenia!",
        "rules" : [
            "Zadawane pytania dotyczą przesłanych przez ciebie materiałów.",
            "Z podanych odpowiedzi tylko jedna jest prawidłowa.",
            "Podaj A, B, C lub D.",
        ],
        "status" : "success"
    })

@app.route('/quiz/question')
def quiz_question():
    question = get_quiz_question()
    try:
        return jsonify({
            "question" : question["question"],   
            "number_of_questions" : len(existing_questions),
            "answers" : question["answers"],
            "correct_answer" : question["correct_answer"],
            "status" : "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/quiz/answer', methods=['POST'])
def quiz_answer():
    global number_of_questions
    try:
        current_q = get_current_question()
        current_correct_answer = get_current_correct_answer()
        if not current_q:
            return jsonify({"error": "No question found"}), 404
        if not current_correct_answer:
            return jsonify({"error": "No correct answer found"}), 404
        user_answer = request.json['user_answer']
        result = check_answer(user_answer, current_correct_answer)
        return jsonify(result)
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


@app.route('/quiz/result')
def quiz_result():
    result = get_current_result()
    return jsonify({"status" : "success", "result": result})


@app.route('/quiz/upload', methods=['POST'])
def quiz_upload():
    try:
        if 'file' not in request.files:
            return jsonify({"status" : "error", "message": "Nie załączono pliku"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"status" : "error", "message": "Nazwa pliku jest pusta"}), 400
        if not file.filename.endswith(('.csv', '.docx', '.pdf', '.txt')):
            return jsonify({"status" : "error", "message": "Nieprawidłowy typ pliku"}), 400
        
        else:
            upload_path = Path("Backend", "upload", file.filename)
            if upload_path.exists():
                return jsonify({"status" : "error", "message": "Plik o takiej nazwie już istnieje"}), 400
            upload_path.parent.mkdir(parents=True, exist_ok=True)
            file.save(upload_path)
            return jsonify({"message": "Plik załadowany pomyślnie", "file": file.filename, "status": "success"})
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500  


@app.route('/quiz/processing', methods=['GET'])
def quiz_processing_get():
    data_path = Path("Backend", "data", "data.txt")
    if not data_path.exists():
        return jsonify({"status" : "no-data", "message" : "Obecnie brak danych do quizu"}), 200
    try:
        with data_path.open("r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                return jsonify({"status" : "empty", "message" : "Obecnie brak danych do quizu"}), 200
            return jsonify({"status": "success", "has_data": True, "data": content, "user_decision": True})
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500
        

@app.route('/quiz/processing', methods=['POST'])
def quiz_processing_post():
    data_path = Path("Backend", "data", "data.txt")
    try:     
        if request.json['user_decision'] == True:
            return jsonify({"status": "success", "message": "Dotychczasowe dane zostały zachowane"})
        else:
            with data_path.open("w", encoding="utf-8") as open_data_file:
                open_data_file.write("")
            return jsonify({"status": "success", "message": "Dotychczasowe dane zostały usunięte"})
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500






















# @app.route('/upload', methods=['POST'])
# def upload_files():
#     try:
#         if 'files' not in request.files:
#             return jsonify({"error": "No files provided"}), 400
        
#         files = request.files.getlist('files')
#         if not files or all(file.filename == '' for file in files):
#             return jsonify({"error": "No files selected"}), 400
        
#         # Create upload directory if it doesn't exist
#         upload_dir = Path("upload")
#         upload_dir.mkdir(exist_ok=True)
        
#         # Clear existing files in upload directory
#         for file_path in upload_dir.glob("*"):
#             if file_path.is_file():
#                 file_path.unlink()
        
#         uploaded_files = []
#         for file in files:
#             if file.filename:
#                 filename = file.filename
#                 file_path = upload_dir / filename
#                 file.save(file_path)
#                 uploaded_files.append(filename)
        
#         return jsonify({
#             "message": "Files uploaded successfully",
#             "files": uploaded_files,
#             "status": "success"
#         })
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route('/parse', methods=['POST'])
# def parse_files():
#     try:
#         # Clear existing data.txt
#         data_path = Path("data", "data.txt")
#         data_path.parent.mkdir(exist_ok=True)
#         if data_path.exists():
#             data_path.unlink()
        
#         # Parse different file types
#         parsed_files = []
        
#         # Check for CSV files
#         csv_files = list(Path("upload").glob("*.csv"))
#         if csv_files:
#             csv_parser()
#             parsed_files.extend([f.name for f in csv_files])
        
#         # Check for DOCX files
#         docx_files = list(Path("upload").glob("*.docx"))
#         if docx_files:
#             docx_parser()
#             parsed_files.extend([f.name for f in docx_files])
        
#         # Check for PDF files
#         pdf_files = list(Path("upload").glob("*.pdf"))
#         if pdf_files:
#             pdf_txt_parser()
#             parsed_files.extend([f.name for f in pdf_files])
        
#         # Check for TXT files
#         txt_files = list(Path("upload").glob("*.txt"))
#         if txt_files:
#             text_parser()
#             parsed_files.extend([f.name for f in txt_files])
        
#         if not parsed_files:
#             return jsonify({"error": "No supported files found for parsing"}), 400
        
#         # Check if data.txt was created and has content
#         if data_path.exists() and data_path.stat().st_size > 0:
#             return jsonify({
#                 "message": "Files parsed successfully",
#                 "parsed_files": parsed_files,
#                 "data_ready": True,
#                 "status": "success"
#             })
#         else:
#             return jsonify({"error": "Failed to parse files or data.txt is empty"}), 500
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @app.route('/data/status')
# def data_status():
#     try:
#         data_path = Path("data", "data.txt")
#         if data_path.exists() and data_path.stat().st_size > 0:
#             return jsonify({
#                 "data_ready": True,
#                 "file_size": data_path.stat().st_size,
#                 "status": "success"
#             })
#         else:
#             return jsonify({
#                 "data_ready": False,
#                 "status": "success"
#             })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5003, host='localhost')
