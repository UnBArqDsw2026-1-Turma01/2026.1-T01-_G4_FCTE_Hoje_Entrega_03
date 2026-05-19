from Factory.Factory import CreateConteudo, CreateCardapioRU, CreateEvento, Publicador, CreateNoticia, CreateEdital
from Proxy.Proxy import Autenticador, AutenticadorProxy, Login

if __name__ == "__main__":
    
    print("--- Teste do Proxy ---")
    
    autenticador_real = Autenticador()
    
    autenticador_proxy = AutenticadorProxy(service=autenticador_real)
    
    print("\n[Tentativa 1 - Dados Inválidos]")
    sucesso_1 = autenticador_proxy.Autenticar("usuario_errado", "")
    
    print("\n[Tentativa 2 - Dados Válidos]")
    email_valido = "admin@unb.br"
    senha_valida = "123456"
    
    Publicador_Validado = autenticador_proxy.Autenticar(email_valido, senha_valida)

    print("--- Teste do Factory ---")


    if Publicador_Validado:
        print("\nLogin autorizado! Prosseguindo para a publicação de conteúdos...\n")
        
        publicador = Publicador()

        factory_noticia = CreateNoticia("NOT-001")
        factory_edital = CreateEdital("EDI-2024")

        noticia_publicada = publicador.publicarConteudo(factory_noticia)
        edital_publicado = publicador.publicarConteudo(factory_edital)

        print("--- Conteúdos do Publicador ---")
        for conteudo in publicador.conteudos:
            print(conteudo.exibirConteudo())
    else:
        print("\nAcesso negado. Não foi possível publicar os conteúdos.")