class Conteudo:
    def __init__(self, titulo: str, tipo: str, data: str):
        self.titulo = titulo
        self.tipo = tipo
        self.data = data

    def __str__(self):
        return f"[{self.tipo}] {self.titulo} | Data: {self.data}"


class FeedService:
    def __init__(self):
        self._observers = []
        self._conteudos = []

    def registrar(self, observer) -> None:
        self._observers.append(observer)

    def remover(self, observer) -> None:
        self._observers.remove(observer)

    def notificar(self, conteudo: Conteudo) -> None:
        for observer in self._observers:
            observer.update(conteudo)

    def publicarConteudo(self, conteudo: Conteudo) -> None:
        self._conteudos.append(conteudo)
        self.notificar(conteudo)


class HomeScreen:
    def update(self, conteudo: Conteudo) -> None:
        print(f"[HomeScreen] Feed atualizado com novo conteudo: {conteudo}")


class NoticiasScreen:
    def update(self, conteudo: Conteudo) -> None:
        print(f"[NoticiasScreen] Nova noticia listada: {conteudo}")


class NotificacoesService:
    def update(self, conteudo: Conteudo) -> None:
        print(f"[NotificacoesService] Notificacao enviada ao leitor: '{conteudo.titulo}'")
