from modelos.caso import Caso

def escolher_opcao(quantidade):
    while True:
        try:
            escolha = int(input("Escolha: ")) - 1

            if 0 <= escolha < quantidade:
                return escolha

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")

def acusar(caso):

    suspeitos = caso.get_suspeitos()

    print("\n===== ACUSAÇÃO FINAL =====")

    for i, suspeito in enumerate(suspeitos):
        print(f"{i+1} - {suspeito.get_nome()}")

    escolha = int(input("\nQuem é o culpado? ")) - 1

    acusado = suspeitos[escolha]

    if acusado == caso.get_culpado():

        print(Caso.get_solucao(caso))

    else:
        print("\nVocê acusou a pessoa errada.")
        print("O verdadeiro culpado escapou.")