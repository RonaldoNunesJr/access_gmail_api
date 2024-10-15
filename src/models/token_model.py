from ..components.req import Req

class Token_model:
    def __init__(self, refresh_token:str, client_secret:str, client_id:str):
        self.endpoint = "https://oauth2.googleapis.com/token"
        self.refresh_token = refresh_token
        self.client_secret = client_secret
        self.client_id = client_id
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    def get_token(self):
        # Prepara o corpo da requisição
        body = {
            'refresh_token': self.refresh_token,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'client_id': self.client_id    
        }        
        req = Req(self.endpoint, body, self.headers, "POST")       
        return req.request()