import datetime

class GerenciadorDeCache:

    _instancia = None

    def __new__(cls):
        
        if cls._instancia is None:
            cls._instancia = super(GerenciadorDeCache, cls).__new__(cls)
            # Garante que o estado inicial rode apenas UMA vez
            cls._instancia._inicializar_estado()
            print("[SISTEMA] Gerenciador de Cache criado na memória pela 1ª vez.")
        
        return cls._instancia

    def _inicializar_estado(self) -> None:
        
        self._cache_local = {}
        self._ultima_sincronizacao = None
        self._conectado_internet = False

    def set_conexao_internet(self, status: bool) -> None:
        
        self._conectado_internet = status
        print(f"\n[REDE] Internet ativa? {self._conectado_internet}")
        
        if self._conectado_internet:
            self._tentar_sincronizar()

    def _tentar_sincronizar(self) -> None:
        
        agora = datetime.datetime.now()
        nunca_sincronizou = self._ultima_sincronizacao is None
        
        passou_de_24h = False
        if not nunca_sincronizou:
            diferenca = agora - self._ultima_sincronizacao
            passou_de_24h = diferenca.total_seconds() > 86400  

        precisa_sincronizar = nunca_sincronizou or passou_de_24h

        if precisa_sincronizar and self._conectado_internet:
            print("[SYNC] Baixando dados do servidor da FCTE...")
            
            self._cache_local["noticias"] = ["Notícia 1: Semana Acadêmica", "Notícia 2: Novo Edital"]
            self._cache_local["ru"] = "Almoço: Frango Assado | Jantar: Strogonoff"
            
            self._ultima_sincronizacao = agora
            print("[SYNC] Sucesso! Relógio de 24 horas reiniciado.")
            
        elif precisa_sincronizar and not self._conectado_internet:
            print("[AVISO] App precisa sincronizar, mas está offline. Mantendo cache antigo.")

    def obter_dado(self, chave: str):
        
        self._tentar_sincronizar()
        
        if chave in self._cache_local:
            print(f"[APP] Lendo '{chave}' do cache: {self._cache_local[chave]}")
            return self._cache_local[chave]
        else:
            print(f"[ERRO] Dado '{chave}' não existe no cache.")
            return None

if __name__ == "__main__":
    print("--- 1. App abriu na Tela Principal (Sem internet) ---")
    cache_home = GerenciadorDeCache()
    cache_home.set_conexao_internet(False)
    cache_home.obter_dado("noticias") 

    print("\n--- 2. Usuário conectou no Wi-Fi ---")
    cache_home.set_conexao_internet(True)

    print("\n--- 3. Usuário navegou para a Tela do RU ---")
    cache_ru = GerenciadorDeCache() 
    cache_ru.obter_dado("ru") 

    print("\n--- 4. Comprovando o Singleton na prática ---")
    if cache_home is cache_ru:
        print("✅ SUCESSO! 'cache_home' e 'cache_ru' são o exato mesmo objeto na memória.")