import pandas as pd
import numpy as np
from data_processing import get_mongo_connection, insert_data_mongo

def get_top_consuming_sectors(collection):
    """
    Retorna os setores que mais consomem energia, água e emitem CO₂,
    ordenando os dados do maior para o menor consumo.
    """
    df = pd.DataFrame(list(collection.find()))
    df_grouped = df.groupby("setor", as_index=False)[["energia_kwh","agua_m3","co2_emissoes"]].sum()
    df_grouped = df_grouped.sort_values(by=["energia_kwh", "agua_m3", "co2_emissoes"], ascending=[False, False, False])
    return df_grouped

 
if __name__ == "__main__": 
    data_path = "../data/dados_sensores_5000.parquet"
    df = pd.read_parquet(data_path, engine="pyarrow")
    collection = get_mongo_connection() 
    print("Conexão com o MongoDB estabelecida e coleção pronta!")
    count = insert_data_mongo(df, collection)
    df_top_consuming_sectors = get_top_consuming_sectors(collection)
    print(df_top_consuming_sectors)