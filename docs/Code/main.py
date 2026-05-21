from Factory.Factory import CreateConteudo, CreateCardapioRU, CreateEvento, Publicador, CreateNoticia, CreateEdital
from Proxy.Proxy import Autenticador, AutenticadorProxy, Login
from Builder.Builder import EventoBuilder, TipoDeEvento
from Strategy.Strategy import Noticia, FiltrarCategoria, FiltrarData
from Singleton.singleton import GerenciadorDeCache

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

        print("\n--- Teste do Strategy ---")
        estrategia_cat = FiltrarCategoria("Tecnologia")
        noticia_tech = Noticia(estrategia_cat)
        noticia_tech.listar_conteudo("TEC-2026")
        estrategia_data = FiltrarData("01/05/2026", "20/05/2026")
        noticia_tech.estrategia_filtragem = estrategia_data
        noticia_tech.listar_conteudo("DATA-5-2026")
    else:
        print("\nAcesso negado. Não foi possível publicar os conteúdos.")

    print("\n--- Teste do Builder ---")

    builder = EventoBuilder()

    evento_customizado = (
        builder
        .comId("EVT-WS-001")
        .comTitulo("Workshop de Arquitetura de Software")
        .comTipo(TipoDeEvento.WORKSHOP)
        .comData("2026-06-10")
        .comLocal("Sala 302 - FCTE")
        .comHorario("14:00", "17:00")
        .comAgenda(["Padrões Criacionais", "Padrões Estruturais", "Padrões Comportamentais"])
        .build()
    )
    print("\nEvento customizado:")
    print(f"  {evento_customizado.exibirConteudo()}")

    palestra = builder.criarPalestraMatutina()
    print("\nPalestra matutina (atalho de conveniência):")
    print(f"  {palestra.exibirConteudo()}")

    evento_simples = (
        builder
        .comId("EVT-DEB-002")
        .comTitulo("Debate sobre Educação")
        .comTipo(TipoDeEvento.DEBATE)
        .build()
    )
    print("\nEvento simples (apenas campos obrigatórios):")
    print(f"  {evento_simples.exibirConteudo()}")

    print("\n--- Teste do Singleton (Gerenciador de Cache) ---")
    
    print("\n[1] App abriu na Tela Principal (Sem internet)")
    cache_home = GerenciadorDeCache()
    cache_home.set_conexao_internet(False)
    cache_home.obter_dado("noticias") 

    print("\n[2] Usuário conectou no Wi-Fi")
    cache_home.set_conexao_internet(True)

    print("\n[3] Usuário navegou para a Tela do RU")
    cache_ru = GerenciadorDeCache() 
    cache_ru.obter_dado("ru") 

    print("\n[4] Comprovando a Instância Única")
    if cache_home is cache_ru:
        print("✅ SUCESSO! 'cache_home' e 'cache_ru' são o exato mesmo objeto na memória.")
    else:
        print("❌ ERRO! As instâncias são diferentes.")