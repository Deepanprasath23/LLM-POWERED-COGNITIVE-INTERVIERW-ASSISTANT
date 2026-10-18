# LLM-Powered Cognitive Interview Assistant

## 1. Project Overview

The project is a full-stack AI interview preparation system designed to help students, freshers, and job seekers practice interviews in a realistic and personalized manner. It combines resume analysis, role-based question generation, and AI-driven feedback to simulate an interview experience that is tailored to the user’s profile.

The system addresses common issues in interview preparation: generic questions, lack of personalized guidance, and insufficient immediate feedback. By integrating Google Gemini AI with a web application, the project creates an adaptive interview assistant that can evaluate user responses and suggest improvements.

## 2. Problem Statement

Traditional interview preparation often lacks personalization and real-time constructive guidance. Students typically practice with generic questions and do not receive structured feedback on communication, technical accuracy, or confidence. The project solves this by:

- analyzing candidate resumes,
- extracting technical and soft skills,
- generating role-specific or resume-specific questions,
- collecting user answers, and
- evaluating those answers using AI.

## 3. Core Functionalities

### Resume-Based Interview Mode

- User uploads a PDF resume.
- The backend extracts content from the PDF.
- Skills, experience level, and project summaries are identified.
- The system generates targeted interview questions from the candidate's actual background.

### Role-Based Interview Mode

- User selects a role such as software engineer, data scientist, or similar.
- The backend uses the chosen role to generate industry-specific questions.
- Difficulty levels can be adjusted for beginner, intermediate, or advanced interviews.

### Interview Processing

- Users answer questions in text form.
- Responses are stored in the user’s interview session.
- The AI model evaluates each response for strengths, weaknesses, and improvement suggestions.

### Feedback Dashboard

- Final feedback is provided in a structured format.
- Evaluation includes communication quality, technical depth, problem-solving ability, and soft-skill alignment.
- Users can review their performance and improve over time.

## 4. System Architecture

The application follows a layered architecture:

1. Frontend layer: React application for user interactions and interface management.
2. Backend layer: Flask API that handles authentication, file upload, interview generation, and evaluation.
3. Database layer: SQLAlchemy models with SQLite for local development and PostgreSQL compatibility for production.
4. AI services layer: Google Gemini AI performs resume analysis, question generation, and response evaluation.
5. File processing layer: PDF text extraction using pdfplumber and fallback parsing for resume content.

## 5. Technology Stack

### Frontend

- React
- Vite
- React Router
- CSS for responsive UI and animations

### Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-CORS

### AI and Processing

- Google Gemini API
- pdfplumber
- PyPDF2 fallback support
- Pydantic for structured parsing and validation

### Authentication and Security

- Google OAuth 2.0
- WebApplicationClient for OAuth flow
- Session-based login management

### Database

- SQLite in development
- PostgreSQL-ready configuration for production

## 6. Key Backend Modules

### app.py

This is the central Flask application. It configures the app, initializes extensions, registers the Google authentication blueprint, serves the frontend, and exposes API endpoints for:

- health checks,
- resume upload,
- question generation,
- answer submission,
- interview completion,
- feedback retrieval.

### models.py

Defines the core application entities:

- User: stores authentication profile and contact information.
- InterviewSession: stores mode, difficulty, role, questions, answers, feedback, and user-specific metadata.

### google_auth.py

Handles Google OAuth login flow. It redirects the user to Google for consent, handles the callback, creates or loads a user record, and logs the user into the Flask app.

### resume_analyzer.py

Performs the resume intelligence layer. It extracts raw text from uploaded PDF files and inspects content to identify:

- technical skills,
- soft skills,
- project details,
- experience level,
- summary of candidate background.

This module uses a hybrid strategy: keyword-based matching combined with LLM-powered extraction when available.

### question_generator.py

Builds context-aware questions based on skills, projects, or role context. The question generation logic adapts to a chosen difficulty level and interview mode.

### gemini.py

Provides the Gemini client interface used by the backend for AI tasks such as generating questions and feedback.

## 7. Frontend Design and User Experience

The frontend is built using React and follows a single-page application model. The app routes between authentication, dashboard, interview sessions, and informational pages. The interface is designed to be modern, responsive, and easy to navigate. It includes:

- login screen,
- dashboard,
- role selection,
- resume upload interaction,
- interview session flow,
- feedback dashboard,
- privacy/about pages.

## 8. Data Flow

A typical interview journey works like this:

1. User signs in using Google OAuth.
2. User chooses either resume-based or role-based interview.
3. If resume mode is selected, a PDF is uploaded and parsed.
4. Skills and experience are extracted and stored.
5. The backend requests AI-generated interview questions.
6. The user answers each question.
7. Responses are saved to the session record.
8. At completion, Gemini evaluates the entire interview.
9. A detailed feedback report is generated and shown to the user.

## 9. Database Model

The project uses a relational model with at least two major tables:

- User table: unique email, username, created timestamp.
- InterviewSession table: stores interview mode, difficulty, role, questions, answers, feedback, status, and timestamps.

This structure supports per-user interview history and feedback tracking.

## 10. Strengths of the Project

- Personalized interview preparation based on resume or role.
- Real-time AI evaluation for more meaningful feedback.
- Modern, responsive web-based interface.
- Modular architecture with clear separation of frontend and backend responsibilities.
- Extensible design for adding more roles, AI prompts, or evaluation metrics.

## 11. Areas for Improvement

- Add stronger validation and error handling for malformed PDFs.
- Support more advanced session analytics and performance trends.
- Improve production deployment configuration.
- Add multi-user concurrency safeguards and richer database indexing.
- Expand evaluation scoring with rubric-based metrics and confidence scoring.

## 12. Conclusion

This project demonstrates the practical use of LLMs in a real-world interview preparation platform. It combines modern web development, AI services, and secure user flows to create an intelligent system that can generate context-aware interview questions and actionable feedback. The design is scalable and can be extended into a commercial-grade interview assistant for educational and recruitment use cases.
