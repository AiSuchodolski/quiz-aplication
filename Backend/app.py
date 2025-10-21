from flask import Flask, jsonify, request
from flask_cors import CORS
from quiz_main import (existing_questions, 
                        reset_quiz, 
                        get_quiz_question, 
                        check_answer, 
                        get_current_question, 
                        get_current_result, 
                        number_of_questions, 
                        get_current_correct_answer,
                        get_current_answers,
                        get_current_number_of_questions)

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
            "Wpisz 'q' aby zakończyć quiz"
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
        return jsonify({"error": str(e)}), 500


@app.route('/quiz/result')
def quiz_result():
    result = get_current_result()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5003, host='localhost')
