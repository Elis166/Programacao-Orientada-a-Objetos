class Recompensa:
    def __init__(self, id_recompensa: int, nome: str, descricao: str, tipo: str):
        self._id_recompensa = id_recompensa
        self._nome = nome
        self._descricao = descricao
        self._tipo = tipo

    @property
    def id_recompensa(self):
        return self._id_recompensa

    @id_recompensa.setter
    def id_recompensa(self, novo_id):
        self._id_recompensa = novo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo