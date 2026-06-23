class Suspeito:
    def __init__(self, nome, descricao, caracteristicas, depoimento, caso):
        self.__nome = nome
        self.__descricao = descricao
        self.__caracteristicas = caracteristicas
        self.__depoimento = depoimento
    
        caso.adicionar_suspeito(self)

    # GETTERS
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_caracteristicas(self):
        return self.__caracteristicas
    
    def get_depoimento(self):
        return self.__depoimento
    
    # SETTERS
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def set_caracteristicas(self, caracteristicas):
        self.__caracteristicas = caracteristicas
    
    def set_depoimento(self, depoimento):
        self.__depoimento = depoimento

    def interrogar(self):
        print(f"\n===== {self.get_nome()} =====")
        print(f"Descrição: {self.get_descricao()}")
        print(f"Características: {self.get_caracteristicas()}")
        print(f"Depoimento: {self.get_depoimento()}")

    def __str__(self):
        return self.__nome

    def __repr__(self):
        return self.__nome