import json
import os
import random

ARQUIVO_SALVAMENTO = "progresso_rpg.json"

CLASSES = {
    "Mago": {
        "hp": 90,
        "mana": 60,
        "ataque": (12, 22),
        "especial": (28, 40),
        "custo_especial": 15,
        "habilidade": "Escudo Arcano",
        "custo_habilidade": 10
    },
    "Arqueiro": {
        "hp": 105,
        "mana": 45,
        "ataque": (15, 25),
        "especial": (25, 38),
        "custo_especial": 12,
        "habilidade": "Mira Perfeita",
        "custo_habilidade": 10
    },
    "Guerreiro": {
        "hp": 130,
        "mana": 35,
        "ataque": (18, 28),
        "especial": (27, 42),
        "custo_especial": 14,
        "habilidade": "Defesa de Ferro",
        "custo_habilidade": 10
    }
}

NIVEIS = [
    {
        "nome": "A Floresta dos Perdidos",
        "inimigo": "Lobo Selvagem",
        "hp": 75,
        "ataque": (10, 18),
        "xp": 35,
        "moedas": 20
    },
    {
        "nome": "As Ruínas do Distrito",
        "inimigo": "Tributo Corrompido",
        "hp": 100,
        "ataque": (14, 22),
        "xp": 45,
        "moedas": 25
    },
    {
        "nome": "O Pântano Mortal",
        "inimigo": "Guardião do Pântano",
        "hp": 125,
        "ataque": (16, 25),
        "xp": 55,
        "moedas": 30
    },
    {
        "nome": "A Arena das Sombras",
        "inimigo": "Caçador da Arena",
        "hp": 150,
        "ataque": (18, 28),
        "xp": 70,
        "moedas": 35
    },
    {
        "nome": "O Último Julgamento",
        "inimigo": "O Soberano",
        "hp": 220,
        "ataque": (22, 32),
        "xp": 100,
        "moedas": 60
    }
]

TRIBUTOS = {
    "Lira": {
        "descricao": "uma arqueira que conhece os caminhos da floresta",
        "comum": "Lira observa suas armas antes de falar.",
        "ajuda": "Lira promete distrair um inimigo durante uma batalha.",
        "classe": {
            "Mago": "Lira conta que viu símbolos mágicos nas ruínas.",
            "Arqueiro": "Lira compartilha uma técnica para mirar em pontos fracos.",
            "Guerreiro": "Lira revela que os guardas temem ataques diretos."
        }
    },
    "Davi": {
        "descricao": "um tributo que parece conhecer os patrocinadores",
        "comum": "Davi olha para os céus, procurando câmeras e patrocinadores.",
        "ajuda": "Davi entrega uma poção que guardava para emergências.",
        "classe": {
            "Mago": "Davi ensina você a economizar energia mágica.",
            "Arqueiro": "Davi mostra como preparar uma flecha sem fazer barulho.",
            "Guerreiro": "Davi explica como proteger o corpo durante um golpe."
        }
    },
    "Íris": {
        "descricao": "uma estrategista que parece saber mais do que diz",
        "comum": "Íris sussurra que a arena esconde um segredo.",
        "ajuda": "Íris revela uma passagem secreta que pode enfraquecer o chefe final.",
        "classe": {
            "Mago": "Íris revela uma inscrição que fortalece os feitiços.",
            "Arqueiro": "Íris aponta uma abertura escondida na armadura do chefe.",
            "Guerreiro": "Íris explica onde o chefe concentra sua força."
        }
    }
}

CONQUISTAS = {
    "primeira_vitoria": "Primeira Vitória",
    "aliado": "Não Estou Só",
    "explorador": "Olhos Abertos",
    "sobrevivente": "Sobrevivente",
    "especialista": "Poder Especial",
    "campeao": "Campeão da Arena"
}


