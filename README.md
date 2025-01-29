# ChallengeDataOps

GreenFlow - Startup Data Challenge

🌱 Sobre o Desafio

Este projeto faz parte do Startup Data Challenge – Insights Sustentáveis com Parquet, onde desenvolvemos uma solução para processar grandes volumes de dados de consumo e fornecer insights úteis para pequenas e médias empresas.

Recebemos um arquivo Parquet contendo dados simulados de sensores ambientais e criamos uma solução para transformar esses dados em métricas e insights relevantes.

📌 Funcionalidades Implementadas

✅ Carregamento dos dados do arquivo dados_sensores_5000.parquet
✅ Processamento dos dados para extrair insights sobre consumo sustentável
✅ Desenvolvimento de um dashboard interativo para visualização dos insights
✅ Geração de relatórios automatizados com estatísticas sobre consumo de energia, água e CO₂

📂 Estrutura do Repositório

📦 GreenFlow-DataChallenge
 ├── 📁 data                  # Arquivo Parquet com os dados brutos
 ├── 📁 notebooks             # Notebooks Jupyter com exploração e análises
 ├── 📁 src                   # Código-fonte da aplicação
 │   ├── data_processing.py   # Processamento e limpeza dos dados
 │   ├── insights.py          # Geração de insights e estatísticas
 │   ├── api.py               # API para fornecer insights via endpoints (opcional)
 │   ├── dashboard.py         # Dashboard interativo
 ├── 📁 reports               # Relatórios gerados automaticamente
 ├── Dockerfile               # Configuração para execução via Docker (extra)
 ├── requirements.txt         # Dependências do projeto
 ├── README.md                # Instruções de uso

🛠 Tecnologias Utilizadas

Python 🐍 (Pandas, PySpark, Matplotlib, Seaborn)

Jupyter Notebook 📓 para exploração inicial dos dados

Streamlit 📊 para desenvolvimento do dashboard interativo

FastAPI 📡 para criação de uma API (opcional)

Docker 🐳 para empacotamento da aplicação (extra)

🚀 Como Rodar o Projeto

1️⃣ Clonar o Repositório

git clone https://github.com/luispedro30/ChallengeDataOps.git
cd ChallengeDataOps

2️⃣ Criar um Ambiente Virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3️⃣ Instalar Dependências

pip install -r requirements.txt

4️⃣ Rodar a Análise Inicial

Abra o Jupyter Notebook e execute os notebooks na pasta notebooks/ para explorar os dados.

5️⃣ Rodar o Dashboard


6️⃣ Rodar a API (Opcional)


📊 Exemplos de Insights Gerados

Empresas que mais consomem energia, água e CO₂

Comparação entre setores e padrões de consumo

Tendências de sustentabilidade

Sugestões de otimização do consumo
