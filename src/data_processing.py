import pandas as pd
import numpy as np
from pymongo import MongoClient 
 
def get_mongo_connection(): 
    """ 
    Estabelece uma conexão com o MongoDB local e retorna a coleção 'movies'. 
    """ 
    client = MongoClient("mongodb://localhost:27017/") 
    db = client["greenFlow"] 
    return db["greenFlow"] 

def insert_data_mongo(data, collection): 
    """ 
    Insere um dicionário de dados em uma coleção do MongoDB. 
    """
    collection.delete_many({})  # Limpa a coleção
    data_dicts = [row.to_dict() for _, row in data.iterrows()]
    collection.insert_many(data_dicts)
    return collection.count_documents({})
 
if __name__ == "__main__": 
    data_path = "../data/dados_sensores_5000.parquet"
    df = pd.read_parquet(data_path, engine="pyarrow")
    collection = get_mongo_connection() 
    print("Conexão com o MongoDB estabelecida e coleção pronta!")
    count = insert_data_mongo(df, collection)
    print(count)