from flask import Flask, request
from main import insert_peso, find_all_pesos

app = Flask("OK")

@app.route("/", methods=["GET"])
def olaMundo():
    return {"home":"Pequena API de Teste"}

@app.route("/list/", methods=["GET"])
def list_colecao():
    return find_all_pesos()

@app.route("/insert/", methods=["POST"])
def insert():
    body = request.get_json()

    if("nome" not in body):
        return geraResponse(400, "O parâmetro nome é obrigatório")
    
    if("peso" not in body):
        return geraResponse(400, "O parâmetro peso é obrigatório")

    if("data" not in body):
        return geraResponse(400, "O parâmetro data é obrigatório")

    return insert_peso(body["nome"], body["peso"], body["data"])

def geraResponse(status, msg, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["msg"] = msg

    if (nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run()