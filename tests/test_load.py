import pandas as pd
from src import load

def test_carregar_dados(monkeypatch):

    dados_falsos = {
        "par_moedas": ["BRLBTC"],
        "preco_ultimo": [610000.00],
        "preco_maximo": [620000.00],
        "preco_minimo": [600000.00],
        "preco_abertura": [605000.00],
        "preco_compra": [609000.00],
        "preco_venda": [611000.00],
        "volume_24h": [10.5],
        "timestamp_api": [1791052200]
    }

    df_falso = pd.DataFrame(dados_falsos)

    class CursorFalso:

        def execute(self, query, valores):
            self.query = query # Guarda o comando SQL executado
            self.valores = valores # Guarda os valores que seriam salvos

        def close(self):
            pass  # Apenas simula o fechamento

    class ConexaoFalsa:

        def __init__(self):
            self.cursor_falso = CursorFalso()

        def cursor(self):
            return self.cursor_falso  # Retorna o nosso cursor falso

        def commit(self):
            self.comitou = True       # Marca que o salvamento foi acionado

        def close(self):
            pass                     # Apenas simula o fechamento

    conexao_falsa = ConexaoFalsa()

    def conectar_falso():
        return conexao_falsa

    monkeypatch.setattr(
        load,
        "conectar_banco",
        conectar_falso
    )

    load.carregar_dados(df_falso)

    assert conexao_falsa.cursor_falso.query is not None
    assert conexao_falsa.comitou is True