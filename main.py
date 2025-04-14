import streamlit as st
import io
import os
from resume_parser import DocumentParser
from ai_coach import AICoach
from chat_interface import ChatInterface
from utils import format_report

def main():
    st.set_page_config(page_title="AI Career Coach", page_icon="👔", layout="wide")

    # Load custom CSS
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.title("AI Career Coach 👔")

    # Initialize document parser (lightweight)
    document_parser = DocumentParser()
    
    # Model selection
    available_models = ["llama-3", "llama2", "gemma"]
    selected_model = st.sidebar.selectbox(
        "Select AI Model",
        options=available_models,
        index=0
    )
    
    # Set the model in environment variable for persistence
    os.environ["MODEL"] = selected_model

    # File upload section
    st.header("Upload Your Resume")
    uploaded_resume = st.file_uploader(
        "Choose your resume file", 
        type=document_parser.supported_formats,
        key="resume_uploader"
    )

    # Job description input - both text and file upload
    st.header("Job Description")
    job_desc_tab1, job_desc_tab2 = st.tabs(["Enter Text", "Upload File"])
    
    with job_desc_tab1:
        job_description_text = st.text_area(
            "Paste the job description here",
            height=200
        )
        
    with job_desc_tab2:
        uploaded_job_desc = st.file_uploader(
            "Choose job description file",
            type=document_parser.supported_formats,
            key="job_desc_uploader"
        )

    # Initialize AI Coach with selected model
    try:
        ai_coach = AICoach(model=selected_model)  # Use the selected model
    except Exception as e:
        st.error("The AI model is still initializing. Please wait a moment and refresh the page.")
        st.error(f"Details: {str(e)}")
        return

    # Process job description from either text input or file upload
    job_description = ""
    if job_description_text:
        job_description = job_description_text
    elif uploaded_job_desc:
        try:
            file_extension = f".{uploaded_job_desc.name.split('.')[-1]}"
            job_description = document_parser.parse_document(
                uploaded_job_desc.getvalue(),
                file_extension
            )
        except Exception as e:
            st.error(f"Error parsing job description file: {str(e)}")
    
    # Analysis section
    if uploaded_resume and job_description:
        try:
            with st.spinner("Analyzing your resume..."):
                # Parse resume
                file_extension = f".{uploaded_resume.name.split('.')[-1]}"
                resume_text = document_parser.parse_document(
                    uploaded_resume.getvalue(),
                    file_extension
                )

                if resume_text:
                    # Store in session state
                    st.session_state.resume_text = resume_text
                    st.session_state.job_description = job_description

                    # Analyze resume
                    analysis = ai_coach.analyze_resume(resume_text, job_description)
                    st.session_state.analysis = analysis

                    # Display analysis report
                    st.header("Analysis Report")
                    with st.container():
                        # Match percentage
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Match Score", f"{analysis['match_percentage']}%")
                        with col2:
                            st.progress(analysis['match_percentage'] / 100)

                        # Detailed report
                        st.markdown(format_report(analysis))

                        # Generate improvement plan
                        if analysis['missing_skills']:
                            st.subheader("Skill Development Plan")
                            improvement_plan = ai_coach.generate_improvement_plan(
                                analysis['missing_skills']
                            )
                            for item in improvement_plan:
                                st.markdown(f"- {item}")

                    # Chat interface
                    st.markdown("---")
                    chat_interface = ChatInterface(ai_coach)
                    chat_interface.display_chat()
                else:
                    st.error("Could not extract text from the resume. Please check the file format.")

        except Exception as e:
            st.error(f"An error occurred during analysis: {str(e)}")

    else:
        st.info("Please upload your resume and paste the job description to get started.")

if __name__ == "__main__":
    main()