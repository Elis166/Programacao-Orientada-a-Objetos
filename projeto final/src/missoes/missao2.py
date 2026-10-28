# missão do armário

from src.models.missao import Missao

class MissaoArmario(Missao):

    def __init__(self):
        super().__init__(
            1,
            "O armário misterioso",
            "Resolva as charadas e descubra a senha.",
            "Média",
            50
        )
        self.configurar_armario()

    def configurar_armario(self):
        self.item_armario = "Chave dourada antiga"
        self.item_encontrado = False

        self.charadas = {
            "Biblioteca": {
                "pergunta": (
                    "Qual será a saída deste código?\n\n"
                    "class Animal:\n"
                    "    def falar(self):\n"
                    "        print('Som')\n\n"
                    "animal = Animal()\n"
                    "(A)  Animal\n"
                    "(B)  falar\n"
                    "(C)  Som"
                ),
                "resposta": "C",
                "pista": "O primeiro número da senha é 3."
            },

            "Sala de Matemática": {
                "pergunta": (
                    "Qual conceito de POO permite que uma classe filha reutilize atributos e métodos de uma classe pai?\n\n"
                    "(A)  Encapsulamento\n"
                    "(B)  Herança\n"
                    "(C)  Polimorfismo"
                ),
                "resposta": "B",
                "pista": "O segundo número da senha é 5."
            },
            "Laboratório de Ciências": {
                "pergunta": (
                    "Em Python, usando a biblioteca Tkinter, qual widget permite que o usuário digite informações, como seu nome, em uma interface gráfica?\n\n"
                    "(A)  Entry\n"
                    "(B)  Label\n"
                    "(C)  Button"
                ),
                "resposta": "B",
                "pista": "O terceiro número da senha é 2."
            }
        }

        self.pistas_encontradas = []
        self.senha_armario = "352"
        self.armario_aberto = False

    def resolver_charada(self, local):
        if self.armario_aberto:
            print("O armário já foi aberto!")
            return

        if local in self.pistas_encontradas:
            print("Você já resolveu a charada desse local!")
            return

        charada = self.charadas[local]

        print("\n" + charada["pergunta"])
        resposta = input("Sua resposta: ")

        if resposta.strip() == charada["resposta"]:
            self.pistas_encontradas.append(local)
            print(charada["pista"])
        else:
            print("Resposta incorreta! Tente novamente.")

    def realizar_desafio_armario(self):
        if self.armario_aberto:
            print("Você já concluiu essa missão!")
            return

        if len(self.pistas_encontradas) < len(self.charadas):
            print("Você precisa resolver todas as charadas primeiro!")
            return

        resposta = input("Digite a senha do armário: ")

        if resposta == self.senha_armario:
            self.armario_aberto = True
            print("\nParabéns! Você abriu o armário misterioso!")
            print("Missão concluída!")
            print(
                f"Você ganhou {self.experiencia} "
                "pontos de experiência!"
            )

            self.item_encontrado = True
            print(f"Você encontrou: {self.item_armario}!")
            print("Guarde este item: ele será útil em uma próxima missão.")
        else:
            print("Senha incorreta! Tente novamente.")

    def menu_locais(self):
        while not self.armario_aberto:
            print("\n===== ARMÁRIO MISTERIOSO =====")
            print("1 - Biblioteca")
            print("2 - Sala de Matemática")
            print("3 - Laboratório de Ciências")
            print("4 - Tentar abrir o armário")
            print("5 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.resolver_charada("Biblioteca")
            elif opcao == "2":
                self.resolver_charada("Sala de Matemática")
            elif opcao == "3":
                self.resolver_charada("Laboratório de Ciências")
            elif opcao == "4":
                self.realizar_desafio_armario()
            elif opcao == "5":
                break
            else:
                print("Opção inválida! Tente novamente.")

        if self.armario_aberto:
            print("Você pode voltar para o jogo principal.")
