# 🤖 CodeTutor AI
**Smart Error Detection & Learning Platform**  
*First Client Project • Pre-Production MVP*

<div align="center">
  <img src="https://img.shields.io/badge/Status-Pre--Production-yellow" alt="Status: Pre-Production">
  <img src="https://img.shields.io/badge/Client_Project-First_Client-blue" alt="First Client Project">
  <img src="https://img.shields.io/badge/Version-1.0.0-brightgreen" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License MIT">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</div>

## 📌 Project Overview

**CodeTutor AI** is a web-based programming assistant designed to help developers understand and fix coding errors through educational feedback. Unlike traditional linters that provide cryptic error messages, CodeTutor explains *why* errors occur and offers *learning-focused* guidance to improve programming skills.

Built as my **first professional client project**, this MVP focuses on delivering clear, educational value with a clean, maintainable codebase that can scale for future enhancements.

---

## 🎯 Project Goals & Value Proposition

### **For Learners & Students**
- Understand programming concepts through error explanations
- Receive progressive guidance instead of direct answers
- Build debugging skills with structured learning hints
- Access multiple solutions to common problems

### **For Educators & Trainers**
- Provide interactive learning tool for coding classes
- Supplement traditional teaching with instant feedback
- Track common student mistakes across programming languages
- Customize learning paths based on error patterns

### **For Developers**
- Quick debugging assistant for multiple languages
- Learn new languages through practical examples
- Understand compiler/interpreter messages better
- Improve code quality with style suggestions

---

## ✨ Core Features

### 🔍 **Intelligent Code Analysis**
- **Multi-language Support**: Python, JavaScript, Java, C++, C#
- **Error Categorization**: Syntax errors, logical errors, warnings, best practices
- **Context-Aware Detection**: Understands code intent, not just syntax
- **Line-by-Line Analysis**: Precise error location with code snippets

### 🎓 **Learning-Focused Feedback System**
- **3-Level Progressive Hints**:
  - **Level 1**: Gentle nudge (minimal guidance)
  - **Level 2**: Partial explanation (conceptual hint)
  - **Level 3**: Full solution with example
- **Multiple Correction Strategies**: Different approaches to solve the same problem
- **Concept Mapping**: Errors grouped by programming concepts
- **Best Practices**: Style and optimization suggestions

### 🖥️ **Professional User Interface**
- **Dual-Panel Design**: Code editor + Analysis results side-by-side
- **Syntax Highlighting**: Language-aware code coloring
- **Dark Theme**: Eye-friendly dark mode interface
- **Mobile Responsive**: Full functionality on all devices
- **Interactive Elements**: Clickable hints, filterable results, concept badges

### ⚡ **Performance & Usability**
- **Real-time Analysis**: Instant feedback as you type
- **Session Persistence**: Code remains during page refresh
- **Example Library**: Pre-loaded examples for each language
- **One-Click Actions**: Copy corrected code, clear editor, switch languages

---

## 🏗️ Technical Architecture

### **System Architecture**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │   Django Backend │    │   Analysis Engine│
│   (Single Page) │◄──►│   (API Layer)    │◄──►│   (Rule-Based)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Browser       │    │   SQLite DB     │    │   Hint Generator│
│   Storage       │    │   (Dev Only)    │    │   (3-Level)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **Project Structure**
```
codeTutor/                              # Root Directory
│
├── codeTutor/                          # Django Project Configuration
│   ├── __init__.py
│   ├── settings.py                     # Project settings (debug mode enabled)
│   ├── urls.py                         # Main URL routing (includes tutor URLs)
│   ├── asgi.py                         # ASGI config for async support
│   └── wsgi.py                         # WSGI config for deployment
│
├── tutor/                              # Core Application Module
│   ├── __init__.py
│   ├── apps.py                         # App configuration
│   ├── models.py                       # Database models (placeholder for future)
│   ├── views.py                        # Main business logic (analysis & hints)
│   ├── urls.py                         # API endpoints (/api/analyze/, /api/get-hint/)
│   ├── tests.py                        # Test suite (to be developed)
│   └── templates/
│       └── coder.html                  # Complete frontend (HTML + CSS + JS in one file)
│
├── db.sqlite3                          # SQLite database (development)
├── requirements.txt                    # Python dependencies (Django, etc.)
├── manage.py                           # Django management script
├── .env                                # Environment variables (template)
├── .gitignore                          # Git exclusion rules
├── README.md                           # This documentation
└── Licence                             # MitLicence
```

