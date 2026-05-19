from Factory.Factory import CreateConteudo, CreateCardapioRU, CreateEvento, Publicador, CreateNoticia, CreateEdital

if __name__ == "__main__":
    publicador = Publicador()

    factory_noticia = CreateNoticia("NOT-001")
    factory_edital = CreateEdital("EDI-2024")

    noticia_publicada = publicador.publicarConteudo(factory_noticia)
    edital_publicado = publicador.publicarConteudo(factory_edital)

    print("\n--- Conteúdos do Publicador ---")
    for conteudo in publicador.conteudos:
        print(conteudo.exibirConteudo())