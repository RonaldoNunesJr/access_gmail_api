from ..components.req import Req

class Gmail_id_model:
    def __init__(self, email:str, accessToken):        
        token_type = accessToken['response']['token_type']
        token = accessToken['response']['access_token']
        
        self.endpoint = f"https://www.googleapis.com/gmail/v1/users/me/messages?q=is:unread"        
        self.headers = {            
            "Authorization": f'{token_type} {token}'
        }
    
    def get_msgs_id(self):
        # Prepara o corpo da requisição
        body = {}        
        req = Req(self.endpoint, body, self.headers, "GET")       
        return req.request()