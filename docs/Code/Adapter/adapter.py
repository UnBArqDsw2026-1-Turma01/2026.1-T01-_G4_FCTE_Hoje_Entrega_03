# 6.3.1 Classe de Dados Interna (CardapioRU)
class CardapioRU:
    def __init__(self, prato: str, tipo_refeicao: str, data: str):
        self.prato = prato
        self.tipo_refeicao = tipo_refeicao
        self.data = data

    def __str__(self):
        return f"[{self.tipo_refeicao}] {self.prato} | Data: {self.data}"


# 6.3.2 Adaptee — API externa com formato incompativel
class RUApiExterna:
    def buscarDados(self) -> dict:
        return {
            "nome_prato": "Frango grelhado ao limao",
            "turno": "almoco",
            "dt_referencia": "20/05/2026"
        }


# 6.3.3 Adapter — converte o formato externo para o formato interno
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


# 6.3.4 Cliente — usa o Adapter sem conhecer a API externa
class CardapioService:
    def __init__(self, adapter):
        self._adapter = adapter

    def exibirCardapio(self) -> None:
        cardapio = self._adapter.getCardapio()
        print(f"[CardapioService] Cardapio carregado: {cardapio}")


# 6.3.5 Exemplo de uso
api_externa = RUApiExterna()
adapter = CardapioRUAdapter(api_externa)
service = CardapioService(adapter)

service.exibirCardapio()