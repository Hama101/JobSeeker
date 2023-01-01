"""
Base model for all models
"""

import json
from config import Settings
import os

class BaseModel:
    """
    Base model for all models
    """

    def __init__(self):
        self.settings = Settings()
        self.filepath = os.path.join(
            self.settings.CURRENT_PATH,
            self.settings.DATABASE_URL,
        )

    def save(self, data, filename):
        """
        Save data to a file
        """
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load(self, filename):

        """
        Load data from a file
        """
        with open(filename, 'r') as file:
            return json.load(file)

    def get_all(self):

        """
        Get all data from a file
        """
        return self.load(self.filepath)


    