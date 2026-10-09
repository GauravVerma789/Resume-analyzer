from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import UploadFile, File
import pymupdf
from fastapi import Form
from fastapi import HTTPException
from skills import SKILLS
import string
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeRequest(BaseModel):
    job_description: str


@app.get("/")
def home():
    return {"message": "Resume Analyzer API is running"}


@app.post("/analyze")
def analyze_resume(request: ResumeRequest):
    return {"received_job_description": request.job_description}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF file"
        )
    content = await file.read()

    pdf = pymupdf.open(stream=content, filetype="pdf")

    all_text = ""

    for page in pdf:
        all_text = all_text + page.get_text() # type: ignore
    
    all_skills = []

    for category in SKILLS:
        for skill in SKILLS[category]:
            all_skills.append(skill)

    found_skills = []

    jd_skills = []
    jd_words = job_description.lower().translate(
        str.maketrans("", "", string.punctuation)
    ).split()

    for skill in all_skills:
        if skill in jd_words:
            jd_skills.append(skill)

    print(jd_skills)
    print("Total skills:", len(all_skills))
    print("JD words:", jd_words)
    print("Extracted resume text:", all_text[:500])

    for skill in all_skills:
        if skill in all_text.lower():
            found_skills.append(skill)

    matched_skills = []
    missing_skills = []

    for skill in jd_skills:
        if skill in found_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(jd_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(matched_skills) / len(jd_skills)) * 100

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }

