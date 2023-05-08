import os
import sys
import requests
import base64
import json
if __name__ == "__main__":
    import inspect
    file_path = os.path.dirname(
        os.path.realpath(
            inspect.getfile(
                inspect.currentframe())))
    sys.path.insert(0, os.path.join(file_path, '../'))
import configloader
from tools.base import aes,rsa_utils

class request_handler:
    def __init__(self) -> None:
        self.c = configloader.config()
        self.url = self.c.getkey("server_endpoint")
        self.token = self.c.getkey("bearer_token")

    def post_request(self,path,data):
        data = json.dumps(data)
        headers = {
            "Authorization":"Bearer "+self.token,
            "Content-Type":"application/json"
        }
        url = self.url + path
        r = requests.post(url,data=data,headers=headers)
        if r.status_code != 200:
            raise Exception("Request failed")
        
        return r.json()

if __name__ == "__main__":
    r = request_handler()
    data = r.post_request("/v0/ping",{})
    print(data)