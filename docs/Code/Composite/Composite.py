from abc import ABC, abstractmethod


class IConteudoComponent(ABC):
    @abstractmethod
    def exibir(self) -> None:
        pass

    @abstractmethod
    def add(self, component: "IConteudoComponent") -> None:
        pass

    @abstractmethod
    def remove(self, component: "IConteudoComponent") -> None:
        pass


class ItemConteudo(IConteudoComponent):
    def __init__(self, titulo: str, descricao: str, categoria: str):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria

    def exibir(self) -> None:
        print(f"[ItemConteudo] {self.titulo} — {self.descricao} ({self.categoria})")

    def getTitulo(self) -> str:
        return self.titulo

    def add(self, component: IConteudoComponent) -> None:
        print("[ItemConteudo] Operação add() não é suportada em folhas.")

    def remove(self, component: IConteudoComponent) -> None:
        print("[ItemConteudo] Operação remove() não é suportada em folhas.")


class SecaoFeed(IConteudoComponent):
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.filhos: list[IConteudoComponent] = []

    def getTitulo(self) -> str:
        return self.titulo

    def add(self, component: IConteudoComponent) -> None:
        self.filhos.append(component)
        titulo_componente = component.getTitulo() if hasattr(component, 'getTitulo') else "Seção"
        print(f"[SecaoFeed] '{titulo_componente}' adicionado.")

    def remove(self, component: IConteudoComponent) -> None:
        if component in self.filhos:
            self.filhos.remove(component)
            print(f"[SecaoFeed] Componente removido.")
        else:
            print("[SecaoFeed] Componente não encontrado.")

    def exibir(self) -> None:
        print(f"\n=== Seção: {self.titulo} ===")
        for filho in self.filhos:
            filho.exibir()


class FeedController:
    def __init__(self):
        self.raiz = SecaoFeed("Feed Principal")

    def exibirFeed(self) -> None:
        self.raiz.exibir()

    def adicionarConteudo(self, component: IConteudoComponent) -> None:
        self.raiz.add(component)

    def removerConteudo(self, component: IConteudoComponent) -> None:
        self.raiz.remove(component)
