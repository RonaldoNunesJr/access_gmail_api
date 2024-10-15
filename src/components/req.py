from urllib import request, parse

class Req:
    def __init__(self, endpoint:str, body:dict, headers:dict, method:str):        
        self.endpoint = endpoint
        self.body = parse.urlencode(body).encode('utf-8')     
        self.headers = headers
        self.method = method
                
        
    def request(self):
        
        # Faz a requisição POST para o endpoint
        req = request.Request(url=self.endpoint, data=self.body, headers=self.headers, method=self.method)
        
        # Retorna a resposta
        with request.urlopen(req) as f:
            response = f.read().decode('utf-8')
            status = f.status
            reason = f.reason
        return status, reason, response