class Missao:
    def __init__(self, id_missao: int, titulo: str, descricao: str, dificuldade: str, experiencia):
        self._id_missao = id_missao
        self._titulo = titulo
        self._descricao = descricao
        self._dificuldade = dificuldade
        self._experiencia = experiencia

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
