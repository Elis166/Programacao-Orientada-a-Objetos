class MissaoRealizada:
    def __init__(self, personagem, missao, data_realizacao, status):
        self._personagem = personagem
        self._missao = missao
        self._data_realizacao = data_realizacao
        self._status = status

    @property
    def personagem(self):
        return self._personagem
    
    @personagem.setter
    def personagem(self, novo_personagem):
        self._personagem = novo_personagem

    @property
    def missao(self):
        return self._missao
    
    @missao.setter
    def missao(self, nova_missao):
        self._missao = nova_missao