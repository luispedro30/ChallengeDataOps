import pandas as pd
import numpy as np
from pymongo import MongoClient 
import requests

def get_data_api(collection):
    data = list(collection.find())

    for entry in data:
        entry["_id"] = str(entry["_id"]) 
    return data

def insert_data_api(new_data, collection):
    inserted = collection.insert_one(new_data)

    return inserted, collection