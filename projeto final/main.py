from src.models.estudante import Estudante
from src.models.classes import Mago, Guerreiro
from src.models.missao import Missao
from src.models.recompensa import Recompensa
from src.models.conquista import Conquista
from src.services.jogo import Jogo


def criar_novo_jogo() -> Jogo:
    print("=== CRIAÇÃO DE PERSONAGEM ===")
    nome_aluno = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    turma = input("Digite sua turma: ")

    aluno = Estudante(1, nome_aluno, email, turma)

    print("\nEscolha sua classe:")
    print("1 - Mago")
    print("2 - Guerreiro")
    opcao = input("Opção: ")

    nome_heroi = input("Digite o nome do seu personagem: ")

    if opcao == "2":
        personagem = Guerreiro(id_personagem=1, nome=nome_heroi, estudante=aluno)
    else:
        personagem = Mago(id_personagem=1, nome=nome_heroi, estudante=aluno)

    return Jogo(jogador=personagem)


def main():
    # 1. Cria o jogo para o jogador
    jogo = criar_novo_jogo()

    # 2. Cadastra algumas missões iniciais
    r1 = Recompensa(1, "Poção de Vida", "Restaura HP", "Item")
    c1 = Conquista(1, "Primeiro Código", "Aprendeu POO", "Missão 1")

    m1 = Missao(
        id_missao=1,
        titulo="Estruturas Condicionais",
        descricao="Crie um programa que usa if/else",
        dificuldade="Fácil",
        experiencia=120,
        nivel_minimo=1,
        recompensa=r1,
        conquista=c1,
    )

    jogo.adicionar_missao(m1)

    # 3. Loop principal do jogo (CLI Single Player)
    rodando = True
    while rodando:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Ver Status do Personagem")
        print("2 - Ver Missões Disponíveis")
        print("3 - Aceitar e Concluir Missão")
        print("0 - Sair do Jogo")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            jogo.exibir_painel_jogador()

        elif escolha == "2":
            missoes = jogo.listar_missoes_disponiveis()
            print("\n📜 MISSÕES DISPONÍVEIS:")
            for m in missoes:
                print(
                    f"[{m.id_missao}] {m.titulo} ({m.dificuldade}) - Recompensa: {m.experiencia} XP"
                )

        elif escolha == "3":
            missoes = jogo.listar_missoes_disponiveis()
            if not missoes:
                print("Nenhuma missão disponível no momento!")
            else:
                m = missoes[0]
                jogo.jogador.aceitar_missao(m)
                # Simula a conclusão da missão pelo aluno
                jogo.jogador.concluir_missao(m)

        elif escolha == "0":
            print("Saindo do jogo... Progresso finalizado!")
            rodando = False


if __name__ == "__main__":
    main()