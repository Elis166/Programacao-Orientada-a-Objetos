class Caso:
    def __init__(self, info, solucao):
        self.__info = info
        self.__solucao = solucao
        self.__culpado = None
        self.__suspeitos = []
        self.__testemunhas = []
        self.__evidencias = []

    def get_info(self):
        return self.__info

    def get_solucao(self):
        return self.__solucao
    
    def get_culpado(self):
        return self.__culpado
    
    def get_suspeitos(self):
        return self.__suspeitos
    
    def get_testemunhas(self):
        return self.__testemunhas
    
    def get_evidencias(self):
        return self.__evidencias
    
    def set_info(self, info):
        self.__info = info
    
    def set_solucao(self, solucao):
        self.__solucao = solucao

    def set_culpado(self, culpado):
        self.__culpado = culpado

    def adicionar_suspeito(self, suspeito):
        self.__suspeitos.append(suspeito)

    def adicionar_testemunha(self, testemunha):
        self.__testemunhas.append(testemunha)

    def adicionar_evidencia(self, evidencia):
        self.__evidencias.append(evidencia)

    def __str__(self):
        return self.__info

    def __repr__(self):
        return self.__info