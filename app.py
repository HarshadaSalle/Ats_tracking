# import libraries
from dotenv import load_dotenv
from pdf2image.exceptions import PDFInfoNotInstalledError

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64
import io 


poppler_path = r"D:\poppler\poppler-24.08.0\Library\bin"


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=poppler_path)
        first_page=images[0]
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


#streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text =st.text_area("Job Description:", key="input")
uploaded_files=st.file_uploader("upload your resume(PDF)...", type=["pdf"])

if uploaded_files is not None:
    st.write("PDF Uploaded Successfully")


submit1=st.button("Tell Me About the Resume")

submit2=st.button("How Can I Improve my Skills")

#submit3=st.button("What are the keywords That are Missing")

submit4=st.button("Percentage march")

input_prompt1 ="""
You are an experienced Technical human resource manager with tech experiense in the field of Data Science,
full stack web development, big data engineering, data analyst, devops your  task is to review the provide
resume agianst the job description for these profiles.
please share your professional evaluation on whether the candidate's profile alligns with the 
role.
Highlight the strengths and weaknesses of the applicant to the specified jib requirements.
"""



input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science , Full stack web development ,big data engineering, data analyst
and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_files is not None:
        pdf_content=input_pdf_setup(uploaded_files)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("the response is")
        st.write(response)
    
    else:
        st.write("please upload the resume")


elif submit4:
    if uploaded_files is not None:
        pdf_content=input_pdf_setup(uploaded_files)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("the response is")
        st.write(response)
    
    else:
        st.write("please upload the resume")