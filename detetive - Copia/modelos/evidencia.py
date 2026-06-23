class Evidencia:
    def __init__(self, nome, descricao, caso):
        self.__nome = nome
        self.__descricao = descricao

        caso.adicionar_evidencia(self)

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def examinar(self):
        print(f"\n===== {self.get_nome()} =====")
        print(self.get_descricao())

    def __str__(self):
        return self.__nome

    def __repr__(self):
        return self.__nome