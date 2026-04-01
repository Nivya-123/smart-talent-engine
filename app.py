import os
import csv
from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from backend.utils import extract_skills, compare_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store results globally for download
global_results = []

# -------------------------------
# Extract text from PDF
# -------------------------------
def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text

# -------------------------------
# Preprocess text
# -------------------------------
def preprocess_text(text):
    return text.lower()

# -------------------------------
# Calculate similarity
# -------------------------------
def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

# -------------------------------
# HOME ROUTE
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    global global_results
    results = []

    if request.method == "POST":
        jd = request.form["job_description"]
        files = request.files.getlist("resumes")

        jd_text = preprocess_text(jd)

        for file in files:
            if file and file.filename.endswith(".pdf"):
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)

                # Process resume
                resume_text = extract_text_from_pdf(filepath)
                resume_text = preprocess_text(resume_text)

                score = calculate_similarity(resume_text, jd_text)
                skills = extract_skills(resume_text)
                matched, missing = compare_skills(skills, jd_text)

                results.append({
                    "name": file.filename,
                    "score": round(score * 100, 2),
                    "skills": skills,
                    "matched": matched,
                    "missing": missing[:5]
                })

        # Sort by score
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        # Save for download
        global_results = results

    return render_template("index.html", results=results)

# -------------------------------
# DOWNLOAD CSV ROUTE
# -------------------------------
@app.route("/download")
def download():
    file_path = "results.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score", "Skills", "Matched Skills", "Missing Skills"])

        for r in global_results:
            writer.writerow([
                r["name"],
                r["score"],
                ", ".join(r["skills"]),
                ", ".join(r["matched"]),
                ", ".join(r["missing"])
            ])

    return send_file(file_path, as_attachment=True)

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)