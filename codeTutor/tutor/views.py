# views.py
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from openai import OpenAI
from dotenv import load_dotenv
from django.shortcuts import render
import re

load_dotenv()

# Configure OpenAI with new API
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


@csrf_exempt
def home(request):
    return render(request, 'coder.html')


@csrf_exempt
@require_POST
def analyze_code(request):
    """
    Analyze code using OpenAI API with detailed error explanations, corrected code, and learning features
    """
    try:
        # Parse JSON data
        data = json.loads(request.body)
        code = data.get('code', '').strip()
        language = data.get('language', 'python').lower()
        
        if not code:
            return JsonResponse({
                'error': 'No code provided'
            }, status=400)
        
        # Prepare the prompt for OpenAI with enhanced analysis requirements
        prompt = f"""
        You are an expert {language} code analyzer and educator. Analyze the following code thoroughly and provide:
        
        1. All syntax errors
        2. All logical errors  
        3. All warnings about best practices
        4. Performance issues
        5. Security vulnerabilities
        6. Style and readability issues
        
        For EACH issue found, provide:
        - Error Type: The type/category of error
        - Category: One of: "syntax", "logic", "performance", "security", "best_practice", "style"
        - Title: A brief title describing the issue
        - What the error is: Detailed explanation of what's wrong
        - Why it occurred: Explanation of why this error happens
        - How to correct it: Step-by-step guidance on fixing it
        - Line Number: Where the error occurs (if applicable)
        - Column Number: Where the error occurs (if applicable)
        - Code Snippet: The problematic code
        - Severity: "low", "medium", "high", or "critical"
        
        IMPORTANT ADDITIONAL REQUIREMENTS:
        
        A) CONCEPT MAP: 
        Create a concept map that groups issues by their root concepts. For example:
        - **Syntax**: Indentation, Missing Parentheses, Missing Colons, etc.
        - **Logic**: Type Errors, None Handling, Loop Issues, etc.
        - **Performance**: Inefficient Algorithms, Unnecessary Computation, etc.
        - **Security**: Input Validation, SQL Injection, etc.
        
        For each concept category, show how many issues belong to it (like: Indentation (3), Missing Parentheses (2), etc.)
        
        B) PROGRESSIVE HINTS:
        For each significant error, provide 3 levels of hints:
        - Level 1: Gentle Nudge (subtle hint without giving away the solution)
        - Level 2: Partial Clue (more specific hint pointing towards solution)
        - Level 3: Full Solution (explicit solution and explanation)
        
        C) CORRECTION STRATEGIES:
        For common error patterns, provide multiple correction strategies with:
        - Strategy Name
        - Code implementation
        - Pros of this approach
        - Cons of this approach
        
        After analyzing all issues, provide:
        - A fully corrected version of the entire code
        - General suggestions for improvement
        - Best practices to follow
        
        Code to analyze:
        ```
        {code}
        ```
        
        Return the analysis in the following JSON format:
        {{
            "analysis_summary": {{
                "total_errors": number,
                "total_warnings": number,
                "overall_severity": "low/medium/high/critical",
                "language": "{language}",
                "concepts_covered": ["concept1", "concept2", ...]
            }},
            "concept_map": {{
                "syntax": [
                    {{"concept": "Indentation", "count": 3, "issues": [1, 2, 3]}},
                    {{"concept": "Missing Parentheses", "count": 2, "issues": [4, 5]}}
                ],
                "logic": [
                    {{"concept": "Type Errors", "count": 1, "issues": [6]}}
                ]
            }},
            "issues": [
                {{
                    "id": 1,
                    "type": "error/warning",
                    "category": "syntax/logic/performance/security/best_practice/style",
                    "title": "Issue title",
                    "description": "What the error is",
                    "cause": "Why it occurred",
                    "fix": "How to correct it",
                    "line": line_number,
                    "column": column_number,
                    "code_snippet": "problematic code",
                    "severity": "low/medium/high/critical",
                    "hints": {{
                        "level1": "Gentle nudge hint",
                        "level2": "Partial clue hint",
                        "level3": "Full solution explanation"
                    }}
                }}
            ],
            "correction_strategies": [
                {{
                    "name": "Strategy Name",
                    "description": "Brief description",
                    "code": "Code implementation",
                    "pros": ["Pro 1", "Pro 2"],
                    "cons": ["Con 1", "Con 2"],
                    "applicable_to_issues": [1, 2, 3]
                }}
            ],
            "corrected_code": "The fully corrected version of the code",
            "suggestions": [
                "General suggestions for improvement"
            ],
            "best_practices": [
                "Best practices to follow"
            ]
        }}
        
        Important guidelines:
        1. Be extremely thorough and detailed in your analysis
        2. Don't miss any potential issues
        3. Provide practical, actionable fixes
        4. The corrected code should be production-ready
        5. Explain concepts clearly for learning purposes
        6. If no issues are found, return empty arrays but still provide corrected code
        7. Only return the JSON object, no other text
        8. For the concept map, group similar issues under appropriate concepts
        9. Hints should be educational and progressive
        10. Correction strategies should show different approaches to solving problems
        """
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are an expert {language} developer and educator. You analyze code thoroughly, explain issues clearly, provide educational hints, and show multiple correction strategies."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=6000  # Increased for detailed analysis with new features
        )
        
        # Parse the response
        analysis_text = response.choices[0].message.content.strip()
        
        # Try to extract JSON from the response
        try:
            # Find JSON in the response
            start_idx = analysis_text.find('{')
            end_idx = analysis_text.rfind('}') + 1
            if start_idx != -1 and end_idx != 0:
                analysis_json = json.loads(analysis_text[start_idx:end_idx])
            else:
                analysis_json = json.loads(analysis_text)
            
            # Transform the response to match frontend expectations
            transformed_response = transform_response_for_frontend(analysis_json)
            
            return JsonResponse(transformed_response)
            
        except json.JSONDecodeError as e:
            # Log the error and the response for debugging
            print(f"JSON Decode Error: {e}")
            print(f"Raw response: {analysis_text[:500]}")
            
            # Try to clean the response and parse again
            try:
                # Remove markdown code blocks if present
                cleaned_text = analysis_text.replace('```json', '').replace('```', '')
                analysis_json = json.loads(cleaned_text)
                transformed_response = transform_response_for_frontend(analysis_json)
                return JsonResponse(transformed_response)
            except:
                # Return a helpful error
                return JsonResponse({
                    'error': 'Could not parse analysis results. Please try again.',
                    'raw_response': analysis_text[:500]
                }, status=500)
            
    except Exception as e:
        import traceback
        print(f"Error: {e}")
        print(traceback.format_exc())
        
        # Check for specific OpenAI errors
        error_msg = str(e)
        if "authentication" in error_msg.lower() or "api key" in error_msg.lower():
            return JsonResponse({
                'error': 'OpenAI API authentication failed. Please check your API key.'
            }, status=500)
        elif "rate limit" in error_msg.lower():
            return JsonResponse({
                'error': 'OpenAI API rate limit exceeded. Please try again later.'
            }, status=429)
        elif "openai" in error_msg.lower():
            return JsonResponse({
                'error': f'OpenAI API error: {error_msg}'
            }, status=500)
        else:
            return JsonResponse({
                'error': f'Server error: {error_msg}'
            }, status=500)