class Personagem:
    def __init__(self, nome, classe):
        dados_classe = CLASSES[classe]

        self.nome = nome
        self.classe = classe
        self.hp_maximo = dados_classe["hp"]
        self.hp = self.hp_maximo
        self.mana_maxima = dados_classe["mana"]
        self.mana = self.mana_maxima
        self.xp = 0
        self.nivel = 1
        self.moedas = 30
        self.nivel_concluido = 0
        self.pocoes = 2
        self.pocoes_mana = 1
        self.aliados = []
        self.segredo = False
        self.eventos_concluidos = []
        self.dialogos_vistos = []
        self.conquistas = []
        self.recompensa_final = False
        self.especiais_usados = 0

    def salvar(self):
        dados = {
            "nome": self.nome,
            "classe": self.classe,
            "hp": self.hp,
            "hp_maximo": self.hp_maximo,
            "mana": self.mana,
            "mana_maxima": self.mana_maxima,
            "xp": self.xp,
            "nivel": self.nivel,
            "moedas": self.moedas,
            "nivel_concluido": self.nivel_concluido,
            "pocoes": self.pocoes,
            "pocoes_mana": self.pocoes_mana,
            "aliados": self.aliados,
            "segredo": self.segredo,
            "eventos_concluidos": self.eventos_concluidos,
            "dialogos_vistos": self.dialogos_vistos,
            "conquistas": self.conquistas,
            "recompensa_final": self.recompensa_final,
            "especiais_usados": self.especiais_usados
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

            if dados.get("classe") not in CLASSES:
                print("\nO salvamento antigo não possui uma classe válida.")
                print("Será necessário começar um novo jogo.")
                return None

            personagem = cls(dados["nome"], dados["classe"])

            personagem.hp_maximo = dados.get(
                "hp_maximo", personagem.hp_maximo
            )
            personagem.hp = dados.get("hp", personagem.hp_maximo)
            personagem.mana_maxima = dados.get(
                "mana_maxima", personagem.mana_maxima
            )
            personagem.mana = dados.get("mana", personagem.mana_maxima)
            personagem.xp = dados.get("xp", 0)
            personagem.nivel = dados.get("nivel", 1)
            personagem.moedas = dados.get("moedas", 30)
            personagem.nivel_concluido = dados.get("nivel_concluido", 0)
            personagem.pocoes = dados.get("pocoes", 2)
            personagem.pocoes_mana = dados.get("pocoes_mana", 1)
            personagem.aliados = dados.get("aliados", [])
            personagem.segredo = dados.get("segredo", False)
            personagem.eventos_concluidos = dados.get(
                "eventos_concluidos", []
            )
            personagem.dialogos_vistos = dados.get("dialogos_vistos", [])
            personagem.conquistas = dados.get("conquistas", [])
            personagem.recompensa_final = dados.get(
                "recompensa_final", False
            )
            personagem.especiais_usados = dados.get("especiais_usados", 0)

            return personagem

        except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
            print("\nNão foi possível carregar o salvamento.")
            return None


def linha():
    print("=" * 55)


def introducao():
    linha()
    print("             OS JOGOS DA SOBREVIVÊNCIA")
    linha()
    print("\nA Capital observa cada movimento seu.")
    print("Distritos inteiros acompanham sua entrada na arena.")
    print("Você não está aqui apenas para sobreviver.")
    print("Você precisa vencer cinco desafios e derrotar o Soberano.")
    print("\nOs recursos são limitados, os inimigos são perigosos")
    print("e nem todo tributo que você encontrar será seu inimigo.")
    print("\nQue a sorte esteja sempre a seu favor.")
    linha()


def criar_personagem():
    print("\nESCOLHA SUA CLASSE")
    print("1. Mago")
    print("   Pouco HP, muita mana e feitiços poderosos.")
    print("2. Arqueiro")
    print("   Equilíbrio entre ataque, mana e precisão.")
    print("3. Guerreiro")
    print("   Muito HP, ataques fortes e grande resistência.")

    while True:
        escolha = input("\nDigite 1, 2 ou 3: ").strip()

        if escolha == "1":
            classe = "Mago"
            break
        elif escolha == "2":
            classe = "Arqueiro"
            break
        elif escolha == "3":
            classe = "Guerreiro"
            break

        print("Escolha inválida.")

    nome = input("Digite o nome do seu personagem: ").strip()

    if not nome:
        nome = "Tributo"

    personagem = Personagem(nome, classe)
    personagem.salvar()

    print(f"\nVocê será {nome}, da classe {classe}.")
    print("A arena está esperando por você.")

    return personagem


def mostrar_status(personagem):
    linha()
    print(f"PERSONAGEM: {personagem.nome}")
    print(f"Classe: {personagem.classe}")
    print(f"Nível do personagem: {personagem.nivel}")
    print(f"HP: {personagem.hp}/{personagem.hp_maximo}")
    print(f"Mana: {personagem.mana}/{personagem.mana_maxima}")
    print(f"XP: {personagem.xp}")
    print(f"Moedas: {personagem.moedas}")
    print(f"Poções de vida: {personagem.pocoes}")
    print(f"Poções de mana: {personagem.pocoes_mana}")
    print(f"Desafios concluídos: {personagem.nivel_concluido}/5")
    print(f"Aliados: {len(personagem.aliados)}")
    print(f"Conquistas: {len(personagem.conquistas)}/{len(CONQUISTAS)}")
    linha()


def desbloquear_conquista(personagem, codigo):
    if codigo not in personagem.conquistas and codigo in CONQUISTAS:
        personagem.conquistas.append(codigo)
        print(f"\nCONQUISTA DESBLOQUEADA: {CONQUISTAS[codigo]}!")
        personagem.salvar()


def verificar_nivel(personagem):
    while personagem.nivel < 10 and personagem.xp >= personagem.nivel * 60:
        personagem.nivel += 1
        personagem.hp_maximo += 8
        personagem.mana_maxima += 5
        personagem.hp = min(personagem.hp_maximo, personagem.hp + 20)
        personagem.mana = min(personagem.mana_maxima, personagem.mana + 15)

        print(f"\nVocê subiu para o nível {personagem.nivel}!")
        print("Seu HP máximo aumentou em 8.")
        print("Sua mana máxima aumentou em 5.")
        print("Você recuperou um pouco de HP e mana.")


def conversar_com_tributos(personagem):
    while True:
        linha()
        print("TRIBUTOS DA ARENA")

        nomes = list(TRIBUTOS.keys())

        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome} — {TRIBUTOS[nome]['descricao']}")

        print("0. Voltar")

        escolha = input("\nCom quem deseja conversar? ").strip()

        if escolha == "0":
            return

        if escolha not in ["1", "2", "3"]:
            print("Escolha inválida.")
            continue

        nome = nomes[int(escolha) - 1]
        tributo = TRIBUTOS[nome]

        while True:
            linha()
            print(f"CONVERSANDO COM {nome.upper()}")
            print(tributo["comum"])
            print("\n1. Oferecer ajuda")
            print("2. Perguntar sobre segredos da arena")
            print("3. Conversa exclusiva da sua classe")
            print("4. Encerrar conversa")

            opcao = input("\nEscolha: ").strip()

            if opcao == "1":
                chave = nome + "_ajuda"

                if chave in personagem.dialogos_vistos:
                    print("Você já conversou sobre isso com esse tributo.")
                    continue

                personagem.dialogos_vistos.append(chave)

                if nome == "Lira":
                    if nome not in personagem.aliados:
                        personagem.aliados.append(nome)
                    print(tributo["ajuda"])
                    desbloquear_conquista(personagem, "aliado")

                elif nome == "Davi":
                    personagem.pocoes += 1
                    print(tributo["ajuda"])
                    print("Você recebeu uma poção de vida.")

                else:
                    personagem.segredo = True
                    print(tributo["ajuda"])
                    print("O chefe final poderá começar com menos HP.")
                    desbloquear_conquista(personagem, "explorador")

                personagem.salvar()

            elif opcao == "2":
                chave = nome + "_segredo"

                if chave in personagem.dialogos_vistos:
                    print("Você já ouviu tudo o que esse tributo sabe.")
                    continue

                personagem.dialogos_vistos.append(chave)

                if nome == "Íris":
                    personagem.segredo = True
                    print("Íris revela uma passagem secreta na arena.")
                    print("Você descobriu uma fraqueza do chefe final.")
                    desbloquear_conquista(personagem, "explorador")
                elif nome == "Lira":
                    personagem.moedas += 5
                    print("Lira indica um esconderijo com 5 moedas.")
                else:
                    personagem.pocoes_mana += 1
                    print("Davi entrega uma poção de mana escondida.")

                personagem.salvar()

            elif opcao == "3":
                chave = nome + "_classe"

                if chave in personagem.dialogos_vistos:
                    print("Você já teve essa conversa especial.")
                    continue

                personagem.dialogos_vistos.append(chave)
                print(tributo["classe"][personagem.classe])

                if personagem.classe == "Mago":
                    personagem.mana = min(
                        personagem.mana_maxima, personagem.mana + 10
                    )
                    print("Você recuperou 10 pontos de mana.")
                elif personagem.classe == "Arqueiro":
                    personagem.moedas += 5
                    print("Você recebeu 5 moedas.")
                else:
                    personagem.hp = min(
                        personagem.hp_maximo, personagem.hp + 10
                    )
                    print("Você recuperou 10 pontos de HP.")

                personagem.salvar()

            elif opcao == "4":
                break

            else:
                print("Escolha inválida.")


