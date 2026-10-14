class Estudante:
    def __init__(self, id_estudante: int, nome: str, email: str, turma: str):
        self._id_estudante = id_estudante
        self._nome = nome
        self._email = email
        self._turma = turma
        self._personagem = None

    @property
    def id_estudante(self):
        return self._id_estudante

    @id_estudante.setter
    def id_estudante(self, novo_id):
        self._id_estudante = novo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def turma(self):
        return self._turma

    @turma.setter
    def turma(self, novo_turma):
        self._turma = novo_turma