from animais import Leao, Cachorro, Gato

class Floresta:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.animais = []
        self.rodada = 0

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def mover_animais(self):
        self.rodada += 1

        print(f"\n========= RODADA {self.rodada} =========")

        for animal in self.animais:
            animal.andar(self.rodada, self.tamanho)

        self.imprimir_posicoes()
        self.verificar_encontros()

    def imprimir_posicoes(self):
        print("\nPOSIÇÕES DOS ANIMAIS")

        for animal in self.animais:
            if animal.vivo:
                print(
                    f"{animal.get_nome()} -> "
                    f"({animal.get_pos_x()}, {animal.get_pos_y()})"
                )

    def verificar_encontros(self):
        vivos = [a for a in self.animais if a.vivo]

        for i in range(len(vivos)):
            for j in range(i + 1, len(vivos)):
                a1 = vivos[i]
                a2 = vivos[j]

                if a1.checar_colisao(a2):
                    print(
                        f"\n{a1.get_nome()} encontrou "
                        f"{a2.get_nome()}"
                    )

                    self.conflito(a1, a2)

    def conflito(self, a1, a2):

        # LEÃO
        if isinstance(a1, Leao):
            a1.rugir()

            if isinstance(a2, Leao):
                a2.rugir()

                if a1.get_idade() > a2.get_idade():
                    self.matar(a1, a2)
                else:
                    self.matar(a2, a1)

            else:
                self.matar(a1, a2)

        elif isinstance(a2, Leao):
            a2.rugir()
            self.matar(a2, a1)

        # CACHORRO X GATO
        elif isinstance(a1, Cachorro) and isinstance(a2, Gato):
            a1.latir()
            a2.miar()
            self.matar(a1, a2)

        elif isinstance(a2, Cachorro) and isinstance(a1, Gato):
            a2.latir()
            a1.miar()
            self.matar(a2, a1)

        else:
            print("Nada aconteceu.")

    def matar(self, assassino, vitima):
        vitima.vivo = False

        assassino.set_peso(assassino.get_peso() + 1)

        print(
            f"{assassino.get_nome()} matou "
            f"{vitima.get_nome()}"
        )

        print(
            f"{assassino.get_nome()} agora pesa "
            f"{assassino.get_peso()}kg"
        )