### **Key Technical Decisions**
1. **Single-Page Application**: All frontend code in one HTML file for simplicity
2. **Mock Analysis Engine**: Rule-based error detection for MVP phase
3. **SQLite Database**: Lightweight for development, easy migration to PostgreSQL
4. **Vanilla JavaScript**: No framework dependencies for faster loading
5. **Responsive CSS**: Custom Flexbox/Grid implementation for mobile support

---

## 🚀 Quick Start (Development)

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Git
- Modern web browser

### **Installation Steps**

```bash
# 1. Clone the repository
git clone https://github.com/rithik-dev31/codeTutor_ai.git
cd codeTutor_ai

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Start development server
python manage.py runserver
```

### **Access the Application**
Open your browser and navigate to:  
**http://127.0.0.1:8000/**

---

## ⚡ How to Use CodeTutor AI

### **Basic Workflow**
1. **Select Language**: Choose from Python, JavaScript, Java, C++, or C#
2. **Write Code**: Type directly or paste your code into the editor
3. **Click Analyze**: Get instant feedback on errors and warnings
4. **Review Results**: See categorized issues with explanations
5. **Use Learning Hints**: Click through three levels of guidance
6. **Apply Fixes**: Copy corrected code or implement suggestions

### **Example Use Cases**

#### **For Students Learning Python**
```python
# Try this example with intentional errors
def calculate_average(numbers)
    total = 0
    for num in numbers
        total += num
    return total / len(numbers)

print(calculate_average([10, 20, 30, 40]))
```

**CodeTutor will identify:**
- Missing colon in function definition
- Missing colon in for loop
- Return statement indentation
- Provide learning hints for each issue

#### **For JavaScript Developers**
```javascript
// Common JavaScript mistakes
function getUserData(userId) {
    fetch(`/api/users/${userId}`)
    .then(response => response.json())
    .then(data => console.log(data)
}
```

**CodeTutor will detect:**
- Missing closing parenthesis
- Promise handling patterns
- Error handling suggestions

### **Learning Hints System**
Each issue includes three levels of educational content:

| Level | Description | Example |
|-------|-------------|---------|
| **Level 1** | Gentle nudge | "Check the function definition syntax" |
| **Level 2** | Partial clue | "In Python, function definitions need specific punctuation" |
| **Level 3** | Full solution | "Add a colon at the end: `def calculate_average(numbers):`" |

---

## 🔌 API Documentation

### **Base URL**
```
http://localhost:8000/
```

### **Available Endpoints**

#### **1. Analyze Code**
```http
POST /api/analyze/
Content-Type: application/json

Request Body:
{
    "code": "def hello(): print('Hello World')",
    "language": "python"
}
```

#### **2. Get Learning Hint**
```http
POST /api/get-hint/
Content-Type: application/json

Request Body:
{
    "code": "def hello(): print('Hello World')",
    "issue_id": 1,
    "level": 2,
    "language": "python"
}
```

#### **3. Get Correction Strategies**
```http
POST /api/correction-strategies/
Content-Type: application/json

Request Body:
{
    "code": "def hello(): print('Hello World')",
    "issue_id": 1,
    "language": "python"
}
```

#### **4. Get Corrected Code**
```http
POST /api/corrected-code/
Content-Type: application/json

Request Body:
{
    "code": "def hello(): print('Hello World')",
    "language": "python",
    "apply_fixes": true
}
```

---

## 🧪 Current Project Status

### **✅ Implemented Features**
- [x] Multi-language code editor with syntax support
- [x] Rule-based error detection for 5 programming languages
- [x] 3-level progressive hint system
- [x] Responsive web interface (desktop & mobile)
- [x] Real-time code analysis
- [x] Example code library
- [x] Filterable results (All/Errors/Warnings)
- [x] One-click copy functionality
- [x] Session persistence in browser
- [x] Professional dark theme UI

