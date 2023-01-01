"""
    - this is a controller class that handles the file upload button event
"""
from providers.googler import GoogleJobBank
from providers.cv_miner import CvMiner

from config import Settings
import os

class FileUploader:

    def __init__(self):
        self.google_job_bank = GoogleJobBank()
        self.cv_miner = CvMiner()

    def parse_skills(self , file_path : str):
        # get the most common skill from the resume
        skills = self.cv_miner.process_cv(file_path)
        return skills


class ImageProvider:

    def __init__(self , name : str):
        self.name = name.lower().replace("#","sharp")
        self.settings = Settings()

    @property
    def get_image_path(self) -> str:
        try:
            dir_path = os.path.join(
                self.settings.CURRENT_PATH ,
                self.settings.LANGUAGES_LANGS_DIR ,
                self.name
            )
            if not os.path.exists(dir_path):
                return None
            image_path = os.path.join(
                dir_path ,
                f"{self.name}_64x64.png"
            )
            return image_path
        except Exception as e:
            print(e)
            return None