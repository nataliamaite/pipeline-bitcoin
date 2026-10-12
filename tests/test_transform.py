import pandas as pd

from src.transform import transformar_dados


def test_transformar_dados():

    dados = {
        "pair": "BRLBTC",
        "last": "610000",
        "high": "620000",
        "low": "600000",
        "open": "605000",
        "buy": "609000",
        "sell": "611000",
        "vol": "10.5",
        "date": 1791052200
    }

    resultado = transformar_dados(dados)

    # Verificar se o resultado é um DataFrame
    assert isinstance(resultado, pd.DataFrame)

    # Verificar se as colunas foram renomeadas
    assert "par_moedas" in resultado.columns
    assert "preco_ultimo" in resultado.columns
    assert "timestamp_api" in resultado.columns

    # Verificar se os valores foram convertidos para números
    assert resultado["preco_ultimo"].iloc[0] == 610000
    assert resultado["volume_24h"].iloc[0] == 10.5

    # Verificar se a coluna derivada foi criada
    assert "variacao_percentual" in resultado.columns

    # Verificar o cálculo da variação percentual
    variacao_esperada = ((610000 - 605000) / 605000) * 100

    assert abs(
        resultado["variacao_percentual"].iloc[0] - variacao_esperada
    ) < 0.0001