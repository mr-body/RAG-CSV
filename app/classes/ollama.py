import requests
import json

class Ollama:
    def __init__(self, url):
        self.url = url
        self.history = []  # Armazena o histórico da conversa

    def generate(self, prompt):
        # Adiciona a nova mensagem do usuário ao histórico
        self.history.append({"role": "user", "content": prompt})

        data = {
            "model": "llama3",
            "prompt": prompt,
            "messages": self.history  # Envia o histórico completo junto com a solicitação
        }

        # Enviando a solicitação POST
        response = requests.post(self.url, json=data, stream=True)
        full_response = ""  # Variável para armazenar a resposta completa

        # Processando a resposta linha por linha
        for line in response.iter_lines():
            if line:
                try:
                    # Decodifica e processa cada linha JSON
                    decoded_line = json.loads(line.decode("utf-8"))

                    # Verifica se há uma resposta do assistente
                    if "response" in decoded_line:
                        # Concatena a resposta parcial do assistente
                        full_response += decoded_line["response"]
                        # Retorna a parte da resposta para o streaming
                        yield json.dumps({"response": decoded_line["response"]}) + "\n"

                    # Verifica se o processamento está concluído
                    if decoded_line.get("done", False):
                        self.history.append({
                            "role": "user",
                            "parts": [prompt]  # O prompt do usuário em formato de lista
                        })
                        self.history.append({
                            "role": "model",
                            "parts": [full_response]  # A resposta do modelo em formato de lista
                        })
                        break

                except json.JSONDecodeError:
                    print("Erro ao decodificar JSON:", line)

    def get_history(self):
        # Retorna o histórico completo da conversa
        return self.history
