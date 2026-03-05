import requests
import json
def btc_info():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    dic_requisicao = requisicao.json()
    btc = dic_requisicao['BTCBRL']
    btc_preco = btc['bid']
    return btc_preco

def obter():
    with open("devices.json", "r") as a:    
        dados = json.load(a)
        return dados
        

def salvar(arquivo):
    with open("devices.json", "r") as s:    
        dados = json.load(s)
        dados.append(arquivo)
    with open("devices.json", "w") as s:
        json.dump(dados, s, indent=4)

def verificador_id(comparacao=0):
    a = obter()
    for d in a:
        _id = d["id"]
        if _id == comparacao:
            return _id
    return False
def verificador_senha(busca_id):
    a = obter()
    for d in a:
        _id = d["id"]
        if _id == busca_id:
            senha_real = d["senha"]
            return senha_real
        
def busca_usuario(userid):
    a = obter()
    for d in a:
        if d["id"] == userid:
            return d