def transform_response_for_frontend(analysis_json):
    """
    Transform the detailed analysis response to match frontend expectations
    with new features
    """
    # Separate errors and warnings for frontend
    errors = []
    warnings = []
    
    for issue in analysis_json.get('issues', []):
        issue_type = issue.get('type', '').lower()
        
        issue_data = {
            'id': issue.get('id', len(errors) + len(warnings) + 1),
            'type': issue.get('category', ''),
            'title': issue.get('title', ''),
            'description': issue.get('description', ''),
            'cause': issue.get('cause', ''),
            'fix': issue.get('fix', ''),
            'line': issue.get('line'),
            'column': issue.get('column'),
            'code': issue.get('code_snippet', ''),
            'severity': issue.get('severity', 'medium'),
            'hints': issue.get('hints', {
                'level1': 'Try examining the syntax more carefully.',
                'level2': 'Check for common syntax patterns.',
                'level3': 'Here\'s the complete solution.'
            })
        }
        
        if issue_type == 'error':
            errors.append(issue_data)
        else:  # warning or other
            warnings.append(issue_data)
    
    # Build concept map for frontend
    concept_map = []
    if 'concept_map' in analysis_json:
        for category, concepts in analysis_json['concept_map'].items():
            for concept in concepts:
                concept_map.append({
                    'category': category,
                    'concept': concept.get('concept', ''),
                    'count': concept.get('count', 0),
                    'issues': concept.get('issues', [])
                })
    
    # Prepare the final response
    response = {
        'analysis_summary': analysis_json.get('analysis_summary', {}),
        'concept_map': concept_map,
        'errors': errors,
        'warnings': warnings,
        'correction_strategies': analysis_json.get('correction_strategies', []),
        'corrected_code': analysis_json.get('corrected_code', ''),
        'suggestions': analysis_json.get('suggestions', []),
        'best_practices': analysis_json.get('best_practices', [])
    }
    
    return response


