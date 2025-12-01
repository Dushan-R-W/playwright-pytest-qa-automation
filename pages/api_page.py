import requests


class APIpage:
    def __init__ (self, base_url):
        self.base_url = base_url

    def request_get_no_redirect(self, href):
        return requests.get(f"{self.base_url}{href}", allow_redirects=False)
    
    def request_get(self, href):
        return requests.get(f"{self.base_url}{href}")
    
    def request_post(self, href, payload):
        return requests.post(f"{self.base_url}{href}", data=payload)
    

