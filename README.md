# 🚀 Smart Talent Selection Engine

An AI-powered web application that analyzes and ranks resumes based on a given job description using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 📌 Features

- 📄 Upload and process multiple resumes (PDF)
- 🧠 Extract skills using text processing
- 📊 TF-IDF based similarity scoring
- 🏆 Rank candidates based on match %
- 📉 Visualize top candidates using charts
- 📥 Download results as CSV
- 🌐 Clean and user-friendly web interface

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- HTML, CSS
- Chart.js

---

## 📂 Project Structure

smart-talent-engine/

├── app.py  
├── backend/  
│   └── utils.py  
├── templates/  
│   └── index.html  
├── static/  
│   └── style.css  
├── resumes/  
├── uploads/  
└── README.md  

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/Nivya-123/smart-talent-engine.git  
cd smart-talent-engine  

---

### 2. Install dependencies

pip install flask scikit-learn PyPDF2  

---

### 3. Run the application

python app.py  

---

### 4. Open in browser

http://127.0.0.1:5000/

---

## 📊 How It Works

1. Extract text from resumes  
2. Clean and preprocess text  
3. Convert text to TF-IDF vectors  
4. Compare with job description  
5. Rank candidates based on similarity score  

---

## 📈 Example Output

1. resume1.pdf → 85% match  
2. resume2.pdf → 72% match  
3. resume3.pdf → 60% match  

---

## 🔮 Future Improvements

- Advanced NLP models (BERT)
- User login system
- Cloud deployment
- Improved UI/UX

---

## 👩‍💻 Author

Nivya Varghese  

---

## ⭐ If you like this project, give it a star!