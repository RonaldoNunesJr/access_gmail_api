from ..models.gmail_id_model import Gmail_id_model

class Gmail_id_controller:
    def __init__(self, view):
        self.view = view

    def gmail_msgs_id(self, email, accessToken):
        # Instancia o model
        gmail_model = Gmail_id_model(email, accessToken)
        
        # Obtém os ids de threads e mensagens (fazendo a requisição ao endpoint)
        status, reason, response = gmail_model.get_msgs_id()
        
        # Passa os resultados para a view
        return self.view.display_response(status, reason, response)