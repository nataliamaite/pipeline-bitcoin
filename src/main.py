from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados
import pandas as pd

def main():
    #Chama o extract.py e pega os dados da API
    dados = extrair_dados()
    #Pega os dados extraídos e envia para o transform.py
    dados_transformados = transformar_dados(dados)
    #Envia o DataFrame resultante para o load.py que insere os dados no PostgreSQL:
    carregar_dados(dados_transformados)

    print("Pipeline executado com sucesso!")


if __name__ == "__main__":
    main()


