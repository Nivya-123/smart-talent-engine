import os
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    
    return text

# Preprocess text
def preprocess_text(text):
    return text.lower()

# Calculate similarity
def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

# MAIN
if __name__ == "__main__":
    
    resumes_folder = "resumes"

    job_description = """
    Looking for a Python developer with skills in machine learning,
    data analysis, and backend development.
    """

    jd_text = preprocess_text(job_description)

    results = []

    # Loop through all resumes
    for file in os.listdir(resumes_folder):
        if file.endswith(".pdf"):
            path = os.path.join(resumes_folder, file)

            resume_text = extract_text_from_pdf(path)
            resume_text = preprocess_text(resume_text)

            score = calculate_similarity(resume_text, jd_text)

            results.append((file, score))

    # Sort by score (highest first)
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n🎯 Candidate Ranking:\n")

    for i, (name, score) in enumerate(results):
        print(f"{i+1}. {name} → {round(score*100, 2)}% match")