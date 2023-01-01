"""
    - this is a controller class that handles the file upload button event
"""
from providers.googler import GoogleJobBank
from providers.cv_miner import CvMiner



class FileUploader:

    def __init__(self):
        self.google_job_bank = GoogleJobBank()
        self.cv_miner = CvMiner()

    def parse_skills(self , file_path : str):
        # get the most common skill from the resume
        skills = self.cv_miner.process_cv(file_path)
        return skills