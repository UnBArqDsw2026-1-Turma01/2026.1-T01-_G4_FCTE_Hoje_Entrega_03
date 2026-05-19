from abc import ABC, abstractmethod
from typing import List

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

class CreateConteudo(ABC):
    def __init__(self, code: str):
        self._code = code

    @abstractmethod
    def createConteudo(self) -> Conteudo:
        pass

class CreateCardapioRU(CreateConteudo):
    def createConteudo(self) -> Conteudo:
        return CardapioRU(self._code)

class CreateEvento(CreateConteudo):
    def createConteudo(self) -> Conteudo:
        return Evento(self._code)

class CreateEdital(CreateConteudo):
    def createConteudo(self) -> Conteudo:
        return Edital(self._code)

class CreateNoticia(CreateConteudo):
    def createConteudo(self) -> Conteudo:
        return Noticia(self._code)

class Publicador:
    def __init__(self):
        self.conteudos: List[Conteudo] = []

    def publicarConteudo(self, factory: CreateConteudo) -> Conteudo:
        novo_conteudo = factory.createConteudo()
        self.conteudos.append(novo_conteudo)
        print(f"Sucesso: {novo_conteudo.__class__.__name__} publicado!")
        return novo_conteudo

    def editarConteudo(self, conteudo: Conteudo) -> str:
        return f"Editando o conteúdo com código {conteudo._code}..."

    def removerConteudo(self, conteudo: Conteudo) -> str:
        if conteudo in self.conteudos:
            self.conteudos.remove(conteudo)
            return f"Conteúdo com código {conteudo._code} removido com sucesso!"
        else:
            return f"Conteúdo com código {conteudo._code} não encontrado para remoção."