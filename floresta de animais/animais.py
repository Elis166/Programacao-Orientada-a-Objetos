from animal import Animal

class Leao(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso,
                 estamina, pos_x, pos_y, idade):

        super().__init__(nome, cor, sexo, velocidade,
                         peso, estamina, pos_x, pos_y)

        self.__idade = idade

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def rugir(self):
        print(f"{self.get_nome()} rugiu: ROAAAAAR!")


class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, velocidade,
                 peso, estamina, pos_x, pos_y, raca, idade):

        super().__init__(nome, cor, sexo, velocidade,
                         peso, estamina, pos_x, pos_y)

        self.__raca = raca
        self.__idade = idade

    def get_raca(self):
        return self.__raca

    def get_idade(self):
        return self.__idade

    def set_raca(self, raca):
        self.__raca = raca

    def set_idade(self, idade):
        self.__idade = idade

    def latir(self):
        print(f"{self.get_nome()} latiu: AU AU!")


class Gato(Animal):
    def __init__(self, nome, cor, sexo, velocidade,
                 peso, estamina, pos_x, pos_y, raca):

        super().__init__(nome, cor, sexo, velocidade,
                         peso, estamina, pos_x, pos_y)

        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def set_raca(self, raca):
        self.__raca = raca

    def miar(self):
        print(f"{self.get_nome()} miou: MIAU!")


class Vaca(Animal):
    def __init__(self, nome, cor, sexo, velocidade,
                 peso, estamina, pos_x, pos_y, raca):

        super().__init__(nome, cor, sexo, velocidade,
                         peso, estamina, pos_x, pos_y)

        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def set_raca(self, raca):
        self.__raca = raca

    def mugir(self):
        print(f"{self.get_nome()} mugiu: MUUUU!")


class Elefante(Animal):
    def __init__(self, nome, cor, sexo, velocidade,
                 peso, estamina, pos_x, pos_y, tamanho_tromba):

        super().__init__(nome, cor, sexo, velocidade,
                         peso, estamina, pos_x, pos_y)

        self.__tamanho_tromba = tamanho_tromba

    def get_tamanho_tromba(self):
        return self.__tamanho_tromba

    def set_tamanho_tromba(self, tamanho):
        self.__tamanho_tromba = tamanho

    def trombetear(self):
        print(f"{self.get_nome()} fez: PRUUUU!")


class Macaco(Animal):
    def __init__(self, nome, cor, sexo, velocidade,
                 peso, estamina, pos_x, pos_y, especie):

        super().__init__(nome, cor, sexo, velocidade,
                         peso, estamina, pos_x, pos_y)

        self.__especie = especie

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie

    def gritar(self):
        print(f"{self.get_nome()} gritou: UH UH AH AH!")