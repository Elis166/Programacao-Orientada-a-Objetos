"""Menu principal do projeto

Reúne as missões em um único ponto de entrada

"""
import json
import os

from src.missoes.missao2 import MissaoArmario
from src.missoes.missao3 import Jogo as JogoEldoria
from src.missoes.missao4 import main as jogo_sobrevivencia, ARQUIVO_SALVAMENTO

ARQUIVO_ELDORIA = "resultado_eldoria.txt"
LARGURA = 50


def linha(char="="):
    print(char * LARGURA)


def titulo(texto):
    print()
    linha()
    print(texto.center(LARGURA))
    linha()


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def executar_missao(nome, funcao):
    """Roda uma missão sem derrubar o menu se algo der errado."""
    try:
        funcao()
    except (KeyboardInterrupt, EOFError):
        print("\nMissão interrompida. Voltando ao menu...")
    except Exception as erro:
        print(f"\nOcorreu um erro na missão '{nome}': {erro}")


def ver_progresso():
    titulo("PROGRESSO")

    print("\n[Os Jogos da Sobrevivência]")
    if os.path.exists(ARQUIVO_SALVAMENTO):
        try:
            with open(ARQUIVO_SALVAMENTO, encoding="utf-8") as f:
                d = json.load(f)
            print(f"  Personagem: {d.get('nome')} ({d.get('classe')})")
            print(f"  Nível: {d.get('nivel')} | XP: {d.get('xp')} | Moedas: {d.get('moedas')}")
            print(f"  HP: {d.get('hp')}/{d.get('hp_maximo')} | Mana: {d.get('mana')}/{d.get('mana_maxima')}")
            print(f"  Conquistas: {', '.join(d.get('conquistas', [])) or 'Nenhuma'}")
        except (OSError, ValueError):
            print("  Não foi possível ler o salvamento.")
    else:
        print("  Nenhum progresso salvo.")

    print("\n[A Vila dos Amaldiçoados]")
    if os.path.exists(ARQUIVO_ELDORIA):
        try:
            with open(ARQUIVO_ELDORIA, encoding="utf-8") as f:
                for l in f.read().splitlines():
                    print(f"  {l}")
        except OSError:
            print("  Não foi possível ler o resultado.")
    else:
        print("  Ainda não jogada.")

    pausar()


def creditos():
    titulo("CRÉDITOS")
    print("Projeto Final - Programação Orientada a Objetos\n")
    for nome in ("Aleff Lohan", "Anny Beatriz", "Elis Vitória", "Keyty Winslet"):
        print(f"  - {nome}")
    pausar()


def main():
    # A missão do armário é criada uma vez para manter as pistas entre visitas.
    armario = MissaoArmario()

    opcoes = {
        "1": ("O Armário Misterioso", armario.menu_locais),
        "2": ("A Vila dos Amaldiçoados", lambda: JogoEldoria().iniciar()),
        "3": ("Os Jogos da Sobrevivência", jogo_sobrevivencia),
    }

    while True:
        titulo("RPG - MENU PRINCIPAL")
        for chave, (nome, _) in opcoes.items():
            print(f"  {chave} - {nome}")
        print("  4 - Ver progresso")
        print("  5 - Créditos")
        print("  0 - Sair")

        try:
            escolha = input("\nEscolha uma opção: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAté a próxima aventura!")
            break

        if escolha in opcoes:
            nome, funcao = opcoes[escolha]
            executar_missao(nome, funcao)
        elif escolha == "4":
            ver_progresso()
        elif escolha == "5":
            creditos()
        elif escolha == "0":
            print("Até a próxima aventura!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
