from enum import Enum


class TipoDeEvento(Enum):
    PALESTRA = "Palestra"
    WORKSHOP = "Workshop"
    DEBATE = "Debate"
    ATIVIDADE_ESPORTIVA = "Atividade Esportiva"


class Evento:
    def __init__(
        self,
        code: str,
        titulo: str,
        tipo: TipoDeEvento,
        data: str = None,
        local: str = None,
        horario_inicio: str = None,
        horario_fim: str = None,
        agenda: list = None,
    ):
        self._code = code
        self._titulo = titulo
        self._tipo = tipo
        self._data = data
        self._local = local
        self._horario_inicio = horario_inicio
        self._horario_fim = horario_fim
        self._agenda = agenda or []

    def exibirConteudo(self) -> str:
        info = f"[{self._tipo.value}] {self._titulo} (Código: {self._code})"
        if self._data:
            info += f" | Data: {self._data}"
        if self._local:
            info += f" | Local: {self._local}"
        if self._horario_inicio and self._horario_fim:
            info += f" | Horário: {self._horario_inicio} - {self._horario_fim}"
        if self._agenda:
            info += f" | Agenda: {', '.join(self._agenda)}"
        return info


class EventoBuilder:
    def __init__(self):
        self.reset()

    def reset(self) -> "EventoBuilder":
        self._id = None
        self._titulo = None
        self._tipoEvento = None
        self._data = None
        self._local = None
        self._horario_inicio = None
        self._horario_fim = None
        self._agenda = []
        return self

    def comId(self, id: str) -> "EventoBuilder":
        self._id = id
        return self

    def comTitulo(self, titulo: str) -> "EventoBuilder":
        self._titulo = titulo
        return self

    def comTipo(self, tipo: TipoDeEvento) -> "EventoBuilder":
        self._tipoEvento = tipo
        return self

    def comData(self, data: str) -> "EventoBuilder":
        self._data = data
        return self

    def comLocal(self, local: str) -> "EventoBuilder":
        self._local = local
        return self

    def comHorario(self, inicio: str, fim: str) -> "EventoBuilder":
        self._horario_inicio = inicio
        self._horario_fim = fim
        return self

    def comAgenda(self, itens: list) -> "EventoBuilder":
        self._agenda = itens
        return self

    def build(self) -> Evento:
        if not self._id:
            raise ValueError("O ID do evento é obrigatório.")
        if not self._titulo:
            raise ValueError("O título do evento é obrigatório.")
        if not self._tipoEvento:
            raise ValueError("O tipo do evento é obrigatório.")

        evento = Evento(
            code=self._id,
            titulo=self._titulo,
            tipo=self._tipoEvento,
            data=self._data,
            local=self._local,
            horario_inicio=self._horario_inicio,
            horario_fim=self._horario_fim,
            agenda=self._agenda,
        )
        self.reset()
        return evento

    def criarPalestraMatutina(self) -> Evento:
        return (
            self.comId("EVT-PAL-MAT")
            .comTitulo("Palestra Matutina FCTE")
            .comTipo(TipoDeEvento.PALESTRA)
            .comData("2026-05-20")
            .comLocal("Auditório FCTE")
            .comHorario("08:00", "10:00")
            .comAgenda(["Abertura", "Apresentação", "Q&A"])
            .build()
        )

