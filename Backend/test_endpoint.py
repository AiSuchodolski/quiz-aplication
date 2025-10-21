#!/usr/bin/env python3
"""
Test script for the quiz generation endpoint.
Run this after starting the Flask app to test the functionality.
"""

import requests
import json

def test_quiz_generation():
    """Test the /api/generate-quiz endpoint."""
    
    # Test data
    test_material = """
    Python is a high-level, interpreted programming language known for its simplicity and readability.
    It was created by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms,
    including procedural, object-oriented, and functional programming. Key features include dynamic typing,
    automatic memory management, and a large standard library. Python is widely used in web development,
    data science, artificial intelligence, and automation.
    """
    
    payload = {
        "material": test_material,
        "num_questions": 3
    }
    
    try:
        # Make request to the endpoint
        response = requests.post(
            'http://localhost:5000/api/generate-quiz',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(payload)
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\nQuiz generated successfully!")
            quiz_data = response.json()['quiz']
            print(f"Generated {len(quiz_data['questions'])} questions")
            
            # Display questions
            for i, question in enumerate(quiz_data['questions'], 1):
                print(f"\nQuestion {i}: {question['question']}")
                for j, option in enumerate(question['options'], 1):
                    print(f"  {chr(64+j)}. {option}")
                print(f"Correct Answer: {question['correct_answer']}")
                print(f"Explanation: {question['explanation']}")
        else:
            print("Error generating quiz")
            
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Make sure the Flask app is running on http://localhost:5000")
    except Exception as e:
        print(f"Error: {e}")

def test_health_endpoint():
    """Test the health check endpoint."""
    try:
        response = requests.get('http://localhost:5000/health')
        print(f"Health Check Status: {response.status_code}")
        print(f"Health Check Response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")

if __name__ == "__main__":
    print("Testing Quiz API Endpoints")
    print("=" * 50)
    
    print("\n1. Testing Health Endpoint:")
    test_health_endpoint()
    
    print("\n2. Testing Quiz Generation:")
    test_quiz_generation()
