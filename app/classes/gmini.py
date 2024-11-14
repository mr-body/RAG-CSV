import google.generativeai as genai

class Gmini:
    def __init__(self, key):
        self.key = key
        self.history = []  # To store conversation history

        # Configure the API key
        try:
            genai.configure(api_key=self.key)
        except Exception as e:
            raise ValueError(f"Error configuring Google API: {str(e)}")

    def generate(self, prompt):
        # Define the generation configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        # Create the Gemini model instance
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        # Start the chat session using the stored conversation history
        chat_session = model.start_chat(history=self.history)
        
        # Send the user prompt to the model
        response = chat_session.send_message(prompt)
        
        # Adicionar a nova interação ao histórico para o contexto futuro
        self.history.append({
            "role": "user",
            "parts": [prompt]  # O prompt do usuário em formato de lista
        })
        self.history.append({
            "role": "model",
            "parts": [response.text]  # A resposta do modelo em formato de lista
        })

        # Return the assistant's response
        return response.text
