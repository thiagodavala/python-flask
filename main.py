import pymongo
import json
import os
from pymongo import MongoClient

def get_colecao():
    client = MongoClient("mongodb+srv://"+os.environ.get('USER')+":teste1234@cluster0.fachx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.gatos
    return db["controlePeso"]

def insert_peso(nome, peso, data):
    get_colecao().insert_one({"nome": nome, "peso": peso, "data": data})
    return {"nome": nome, "peso": peso, "data": data}

def find_all_pesos():
    pesos = []
    for peso in get_colecao().find():
        pesos.append(peso["nome"])

    return json.dumps(pesos)