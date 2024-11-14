from flask import Flask, Blueprint, request, Response, stream_with_context, jsonify
from dotenv import load_dotenv
from classes.ollama import Ollama
from classes.gmini import Gmini
from classes.rag import Rag
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Create Blueprint for the API
morning_bp = Blueprint('morning', __name__)

# Instances of Ollama and Gmini classes (http://localhost:11434/api/generate)
ollama = Ollama(os.getenv("OLLAMA_API_HOST"))
gmini = Gmini(os.getenv("GOOGLE_API_KEY"))

training = Rag("training/dados.csv")

@app.route('/')
def index():
    return "<h1>API route</h1>"

@morning_bp.route('/ollama/api/generate/', methods=['POST'])
def generate_ollama():
    if not request.json or 'prompt' not in request.json:
        return jsonify({'error': 'O campo "prompt" é obrigatório'}), 400

    prompt = request.json['prompt']

    prompt = request.json['prompt']

    query = training.get_text_more_relative(prompt, "coluna_texto")
    
    message = f"Com base nas informações do CSV: {query}\nAgora, responda à consulta: {prompt}"
    
    def generate_stream():
        # Assuming ollama.generate is a generator that yields parts of the response
        for chunk in ollama.generate(message):
            yield chunk  # Yield each part of the response

    return Response(generate_stream(), content_type='application/json')

@morning_bp.route('/gmini/api/generate/', methods=['POST'])
def generate_gmini():
    if not request.json or 'prompt' not in request.json:
        return jsonify({'error': 'O campo "prompt" é obrigatório'}), 400

    prompt = request.json['prompt']

    query = training.get_text_more_relative(prompt, "coluna_texto")
    
    message = f"Com base nas informações do CSV: {query}\nAgora, responda à consulta: {prompt}"

    try:
        response = gmini.generate(message)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Register blueprint in the app
app.register_blueprint(morning_bp, url_prefix='/morning')

if __name__ == '__main__':
    app.run(debug=True)
