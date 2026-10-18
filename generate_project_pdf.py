from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, PageBreak
from reportlab.lib import colors

TITLE = "LLM-Powered Cognitive Interview Assistant"

content = [
    Paragraph("<b>Technical Project Explanation</b>", ParagraphStyle(
        name='title',
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0F172A'),
        alignment=1,
    )),
    Spacer(1, 18),
    Paragraph(
        "This project is a full-stack AI interview preparation system built to help students and job seekers practice interviews in a personalized and realistic way. It combines resume analysis, question generation, and AI-powered feedback to simulate a guided interview experience.",
        ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937')),
    ),
    Spacer(1, 16),

    Paragraph("<b>1. Project Overview</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    Paragraph("The system addresses common weaknesses in preparation: generic questions, lack of role relevance, and limited real-time feedback. Users can either upload a resume or choose a target role. The application then generates tailored interview questions and evaluates their responses using Google Gemini AI.", ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937'))),
    Spacer(1, 12),

    Paragraph("<b>2. Core Functionalities</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    ListFlowable([
        ListItem(Paragraph("Resume-based mode: upload a PDF resume and extract technical skills, projects, and experience trends.")),
        ListItem(Paragraph("Role-based mode: generate industry-specific questions from a selected job role and difficulty level.")),
        ListItem(Paragraph("Interview session tracking: save questions, answers, and user performance state in the database.")),
        ListItem(Paragraph("AI-driven feedback: evaluate response quality, strengths, and improvement areas after interview completion.")),
    ], bulletType='bullet', bulletFontName='Helvetica', bulletFontSize=10, spacing='normal', leftIndent=18, bulletColor=colors.HexColor('#1D4ED8')),
    Spacer(1, 12),

    Paragraph("<b>3. System Architecture</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    Paragraph("The application follows a layered architecture. The frontend is a React application built with Vite. The backend is a Flask service that handles route logic, auth, file handling, and AI orchestration. The database uses SQLAlchemy models, while AI features are powered by Google Gemini. Resume parsing is handled through pdfplumber and fallback support from PyPDF2.", ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937'))),
    Spacer(1, 12),

    Paragraph("<b>4. Technology Stack</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    ListFlowable([
        ListItem(Paragraph("Frontend: React, Vite, React Router, custom CSS.")),
        ListItem(Paragraph("Backend: Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-CORS.")),
        ListItem(Paragraph("AI: Google Gemini API for question generation and response evaluation.")),
        ListItem(Paragraph("Authentication: Google OAuth 2.0 using flask-login and oauthlib patterns.")),
        ListItem(Paragraph("Data / file processing: SQLite for local storage and PDF parsing with pdfplumber.")),
    ], bulletType='bullet', bulletFontName='Helvetica', bulletFontSize=10, spacing='normal', leftIndent=18, bulletColor=colors.HexColor('#1D4ED8')),
    Spacer(1, 12),

    Paragraph("<b>5. Key Backend Modules</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    Paragraph("The backend entry point is app.py, which configures the Flask app and exposes endpoints such as /api/upload-resume, /api/generate-questions, /api/submit-answer, and /api/complete-interview. Models are defined in models.py, where User and InterviewSession encapsulate user identity and session lifecycle. google_auth.py implements the Google OAuth flow, while resume_analyzer.py extracts skills and project context from uploaded PDF resumes. The question generation and feedback logic rely on Gemini-based AI orchestration.", ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937'))),
    Spacer(1, 12),

    Paragraph("<b>6. Frontend Experience</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    Paragraph("The frontend is a modern single-page application with routing for the login screen, dashboard, resume upload, interview flow, and feedback pages. It manages authentication state and interacts with the backend through API requests, creating a clean and responsive user experience.", ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937'))),
    Spacer(1, 12),

    Paragraph("<b>7. Data Flow</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    ListFlowable([
        ListItem(Paragraph("User signs in using Google OAuth.")),
        ListItem(Paragraph("User uploads a resume or selects a role.")),
        ListItem(Paragraph("AI analyzes resume content or role context to generate questions.")),
        ListItem(Paragraph("User answers the questions during the session.")),
        ListItem(Paragraph("The system stores answers and produces feedback at the end of the interview.")),
    ], bulletType='bullet', bulletFontName='Helvetica', bulletFontSize=10, spacing='normal', leftIndent=18, bulletColor=colors.HexColor('#1D4ED8')),
    Spacer(1, 12),

    Paragraph("<b>8. Strengths and Extensibility</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    Paragraph("This project demonstrates an effective use of LLMs in practical interview preparation. It is modular, scalable, and suitable for extension with richer analytics, additional roles, better deployment configuration, and more robust evaluation scoring. The architecture clearly separates concerns between frontend interaction, API logic, data persistence, and AI processing.", ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937'))),
    Spacer(1, 14),

    Paragraph("<b>Conclusion</b>", ParagraphStyle(name='h1', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=colors.HexColor('#1D4ED8'))),
    Paragraph("The LLM-Powered Cognitive Interview Assistant is a practical and modern solution for interview preparation. By combining resume-based personalization with AI-generated questions and actionable feedback, it offers a powerful platform for skill development and interview readiness.", ParagraphStyle(name='body', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#1F2937'))),
]


def build_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=30,
        bottomMargin=30,
    )
    doc.build(content)


if __name__ == "__main__":
    build_pdf("technical_explanation.pdf")
    print("PDF generated successfully: technical_explanation.pdf")
