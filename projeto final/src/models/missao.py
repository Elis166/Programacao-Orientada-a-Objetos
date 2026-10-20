from typing import Optional
from src.models.recompensa import Recompensa
from src.models.conquista import Conquista
from src.models.enums import StatusMissao

class Missao:
    def __init__(self, 
                 id_missao: int, 
                 titulo: str, 
                 descricao: str, 
                 dificuldade: str, 
                 experiencia: int,
                 recompensa: Optional[Recompensa] = None,
                 conquista: Optional[Conquista] = None):
        
        self._id_missao = id_missao
        self._titulo = titulo
        self._descricao = descricao
        self._dificuldade = dificuldade
        self._experiencia = experiencia
        self._recompensa = recompensa
        self._conquista = conquista
        self._status = StatusMissao.DISPONIVEL

    @property
    def id_missao(self):
        return self._id_missao

    @id_missao.setter
    def id_missao(self, novo_id):
        self._id_missao = novo_id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, nova_dificuldade):
        self._dificuldade = nova_dificuldade

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, nova_exp):
        self._experiencia = nova_exp

    @property
    def recompensa(self):
        return self._recompensa

    @recompensa.setter
    def recompensa(self, nova_recompensa):
        self._recompensa = nova_recompensa

    @property
    def conquista(self):
        return self._conquista

    @conquista.setter
    def conquista(self, nova_conquista):
        self._conquista = nova_conquista

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, novo_status: str):
        self._status = novo_status