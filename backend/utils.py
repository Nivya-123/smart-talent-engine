import re

# Predefined skills list
SKILLS = [
    "python", "java", "c++", "machine learning",
    "data analysis", "django", "flask",
    "sql", "html", "css", "javascript"
]

# Extract skills from resume
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# Compare resume skills with job description
def compare_skills(resume_skills, jd_text):
    jd_text = jd_text.lower()

    matched = []
    missing = []

    # Find matched skills
    for skill in resume_skills:
        if skill in jd_text:
            matched.append(skill)

    # Extract important words from JD (simple approach)
    jd_words = set(jd_text.split())

    for word in jd_words:
        if word not in resume_skills:
            missing.append(word)

    return matched, missing