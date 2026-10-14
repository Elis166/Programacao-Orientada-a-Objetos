class Conquista:
    def __init__(self, id_conquista: int, nome: str, descricao: str, requisito):
        self._id_conquista = id_conquista
        self._nome = nome
        self._descricao = descricao
        self._requisito = requisito

    @property
    def id_conquista(self):
        return self._id_conquista

    @id_conquista.setter
    def id_conquista(self, novo_id):
        self._id_conquista = novo_id

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
    def requisito(self):
        return self._requisito

    @requisito.setter
    def requisito(self, novo_requisito):
        self._requisito = novo_requisito