@csrf_exempt
@require_POST
def get_hint(request):
    """
    Get progressive hints for a specific issue
    """
    print("=== GET HINT ENDPOINT CALLED ===")
    try:
        data = json.loads(request.body)
        code = data.get('code', '').strip()
        issue_id = data.get('issue_id')
        hint_level = data.get('level', 1)  # 1, 2, or 3
        language = data.get('language', 'python').lower()
        
        if not code or not issue_id:
            return JsonResponse({
                'error': 'Code and issue_id are required'
            }, status=400)
        
        prompt = f"""
        For the following {language} code, provide a hint for issue #{issue_id} at level {hint_level}.
        
        Code:
        ```
        {code}
        ```
        
        Hint levels:
        - Level 1: Gentle nudge (subtle hint without giving away solution)
        - Level 2: Partial clue (more specific hint pointing towards solution)
        - Level 3: Full solution (explicit solution and explanation)
        
        Return ONLY the hint text for level {hint_level}, nothing else.
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a helpful coding tutor providing progressive hints for {language}."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300
        )
        
        hint = response.choices[0].message.content.strip()
        
        return JsonResponse({
            'hint': hint,
            'level': hint_level,
            'issue_id': issue_id
        })
        
    except Exception as e:
        return JsonResponse({
            'error': f'Error getting hint: {str(e)}'
        }, status=500)


@csrf_exempt
@require_POST
def get_correction_strategy(request):
    """
    Get detailed correction strategy for a specific issue or pattern
    """
    try:
        data = json.loads(request.body)
        code = data.get('code', '').strip()
        issue_type = data.get('issue_type', '')
        language = data.get('language', 'python').lower()
        
        if not code:
            return JsonResponse({
                'error': 'Code is required'
            }, status=400)
        
        prompt = f"""
        For the following {language} code issue: "{issue_type}", provide multiple correction strategies.
        
        Code:
        ```
        {code}
        ```
        
        For each strategy, provide:
        1. Strategy name
        2. Brief description
        3. Code implementation
        4. Pros of this approach
        5. Cons of this approach
        
        Return in this JSON format:
        {{
            "strategies": [
                {{
                    "name": "Strategy Name",
                    "description": "Brief description",
                    "code": "Code implementation",
                    "pros": ["Pro 1", "Pro 2"],
                    "cons": ["Con 1", "Con 2"]
                }}
            ]
        }}
        
        Only return the JSON object.
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You provide multiple solutions to coding problems with pros and cons."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        strategy_text = response.choices[0].message.content.strip()
        
        # Parse JSON response
        start_idx = strategy_text.find('{')
        end_idx = strategy_text.rfind('}') + 1
        if start_idx != -1 and end_idx != 0:
            strategies_json = json.loads(strategy_text[start_idx:end_idx])
        else:
            strategies_json = json.loads(strategy_text)
        
        return JsonResponse(strategies_json)
        
    except Exception as e:
        return JsonResponse({
            'error': f'Error getting correction strategy: {str(e)}'
        }, status=500)


@csrf_exempt
@require_POST
def get_corrected_code(request):
    """
    Get only the corrected code without full analysis
    """
    try:
        data = json.loads(request.body)
        code = data.get('code', '').strip()
        language = data.get('language', 'python').lower()
        
        if not code:
            return JsonResponse({
                'error': 'No code provided'
            }, status=400)
        
        prompt = f"""
        Correct this {language} code. Fix all errors and improve it following best practices.
        Return ONLY the corrected code, no explanations.
        
        Code to correct:
        ```
        {code}
        ```
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a code corrector. Return only corrected code, no explanations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            max_tokens=2000
        )
        
        corrected_code = response.choices[0].message.content.strip()
        
        # Clean up the response
        corrected_code = corrected_code.replace('```python\n', '').replace('```javascript\n', '').replace('```java\n', '').replace('```cpp\n', '').replace('```\n', '').replace('```', '')
        
        return JsonResponse({
            'corrected_code': corrected_code
        })
        
    except Exception as e:
        return JsonResponse({
            'error': f'Error: {str(e)}'
        }, status=500)


@csrf_exempt
@require_POST
def analyze_code_mock(request):
    """
    Mock analysis for testing without OpenAI API
    """
    try:
        data = json.loads(request.body)
        code = data.get('code', '').strip()
        language = data.get('language', 'python').lower()
        
        if not code:
            return JsonResponse({
                'error': 'No code provided'
            }, status=400)
        
        # Enhanced mock response with new features
        mock_response = {
            'analysis_summary': {
                'total_errors': 5,
                'total_warnings': 0,
                'overall_severity': 'high',
                'language': language,
                'concepts_covered': ['Syntax', 'Indentation', 'Missing Operators']
            },
            'concept_map': [
                {'category': 'syntax', 'concept': 'Indentation', 'count': 3, 'issues': [1, 2, 3]},
                {'category': 'syntax', 'concept': 'Missing Colon', 'count': 1, 'issues': [4]},
                {'category': 'syntax', 'concept': 'Incomplete Comparison', 'count': 1, 'issues': [5]}
            ],
            'errors': [
                {
                    'id': 1,
                    'type': 'SyntaxError',
                    'title': 'Missing colon in function definition',
                    'description': 'Function definitions require a colon at the end of the line.',
                    'cause': 'This is a syntax error in Python where function definitions must end with a colon.',
                    'fix': 'Add a colon (:) at the end of the function definition line.',
                    'line': 2,
                    'column': 15,
                    'code': 'def greet(name)',
                    'severity': 'high',
                    'hints': {
                        'level1': 'Look at how Python defines functions.',
                        'level2': 'Function definitions need proper punctuation at the end.',
                        'level3': 'Add a colon at the end: def greet(name):'
                    }
                },
                {
                    'id': 2,
                    'type': 'IndentationError',
                    'title': 'Inconsistent indentation',
                    'description': 'The function body is not properly indented.',
                    'cause': 'Python uses indentation to define code blocks.',
                    'fix': 'Indent the print statement with 4 spaces.',
                    'line': 3,
                    'column': 1,
                    'code': 'print("Hello, " + name)',
                    'severity': 'high',
                    'hints': {
                        'level1': 'Check the indentation of the code block.',
                        'level2': 'Python requires consistent indentation for code blocks.',
                        'level3': 'Add 4 spaces before the print statement inside the function.'
                    }
                }
            ],
            'warnings': [],
            'correction_strategies': [
                {
                    'name': 'Fix indentation with 4 spaces',
                    'description': 'Standardize all indentation to use 4 spaces.',
                    'code': 'def greet(name):\n    print("Hello, " + name)',
                    'pros': ['PEP 8 compliant', 'Most common convention', 'Improves readability'],
                    'cons': ['Need to ensure entire file follows same convention'],
                    'applicable_to_issues': [1, 2]
                }
            ],
            'corrected_code': '''# Python Example corrected
def greet(name):
    print("Hello, " + name)

x = 0
if x > 5:
    print("x is greater than 5")

for i in range(10):
    print(i)
    print(i * 2)''',
            'suggestions': [
                "Use f-strings for string formatting in Python 3.6+: print(f'Hello, {name}')",
                "Add type hints for better code documentation",
                "Consider adding docstrings to functions"
            ],
            'best_practices': [
                "Use consistent indentation (4 spaces recommended)",
                "Follow PEP 8 style guide",
                "Add comments for complex logic"
            ]
        }
        
        return JsonResponse(mock_response)
        
    except Exception as e:
        return JsonResponse({
            'error': f'Error: {str(e)}'
        }, status=500)