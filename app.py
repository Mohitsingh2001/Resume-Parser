import spacy
import streamlit as st
from PyPDF3 import PdfFileReader

# Load the Spacy model for resume parsing
nlp =spacy.load("/content/drive/MyDrive/output/model-best")

def extract_info(resume_text):
    # Process the resume text with Spacy
    doc = nlp(resume_text)
    
    # Extract information from the resume
    education = []
    work_experience = []
    skills = []
    Name = []
    Designation = []
    Location = []
    Companies_worked_at = []
    Email_Address = []
    college_name = []
    for ent in doc.ents:
        if ent.label_ == "Degree":
            education.append(ent.text)
        elif ent.label_ == "Years of Experience":
            work_experience.append(ent.text)
        elif ent.label_ == "Skills":
            skills.append(ent.text)
        elif ent.label_ == "Name":
            Name.append(ent.text) 
        elif ent.label_ == "Companies worked at":
            Companies_worked_at.append(ent.text)  
        elif ent.label_ == "Location":
            Location.append(ent.text) 
        elif ent.label_ == "Designation":
            Location.append(ent.text) 
        elif ent.label_ == "Email Address":
            Location.append(ent.text)   
        elif ent.label_ == "college name":
            Location.append(ent.text)                       

    return education, work_experience, skills, Name, Location, Companies_worked_at, Designation, Email_Address, college_name

def main():
    st.set_page_config(page_title="Resume Parser", page_icon=":guardsman:", layout="wide")
    st.title("Resume Parser")
    
    # Get the resume text from the user
   # resume_text = st.text_area("Paste your resume text here")
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf_file is not None:
        pdf_reader = PdfFileReader(pdf_file)
        resume_text = pdf_reader.getPage(0).extractText()
        st.write(resume_text)

    
    # Extract information from the resume
    if st.button("Extract"):
        education, work_experience, skills, Name, Designation, Location, Companies_worked_at, Email_Address, college_name = extract_info(resume_text)
        
        # Display the results
        st.header("Education")
        for edu in education:
            st.write("- " + edu)
        st.header("Work Experience")
        for exp in work_experience:
            st.write("- " + exp)
        st.header("Skills")
        for skill in skills:
            st.write("- " + skill)
        st.header("Name")
        for name in Name:
            st.write("- " + name)
        st.header("Location")
        for location in Location:
            st.write("- " + location)
        st.header("Companies Worked")
        for cwa in Companies_worked_at:
            st.write("- " + cwa)
        st.header("Designation")
        for desg in Designation:
            st.write("- " + desg)            
        st.header("Contacts")
        for email in Email_Address:
            st.write("- " + email)     
        st.header("college name")
        for clg in college_name:
            st.write("- " + clg)                   

if __name__ == "__main__":
    main()
