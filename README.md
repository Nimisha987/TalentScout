# TalentScout
# TalentScout – AI Hiring Assistant Chatbot 

## Project Overview

TalentScout is an AI-powered hiring assistant chatbot designed to automate the initial screening of job candidates. The system interacts with candidates through a conversational interface, collects essential information, and generates tailored technical interview questions based on the candidate’s declared tech stack.

This project demonstrates the use of Large Language Models (LLMs), prompt engineering, conversation flow management, and a modern Streamlit-based user interface.

---

## Features

* Conversational chatbot interface using Streamlit
* Step-by-step candidate information collection:

  * Full Name
  * Email Address
  * Phone Number
  * Years of Experience
  * Desired Position
  * Current Location
  * Tech Stack
* Automatic generation of technical interview questions
* Technical question answering flow
* Context-aware conversation handling
* Fallback handling for unexpected inputs
* Simulated data storage
* Modern, responsive UI with custom CSS
* Privacy-friendly design using dummy/simulated data

---

## Tech Stack

* **Programming Language:** Python
* **Frontend:** Streamlit
* **LLM Provider:** Groq API (LLaMA / Mixtral models)
* **Styling:** Custom CSS
* **Storage:** JSON (simulated database)

---

## Installation Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd talentscout-chatbot
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## Usage Guide

1. Open the web interface in your browser.
2. The chatbot greets the candidate automatically.
3. Enter details step by step as requested.
4. Provide your tech stack (comma separated).
5. Answer the generated technical questions.
6. Receive confirmation message after completion.

---

## System Architecture

```
User
  │
  ▼
Streamlit UI
  │
  ▼
ChatFlow Controller
  │
  ├── Candidate Memory
  ├── Question Generator
  ├── LLM (Groq API)
  └── Data Storage (JSON)
```

---

## Prompt Engineering Strategy

The chatbot uses structured prompting to:

* Collect candidate information one field at a time
* Maintain conversation context
* Generate relevant technical questions based on the tech stack
* Avoid deviating from the recruitment purpose
* Handle unclear input gracefully

Separate prompt logic is used for:

* Candidate information gathering
* Technical question generation
* Conversation control

---

## Data Handling & Privacy

* Only simulated/dummy data is stored
* No real personal data is required for testing
* Data is stored locally in JSON format
* No third-party database is used
* Designed following GDPR-friendly principles

---

## Challenges & Solutions

| Challenge                                | Solution                                            |
| ---------------------------------------- | --------------------------------------------------- |
| Maintaining multi-step conversation flow | Implemented state-based controller (ChatFlow class) |
| Parsing tech stack input                 | Normalized and validated user input                 |
| Asking technical questions sequentially  | Implemented technical interview round logic         |
| UI limitations of Streamlit              | Used custom CSS styling                             |
| Session persistence                      | Used Streamlit session_state                        |

---

## Future Improvements

* Resume upload and parsing
* Candidate scoring using AI
* Sentiment analysis
* Multilingual chatbot support
* Admin dashboard for recruiters
* Database integration (PostgreSQL / MongoDB)
* Authentication system
* Cloud deployment (AWS / GCP)

---

## Demo

A demo video showcasing the full chatbot workflow is included with the submission.

---

## Submission Checklist

* [x] Source code
* [x] Streamlit UI
* [x] Technical question generation
* [x] Conversation flow handling
* [x] README documentation
* [x] Demo video

---

## Author

**Name:** Nimisha Agrawal
**Project:** AI/ML Intern Assignment – TalentScout Hiring Assistant

---

## License

This project is created for educational and evaluation purposes only.
