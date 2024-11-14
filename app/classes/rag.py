import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class Rag:
    def __init__(self, database):
        self.data = database

    # Função para carregar o CSV e gerar embeddings
    def carregar_csv_e_gerar_embeddings(self, coluna_texto):
        # Carregar os dados do CSV
        df = pd.read_csv(self.data)
        textos = df[coluna_texto].tolist()
        
        # Inicializar o modelo de embeddings
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Gerar os embeddings dos textos
        embeddings = embedder.encode(textos)
        
        return df, textos, embeddings

    # Função para buscar o texto mais relevante baseado na similaridade
    def buscar_relevante(self, query, embeddings, textos):
        # Gerar o embedding da consulta
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = embedder.encode([query])
        
        # Calcular a similaridade de cosine
        similarity_scores = cosine_similarity(query_embedding, embeddings)
        
        # Encontrar o índice do texto mais similar
        most_similar_index = np.argmax(similarity_scores)
        
        # Retornar o texto mais relevante
        return textos[most_similar_index]
    
    def get_text_more_relative(self, query, coluna):
        df, textos, embeddings = self.carregar_csv_e_gerar_embeddings(coluna)
        return self.buscar_relevante(query, embeddings, textos)
