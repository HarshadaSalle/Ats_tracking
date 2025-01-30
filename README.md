# Ats_tracking

# AI-Powered ATS Resume Screening System

## Introduction
The **AI-Powered ATS Resume Screening System** is a smart application that leverages **AI and NLP** to analyze resumes and compare them with job descriptions. It provides valuable insights such as **resume evaluation, missing keywords, and match percentage**, helping job seekers optimize their resumes for better ATS compatibility.

## Tech Stack
- **Programming Language:** Python
- **Framework:** Streamlit
- **AI Model:** Google Gemini API
- **NLP Libraries:** spaCy, NLTK
- **PDF Processing:** pdf2image, PIL (Pillow)
- **Environment Management:** dotenv

## Features
✅ Upload a resume in **PDF format**  
✅ Compare the resume against a **job description**  
✅ Get an AI-generated **resume evaluation** (strengths & weaknesses)  
✅ Get a **match percentage** with missing keywords  
✅ Interactive **Streamlit-based UI**  



### **1. Create a Virtual Environment (Optional but Recommended)**
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```
### **2. Install Dependencies**
```
pip install -r requirements.txt
```
### **3. Set Up Environment Variables**
Create a `.env` file and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### **4. Run the Streamlit App**
```sh
streamlit run app.py

## How It Works
1️⃣ Upload your resume (PDF format).  
2️⃣ Enter a job description in the text area.  
3️⃣ Click **"Tell Me About the Resume"** for an AI-powered evaluation.  
4️⃣ Click **"Percentage Match"** to see how well your resume fits the job.  
5️⃣ The AI provides a match percentage, missing keywords, and suggestions.  

## Future Enhancements
- ✅ Support for **multiple resume formats** (DOCX, TXT)
- ✅ AI-powered **resume ranking system**
- ✅ Integration with **LinkedIn API** for job recommendations
