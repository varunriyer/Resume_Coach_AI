# AI Career Coach

Welcome to the AI Career Coach, a Streamlit-based web application that analyzes your resume against a job description, calculates skill matches, and provides personalized career advice through an interactive chat interface. This repository contains everything you need to set up and run the project on your PC.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Project Details](#project-details)
- [Troubleshooting](#troubleshooting)

## Overview
The AI Career Coach helps you:
- Parse resumes in PDF, DOCX, or TXT formats.
- Analyze skill alignment with job descriptions.
- Offer actionable career advice using AI models (e.g., LLaMA-3, LLaMA2, Gemma).

## Prerequisites
Ensure your system meets these requirements:
- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.9 or higher ([Download Python](https://www.python.org/downloads/))
- **Git**: For cloning the repository ([Download Git](https://git-scm.com/downloads))
- **Internet Connection**: Required for the Groq API
- A **Groq API Key** (sign up at [Groq Console](https://console.groq.com/))

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/AI-Career-Coach.git
cd AI-Career-Coach
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
```
- Activate it:
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
Create a file named `.env` in the `AI-Career-Coach` directory and add:
```bash
GROQ_API_KEY=<your-groq-api-key>
```

> **Note**: Do not share this file or key publicly.

## Running the Project
```bash
streamlit run main.py
```
Then visit `http://localhost:8501`.

## Usage
1. **Upload Resume**: PDF, DOCX, or TXT.
2. **Enter Job Description**: Paste or upload a file.
3. **Select AI Model**: LLaMA-3, LLaMA2, or Gemma.
4. **View Analysis**: Skill match percentage and report.
5. **Chat with Coach**: Ask questions for personalized advice.

## Project Details

### Functionalities
- **Resume Parsing**: Uses `DocumentParser` to extract text from resumes.
- **Skill Matching**: Calculates match % between resume and job description using `utils.py`.
- **Analysis Report**: Shows matching, missing, and extra skills.
- **Interactive Chat**: AI-powered advice via the `AICoach` class.
- **Model Selection**: Choose LLaMA-3, LLaMA2, or Gemma for different styles of analysis.

### How It Works
- Users upload a resume and job description.
- Text is extracted using `resume_parser.py`.
- Skills are extracted and matched using `utils.py`.
- AI generates a JSON report via the `Groq API` and `AICoach`.
- `Streamlit` displays all results, including the chat.

## Troubleshooting
- **“ModuleNotFoundError”**: Run `pip install -r requirements.txt` again.
- **API Key Issues**: Check your `.env` file.
- **App Won’t Start**: Try another port:
```bash
streamlit run main.py --server.port=8502
```
- **Contact**: For help, email [rvaruniyer@gmail.com](mailto:rvaruniyer@gmail.com).

---
