from src.extract import extrair_dados

def test_extrair_dados(monkeypatch):

    class RespostaFalsa:

        status_code = 200
        def json(self):
            return {
            "ticker": {
                "high": "620000",
                "low": "600000",
                "vol": "10.5",
                "last": "610000",
                "buy": "609000",
                "sell": "611000",
                "open": "605000",
                "date": 1791052200  
            }
            }

    def get_falso(url):
            return RespostaFalsa()

    monkeypatch.setattr(
        "src.extract.requests.get",
        get_falso
    )

    resultado = extrair_dados()

    