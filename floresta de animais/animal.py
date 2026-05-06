class Animal:
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, pos_x, pos_y):   
        self.__nome = nome
        self.__cor = cor
        self.__sexo = sexo
        self.__velocidade = velocidade
        self.__peso = peso
        self.__estamina = estamina
        self.__pos_x = pos_x
        self.__pos_y = pos_y

        self.direcao_x = 1
        self.direcao_y = 1
        self.vivo = True

    # GETTERS
    def get_nome(self):
        return self.__nome

    def get_cor(self):
        return self.__cor

    def get_sexo(self):
        return self.__sexo

    def get_velocidade(self):
        return self.__velocidade

    def get_peso(self):
        return self.__peso

    def get_estamina(self):
        return self.__estamina

    def get_pos_x(self):
        return self.__pos_x

    def get_pos_y(self):
        return self.__pos_y

    # SETTERS
    def set_nome(self, nome):
        self.__nome = nome

    def set_cor(self, cor):
        self.__cor = cor

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def set_peso(self, peso):
        self.__peso = peso

    def set_estamina(self, estamina):
        self.__estamina = estamina

    def set_pos_x(self, x):
        self.__pos_x = x

    def set_pos_y(self, y):
        self.__pos_y = y

    def andar(self, rodada, tamanho_tabuleiro):
        if not self.vivo:
            return

        if self.__estamina <= 0:
            print(f"{self.__nome} está sem energia.")
            return

        velocidade = self.__velocidade

        # Rodada ímpar -> eixo Y
        if rodada % 2 != 0:
            novo_y = self.__pos_y + (velocidade * self.direcao_y)

            if novo_y >= tamanho_tabuleiro:
                self.direcao_y = -1
                novo_y = tamanho_tabuleiro - 1

            elif novo_y < 0:
                self.direcao_y = 1
                novo_y = 0

            self.__pos_y = novo_y

        # Rodada par -> eixo X
        else:
            novo_x = self.__pos_x + (velocidade * self.direcao_x)

            if novo_x >= tamanho_tabuleiro:
                self.direcao_x = -1
                novo_x = tamanho_tabuleiro - 1

            elif novo_x < 0:
                self.direcao_x = 1
                novo_x = 0

            self.__pos_x = novo_x

        self.__estamina -= 1

    def checar_colisao(self, outro):
        return (
            self.__pos_x == outro.get_pos_x() and
            self.__pos_y == outro.get_pos_y()
        )

    def imprimir_caracteristicas(self):
        print(f"Nome: {self.__nome}")
        print(f"Cor: {self.__cor}")
        print(f"Sexo: {self.__sexo}")
        print(f"Velocidade: {self.__velocidade}")
        print(f"Peso: {self.__peso}kg")
        print(f"Estamina: {self.__estamina}")
        print(f"Posição: ({self.__pos_x}, {self.__pos_y})")
        print(f"Vivo: {self.vivo}")