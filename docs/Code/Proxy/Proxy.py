from abc import ABC, abstractmethod

class Login(ABC):
    def __init__(self, email: str, senha: str):
        self._email = email
        self._senha = senha

    @abstractmethod
    def Autenticar(self, email: str, senha: str) -> bool:
        pass


class Autenticador(Login):
    def __init__(self, email: str = "", senha: str = ""):
        super().__init__(email, senha)

    def Autenticar(self, email: str, senha: str) -> bool:
        return email == "admin@unb.br" and senha == "123456"


class AutenticadorProxy(Login):
    def __init__(self, service: Login):
        super().__init__("", "")
        self.service = service  

    def Autenticar(self, email: str, senha: str) -> bool:
        if not email or not senha:
            print("Falha: email ou senha não podem ser vazios.")
            return False

        if "@" not in email:
            print("Falha: email inválido.")
            return False

        print("Proxy: validações realizadas. Encaminhando ao serviço real...")
        
        return self.service.Autenticar(email, senha)


if __name__ == "__main__":
    autenticador_real = Autenticador()
    
    proxy = AutenticadorProxy(service=autenticador_real)
    
    sucesso = proxy.Autenticar("admin@unb.br", "123456")
    print(f"Resultado da autenticação: {sucesso}")