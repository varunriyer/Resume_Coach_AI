# AI Career Coach

Welcome to the AI Career Coach, a Streamlit-based web application that analyzes your resume against a job description, calculates skill matches, and provides personalized career advice through an interactive chat interface. This repository contains everything you need to set up and run the project on your PC.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Usage](#usage)
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
1. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux).
2. Run the following commands to clone and navigate to the project directory:
```bash
git clone https://github.com/<your-username>/AI-Career-Coach.git
cd AI-Career-Coach
```

### Step 2: Set Up a Virtual Environment
1. Create a virtual environment (recommended to isolate dependencies):
```bash
python -m venv venv
```
2. Activate it:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
1. Ensure the virtual environment is activated (you’ll see `(venv)` in the terminal).
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration
The project uses a Groq API key stored in a `.env` file. Follow these steps:
1. Create a file named `.env` in the `AI-Career-Coach` directory.
2. Open the `.env` file in a text editor (e.g., Notepad on Windows, TextEdit on macOS).
3. Add this line, replacing `<your-groq-api-key>` with your actual key from Groq:
```
GROQ_API_KEY=<your-groq-api-key>
```
4. Save and close the file.

> **Note**: Do not share this file or key publicly.

## Running the Project
1. Ensure the virtual environment is activated.
2. Start the application:
```bash
streamlit run main.py
```
3. Open a web browser and go to `http://localhost:8501`.

> Keep the terminal window open while using the app.

## Usage
1. **Upload Resume**: Select your resume file (PDF, DOCX, or TXT).
2. **Enter Job Description**: Paste the text or upload a file.
3. **Select AI Model**: Choose from LLaMA-3, LLaMA2, or Gemma in the sidebar.
4. **View Analysis**: See your skill match percentage and detailed report.
5. **Chat with Coach**: Ask questions in the chat interface for personalized advice.

## Troubleshooting
- **“ModuleNotFoundError”**: Run `pip install -r requirements.txt` again.
- **API Key Issues**: Check the `.env` file for typos and correct placement.
- **App Won’t Start**: If port 8501 is busy, try:
```bash
streamlit run main.py --server.port=8502
```
- **Contact**: For help, email [rvaruniyer@gmail.com](mailto:rvaruniyer@gmail.com).

---
