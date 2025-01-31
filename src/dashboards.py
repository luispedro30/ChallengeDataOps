import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo Parquet
data_path = "../data/dados_sensores_5000.parquet"
df = pd.read_parquet(data_path, engine="pyarrow")

# Exibir as primeiras linhas para inspecionar o formato
st.title("Análise de Consumo de Energia, Água e CO₂")

# Exibir as primeiras linhas dos dados
st.subheader("Exemplo de Dados")
st.write(df.head())

# Exibir os nomes das colunas para entender melhor a estrutura
st.subheader("Nomes das Colunas")
st.write(df.columns)