def evento_do_nivel(personagem, indice):
    if indice in personagem.eventos_concluidos:
        return

    nivel = NIVEIS[indice]

    linha()
    print(f"EVENTO OPCIONAL: {nivel['nome']}")
    print("Você encontra uma situação inesperada antes da batalha.")
    print("Deseja investigar?")
    print("1. Investigar")
    print("2. Pular o evento e ir direto para o combate")

    escolha = input("Escolha: ").strip()

    if escolha != "1":
        print("Você decide não arriscar tempo nem recursos.")
        personagem.eventos_concluidos.append(indice)
        personagem.salvar()
        return

    if indice == 0:
        print("\nVocê encontra uma mochila presa entre as árvores.")
        print("1. Abrir a mochila")
        print("2. Deixar a mochila")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            if random.randint(1, 100) <= 75:
                personagem.pocoes += 1
                personagem.moedas += 5
                print("Você encontrou uma poção e 5 moedas!")
            else:
                personagem.hp = max(1, personagem.hp - 15)
                print("Era uma armadilha! Você perdeu 15 HP.")

    elif indice == 1:
        print("\nVocê encontra um tributo ferido pedindo ajuda.")
        print("1. Ajudar")
        print("2. Continuar seu caminho")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            personagem.hp = max(1, personagem.hp - 10)
            personagem.moedas += 15
            personagem.pocoes += 1
            print("Você gastou 10 HP, mas recebeu 15 moedas e uma poção.")
            desbloquear_conquista(personagem, "aliado")
        else:
            personagem.moedas += 5
            print("Você encontra 5 moedas perto das ruínas.")

    elif indice == 2:
        print("\nO pântano possui uma passagem escondida.")
        print("1. Seguir pela passagem")
        print("2. Atravessar o pântano")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            personagem.segredo = True
            personagem.moedas += 10
            print("Você encontrou uma passagem secreta e 10 moedas!")
            desbloquear_conquista(personagem, "explorador")
        else:
            personagem.hp = max(1, personagem.hp - 15)
            print("O pântano era perigoso. Você perdeu 15 HP.")

    elif indice == 3:
        print("\nVocê encontra um pequeno esconderijo.")
        print("1. Descansar")
        print("2. Procurar recursos")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            personagem.hp = min(
                personagem.hp_maximo, personagem.hp + 25
            )
            print("Você recuperou até 25 HP.")
        else:
            if random.randint(1, 100) <= 60:
                personagem.pocoes_mana += 1
                personagem.moedas += 10
                print("Você encontrou uma poção de mana e 10 moedas!")
            else:
                personagem.hp = max(1, personagem.hp - 15)
                print("Uma armadilha causou 15 de dano.")

    else:
        print("\nA arena fica silenciosa.")
        print("Você pode se preparar antes do último combate.")
        print("1. Recuperar mana")
        print("2. Recuperar vida")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            personagem.mana = min(
                personagem.mana_maxima, personagem.mana + 20
            )
            print("Você recuperou até 20 de mana.")
        else:
            personagem.hp = min(
                personagem.hp_maximo, personagem.hp + 25
            )
            print("Você recuperou até 25 HP.")

    personagem.eventos_concluidos.append(indice)
    personagem.salvar()


