from abc import ABC, abstractmethod
from typing import List


class Filtragem(ABC):
    
    @abstractmethod
    def selecionar_filtros(self) -> None:
        """Este método deve ser implementado pelas estratégias reais."""
        pass

class Noticia:
    def __init__(self, estrategia_filtragem: Filtragem):

        self.estrategia_filtragem = estrategia_filtragem
        self.conteudo: List[str] = []

    def listar_conteudo(self, code: str) -> None:
        print(f"Listando conteúdo com o código: {code}")

        self.estrategia_filtragem.selecionar_filtros()

class FiltrarData(Filtragem):
    def __init__(self, data_inicio: str, data_fim: str):
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def selecionar_filtros(self) -> None:
        print(f"Aplicando filtro por Data: de {self.data_inicio} até {self.data_fim}")

class FiltrarCategoria(Filtragem):
    def __init__(self, categoria: str):
        self.categoria = categoria

    def selecionar_filtros(self) -> None:
        print(f"Aplicando filtro pela Categoria: {self.categoria}")

class FiltrarPreferencias(Filtragem):
    def __init__(self, preferencias: str):
        self.preferencias = preferencias

    def selecionar_filtros(self) -> None:
        print(f"Aplicando filtro por Preferências: {self.preferencias}")