class CardapioRU:
    def __init__(self, prato: str, tipo_refeicao: str, data: str):
        self.prato = prato
        self.tipo_refeicao = tipo_refeicao
        self.data = data

    def __str__(self):
        return f"[{self.tipo_refeicao}]\n{self.prato}\nData: {self.data}"


class RUApiExterna:
    def buscarDados(self) -> dict:
        return {
            "nome_prato": "Frango grelhado ao limao",
            "turno": "almoco",
            "dt_referencia": "20/05/2026"
        }


class CardapioRUAdapter:
    def __init__(self, api: RUApiExterna):
        self._api = api

    def getCardapio(self) -> CardapioRU:
        dados = self._api.buscarDados()
        return CardapioRU(
            prato=dados["nome_prato"],
            tipo_refeicao=dados["turno"].capitalize(),
            data=dados["dt_referencia"]
        )


class CardapioService:
    def __init__(self, adapter):
        self._adapter = adapter

    def exibirCardapio(self) -> None:
        cardapio = self._adapter.getCardapio()
        print(f"[CardapioService] Cardapio carregado: {cardapio}")


api_externa = RUApiExterna()
adapter = CardapioRUAdapter(api_externa)
service = CardapioService(adapter)

service.exibirCardapio()