def usar_pocao(personagem):
    if personagem.pocoes <= 0:
        print("Você não possui poções de vida.")
        return False

    if personagem.hp >= personagem.hp_maximo:
        print("Seu HP já está cheio.")
        return False

    personagem.pocoes -= 1
    cura = min(35, personagem.hp_maximo - personagem.hp)
    personagem.hp += cura

    print(f"Você recuperou {cura} HP.")
    return True


def usar_pocao_mana(personagem):
    if personagem.pocoes_mana <= 0:
        print("Você não possui poções de mana.")
        return False

    if personagem.mana >= personagem.mana_maxima:
        print("Sua mana já está cheia.")
        return False

    personagem.pocoes_mana -= 1
    recuperacao = min(25, personagem.mana_maxima - personagem.mana)
    personagem.mana += recuperacao

    print(f"Você recuperou {recuperacao} de mana.")
    return True


def turno_inimigo(personagem, inimigo, escudo, defesa):
    dados_classe = CLASSES[personagem.classe]
    dano = random.randint(inimigo["ataque"][0], inimigo["ataque"][1])

    if inimigo.get("chefe") and random.randint(1, 100) <= 25:
        dano += 10
        print(f"\n{inimigo['nome']} prepara um golpe devastador!")

    if "Lira" in personagem.aliados and random.randint(1, 100) <= 20:
        dano = max(0, dano - 8)
        print("Lira distrai o inimigo! O ataque foi enfraquecido.")

    if escudo:
        dano = dano // 2
        print("Seu Escudo Arcano reduziu o dano!")

    if defesa:
        dano = dano // 2
        print("Sua Defesa de Ferro reduziu o dano!")

    personagem.hp = max(0, personagem.hp - dano)
    print(f"{inimigo['nome']} causou {dano} de dano.")

    return False, False


