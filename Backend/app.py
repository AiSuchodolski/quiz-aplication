from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
from quiz_main import (existing_questions, 
                        reset_quiz, 
                        get_quiz_question_with_key, 
                        check_answer, 
                        get_current_question, 
                        get_current_result, 
                        number_of_questions, 
                        get_current_correct_answer,
                        delete_upload_folder)
from processing import processing_upload_files

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
    try:
        # Pobierz klucz API z nagłówka (opcjonalny dla /start, ale zalecany)
        api_key = request.headers.get('X-OpenAI-API-Key')
        
        reset_quiz()
        result = delete_upload_folder()
        if result["status"] == "success":
            return jsonify({
                "message" : "Witaj w quizie! Powodzenia!",
                "rules" : [
                    "Zadawane pytania dotyczą przesłanych przez ciebie materiałów.",
                    "Z podanych odpowiedzi tylko jedna jest prawidłowa.",
                    "Podaj A, B, C lub D.",
                ],
                "status" : "success"
            })
        else:
            return jsonify({"status" : "error", "message": result["message"]}), 500
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


@app.route('/quiz/question')
def quiz_question():
    try:
        # Pobierz klucz API z nagłówka
        api_key = request.headers.get('X-OpenAI-API-Key')
        if not api_key:
            return jsonify({"status": "error", "message": "Brak klucza API OpenAI. Upewnij się, że wprowadziłeś i zapisałeś klucz API na ekranie głównym."}), 400
        
        question = get_quiz_question_with_key(api_key)
        if not question:
            return jsonify({"status": "error", "message": "Błąd podczas generowania pytania. Sprawdź poprawność klucza API."}), 500
            
        return jsonify({
            "question" : question["question"],   
            "number_of_questions" : len(existing_questions),
            "answers" : question["answers"],
            "status" : "success"
        })
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": f"Błąd podczas generowania pytania: {str(e)}"}), 500


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

file_names = []
@app.route('/quiz/upload', methods=['POST'])
def quiz_upload():
    global file_names
    try:   
        if 'file' not in request.files:
            return jsonify({"status" : "error", "message": "Nie załączono pliku"}), 400
        file = request.files['file']  
        if file.filename == '':
            return jsonify({"status" : "error", "message": "Nazwa pliku jest pusta"}), 400
        if not file.filename.endswith(('.csv', '.docx', '.pdf', '.txt')):
            return jsonify({"status" : "error", "message": "Nieprawidłowy typ pliku"}), 400        
        if file.filename in file_names:
            return jsonify({"status" : "error", "message": "Plik o takiej nazwie został już przetworzony"}), 400
        upload_path = Path("upload", file.filename)
        if upload_path.exists():
            return jsonify({"status" : "error", "message": "Plik o takiej nazwie istnieje i czeka na przetworzenie"}), 400
        else:    
            upload_path.parent.mkdir(parents=True, exist_ok=True)
            file.save(upload_path)
            return jsonify({"message": "Plik załadowany pomyślnie i czeka na przetworzenie", "file": file.filename, "status": "success"})
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500  


@app.route('/quiz/processing', methods=['GET'])
def quiz_processing_get():
    data_path = Path("data", "data.txt")
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
    data_path = Path("data", "data.txt")
    try:     
        if request.json['user_decision'] == True:
            return jsonify({"status": "success", "message": "Dotychczasowe dane zostały zachowane"})
        else:
            with data_path.open("w", encoding="utf-8") as open_data_file:
                open_data_file.write("")
            return jsonify({"status": "success", "message": "Dotychczasowe dane zostały usunięte"})
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


@app.route('/quiz/write_data', methods=['POST'])
def quiz_write_data():
    try:
        file_path = Path("upload", request.json['filename'])
        data_file_path = Path("data", "data.txt")
        with data_file_path.open("a", encoding="utf-8") as open_data_file:
            result = processing_upload_files(file_path, open_data_file)
            return jsonify(result)
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500
        

@app.route('/quiz/delete_upload_file', methods=['DELETE'])
def quiz_delete_upload_file():
    global file_names
    try:
        file_path = Path("upload", request.json['filename'])
        file_path.unlink()
        file_names.append(request.json['filename'])
        return jsonify({"status" : "success", "message": "Plik usunięty z folderu upload", "file": request.json['filename']})
    except Exception as e:
        return jsonify({"status" : "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5003, host='localhost')
