# DEPENDENCY MANAGEMENT
# Source of truth: requirements.txt contains ALL project libraries and versions

RULES FOR LIBRARY USAGE:
1. Before generating code with ANY library, check requirements.txt for exact version
2. Use API syntax and features compatible with the installed version from requirements.txt
3. Use modern best practices within the constraints of the installed version
4. This applies to ALL libraries encountered in the project, not just pre-defined ones

IMPORTANT WORKFLOW:
- Step 1: Check if library exists in requirements.txt
- Step 2: If library EXISTS → use syntax for that specific version
- Step 3: If library MISSING → inform user and suggest adding it to requirements.txt

WARNING SYSTEM:
If you need to generate code for a library NOT found in requirements.txt:
1. Stop and inform the user: "Library [name] not found in requirements.txt"
2. Suggest: "Please add [library]==[version] to requirements.txt first"
3. Do not generate code until library is properly added to requirements.txt

VERSION AWARENESS EXAMPLES:
- OpenAI: v0.x uses openai.Completion.create() vs v1.x uses OpenAI().chat.completions.create()
- Pandas: 1.x vs 2.x have different DataFrame methods and deprecations
- SQLAlchemy: 1.4.x vs 2.0.x have completely different syntax
- Flask: 2.x vs 3.x have different jsonify and routing behaviors

# ==========================================
# FLASK BACKEND RULES - OPTIMIZED
# ==========================================

## 🐍 Python Standards

### Code Style
```python
# PEP 8: snake_case, 4 spaces, max 88 chars
user_name = "john"  # ✅
MAX_RETRIES = 3     # ✅ constants

class QuizService:  # ✅ PascalCase
    def generate_quiz(self) -> Dict[str, Any]:  # ✅ type hints
        pass
```

### Imports Order
```python
# 1. Standard library
import os, json, logging
from typing import Dict, List, Optional, Any

# 2. Third-party
from flask import Flask, request, jsonify
import openai

# 3. Local
from services.quiz_service import QuizService
```

### Error Handling
```python
# Always use specific exceptions and logging
try:
    result = process_data(data)
    logger.info("Success")
    return result
except ValueError as e:
    logger.error(f"Validation error: {e}")
    raise
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

## 🌐 Flask Patterns

### Route Structure
```python
@app.route('/api/quiz/generate', methods=['POST'])
def generate_quiz() -> Dict[str, Any]:
    """Generate quiz from user input."""
    try:
        # 1. Get and validate input
        data = request.get_json()
        if not data or 'topic' not in data:
            return jsonify({'error': 'Topic required'}), 400
        
        # 2. Business logic (delegate to service)
        quiz_service = QuizService()
        result = quiz_service.generate_quiz(**data)
        
        # 3. Return response
        return jsonify({'success': True, 'quiz': result}), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({'error': 'Internal error'}), 500
```

### Data Models
```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Question:
    question: str
    options: List[str]
    correct_answer: str
    explanation: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
```

### Services (Business Logic)
```python
class QuizService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
    
    def generate_quiz(self, topic: str, difficulty: str = "medium", 
                     num_questions: int = 5) -> Dict[str, Any]:
        """Generate quiz with validation."""
        # Validate inputs
        self._validate_params(topic, difficulty, num_questions)
        
        # Generate using AI
        ai_service = AIService()
        questions = ai_service.generate_questions(topic, difficulty, num_questions)
        
        return Quiz(topic, difficulty, questions).to_dict()
    
    def _validate_params(self, topic: str, difficulty: str, num_questions: int) -> None:
        if not topic.strip():
            raise ValueError("Topic cannot be empty")
        if difficulty not in ['easy', 'medium', 'hard']:
            raise ValueError("Invalid difficulty")
        if not 1 <= num_questions <= 20:
            raise ValueError("Questions must be 1-20")
```

## 📁 Simple Structure
```
backend/
├── app.py              # Flask app
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── .env                # Environment variables (add to .gitignore)
├── cursorrules.md
├── uploads/

```

## 🔐 SECURITY & ENVIRONMENT

### Environment Variables (.env)
```python
# Always use environment variables for secrets
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment")

# Config class
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
```

### Input Validation & Sanitization
```python
from flask import request
import re

def validate_topic(topic: str) -> str:
    """Validate and sanitize topic input."""
    if not topic or not topic.strip():
        raise ValueError("Topic is required")
    
    # Remove dangerous characters
    topic = re.sub(r'[<>"\']', '', topic.strip())
    
    if len(topic) > 100:
        raise ValueError("Topic too long (max 100 chars)")
    
    return topic
```

## 🚀 PERFORMANCE & CACHING

### Simple In-Memory Cache
```python
from functools import lru_cache
import time

class CacheService:
    def __init__(self):
        self._cache = {}
        self._timestamps = {}
        self.ttl = 300  # 5 minutes
    
    def get(self, key: str) -> Optional[Any]:
        if key in self._cache:
            if time.time() - self._timestamps[key] < self.ttl:
                return self._cache[key]
            else:
                del self._cache[key]
                del self._timestamps[key]
        return None
    
    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value
        self._timestamps[key] = time.time()
```

## 📊 LOGGING SETUP

### Proper Logging Configuration
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    if not app.debug:
        # File handler
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        
        app.logger.setLevel(logging.INFO)
        app.logger.info('Application startup')
```

## 🧪 TESTING PATTERNS

### Unit Test Structure
```python
import unittest
from unittest.mock import patch, MagicMock

class TestQuizService(unittest.TestCase):
    def setUp(self):
        self.quiz_service = QuizService()
    
    def test_generate_quiz_valid_input(self):
        result = self.quiz_service.generate_quiz("Python", "easy", 3)
        self.assertIn('questions', result)
        self.assertEqual(len(result['questions']), 3)
    
    def test_generate_quiz_invalid_topic(self):
        with self.assertRaises(ValueError):
            self.quiz_service.generate_quiz("", "easy", 3)
```

## ✅ KEY RULES - ENHANCED
- **Always use type hints**: `def func(x: str) -> Dict[str, Any]:`
- **Validate all inputs**: Check required fields, types, ranges, sanitize
- **Delegate business logic**: Routes → Services → Models
- **Handle errors properly**: Specific exceptions + logging
- **Use dataclasses**: For simple data containers
- **Log important events**: Success, errors, warnings
- **Follow naming**: snake_case functions, PascalCase classes
- **Environment variables**: Never hardcode secrets or config
- **Add __init__.py**: To all Python packages
- **Cache expensive operations**: AI calls, database queries
- **Sanitize user input**: Remove dangerous characters
- **Use proper HTTP status codes**: 200, 400, 401, 404, 500
- **Keep it simple**: Start basic, add complexity gradually

## 🧪 Quick Test
```bash
# Test your endpoints
curl -X POST http://localhost:5000/api/quiz/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "Python", "difficulty": "medium", "num_questions": 3}'
```

## 🚨 CRITICAL REMINDERS
- Check requirements.txt FIRST before using any library
- Never commit .env files (add to .gitignore)
- Always validate and sanitize user input
- Use proper error handling and logging
- Test your endpoints manually and with unit tests
- Use environment variables for all configuration

**Remember**: Security first, validate everything, log errors, use services for logic!