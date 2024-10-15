from src.controllers.token_controller import Token_controller
from src.controllers.gmail_id_controller import Gmail_id_controller
from src.controllers.gmail_msg_controller import Gmail_msg_controller
from src.views.token_view import Token_view
from src.views.gmail_id_view import Gmail_id_view
from src.views.gmail_msg_view import Gmail_msg_view
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # Configurações Iniciais
    refresh_token = os.getenv('refresh_token')
    client_secret = os.getenv('client_secret')
    client_id = os.getenv('client_id')
    email = os.getenv('email')
    
    # Recupera o Bearer token de autenticação google.  
    view_token = Token_view()    
    controller_token = Token_controller(view_token)    
    access_token = controller_token.refresh_token(refresh_token, client_secret, client_id)
        
    # Acessa a API do Gmail e recupera os ids de e-mails não lidos.
    view_id_gmail = Gmail_id_view()
    controllerGmail = Gmail_id_controller(view_id_gmail)
    getIdsMsg = controllerGmail.gmail_msgs_id(email, access_token)    
    
    # Get Mensagens do Gmail
    view_msg_gmail = Gmail_msg_view()
    controller_msg_Gmail = Gmail_msg_controller(view_msg_gmail)
    get_msgs_body = controller_msg_Gmail.gmail_msgs_body(email, access_token, getIdsMsg)
    print(get_msgs_body) 
    
if __name__ == '__main__':
    main()