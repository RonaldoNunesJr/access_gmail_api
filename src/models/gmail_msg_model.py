from ..components.req import Req

class Gmail_msg_model:
    def __init__(self, email:str, access_token, get_ids_msg):        
        token_type = access_token['response']['token_type']
        token = access_token['response']['access_token']
        
        if get_ids_msg['response']['resultSizeEstimate'] == 0:
            self.filtered_ids = []
        else:    
            id_list = get_ids_msg['response']['messages']
            
            self.filtered_ids = [item['id'] for item in id_list]
            self.email = email
        
            self.endpoint = f"https://gmail.googleapis.com/gmail/v1/users"        
            self.headers = {            
                "Authorization": f'{token_type} {token}',
                "Content-Type": 'application/x-www-form-urlencoded'
            }
    
    def get_msgs_body(self):
        # Prepara o corpo da requisição        
        content = {}
        if len(self.filtered_ids) > 0:
            for n in self.filtered_ids:
                endpoint = f'{self.endpoint}/{self.email}/messages/{n}'
                body = {}        
                req = Req(endpoint, body, self.headers, "GET")
                status, reason, response = req.request()
                content[n] = {
                    'status': status,
                    'reason': reason,
                    'response': response 
                }    
        
        return content