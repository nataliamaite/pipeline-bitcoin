import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():

    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conexao

def carregar_dados(df):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO bitcoin (
            par_moedas,
            preco_ultimo,
            preco_maximo,
            preco_minimo,
            preco_abertura,
            preco_compra,
            preco_venda,
            volume_24h,
            timestamp_api
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, linha in df.iterrows():
        cursor.execute(
            sql,
            (
                linha["par_moedas"],
                linha["preco_ultimo"],
                linha["preco_maximo"],
                linha["preco_minimo"],
                linha["preco_abertura"],
                linha["preco_compra"],
                linha["preco_venda"],
                linha["volume_24h"],
                linha["timestamp_api"]
            )
        )

    conexao.commit()

    cursor.close()
    conexao.close()