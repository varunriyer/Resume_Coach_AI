# AI Career Coach - Technical Details

This document provides an in-depth look at the AI Career Coach project, including its architecture, current implementation, and potential areas for improvement.

## Project Architecture

- **Frontend**: Streamlit for file upload, analysis display, and chat.
- **Backend**: Python scripts: `main.py`, `chat_interface.py`, `resume_parser.py`, `ai_coach.py`, `utils.py`.
- **Styling**: Custom CSS via `styles.css`.
- **API Integration**: Groq API through the `openai` library and `.env`.

## Current Implementation

- **Resume Parsing**: `DocumentParser` uses PyPDF2, python-docx, and text decoding.
- **Skill Matching**: Regex-based skill extraction in `utils.py` compares resume and JD.
- **AI Analysis**: `AICoach` sends data to Groq API and returns JSON output with skill match and recommendations.
- **Chat Interface**: `ChatInterface` manages state for context-aware replies.
- **Improvement Plans**: AI-generated based on missing skills and user goals.

## Current Working Status

- Successfully parses, matches skills, and generates detailed reports.
- Chatbot responds based on analysis context.
- Stable for standard resume formats.
- Model selection allows switching between LLaMA-3, LLaMA2, and Gemma.

## Potential Improvements

- **Skill Extraction**: Use ML/NLP models for better detection.
- **Error Handling**: More robust error messages in `main.py`.
- **Performance**: Cache or consider local models for efficiency.
- **UI Enhancements**: Add progress indicators and responsive layouts.

## Getting Started

Refer to `README.md` for setup. This file is intended for technical contributors or curious users.

---
