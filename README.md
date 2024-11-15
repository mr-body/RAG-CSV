# RAG-CSV
**Treinamento de IA usando RAG (Retrieval-Augmented Generation)**

## O que é Geração Aumentada por Recuperação (RAG)?

**Retrieval-Augmented Generation (RAG)** é uma técnica que aprimora a saída de um modelo de linguagem (LLM) ao permitir que ele consulte uma base de conhecimento externa antes de gerar uma resposta. Em vez de depender apenas dos dados nos quais o modelo foi treinado, ele pode acessar fontes externas de dados, como bancos de dados ou documentos específicos, para fornecer respostas mais precisas e contextualmente relevantes.

### Como funciona?

Grandes modelos de linguagem, como os LLMs, são treinados em grandes volumes de dados e possuem bilhões de parâmetros. Eles são projetados para realizar tarefas como:

- Responder perguntas
- Traduzir idiomas
- Completar frases

No entanto, esses modelos podem não ter informações específicas de domínios ou de contextos externos que não foram cobertos durante o treinamento. A técnica de RAG resolve esse problema ao permitir que o modelo recupere informações de uma base de dados externa (ou interna) antes de gerar uma resposta, garantindo maior precisão e relevância.

O **RAG** oferece uma maneira econômica de aumentar o desempenho do modelo sem a necessidade de re-treiná-lo, mantendo-o relevante e útil em diferentes contextos, como domínios especializados ou bases de conhecimento privadas de organizações.

## Pré-requisitos

Antes de começar, certifique-se de que você tem:

- Python 3.7 ou superior
- Docker (caso queira usar o Ollama com Llama3)
- Uma chave de API para o **Gmini** e o **Ollama** (se necessário)

## Como instalar

1. **Clone o repositório:**

   Execute o comando abaixo para clonar o repositório do projeto.

   ```bash
   git clone git@github.com:mr-body/RAG-CSV.git morning 
Acesse o diretório do projeto:

Navegue para o diretório onde você clonou o repositório.
  ````
  cd morning
  ````

# Crie um ambiente virtual:

Para evitar conflitos de dependências, é recomendável criar um ambiente virtual Python.
  ````
python3 -m venv myvenv
  ````
Ative o ambiente virtual:

No Linux/macOS:
  ````
source myvenv/bin/activate
  ````
No Windows:
  ````
myvenv\Scripts\activate
  ````
Instale as dependências:

Instale as dependências necessárias usando o pip.

    pip install -r requirements.txt
Nota: Se você planeja usar a funcionalidade Gmini, precisará configurar suas chaves de API.

# Configuração do Ambiente

Criação do arquivo .env:
Para usar o Gmini ou Ollama, você precisa fornecer suas chaves de API. Crie um arquivo chamado .env no diretório raiz do projeto e adicione as seguintes variáveis de ambiente:
```bash
GOOGLE_API_KEY=seu_google_api_key
OLLAMA_API_HOST=seu_ollama_api_host
```

Baixar e configurar o Docker (caso queira usar Ollama com Llama3):

Se você deseja usar o Ollama com o Llama3, você precisará instalar o Docker e configurar o container.

# Baixe a imagem Docker do Ollama
    docker pull ollama/ollama

# Execute o container Ollama
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Acesse o container e inicie o Llama3
    docker exec -it ollama ollama run llama3
