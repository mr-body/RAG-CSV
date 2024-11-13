import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a chave da API do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Função para carregar o CSV e gerar embeddings
def carregar_csv_e_gerar_embeddings(caminho_csv, coluna_texto):
    # Carregar os dados do CSV
    df = pd.read_csv(caminho_csv)
    textos = df[coluna_texto].tolist()
    
    # Inicializar o modelo de embeddings
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Gerar os embeddings dos textos
    embeddings = embedder.encode(textos)
    
    return df, textos, embeddings

# Função para buscar o texto mais relevante baseado na similaridade
def buscar_relevante(query, embeddings, textos):
    # Gerar o embedding da consulta
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = embedder.encode([query])
    
    # Calcular a similaridade de cosine
    similarity_scores = cosine_similarity(query_embedding, embeddings)
    
    # Encontrar o índice do texto mais similar
    most_similar_index = np.argmax(similarity_scores)
    
    # Retornar o texto mais relevante
    return textos[most_similar_index]

# Função para iniciar o chat com o modelo Gemini
def iniciar_chat_gemini(conteudo_relevante, query):
    # Criar a configuração do modelo
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Criar o modelo Gemini
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Iniciar a sessão de chat
    chat_session = model.start_chat(history=[])
    
    # Criar a mensagem com o conteúdo relevante
    mensagem_completa = f"Com base nas informações do CSV: {conteudo_relevante}\nAgora, responda à consulta: {query}"
    
    # Enviar a consulta ao modelo
    response = chat_session.send_message(mensagem_completa)
    
    return response.text

def main():
    # Caminho do arquivo CSV e nome da coluna que contém os textos
    caminho_csv = "dados.csv"
    coluna_texto = "coluna_texto"  # Substitua com o nome da coluna relevante

    # Passo 1: Carregar CSV e gerar embeddings
    df, textos, embeddings = carregar_csv_e_gerar_embeddings(caminho_csv, coluna_texto)

    # Passo 2: Solicitar a consulta ao usuário
    query = input("Digite sua consulta: ")

    # Passo 3: Buscar o texto mais relevante no CSV
    texto_relevante = buscar_relevante(query, embeddings, textos)
    print(f"\033[32mTexto relevante encontrado:\033[33m {texto_relevante}\033[0m\n")

    # Passo 4: Usar o Gemini para gerar uma resposta com base no contexto
    resposta = iniciar_chat_gemini(texto_relevante, query)
    
    # Exibir a resposta gerada
    print("...............................\nResposta gerada pelo Gemini:\n...............................\n")
    print(f"\033[34m{resposta}\033[0m")

if __name__ == "__main__":
    main()
