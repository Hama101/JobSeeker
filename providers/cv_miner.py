"""
   Here is an explanation of the code:
    1. We import the nltk library and download the stopwords.
    2. We import the ResumeParser from the pyresparser library which is used to extract the resume data.
    3. We import the os library which is used to get the path of the current directory.
    4. We import the Document from the docx library which is used to create a word document.
"""
import nltk
nltk.download('stopwords')

from pyresparser import ResumeParser
from docx import Document
from typing import (
    List
)

class CvMiner:

    def process_cv(self, cv_file : str)-> List[str]:
        # in a try catch block we try to extract the data from the resume
        skills = []
        try:
            # initialize the Document object
            doc = Document()
            # read the resume file to context as file
            with open(cv_file, 'r') as file:
                # load paragraphs from the file
                doc.add_paragraph(file.read())
            # save the document
            doc.save("text.docx")
            # extract the data from the resume usiing the ResumeParser.get_extracted_data() method
            data = ResumeParser('text.docx').get_extracted_data()
            # save the skills in a variable
            skills = data['skills']
        except:
            # if there is an error we try directly to extract the data from the resume
            data = ResumeParser(cv_file).get_extracted_data()
            # save the skills in a variable
            skills = data['skills']

        # unquie values
        skills = list(set(skills))
        
        # return the skills
        return skills