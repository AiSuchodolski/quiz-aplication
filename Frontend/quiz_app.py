import streamlit as st
import requests
import time
import json

# Konfiguracja
API_BASE = 'http://localhost:5003'

# Inicjalizacja session state
if 'quiz_state' not in st.session_state:
  st.session_state.quiz_state = 'welcome'
if 'current_question' not in st.session_state:
  st.session_state.current_question = None
if 'question_number' not in st.session_state:
  st.session_state.question_number = 1
if 'score' not in st.session_state:
  st.session_state.score = 0
if 'answered_questions' not in st.session_state:
  st.session_state.answered_questions = 0
if 'selected_answer' not in st.session_state:
  st.session_state.selected_answer = None
if 'answer_submitted' not in st.session_state:
  st.session_state.answer_submitted = False
if 'correct_answer' not in st.session_state:
  st.session_state.correct_answer = None
if 'show_result' not in st.session_state:
  st.session_state.show_result = False

# Konfiguracja strony
st.set_page_config(
  page_title="🧠 Quiz App",
  page_icon="🧠",
  layout="centered",
  initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
  .main-header {
      text-align: center;
      color: #667eea;
      font-size: 3rem;
      font-weight: bold;
      margin-bottom: 1rem;
  }
  
  .subtitle {
      text-align: center;
      color: #666;
      font-size: 1.2rem;
      margin-bottom: 2rem;
  }
  
  .question-header {
      background: #f8f9ff;
      padding: 1.5rem;
      border-radius: 10px;
      border-left: 5px solid #667eea;
      margin-bottom: 1.5rem;
  }
  
  .question-number {
      color: #667eea;
      font-weight: bold;
      font-size: 1rem;
      margin-bottom: 0.5rem;
  }
  
  .question-text {
      font-size: 1.3rem;
      color: #333;
      line-height: 1.6;
  }
  
  .score-display {
      background: #f8f9ff;
      padding: 1rem;
      border-radius: 10px;
      border: 2px solid #667eea;
      text-align: center;
      margin: 1rem 0;
  }
  
  .score-number {
      font-size: 2rem;
      font-weight: bold;
      color: #667eea;
  }
  
  .correct-answer {
      background-color: #d4edda !important;
      border: 2px solid #28a745 !important;
      color: #155724 !important;
  }
  
  .incorrect-answer {
      background-color: #f8d7da !important;
      border: 2px solid #dc3545 !important;
      color: #721c24 !important;
  }
  
  .answer-button {
      width: 100%;
      margin: 0.5rem 0;
      padding: 1rem;
      text-align: left;
      border-radius: 10px;
  }
</style>
""", unsafe_allow_html=True)

def make_api_request(endpoint, method='GET', data=None):
  """Wykonaj zapytanie do API"""
  try:
      url = f"{API_BASE}{endpoint}"
      if method == 'GET':
          response = requests.get(url)
      elif method == 'POST':
          response = requests.post(url, json=data)
      
      if response.status_code == 200:
          return response.json()
      else:
          st.error(f"Błąd API: {response.status_code}")
          return None
  except requests.exceptions.ConnectionError:
      st.error("🔌 Nie można połączyć się z serwerem! Upewnij się, że backend działa na porcie 5003.")
      return None
  except Exception as e:
      st.error(f"Błąd: {str(e)}")
      return None

def start_quiz():
  """Rozpocznij quiz"""
  data = make_api_request('/quiz/start')
  if data and data.get('status') == 'success':
      st.session_state.quiz_state = 'rules'
      st.session_state.rules = data.get('rules', [])
      st.success(data.get('message', 'Quiz rozpoczęty!'))
      st.rerun()

def load_question():
  """Załaduj pytanie"""
  data = make_api_request('/quiz/question')
  if data and data.get('status') == 'success':
      st.session_state.current_question = data
      st.session_state.correct_answer = data.get('correct_answer', '').upper()
      st.session_state.selected_answer = None
      st.session_state.answer_submitted = False
      st.session_state.show_result = False
      st.session_state.quiz_state = 'question'
      st.rerun()

def submit_answer(answer):
  """Prześlij odpowiedź"""
  if st.session_state.answer_submitted:
      return
      
  st.session_state.selected_answer = answer
  st.session_state.answer_submitted = True
  
  data = make_api_request('/quiz/answer', 'POST', {'user_answer': answer})
  if data and 'is_correct' in data:
      st.session_state.answered_questions += 1
      if data['is_correct']:
          st.session_state.score += 1
      st.session_state.show_result = True
      st.session_state.last_result = data
      st.rerun()

def next_question():
  """Przejdź do następnego pytania"""
  st.session_state.question_number += 1
  load_question()

def quit_quiz():
  """Zakończ quiz"""
  st.session_state.quiz_state = 'final_result'
  st.rerun()

def restart_quiz():
  """Restart quiz"""
  for key in ['current_question', 'question_number', 'score', 'answered_questions', 
              'selected_answer', 'answer_submitted', 'correct_answer', 'show_result']:
      if key in st.session_state:
          del st.session_state[key]
  st.session_state.quiz_state = 'welcome'
  st.session_state.question_number = 1
  st.session_state.score = 0
  st.session_state.answered_questions = 0
  st.rerun()

# GŁÓWNA LOGIKA APLIKACJI

if st.session_state.quiz_state == 'welcome':
  # EKRAN POWITALNY
  st.markdown('<div class="main-header">🧠 QUIZ APP</div>', unsafe_allow_html=True)
  st.markdown('<div class="subtitle">Sprawdź swoją wiedzę na podstawie przesłanych materiałów!</div>', unsafe_allow_html=True)
  
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
      if st.button("🚀 Rozpocznij Quiz", use_container_width=True, type="primary"):
          start_quiz()

elif st.session_state.quiz_state == 'rules':
  # EKRAN ZASAD
  st.markdown('<div class="main-header">📋 ZASADY QUIZU</div>', unsafe_allow_html=True)
  
  st.markdown("### Jak grać:")
  rules = st.session_state.get('rules', [])
  for rule in rules:
      # Pomiń zasady o klawiszu 'q'
      if not any(phrase in rule.lower() for phrase in ['naciśnij q', 'wciśnij q', 'klawisz q']):
          st.markdown(f"• {rule}")
  
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
      if st.button("🎯 Zacznij quiz!", use_container_width=True, type="primary"):
          load_question()

elif st.session_state.quiz_state == 'question':
  # EKRAN PYTANIA
  question_data = st.session_state.current_question
  
  if question_data:
      # Nagłówek pytania
      st.markdown(f"""
      <div class="question-header">
          <div class="question-number">Pytanie {st.session_state.question_number}</div>
          <div class="question-text">{question_data['question']}</div>
      </div>
      """, unsafe_allow_html=True)
      
      # Wynik
      st.markdown(f"""
      <div class="score-display">
          <div>Aktualny wynik:</div>
          <div class="score-number">{st.session_state.score} / {st.session_state.answered_questions}</div>
      </div>
      """, unsafe_allow_html=True)
      
      # Odpowiedzi
      answers = question_data.get('answers', {})
      
      if not st.session_state.answer_submitted:
          st.markdown("### Wybierz odpowiedź:")
          for letter, text in answers.items():
              if st.button(f"**{letter})** {text}", key=f"answer_{letter}", use_container_width=True):
                  submit_answer(letter)
      else:
          # Pokaż rezultat
          st.markdown("### Twoja odpowiedź:")
          
          for letter, text in answers.items():
              button_class = ""
              emoji = ""
              
              if letter == st.session_state.selected_answer:
                  if st.session_state.last_result['is_correct']:
                      button_class = "correct-answer"
                      emoji = "✅"
                  else:
                      button_class = "incorrect-answer"
                      emoji = "❌"
              elif letter == st.session_state.correct_answer and not st.session_state.last_result['is_correct']:
                  button_class = "correct-answer"
                  emoji = "✅"
              
              if button_class:
                  st.markdown(f"""
                  <div class="{button_class}" style="padding: 1rem; margin: 0.5rem 0; border-radius: 10px;">
                      {emoji} <strong>{letter})</strong> {text}
                  </div>
                  """, unsafe_allow_html=True)
              else:
                  st.markdown(f"**{letter})** {text}")
          
          # Komunikat o wyniku
          if st.session_state.last_result['is_correct']:
              st.success("🎉 Prawidłowa odpowiedź!")
          else:
              st.error("❌ Nieprawidłowa odpowiedź!")
              if st.session_state.correct_answer:
                  st.info(f"Prawidłowa odpowiedź to: **{st.session_state.correct_answer}**")
          
          # Timer i przyciski
          st.markdown("---")
          col1, col2 = st.columns(2)
          
          with col1:
              if st.button("➡️ Następne pytanie", type="primary", use_container_width=True):
                  next_question()
          
          with col2:
              if st.button("🛑 Zakończ quiz", use_container_width=True):
                  quit_quiz()

elif st.session_state.quiz_state == 'final_result':
  # EKRAN KOŃCOWEGO WYNIKU
  st.markdown('<div class="main-header">🎉 KONIEC QUIZU!</div>', unsafe_allow_html=True)
  
  score = st.session_state.score
  total = st.session_state.answered_questions
  percentage = round((score / total) * 100) if total > 0 else 0
  
  st.markdown(f"""
  <div class="score-display">
      <div>Twój końcowy wynik:</div>
      <div class="score-number">{score} / {total}</div>
      <div style="font-size: 1.5rem; color: #667eea; margin-top: 0.5rem;">{percentage}%</div>
  </div>
  """, unsafe_allow_html=True)
  
  # Komunikat na podstawie wyniku
  if total == 0:
      message = '🤔 Nie odpowiedziałeś na żadne pytanie!'
  elif percentage >= 80:
      message = '🎉 Świetny wynik! Gratulacje!'
  elif percentage >= 60:
      message = '👍 Dobry wynik! Można lepiej!'
  elif percentage >= 40:
      message = '📚 Trzeba jeszcze popracować!'
  else:
      message = '💪 Nie poddawaj się! Spróbuj ponownie!'
  
  st.markdown(f'<div class="subtitle">{message}</div>', unsafe_allow_html=True)
  
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
      if st.button("🔄 Rozpocznij ponownie", use_container_width=True, type="primary"):
          restart_quiz()

# Sidebar z informacjami
with st.sidebar:
  st.markdown("### 🧠 Quiz App")
  st.markdown("**Status:** " + st.session_state.quiz_state.replace('_', ' ').title())
  
  if st.session_state.quiz_state in ['question', 'final_result']:
      st.markdown(f"**Pytanie:** {st.session_state.question_number}")
      st.markdown(f"**Wynik:** {st.session_state.score}/{st.session_state.answered_questions}")
  
  st.markdown("---")
  st.markdown("**Backend:** http://localhost:5003")
  
  if st.button("🔄 Reset aplikacji"):
      restart_quiz()