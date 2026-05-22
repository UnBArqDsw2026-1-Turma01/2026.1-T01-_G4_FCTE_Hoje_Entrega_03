from abc import ABC, abstractmethod


class Conteudo(ABC):
    def __init__(self, code: str):
        self._code = code

    @abstractmethod
    def exibirConteudo(self) -> str:
        pass


class CardapioRU(Conteudo):
    def exibirConteudo(self) -> str:
        return f"Exibindo o cardápio (Código: {self._code})"


class Evento(Conteudo):
    def exibirConteudo(self) -> str:
        return f"Exibindo os detalhes do evento (Código: {self._code})"


class Edital(Conteudo):
    def exibirConteudo(self) -> str:
        return f"Exibindo o edital (Código: {self._code})"


class Noticia(Conteudo):
    def exibirConteudo(self) -> str:
        return f"Exibindo a notícia (Código: {self._code})"


class ConteudoDecorator(Conteudo):
    def __init__(self, conteudo: Conteudo):
        super().__init__(conteudo._code)
        self._conteudo = conteudo

    def exibirConteudo(self) -> str:
        return self._conteudo.exibirConteudo()


class DestaqueDecorator(ConteudoDecorator):
    def exibirConteudo(self) -> str:
        return f"[DESTAQUE] {self._conteudo.exibirConteudo()}"


class FixadoDecorator(ConteudoDecorator):
    def exibirConteudo(self) -> str:
        return f"[FIXADO NO TOPO] {self._conteudo.exibirConteudo()}"


class SeloOficialDecorator(ConteudoDecorator):
    def exibirConteudo(self) -> str:
        return f"[OFICIAL FCTE] {self._conteudo.exibirConteudo()}"


class TraducaoDecorator(ConteudoDecorator):
    def __init__(self, conteudo: Conteudo, idioma: str = "EN"):
        super().__init__(conteudo)
        self._idioma = idioma

    def exibirConteudo(self) -> str:
        return f"{self._conteudo.exibirConteudo()} | (Tradução {self._idioma} disponível)"


if __name__ == "__main__":
    noticia = Noticia("N-2026-01")
    print("Original:")
    print(f"  {noticia.exibirConteudo()}\n")

    noticia_oficial = SeloOficialDecorator(noticia)
    print("Com selo oficial:")
    print(f"  {noticia_oficial.exibirConteudo()}\n")

    noticia_decorada = DestaqueDecorator(
        FixadoDecorator(
            SeloOficialDecorator(
                TraducaoDecorator(noticia)
            )
        )
    )
    print("Notícia totalmente decorada (Destaque + Fixado + Selo Oficial + Tradução):")
    print(f"  {noticia_decorada.exibirConteudo()}\n")

    evento = Evento("E-2026-07")
    evento_destaque = DestaqueDecorator(SeloOficialDecorator(evento))
    print("Evento com destaque e selo oficial:")
    print(f"  {evento_destaque.exibirConteudo()}")
