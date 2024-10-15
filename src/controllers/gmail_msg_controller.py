from ..models.gmail_msg_model import Gmail_msg_model

class Gmail_msg_controller:
    def __init__(self, view):
        self.view = view

    def gmail_msgs_body(self, email, accessToken, getIdsMsg):
        # Instancia o model
        gmail_model = Gmail_msg_model(email, accessToken, getIdsMsg)
        
        # Obtém os ids de threads e mensagens (fazendo a requisição ao endpoint)
        response = gmail_model.get_msgs_body()
                
        # Passa os resultados para a view
        return self.view.list_of_emails(response)