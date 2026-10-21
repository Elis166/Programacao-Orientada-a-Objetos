import random
import json
import os


ARQUIVO_SALVAMENTO = "progresso_rpg.json"

NIVEIS = [
    {
        "nome": "Prova da Colheita",
        "inimigo": "Agente da Capital",
        "hp": 45,
        "ataque": 8,
        "xp": 30
    },
    {
        "nome": "Treinamento dos Tributos",
        "inimigo": "Tributo Rival",
        "hp": 65,
        "ataque": 12,
        "xp": 45
    },
    {
        "nome": "Desafio de Sobrevivência",
        "inimigo": "Predador da Arena",
        "hp": 85,
        "ataque": 15,
        "xp": 60
    },
    {
        "nome": "Confronto na Arena",
        "inimigo": "Tributo de Elite",
        "hp": 110,
        "ataque": 18,
        "xp": 80
    },
    {
        "nome": "A Última Prova",
        "inimigo": "O Campeão da Capital (BOSS)",
        "hp": 170,
        "ataque": 23,
        "xp": 150
    }
]


class Personagem:
    def __init__(self, nome, hp=100, mana=120, xp=0, nivel=1, moedas=0):
        self.nome = nome
        self.hp_maximo = 100
        self.hp = hp
        self.mana_maxima = 120
        self.mana = mana
        self.xp = xp
        self.nivel = nivel
        self.moedas = moedas
        self.nivel_concluido = 0
        self.recompensa_final = False

    def mostrar_status(self):
        print("\n" + "-" * 38)
        print(f"TRIBUTO: {self.nome}")
        print(f"HP: {self.hp}/{self.hp_maximo}")
        print(f"MANA: {self.mana}/{self.mana_maxima}")
        print(f"XP: {self.xp}")
        print(f"Nível atual: {min(self.nivel_concluido + 1, 5)}/5")
        print(f"Moedas: {self.moedas}")
        print("-" * 38)

    def salvar(self):
        dados = {
            "nome": self.nome,
            "hp": self.hp,
            "mana": self.mana,
            "xp": self.xp,
            "nivel": self.nivel,
            "moedas": self.moedas,
            "nivel_concluido": self.nivel_concluido,
            "recompensa_final": self.recompensa_final
        }

        with open(ARQUIVO_SALVAMENTO, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    @classmethod
    def carregar(cls):
        if not os.path.exists(ARQUIVO_SALVAMENTO):
            return None

        try:
            with open(ARQUIVO_SALVAMENTO, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            personagem = cls(
                nome=dados["nome"],
                hp=dados.get("hp", 100),
                mana=dados.get("mana", 120),
                xp=dados.get("xp", 0),
                nivel=dados.get("nivel", 1),
                moedas=dados.get("moedas", 0)
            )

            personagem.nivel_concluido = dados.get("nivel_concluido", 0)
            personagem.recompensa_final = dados.get("recompensa_final", False)

            return personagem

        except (json.JSONDecodeError, KeyError, TypeError):
            print("O arquivo de progresso está inválido. Um novo jogo será iniciado.")
            return None


def combater(personagem, dados_nivel, numero_nivel):
    nome_inimigo = dados_nivel["inimigo"]
    hp_inimigo = dados_nivel["hp"]
    ataque_inimigo = dados_nivel["ataque"]
    recuperou_mana = False

    print("\n" + "=" * 44)
    print(f"NÍVEL {numero_nivel}: {dados_nivel['nome']}")
    print(f"Inimigo: {nome_inimigo}")
    print(f"HP do inimigo: {hp_inimigo}")
    print("=" * 44)

    while personagem.hp > 0 and hp_inimigo > 0:
        personagem.mostrar_status()
        print(f"{nome_inimigo} — HP: {hp_inimigo}")

        print("\n1. Ataque básico")
        print("2. Habilidade especial (20 de mana)")

        if not recuperou_mana:
            print("3. Recuperar 20 de mana")

        escolha = input("Escolha sua ação: ").strip()

        if escolha == "1":
            dano = random.randint(12, 20)
            hp_inimigo -= dano
            print(f"Você causou {dano} de dano!")

        elif escolha == "2":
            if personagem.mana < 20:
                print("Você não tem mana suficiente!")
                continue

            personagem.mana -= 20
            dano = random.randint(28, 40)
            hp_inimigo -= dano
            print(f"Sua habilidade especial causou {dano} de dano!")

        elif escolha == "3" and not recuperou_mana:
            personagem.mana = min(
                personagem.mana + 20,
                personagem.mana_maxima
            )
            recuperou_mana = True
            print("Você recuperou 20 de mana!")

        else:
            print("Opção inválida ou ação já utilizada.")
            continue

        if hp_inimigo <= 0:
            break

        dano_recebido = random.randint(
            max(3, ataque_inimigo - 4),
            ataque_inimigo + 4
        )

        personagem.hp = max(0, personagem.hp - dano_recebido)

        print(
            f"{nome_inimigo} atacou e causou "
            f"{dano_recebido} de dano!"
        )

    if personagem.hp <= 0:
        print("\nVocê foi derrotado!")
        print("Seu progresso nos níveis anteriores foi mantido.")
        personagem.salvar()
        return False

    print(f"\nVocê derrotou {nome_inimigo}!")

    personagem.nivel_concluido = numero_nivel
    personagem.xp += dados_nivel["xp"]
    personagem.moedas += numero_nivel * 10

    print(f"Você recebeu {dados_nivel['xp']} XP!")
    print(f"Você recebeu {numero_nivel * 10} moedas!")

    if numero_nivel < 5:
        personagem.hp = min(
            personagem.hp_maximo,
            personagem.hp + 25
        )

        personagem.mana = min(
            personagem.mana_maxima,
            personagem.mana + 15
        )

        print("Você recuperou 25 HP e 15 de mana!")

    else:
        personagem.recompensa_final = True
        personagem.moedas += 100

        print("\n" + "*" * 44)
        print("BOSS DERROTADO!")
        print("VOCÊ VENCEU OS JOGOS!")
        print("RECOMPENSA FINAL DESBLOQUEADA!")
        print("Você recebeu mais 100 moedas!")
        print("*" * 44)

    personagem.salvar()
    return True


def iniciar_jogo():
    personagem = Personagem.carregar()

    if personagem:
        print(f"Progresso encontrado para {personagem.nome}!")
        print("1. Continuar jogo")
        print("2. Começar novo jogo")

        escolha = input("Escolha: ").strip()

        if escolha == "2":
            nome = input("Nome do seu tributo: ").strip()

            if not nome:
                nome = "Tributo"

            personagem = Personagem(nome)
            personagem.salvar()

    else:
        nome = input("Digite o nome do seu tributo: ").strip()

        if not nome:
            nome = "Tributo"

        personagem = Personagem(nome)
        personagem.salvar()

    while True:
        if personagem.recompensa_final:
            print("\nVocê já concluiu os cinco níveis!")
            print("A recompensa final já foi conquistada.")
            personagem.mostrar_status()
            break

        if personagem.hp <= 0:
            print("\nSeu personagem está sem HP!")
            print("1. Recuperar HP e mana para tentar novamente")
            print("2. Sair")

            escolha = input("Escolha: ").strip()

            if escolha == "1":
                personagem.hp = personagem.hp_maximo
                personagem.mana = personagem.mana_maxima
                personagem.salvar()
            else:
                break

        proximo_nivel = personagem.nivel_concluido + 1
        dados_nivel = NIVEIS[proximo_nivel - 1]

        print("\n" + "=" * 44)
        print("RPG DA ESCOLA — SOBREVIVÊNCIA EM PANEM")
        print("=" * 44)

        personagem.mostrar_status()

        print(f"Próximo desafio: {dados_nivel['nome']}")
        print("1. Entrar no desafio")
        print("2. Ver status")
        print("3. Sair e salvar")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            combater(
                personagem,
                dados_nivel,
                proximo_nivel
            )

        elif escolha == "2":
            personagem.mostrar_status()

        elif escolha == "3":
            personagem.salvar()
            print("Progresso salvo. Até a próxima!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    iniciar_jogo()