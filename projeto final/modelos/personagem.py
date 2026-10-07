class Personagem:
    def __init__(self, id_personagem, nome, nivel, experiencia, classe, estudante):
        self._id_personagem = id_personagem
        self._nome = nome
        self._nivel = nivel
        self._experiencia = experiencia
        self._classe = classe
        self._estudante = estudante

    @property
    def id_personagem(self):
        return self._id_personagem

    @id_personagem.setter
    def id_personagem(self, novo_id):
        self._id_personagem = novo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, novo_nivel):
        self._nivel = novo_nivel

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, nova_exp):
        self._experiencia = nova_exp

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, nova_classe):
        self._classe = nova_classe

    @property
    def estudante(self):
        return self._estudante

    @estudante.setter
    def estudante(self, novo_estudante):
        self._estudante = novo_estudante