### **⚠️ Current Limitations (MVP Phase)**
- **Mock Analysis**: Uses rule-based detection instead of real AI
- **No Authentication**: Single-user system without accounts
- **Limited Error Patterns**: Focus on common beginner mistakes
- **Development Database**: SQLite for simplicity
- **No History Tracking**: Sessions don't persist across browser restarts

### **🛣️ Roadmap & Future Enhancements**

#### **Phase 2: Enhanced Analysis**
- Integrate real AI (OpenAI/Gemini API)
- Add more programming languages (Go, Rust, TypeScript)
- Implement advanced static analysis
- Add code complexity scoring

#### **Phase 3: User Features**
- User authentication system
- Progress tracking and analytics
- Saved code snippets library
- Custom learning paths

#### **Phase 4: Platform Enhancement**
- Classroom mode for educators
- Peer code review features
- Integration with IDEs (VS Code extension)
- API for third-party integrations

---

## 🛠️ Development Guidelines

### **Code Structure Principles**
1. **Separation of Concerns**: Frontend (HTML/CSS/JS) separated from backend (Python/Django)
2. **Modular Design**: Each language parser is independent
3. **Educational Focus**: All feedback must explain "why," not just "what"
4. **Accessibility**: UI works with screen readers and keyboard navigation

### **Adding New Language Support**
1. Add language to frontend selector in `coder.html`
2. Create language-specific error patterns in `views.py`
3. Add example code snippets
4. Test with common errors in that language
5. Update documentation

### **Testing Strategy**
```bash
# Run Django tests
python manage.py test tutor

# Manual testing checklist:
# 1. Test all 5 supported languages
# 2. Verify mobile responsiveness
# 3. Test hint system progression
# 4. Check copy functionality
# 5. Validate filter buttons
```

---

## 🤝 Client Project Notes

### **Project Context**
This project was developed as **my first professional client engagement**, with the following objectives:
- Demonstrate full-stack development capabilities
- Create an educational tool with real value
- Build a maintainable, scalable codebase
- Deliver on time with clear communication

### **Key Client Requirements Met**
- ✅ Educational focus over technical complexity
- ✅ Clean, professional user interface
- ✅ Support for multiple programming languages
- ✅ Progressive learning system
- ✅ Mobile-responsive design
- ✅ Clear documentation for future developers

### **Lessons Learned**
1. **User-Centric Design**: Educational tools need clear, simple interfaces
2. **Progressive Disclosure**: Don't overwhelm users with information
3. **Maintainability**: Clean code structure is crucial for future enhancements
4. **Communication**: Regular updates and clear expectations build trust

---

## 📄 License & Usage

### **License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **Usage Rights**
- ✅ **Free to use** for educational purposes
- ✅ **Can be modified** and distributed
- ✅ **Commercial use** allowed with attribution
- ✅ **No warranty** provided

### **Attribution**
If you use this project, please include:
1. Link to original repository
2. Mention of "CodeTutor AI"
3. Reference to MIT License

---

## ❤️ Acknowledgments

### **Special Thanks**
- **My First Client**: For trusting me with this project and providing valuable feedback
- **Programming Educators**: Whose teaching methods inspired the hint system
- **Open Source Community**: For the tools and libraries that made this possible

### **Built With**
- **Django**: For a robust, scalable backend framework
- **Python**: For clean, readable server-side code
- **Vanilla Web Technologies**: For a lightweight, fast frontend
- **Educational Research**: For insights into effective learning methods

### **Dedication**
This project is dedicated to **every beginner programmer** who's ever been frustrated by a cryptic error message. May your debugging journey be a little easier and a lot more educational.

---

<div align="center">
  <h3>📧 Contact & Support</h3>
  <p>
    <strong>Developer:</strong>RITHIK<br>
    <strong>Email:</strong> <a href="mailto:rithik.devpro@gmail.com">rithik.devpro@gmail.com</a><br>
    <strong>GitHub:</strong> <a href="https://github.com/rithik-dev31">@rithik-dev31</a>
  </p>
  
  <p>
    <em>Built with passion as a first professional client project</em><br>
    <strong>Making programming education more accessible, one error at a time.</strong>
  </p>
</div>