def combater(personagem, indice):
    dados_nivel = NIVEIS[indice]

    inimigo = {
        "nome": dados_nivel["inimigo"],
        "hp": dados_nivel["hp"],
        "hp_maximo": dados_nivel["hp"],
        "ataque": dados_nivel["ataque"],
        "chefe": indice == 4
    }

    if indice == 4 and personagem.segredo:
        reducao = 50
        inimigo["hp"] -= reducao
        personagem.segredo = False
        print(
            f"\nVocê usa o segredo descoberto! "
            f"O chefe começa com {reducao} HP a menos."
        )

    escudo_ativo = False
    defesa_ativa = False
    mira_ativa = False

    linha()
    print(f"DESAFIO {indice + 1}: {dados_nivel['nome']}")
    print(f"Seu adversário é {inimigo['nome']}!")
    print(f"HP do inimigo: {inimigo['hp']}")
    linha()

    while personagem.hp > 0 and inimigo["hp"] > 0:
        print(f"\nSeu HP: {personagem.hp}/{personagem.hp_maximo}")
        print(f"Sua mana: {personagem.mana}/{personagem.mana_maxima}")
        print(f"HP do inimigo: {inimigo['hp']}/{inimigo['hp_maximo']}")
        print("\n1. Ataque básico")
        print(
            f"2. Ataque especial "
            f"({dados_nivel['inimigo']}) — "
            f"custo: {CLASSES[personagem.classe]['custo_especial']} mana"
        )
        print(
            f"3. Habilidade: {CLASSES[personagem.classe]['habilidade']} "
            f"— custo: {CLASSES[personagem.classe]['custo_habilidade']} mana"
        )
        print("4. Usar poção de vida")
        print("5. Usar poção de mana")
        print("6. Tentar fugir")

        escolha = input("\nEscolha sua ação: ").strip()
        turno_realizado = False

        if escolha == "1":
            dados_classe = CLASSES[personagem.classe]
            dano = random.randint(
                dados_classe["ataque"][0],
                dados_classe["ataque"][1]
            )

            if random.randint(1, 100) <= 15:
                dano = int(dano * 1.5)
                print("ATAQUE CRÍTICO!")

            if mira_ativa:
                dano += 15
                mira_ativa = False
                print("Sua Mira Perfeita aumentou o dano!")

            inimigo["hp"] = max(0, inimigo["hp"] - dano)
            print(f"Você causou {dano} de dano.")
            turno_realizado = True

        elif escolha == "2":
            dados_classe = CLASSES[personagem.classe]
            custo = dados_classe["custo_especial"]

            if personagem.mana < custo:
                print("Mana insuficiente para esse ataque.")
                continue

            personagem.mana -= custo
            dano = random.randint(
                dados_classe["especial"][0],
                dados_classe["especial"][1]
            )

            if personagem.classe == "Mago":
                print("Você lança um feitiço poderoso!")
            elif personagem.classe == "Arqueiro":
                print("Você dispara uma flecha precisa!")
            else:
                print("Você executa um golpe devastador!")

            if mira_ativa:
                dano += 15
                mira_ativa = False
                print("Sua Mira Perfeita aumentou o dano!")

            inimigo["hp"] = max(0, inimigo["hp"] - dano)
            print(f"Você causou {dano} de dano especial.")
            personagem.especiais_usados += 1
            turno_realizado = True

            if personagem.especiais_usados >= 3:
                desbloquear_conquista(personagem, "especialista")

        elif escolha == "3":
            dados_classe = CLASSES[personagem.classe]
            custo = dados_classe["custo_habilidade"]

            if personagem.mana < custo:
                print("Mana insuficiente para usar essa habilidade.")
                continue

            personagem.mana -= custo

            if personagem.classe == "Mago":
                escudo_ativo = True
                print("Você cria um Escudo Arcano para reduzir o próximo dano.")
            elif personagem.classe == "Arqueiro":
                mira_ativa = True
                print("Você prepara a Mira Perfeita para o próximo ataque.")
            else:
                defesa_ativa = True
                print("Você assume a Defesa de Ferro para reduzir o próximo dano.")

            turno_realizado = True

        elif escolha == "4":
            turno_realizado = usar_pocao(personagem)

            if not turno_realizado:
                continue

        elif escolha == "5":
            turno_realizado = usar_pocao_mana(personagem)

            if not turno_realizado:
                continue

        elif escolha == "6":
            if indice == 4:
                print("Não é possível fugir do julgamento final!")
                continue

            if random.randint(1, 100) <= 50:
                print("Você conseguiu fugir e preservou sua vida.")
                personagem.salvar()
                return "fuga"

            print("Você tentou fugir, mas o inimigo bloqueou sua passagem.")
            turno_realizado = True

        else:
            print("Escolha inválida.")
            continue

        if inimigo["hp"] <= 0:
            break

        if turno_realizado:
            escudo_ativo, defesa_ativa = turno_inimigo(
                personagem, inimigo, escudo_ativo, defesa_ativa
            )

        personagem.salvar()

    if personagem.hp <= 0:
        print("\nVocê caiu na arena.")
        print("A Capital interrompe o espetáculo por alguns instantes.")
        personagem.salvar()
        return "derrota"

    print(f"\nVocê derrotou {inimigo['nome']}!")
    personagem.xp += dados_nivel["xp"]
    personagem.moedas += dados_nivel["moedas"]

    print(f"Você ganhou {dados_nivel['xp']} XP.")
    print(f"Você ganhou {dados_nivel['moedas']} moedas.")

    personagem.nivel_concluido = max(
        personagem.nivel_concluido, indice + 1
    )

    desbloquear_conquista(personagem, "primeira_vitoria")

    if personagem.hp <= personagem.hp_maximo * 0.2:
        desbloquear_conquista(personagem, "sobrevivente")

    verificar_nivel(personagem)

    if indice == 4:
        personagem.recompensa_final = True
        desbloquear_conquista(personagem, "campeao")
        print("\nVOCÊ VENCEU O JULGAMENTO FINAL!")
        print("A arena inteira testemunha sua vitória.")
        print("Sua recompensa final é a liberdade e a glória.")
        print("Que a sorte esteja sempre a seu favor.")

    personagem.salvar()
    return "vitoria"


