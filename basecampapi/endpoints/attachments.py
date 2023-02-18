import os
from mimetypes import MimeTypes

import requests

from ..basecamp import Basecamp

class Attachments(Basecamp):
    def __init__(self):
        self.files = {}
        self.__base_url = self._Basecamp__base_url
        self.__credentials = Basecamp._Basecamp__credentials
    
    def upload_file(self, path: str, filename):
        '''
        Uploads a file to Basecamp's servers and saves the file sgid in Basecamp().files.

        Parameters:
            path (str): Path to file you wish to upload.
            filename: Name of your file.
        '''
        
        attachments_url = f"{self.__base_url}/attachments.json?name={path}"
        file_size = os.path.getsize(path)
        mime = MimeTypes().guess_type(path)[0]
        headers = {
            'Authorization': 'Bearer '+ self.__credentials['access_token'],
            "Content-Type": mime,
            "Content-Length": str(file_size)
            }

        with open(path, "rb") as file_bytes:
            response = requests.post(attachments_url, headers=headers, data=file_bytes)
        if not response.ok:
            raise Exception(f"Status code: {response.status_code}. {response.reason}. Error text: {response.text}.")
        else:
            sgid = response.json()['attachable_sgid']
        
        self.files[filename] = {
            "filename": filename,
            "file_size": str(file_size),
            "content-type": mime,
            "sgid": sgid
        }