from typing import Optional
from src.models.estudante import Estudante

class Personagem:
    def __init__(self,
                 id_personagem: int, 
                 nome: str, 
                 estudante: Optional["Estudante"], 
                 hp_max: int, 
                 mana_max: int, 
                 dano_base: int):
        
        self._id_personagem = id_personagem
        self._nome = nome
        self._estudante = estudante

        # p/ combate
        self._hp_max = hp_max
        self._hp_atual = hp_max
        self._mana_max = mana_max
        self._mana_atual = mana_max
        self._dano_base = dano_base

        # progresso
        self._nivel = 1
        self._experiencia = 0


    # getters e setters
    @property
    def id_personagem(self) -> int:
        return self._id_personagem

    @id_personagem.setter
    def id_personagem(self, novo_id: int):
        self._id_personagem = novo_id

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome

    @property
    def nivel(self) -> int:
        return self._nivel

    @nivel.setter
    def nivel(self, novo_nivel: int):
        self._nivel = novo_nivel

    @property
    def experiencia(self) -> int:
        return self._experiencia

    @experiencia.setter
    def experiencia(self, nova_exp: int):
        self._experiencia = nova_exp

    @property
    def classe_nome(self) -> str:
        return self.__class__.__name__

    @property
    def estudante(self):
        return self._estudante

    @estudante.setter
    def estudante(self, novo_estudante):
        self._estudante = novo_estudante

    @property
    def hp_max(self) -> int:
        return self._hp_max

    @property
    def hp_atual(self) -> int:
        return self._hp_atual

    @property
    def mana_max(self) -> int:
        return self._mana_max

    @property
    def mana_atual(self) -> int:
        return self._mana_atual

    @property
    def dano_base(self) -> int:
        return self._dano_base