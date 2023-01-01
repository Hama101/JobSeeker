import requests
from config import Settings

from io import BytesIO

class Splasher:

    def __init__(self):
        self.settings = Settings()

    def get_logo(self , name : str) : 
        params = {
            "client_id": self.settings.UNSPLASH_CLIENT_ID,
            "query": name,
        }

        response = requests.get(self.settings.UNSPLASH_URL, params=params)
        response.raise_for_status()
        data = response.json()
        results = data["results"]
        if len(results) == 0:
            return None
        logo_url = results[0]["urls"]["small"]
        return logo_url

    def image_bytes(self, url: str):
        print(url)
        return BytesIO(requests.get(url).content)