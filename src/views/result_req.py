import json

class Result_req:
    def display_response(self, status, reason, response):
        # Exibe os resultados da requisição
        return {
            "status": status,
            "reason": reason,
            "response": json.loads(response)
        }
