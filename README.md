# AI Resume Analyzer

A full-stack web application that analyzes a PDF resume against a job description and identifies matched skills, missing skills, and a skill-match percentage.

## Features

- Upload a resume in PDF format.
- Extract resume text using PyMuPDF.
- Enter a job description for comparison.
- Detect skills using a predefined skills dictionary.
- Display matched skills and missing skills.
- Calculate a skill-match percentage.
- Validate inputs and display results in a clean, responsive interface.

## Tech Stack

**Frontend**
- React
- Vite
- CSS

**Backend**
- Python
- FastAPI
- PyMuPDF

## Project Structure

```text
ai-resume-analyzer/
├── backend/
│   ├── api.py
│   └── skills.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── App.css
│   ├── package.json
│   └── index.html
└── README.md
```

## Getting Started

### Prerequisites

- Python 3
- Node.js and npm

### 1. Clone the repository

```bash
git clone GauravVerma789/Resume-analyzer
cd ai-resume-analyzer
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Start the backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pymupdf python-multipart
uvicorn api:app --reload
```

The API should be available at `http://127.0.0.1:8000`.

Interactive API documentation: `http://127.0.0.1:8000/docs`

### 3. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`.

## How It Works

1. The user uploads a PDF resume and enters a job description.
2. The React frontend sends both inputs to the FastAPI backend.
3. PyMuPDF extracts text from the PDF.
4. The backend compares detected resume skills against skills found in the job description.
5. The API returns matched skills, missing skills, and a match percentage.
6. The frontend displays the analysis results.

## Current Limitations

- Skill detection relies on a predefined vocabulary.
- Matching is based on text comparison, not a trained AI model.
- Synonyms and variations may not always be recognized.
- Scanned PDFs may require OCR if they do not contain extractable text.
- The match percentage is an indicative skill-match score, not a definitive measure of candidate suitability.

## Future Improvements

- Improve skill matching and synonym recognition.
- Add automated tests.
- Improve handling of scanned PDFs.
- Deploy the frontend and backend for public access.

## Project Status

Core MVP implemented and manually tested.

