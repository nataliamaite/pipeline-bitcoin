import requests

def extrair_dados():
    url = "https://www.mercadobitcoin.net/api/BTC/ticker/"

    resposta = requests.get(url)

    dados = resposta.json()

    return dados