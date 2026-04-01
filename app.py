from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    
    return text

# STEP 2: Preprocess text
def preprocess_text(text):
    return text.lower()

# STEP 3: TF-IDF
def apply_tfidf(texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors

# STEP 4: Similarity (Resume vs JD)
def calculate_similarity(resume_text, jd_text):
    texts = [resume_text, jd_text]
    vectors = apply_tfidf(texts)
    
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

# MAIN
if __name__ == "__main__":
    
    resume_path = "resume1.pdf"

    # Example Job Description
    job_description = """
    Looking for a Python developer with knowledge in machine learning,
    data analysis, and web development.
    """

    try:
        # Extract Resume
        resume_text = extract_text_from_pdf(resume_path)
        resume_text = preprocess_text(resume_text)

        # Preprocess JD
        jd_text = preprocess_text(job_description)

        # Calculate similarity
        score = calculate_similarity(resume_text, jd_text)

        print("✅ Resume Processed")
        print("✅ Similarity Score:", round(score * 100, 2), "%")

    except Exception as e:
        print("Error:", e)