from .result_req import Result_req
import json
import re 
import base64

class Gmail_msg_view (Result_req):
    pass

    def display_response(self, status, reason, response):
        # Exibe os resultados da requisição
        return {
            "status": status,
            "reason": reason,
            "response": response
        }

    def list_of_emails(self, content:list):
        # Exibe os resultados da requisição
        list_content = []        
        if len(content) > 0:
            for n in content:
                            
                list_content.append(self.display_response(                 
                    content[n]['status'],
                    content[n]['reason'],
                    self.filter_response_msg(content[n]['response'])
                ))           
            return list_content
        else: 
            return {
                "0": {
                    "status": 200,
                    "reason": "OK",
                    "response": "Não há e-mails na caixa de entrada"
                }
            }
 
    def clean_email_body(self, body):
        signature_patterns = [
            r'--\s*$',  # separador "--"            
            r'^Obrigado,.*$',  # "Thanks"
            r'^Atenciosamente,.*$',  # "Atenciosamente"
            r'^Att,.*$',  # "att"
            r'^Sent from my.*$',  # "Sent from my iPhone"
            r'^Enviado do meu.*$',  # "Sent from my iPhone"
        ]
    
        # Itera sobre os padrões e remove a assinatura
        for pattern in signature_patterns:
            body = re.split(pattern, body, flags=re.MULTILINE)[0]
    
        return body
    
    def filter_response_msg (self, response):
        responseLoad = json.loads(response)
        #print(responseLoad)
        delivered_to = '' 
        body_data = None
        subjetc = ''
        verify_infos_headers = []
        for n in responseLoad['payload']['headers']:
            if n['name'] == 'From':
                delivered_to = n['value']
                verify_infos_headers.append('from')
            if n['name'] == 'Subject':
                subjetc = n['value']
                verify_infos_headers.append('subject')
            
            if all(item in verify_infos_headers for item in ['subject', 'from']):
                break        
            
        for n in responseLoad['payload']['parts']:
            if n['mimeType'] == 'text/plain':
                body_data = n['body']['data']
                break
                  
        if body_data is not None:     
            body_data = base64.b64decode(body_data)
                 
        pattern = r"([a-zA-Z\s]+)\s<([\w\.-]+@[\w\.-]+)>"
        
        match = re.match(pattern, delivered_to)
        if match:
            name = match.group(1)
            email = match.group(2)        
        
        id = responseLoad['id']
        threadId = responseLoad['threadId']
        body_data = self.clean_email_body(body_data.decode('utf8')) 
                                     
        return {
            'id': id,
            'threadId': threadId,
            'titleEmail': subjetc,
            'fromEmail': email,
            'fromName': name,
            'body': body_data
        }
