# RAG-CSV
Treinamente de IA usando RAG (Retrieval-Augmented Generation) 
# O que é a geração aumentada de recuperação? 
Retrieval-Augmented Generation (RAG) é o processo de otimizar a saída de um grande modelo de linguagem, de forma que ele faça referência a uma base de conhecimento confiável fora das suas fontes de dados de treinamento antes de gerar uma resposta. Grandes modelos de linguagem (LLMs) são treinados em grandes volumes de dados e usam bilhões de parâmetros para gerar resultados originais para tarefas como responder a perguntas, traduzir idiomas e concluir frases. A RAG estende os já poderosos recursos dos LLMs para domínios específicos ou para a base de conhecimento interna de uma organização sem a necessidade de treinar novamente o modelo. É uma abordagem econômica para melhorar a produção do LLM, de forma que ele permaneça relevante, preciso e útil em vários contextos.


## install
````
git clone git@github.com:mr-body/RAG-CSV.git morning

cd morning

python3 -m venv myvenv

source myvenv/bin/active

pip install -r rqeuirimente.txtx
````

note:you need create .env file and put yor API_KEY if you want use Gmini
GOOGLE_API_KEY = ..........
OLLAMA_API_HOST = ........

## Baixar docker do ollama com llama3

````
