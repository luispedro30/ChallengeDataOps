import pandas as pd
import numpy as np
from pymongo import MongoClient 
 
def get_mongo_connection(): 
    """ 
    Estabelece uma conexão com o MongoDB local e retorna a coleção 'movies'. 
    """ 
    client = MongoClient("mongodb://mongodb:27017/") 
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