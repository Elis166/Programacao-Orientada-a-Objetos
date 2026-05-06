from animais import Leao, Gato, Cachorro, Macaco, Vaca, Elefante
from floresta import Floresta

floresta = Floresta(10)

leao = Leao(
    "Simba", "Dourado", "M",
    3, 190, 10,
    0, 0, 8
)

cachorro = Cachorro(
    "Bolt", "Branco", "M",
    2, 20, 10,
    5, 5,
    "Pastor Alemão", 4
)

gato = Gato(
    "Mingau", "Cinza", "M",
    2, 8, 10,
    5, 5,
    "Persa"
)

vaca = Vaca(
    "Mimosa", "Preta", "F",
    1, 150, 10,
    2, 2,
    "Holandesa"
)

macaco = Macaco(
    "Kiko", "Marrom", "M",
    2, 30, 10,
    3, 3,
    "Chimpanzé"
)

elefante = Elefante(
    "Dumbo", "Cinza", "M",
    1, 500, 10,
    1, 1,
    2
)

floresta.adicionar_animal(leao)
floresta.adicionar_animal(cachorro)
floresta.adicionar_animal(gato)
floresta.adicionar_animal(vaca)
floresta.adicionar_animal(macaco)
floresta.adicionar_animal(elefante)

while True:
    print("\n====== FLORESTA DE ANIMAIS ======")
    print("1 - Andar")
    print("2 - Mostrar características")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        floresta.mover_animais()

    elif opcao == "2":
        for animal in floresta.animais:
            print("\n----------------")
            animal.imprimir_caracteristicas()

    elif opcao == "3":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")