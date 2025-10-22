import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from prompts import get_prompt


load_dotenv()

existing_questions = []

prompt = get_prompt("quiz_prompt")


def openai_key_test():
    try:
        openai_key = os.getenv('OPENAI_API_KEY')
        if not openai_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        return ("OPENAI_API_KEY exists")
    except Exception as e:
        raise ValueError(f"Error getting OPENAI_API_KEY: {e}")


def user_path_data():
    folder_path = os.path.join("Backend", "download", "data.txt")
    if not os.path.exists(folder_path):
        print(f"Path to data.txt not found: {folder_path}")
        exit()
    try:
        with open(folder_path, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("data.txt is empty")
        return content
    except Exception as e:
        raise ValueError(f"Error reading data.txt: {e}")


def get_ai_answers(content):
    try:
        # Ustawienie klucza API
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"{prompt}\n\n avoid this questions: {existing_questions}"},
                {"role": "user", "content": content}
            ]
        )
        ai_answers = response.choices[0].message.content
        ai_answers = json.loads(ai_answers)

        if not ai_answers:
            raise ValueError("AI answers are empty")

        expected_keys = ["question", "answers", "correct_answer"]
        for key in expected_keys:
            if key not in ai_answers:
                raise ValueError(f"Invalid key: {key}")
        
        return ai_answers
    except json.JSONDecodeError:
        raise ValueError("AI answers are not in JSON format")
    except Exception as e:
        raise ValueError(f"Error getting AI answers: {e}")


score = 0
number_of_questions = 1
def main():
    global score, number_of_questions
    try:
        content = user_path_data()
        quiz_data = get_ai_answers(content)
        print(f'Pytanie {number_of_questions}: {quiz_data["question"]}')
        print("Odpowiedzi:")
        for key, value in quiz_data["answers"].items():
            print(f'{key}. {value}')
        number_of_questions += 1
        user_answer = input("Podaj odpowiedź: ")
        if user_answer == "":
            print("Brak odpowiedzi użytkownika!")
            # return   
        if user_answer == "q":
            print(f"Twój wynik: to {score} pkt z {len(existing_questions)} pytań")
            exit()
        existing_questions.append(quiz_data["question"])
        if user_answer.upper() == quiz_data["correct_answer"].upper():
            score += 1
            print("Odpowiedź poprawna!")
        else:
            print("Odpowiedź niepoprawna!")
            print(f"Poprawna odpowiedź: {quiz_data['correct_answer']}")  
        print(f"Twój aktualny wynik: to {score} pkt z {len(existing_questions)} pytań") 
        print("-" * 70)
    except Exception as e:
        print(f"Error: {e}")


def start_quiz():
    global score
    global number_of_questions
    score = 0
    number_of_questions = 1
    existing_questions.clear()
    welcome_message = 'Witaj w quizie! Powodzenia!'
    print(welcome_message)   
    print("-" * 50)
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print(f"Twój wynik: {score}/{len(existing_questions)}")
            exit()
        except Exception as e:
            print(f"Error: {e}")
            print("-" * 50)
            continue


current_question = None
current_answers = None
current_correct_answer = None


def get_quiz_question():
    global number_of_questions, current_question, current_answers, current_correct_answer
    # print(f'DEBUG: przed procesowaniem {number_of_questions}')  
    try:
        content = user_path_data()
        quiz_data = get_ai_answers(content)
        existing_questions.append(quiz_data["question"])
        current_question = quiz_data["question"]
        current_answers = quiz_data["answers"]
        current_correct_answer = quiz_data["correct_answer"]
        # print(f'DEBUG: po procesowaniu {number_of_questions}')
        return quiz_data
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_current_question():
    global current_question
    return current_question if current_question else "Brak pytania"


def get_current_number_of_questions():
    global number_of_questions
    return number_of_questions


def get_current_answers():
    global current_answers
    return current_answers if current_answers else "Brak odpowiedzi"


def get_current_correct_answer():
    global current_correct_answer
    return current_correct_answer if current_correct_answer else "Brak poprawnej odpowiedzi"
 

def check_answer(user_answer, correct_answer):
    global score, current_correct_answer
    try:
        is_correct = user_answer.upper() == correct_answer.upper()
        if is_correct:
            score += 1

        return{
            'is_correct': is_correct,
            'correct_answer': current_correct_answer,
            'message': "Odpowiedź poprawna!" if is_correct else "Odpowiedź niepoprawna!",
            'score': score,
            }
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_current_result():
    current_result = {
    "Zdobyte punkty" : score,
    "Liczba pytań" : len(existing_questions)
    }
    return current_result


def quit_quiz():
    quit_result = {
        "message" : "Dziękujemy za udział w quizie!",
        "user_result" : f"Twój wynik: {score} pkt z {len(existing_questions)} pytań",
        "exit" : True
    }
    reset_quiz()
    return quit_result

def reset_quiz():
    global score, number_of_questions, existing_questions
    score = 0
    number_of_questions = 1
    existing_questions.clear()    
    return True



if __name__ == "__main__":


#     print('==Test user_path_check==')
#     print('-' * 50)

#     current_dir = os.getcwd()
#     dowland_path = os.path.join(current_dir, "download")
#     data_path = os.path.join(dowland_path, "data.txt")

#     print(f'Download path: {os.path.exists(dowland_path)}')
#     print(f'Data path: {os.path.exists(data_path)}')
#     print('-' * 50)



#     print('==Test get_quiz_question==')
#     print('-' * 50)

#     result = get_quiz_question()
#     if result:
#         print('Success ! File exists!')
#         print(f'Type of result: {type(result)}')
#         print(f'Result: {result}')
#         if isinstance(result, dict):
#             print('Result is a JSON object')
#             important_keys = ['question', 'answers', 'correct_answer']
#             for key in important_keys:
#                 if key in result:
#                     print(f'{key}: {result[key]}')
#                 else:
#                     print(f'Key {key} not found in result')
#         else:
#             print('Result is not a JSON object')
#     else:
#         if result is None:
#             print('Error: Result is None')


#     print('==Test check_answer==')
#     print('-' * 50)
#     print(f'Score: {score}')
#     print("-" * 50)
#     print(check_answer("A", "A"))
#     print("Odpowiedź prawidłowa!")
#     print("-" * 50)
#     print(check_answer("a", "A"))
#     print("Odpowiedź prawidłowa!")
#     print("-" * 50)
#     print(check_answer("B", "A"))
#     print("Odpowiedź nieprawidłowa!")
#     print("-" * 50)
#     print(check_answer("", "A"))
#     print(" Error2: Brak odpowiedzi użytkownika!")
#     print("-" * 50)