def loja(personagem):
    while True:
        linha()
        print("LOJA DE SUPRIMENTOS")
        print(f"Suas moedas: {personagem.moedas}")
        print("1. Poção de vida (+35 HP) — 20 moedas")
        print("2. Poção de mana (+25 mana) — 15 moedas")
        print("3. Voltar")

        escolha = input("\nEscolha: ").strip()

        if escolha == "1":
            if personagem.moedas < 20:
                print("Você não tem moedas suficientes.")
            else:
                personagem.moedas -= 20
                personagem.pocoes += 1
                print("Você comprou uma poção de vida.")

        elif escolha == "2":
            if personagem.moedas < 15:
                print("Você não tem moedas suficientes.")
            else:
                personagem.moedas -= 15
                personagem.pocoes_mana += 1
                print("Você comprou uma poção de mana.")

        elif escolha == "3":
            break

        else:
            print("Escolha inválida.")

        personagem.salvar()


def mostrar_conquistas(personagem):
    linha()
    print("SUAS CONQUISTAS")

    if not personagem.conquistas:
        print("Você ainda não desbloqueou conquistas.")
    else:
        for codigo in personagem.conquistas:
            print(f"- {CONQUISTAS.get(codigo, codigo)}")

    linha()


def recuperar_apos_derrota(personagem):
    perda = min(personagem.moedas, 15)
    personagem.moedas -= perda
    personagem.hp = max(30, personagem.hp_maximo // 3)
    personagem.mana = max(10, personagem.mana_maxima // 4)

    print("\nUm patrocinador envia ajuda de emergência.")
    print(f"Você perdeu {perda} moedas.")
    print(f"Você voltou com {personagem.hp} HP.")
    print(f"Você voltou com {personagem.mana} de mana.")

    personagem.salvar()


def iniciar_jogo(personagem):
    while True:
        if personagem.recompensa_final:
            linha()
            print("VOCÊ JÁ CONCLUIU O RPG!")
            print("A vitória final está registrada no seu salvamento.")
            print("Você pode rever seu status, suas conquistas ou sair.")
            print("1. Ver status")
            print("2. Ver conquistas")
            print("3. Sair")

            escolha = input("\nEscolha: ").strip()

            if escolha == "1":
                mostrar_status(personagem)
            elif escolha == "2":
                mostrar_conquistas(personagem)
            elif escolha == "3":
                personagem.salvar()
                print("Jogo salvo. Até a próxima!")
                break
            else:
                print("Escolha inválida.")

            continue

        if personagem.hp <= 0:
            recuperar_apos_derrota(personagem)

        linha()
        print(f"ARENA DA SOBREVIVÊNCIA — {personagem.nome}")
        print(f"Classe: {personagem.classe}")
        print(
            f"Desafios concluídos: "
            f"{personagem.nivel_concluido}/5"
        )
        print("1. Continuar para o próximo desafio")
        print("2. Conversar com os tributos")
        print("3. Comprar suprimentos")
        print("4. Ver status")
        print("5. Ver conquistas")
        print("6. Salvar jogo")
        print("7. Sair")

        escolha = input("\nEscolha: ").strip()

        if escolha == "1":
            indice = personagem.nivel_concluido

            if indice >= len(NIVEIS):
                personagem.recompensa_final = True
                personagem.salvar()
                continue

            if personagem.hp <= 0:
                print("Você precisa recuperar seu HP antes de continuar.")
                continue

            evento_do_nivel(personagem, indice)

            if personagem.hp <= 0:
                print("Você não consegue continuar sem HP.")
                recuperar_apos_derrota(personagem)
                continue

            resultado = combater(personagem, indice)

            if resultado == "vitoria":
                if indice < 4:
                    print("\nVocê sobreviveu ao desafio.")
                    print("Mas a arena ainda guarda perigos.")
                    input("\nPressione Enter para continuar...")
            elif resultado == "derrota":
                recuperar_apos_derrota(personagem)
            elif resultado == "fuga":
                print("Você poderá tentar o desafio novamente depois.")

        elif escolha == "2":
            conversar_com_tributos(personagem)

        elif escolha == "3":
            loja(personagem)

        elif escolha == "4":
            mostrar_status(personagem)

        elif escolha == "5":
            mostrar_conquistas(personagem)

        elif escolha == "6":
            personagem.salvar()
            print("Seu progresso foi salvo.")

        elif escolha == "7":
            personagem.salvar()
            print("Jogo salvo. Que a sorte esteja sempre a seu favor.")
            break

        else:
            print("Escolha inválida.")


def main():
    linha()
    print("       RPG: OS JOGOS DA SOBREVIVÊNCIA")
    linha()
    print("1. Continuar jogo salvo")
    print("2. Começar novo jogo")

    escolha = input("\nEscolha: ").strip()

    if escolha == "1":
        personagem = Personagem.carregar()

        if personagem is None:
            print("\nNão existe um salvamento compatível.")
            print("Vamos começar uma nova aventura.")
            introducao()
            personagem = criar_personagem()

    elif escolha == "2":
        introducao()
        personagem = criar_personagem()

    else:
        print("Opção inválida. Iniciando uma nova aventura.")
        introducao()
        personagem = criar_personagem()

    iniciar_jogo(personagem)


if __name__ == "__main__":
    main()