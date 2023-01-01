from config import Settings
import requests
import json

from typing import (
    List,
    Dict,
)


class GoogleJobBank:
    def __init__(self):
        self.settings = Settings()
        self.job_url = self.settings.JOB_URL
        self.client = requests

    def get_job_url(self):
        return self.job_url

    def fetch_jobs(self ,
        title : str,
        only_remote : bool = False
    ) -> List[Dict]:
    
        # check this video for more info on how to use the api   
        url = f"{self.job_url}q={title}&page_size=20"
        # print the url on green color
        print(f"\033[92m{url}\033[00m")
        # scrape the data from the google jobs api
        # # make a request to the api
        r = self.client.get(url = url)
        # print json data in a good format
        jobs = r.json().get('jobs' , [])
        if not jobs:
            print("No data found")
            return []
        # get only that have remote in the location
        if only_remote:
            jobs = [job for job in jobs if job.get('has_remote', False)]
        return [
            {
                "title" : job.get('title', None),
                "company_name": job.get('company_name', None),
                "summary": job.get('description', None),
                "apply_url": job.get('apply_url', None),
            }
            for job in jobs
        ]