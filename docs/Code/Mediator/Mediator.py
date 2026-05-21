from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def notify(self, sender: "Component", event: str) -> None:
        """Recebe e roteia eventos emitidos por um Component."""
        pass


class Component:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    def set_mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Textbox(Component):
    def __init__(self, nome: str, mediator: Mediator = None):
        super().__init__(mediator)
        self.nome = nome
        self.valor: str = ""

    def digitar(self, valor: str) -> None:
        self.valor = valor
        print(f"[Textbox-{self.nome}] Valor digitado: '{valor}'.")
        self._mediator.notify(self, "input_change")


class Checkbox(Component):
    def __init__(self, mediator: Mediator = None):
        super().__init__(mediator)
        self.marcado: bool = False

    def alternar(self) -> None:
        self.marcado = not self.marcado
        estado = "marcado" if self.marcado else "desmarcado"
        print(f"[Checkbox] Lembrar-me {estado}.")
        self._mediator.notify(self, "remember_toggle")


class Button(Component):
    def clicar(self) -> None:
        print("[Button] Clique no botão de login.")
        self._mediator.notify(self, "login_click")


class AuthenticationDialog(Mediator):
    def __init__(self):
        self.email = Textbox("email", self)
        self.senha = Textbox("senha", self)
        self.lembrar = Checkbox(self)
        self.botao_login = Button(self)

    def notify(self, sender: Component, event: str) -> None:
        if event == "input_change":
            self._validar_campos()
        elif event == "remember_toggle":
            estado = "ativada" if self.lembrar.marcado else "desativada"
            print(f"[Mediator] Persistência de sessão {estado}.")
        elif event == "login_click":
            self._tentar_login()

    def _validar_campos(self) -> None:
        if self.email.valor and self.senha.valor:
            print("[Mediator] Campos preenchidos — botão de login habilitado.")
        else:
            print("[Mediator] Campos incompletos — botão de login desabilitado.")

    def _tentar_login(self) -> None:
        if not self.email.valor or not self.senha.valor:
            print("[Mediator] Login bloqueado: e-mail ou senha vazios.")
            return
        print(
            f"[Mediator] Autenticando '{self.email.valor}' "
            f"(lembrar={self.lembrar.marcado})..."
        )