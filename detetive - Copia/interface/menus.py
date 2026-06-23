from casos.quarto_trancado import caso1
from casos.desaparecimento_trem import caso2
from casos.nunca_minta import caso3
from util.validacoes import escolher_opcao
from util.validacoes import acusar

def tela_inicio():
    print("=" * 40)
    print("      ARQUIVOS DA DIVISÃO CRIMINAL")
    print("=" * 40)
    print()
    print("        ██████╗ ███████╗████████╗")
    print("        ██╔══██╗██╔════╝╚══██╔══╝")
    print("        ██║  ██║█████╗     ██║")
    print("        ██║  ██║██╔══╝     ██║")
    print("        ██████╔╝███████╗   ██║")
    print("        ╚═════╝ ╚══════╝   ╚═╝")
    print()
    print("       DETETIVE: CASOS CRIMINAIS")
    print()
    print("Você é um investigador da polícia.")
    print("Analise pistas, interrogue suspeitos")
    print("e descubra o verdadeiro culpado.")
    print()
    input("Pressione ENTER para começar...")

def menu_principal():

    while True:

        print("\n" + "=" * 50)
        print("MENU PRINCIPAL")
        print("=" * 50)
        print("1 - Iniciar Caso")
        print("2 - Créditos")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_casos()

        elif opcao == "2":
            print("\nCaso 1: O Quarto Trancado — Criado por Aleff.\nCaso 2: O Desaparecimento no Trem — Criado por Elis.\nCaso 3: Nunca Minta — Criado por Keyty.")

        elif opcao == "3":
            print("\nEncerrando sistema...")
            break

        else:
            print("Opção inválida.")

def iniciar_investigacao(caso):
        while True:

            print("\n===== INVESTIGAÇÃO =====")
            print("1 - Ver caso")
            print("2 - Suspeitos")
            print("3 - Testemunhas")
            print("4 - Evidências")
            print("5 - Acusar")
            print("6 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                print(caso.get_info())

            elif opcao == "2":
                menu_suspeitos(caso)

            elif opcao == "3":
                menu_testemunhas(caso)

            elif opcao == "4":
                menu_evidencias(caso)

            elif opcao == "5":
                acusar(caso)
                break

            elif opcao == "6":
                break

def menu_casos():
    while True:
        print("\n" + "=" * 50)
        print("1 - O Mistério do Quarto Trancado")
        print("2 - O Desaparecimento no Trem")
        print("3 - Nunca Minta")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            iniciar_investigacao(caso1)
            break
        elif opcao == "2":
            iniciar_investigacao(caso2)
            break
        elif opcao == "3":
            iniciar_investigacao(caso3)
            break
        else:
            "Opção inválida."

def menu_suspeitos(caso):

    suspeitos = caso.get_suspeitos()

    print("\n===== SUSPEITOS =====")

    for i, suspeito in enumerate(suspeitos):
        print(f"{i+1} - {suspeito.get_nome()}")

    escolha = escolher_opcao(len(suspeitos))

    suspeitos[escolha].interrogar()

def menu_testemunhas(caso):

    testemunhas = caso.get_testemunhas()

    print("\n===== TESTEMUNHAS =====")

    if not testemunhas:
        print("Não há testemunhas disponíveis.")
        return

    for i, testemunha in enumerate(testemunhas):
        print(f"{i+1} - {testemunha.get_nome()}")

    escolha = escolher_opcao(len(testemunhas))

    testemunhas[escolha].interrogar()

def menu_evidencias(caso):

    evidencias = caso.get_evidencias()

    print("\n===== EVIDÊNCIAS =====")

    if not evidencias:
        print("Não há evidências disponíveis.")
        return

    for i, evidencia in enumerate(evidencias):
        print(f"{i+1} - {evidencia.get_nome()}")

    escolha = escolher_opcao(len(evidencias))

    evidencias[escolha].examinar()