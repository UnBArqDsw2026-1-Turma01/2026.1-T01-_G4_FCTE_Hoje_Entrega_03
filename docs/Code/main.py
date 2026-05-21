from Factory.Factory import CreateConteudo, CreateCardapioRU, CreateEvento, Publicador, CreateNoticia, CreateEdital
from Proxy.Proxy import Autenticador, AutenticadorProxy, Login
from Builder.Builder import EventoBuilder, TipoDeEvento
from Strategy.Strategy import Noticia, FiltrarCategoria, FiltrarData
from Mediator.Mediator import AuthenticationDialog
from Observer.Observer import FeedService, Conteudo, HomeScreen, NoticiasScreen, NotificacoesService
from Composite.Composite import ItemConteudo, SecaoFeed, FeedController

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

    print("\n--- Teste do Mediator ---")

    dialog = AuthenticationDialog()

    print("\n[Tela de Login - usuário interagindo com os componentes]")
    dialog.email.digitar("admin@unb.br")
    dialog.senha.digitar("123456")
    dialog.lembrar.alternar()
    dialog.botao_login.clicar()

    print("\n--- Teste do Observer ---")

    feed = FeedService()

    home = HomeScreen()
    noticias = NoticiasScreen()
    notificacoes = NotificacoesService()

    feed.registrar(home)
    feed.registrar(noticias)
    feed.registrar(notificacoes)

    print("\n[Publicando conteúdo — todos os observers notificados]")
    feed.publicarConteudo(Conteudo(
        titulo="Processo seletivo aberto na Orcestra",
        tipo="Oportunidade",
        data="2026-05-20"
    ))

    print()
    feed.publicarConteudo(Conteudo(
        titulo="Semana de Computacao da FCTE 2025",
        tipo="Evento",
        data="2026-06-13"
    ))

    print("\n[Removendo NotificacoesService e publicando novamente]")
    feed.remover(notificacoes)

    feed.publicarConteudo(Conteudo(
        titulo="Cardapio do RU - Quinta-feira",
        tipo="Cardapio",
        data="2026-05-20"
    ))

    print("\n--- Teste do Composite ---")

    controller = FeedController()

    noticia_ia = ItemConteudo(
        "Avancos em IA",
        "Novos modelos de linguagem",
        "Tecnologia"
    )
    noticia_web = ItemConteudo(
        "Web 3.0",
        "O futuro da internet descentralizada",
        "Tecnologia"
    )
    evento_workshop = ItemConteudo(
        "Workshop de Python",
        "Aprenda Python do zero",
        "Evento"
    )

    secao_tecnologia = SecaoFeed("Tecnologia")
    secao_eventos = SecaoFeed("Eventos")

    secao_tecnologia.add(noticia_ia)
    secao_tecnologia.add(noticia_web)
    secao_eventos.add(evento_workshop)

    controller.adicionarConteudo(secao_tecnologia)
    controller.adicionarConteudo(secao_eventos)

    print("\n[Exibindo hierarquia completa do feed]")
    controller.exibirFeed()