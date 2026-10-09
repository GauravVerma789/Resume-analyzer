import pymupdf

pdf = pymupdf.open("resume.pdf")

all_text = ""

for page in pdf:
    all_text = all_text + page.get_text() # type: ignore

skills = ["python", "java", "sql", "react","docker"]
required_skills=["python", "sql", "docker", "fastapi"]
jd_skills=[]
matched_skills=[]
missing_skills=[]

job_description = """
We are looking for a Python developer with SQL,
Docker and FastAPI knowledge.
"""

def extract_skills(all_text, skills):
    found_skills = []

    for skill in skills:
        if skill in all_text.lower():
            found_skills.append(skill)

    return found_skills

for reqSkill in required_skills:
     if(reqSkill in job_description.lower()):
        jd_skills.append(reqSkill)
        
found_skills = extract_skills(all_text,skills)

for skill in jd_skills:
    if(skill in found_skills):
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)


print("matched skills " , matched_skills)
print("missing skills " ,missing_skills)

def calculate_score(matched, required):
    if required == 0:
        return 0
    return (((matched / required)) * 100)


print(calculate_score(len(matched_skills),len(jd_skills)))