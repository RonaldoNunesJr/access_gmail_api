from ..models.token_model import Token_model

class Token_controller:
    def __init__(self, view):
        self.view = view

    def refresh_token(self, refresh_token:str, client_secret:str, client_id:str):
        # Instancia o model
        token_model = Token_model(refresh_token, client_secret, client_id)
        
        # Obtém o token (fazendo a requisição ao endpoint)
        status, reason, response = token_model.get_token()
        
        # Passa os resultados para a view
        return self.view.display_response(status, reason, response)