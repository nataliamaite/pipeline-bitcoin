import pandas as pd

def transformar_dados(dados):
    df = pd.DataFrame([dados])

    df = df.rename(columns={
        "pair": "par_moedas",
        "last": "preco_ultimo",
        "high": "preco_maximo",
        "low": "preco_minimo",
        "open": "preco_abertura",
        "buy": "preco_compra",
        "sell": "preco_venda",
        "vol": "volume_24h",
        "date": "timestamp_api"
    })

    colunas_numericas = [
    "preco_ultimo",
    "preco_maximo",
    "preco_minimo",
    "preco_abertura",
    "preco_compra",
    "preco_venda",
    "volume_24h"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna])
    
    print(df)
    print(df.dtypes)

    #Tratamento de valores nulos: 1º verificar se existem nulos:
    print("Valores nulos antes:")
    print(df.isnull().sum())
    #2º remover linhas que tenha valor nulo:
    df = df.dropna()
    #3º verifica novamente:
    print("Valores nulos depois:")
    print(df.isnull().sum())
    #Removendo duplicados: 1º Verificar se existem duplicados:
    print("Duplicados antes:")
    print(df.duplicated(subset=["par_moedas", "timestamp_api"]).sum())
    #2º Remover os duplicados:
    df = df.drop_duplicates(
        subset=["par_moedas", "timestamp_api"]
    )
    #Ordenando o DataFrame por data (crescente):
    df_ordenado = df.sort_values(by='timestamp_api', ascending=True)
    #Criando colunas derivadas:
    df["variacao_percentual"] = (
        (df["preco_ultimo"] - df["preco_abertura"])
        / df["preco_abertura"]
    ) * 100

    return df