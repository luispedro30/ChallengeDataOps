import pandas as pd
import numpy as np

def get_top_consuming_sectors(collection):
    """
    Retorna os setores que mais consomem energia, água e emitem CO₂,
    ordenando os dados do maior para o menor consumo.
    """
    df = pd.DataFrame(list(collection.find()))
    df_grouped = df.groupby("setor", as_index=False)[["energia_kwh","agua_m3","co2_emissoes"]].sum()
    df_grouped = df_grouped.sort_values(by=["energia_kwh", "agua_m3", "co2_emissoes"], ascending=[False, False, False])
    return df_grouped
 

def get_top_consuming_company(collection):
    """
    Retorna as empresas que mais consomem energia, água e emitem CO₂,
    ordenando os dados do maior para o menor consumo.
    """
    df = pd.DataFrame(list(collection.find()))
    df_grouped = df.groupby("empresa", as_index=False)[["energia_kwh","agua_m3","co2_emissoes"]].sum()
    df_grouped = df_grouped.sort_values(by=["energia_kwh", "agua_m3", "co2_emissoes"], ascending=[False, False, False])
    return df_grouped


def get_quantity_companys_by_sector(collection):
    """
    Retorna a quantidade de empresas por setor.
    """
    df = pd.DataFrame(list(collection.find()))
    df_grouped = df.groupby("setor", as_index=False)["empresa"].nunique().rename(columns={"empresa": "numero_empresas"})
    return df_grouped
    