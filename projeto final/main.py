from enum import Enum
from typing import List, Optional


# =====================================================================
# 1. ENUMS E CLASSES DE SUPORTE
# =====================================================================

class StatusCampanha(Enum):
    NAO_INICIADA = "Não Iniciada"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"


class StatusMissao(Enum):
    DISPONIVEL = "Disponível"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"


class Recompensa:
    def __init__(self, id_recompensa: int, nome: str, descricao: str, tipo: str):
        self.id_recompensa = id_recompensa
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo


class Conquista:
    def __init__(self, id_conquista: int, nome: str, descricao: str, requisito: str):
        self.id_conquista = id_conquista
        self.nome = nome
        self.descricao = descricao
        self.requisito = requisito


# =====================================================================
# 2. ENTIADES PRINCIPAIS (Personagem e Missão)
# =====================================================================

class Missao:
    def __init__(
        self,
        id_missao: int,
        titulo: str,
        descricao: str,
        dificuldade: str,
        experiencia: int,
        nivel_minimo: int = 1,
        recompensa: Optional[Recompensa] = None,
        conquista: Optional[Conquista] = None,
    ):
        self.id_missao = id_missao
        self.titulo = titulo
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.experiencia = experiencia
        self.nivel_minimo = nivel_minimo
        self.recompensa = recompensa
        self.conquista = conquista
        self.status = StatusMissao.DISPONIVEL


class Personagem:
    def __init__(self, id_personagem: int, nome: str, hp_max: int, mana_max: int, dano_base: int):
        self.id_personagem = id_personagem
        self.nome = nome
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.mana_max = mana_max
        self.mana_atual = mana_max
        self.dano_base = dano_base
        self.nivel = 1
        self.experiencia = 0
        
        self.missoes_ativas: List[Missao] = []
        self.missoes_concluidas: List[Missao] = []
        self.inventario: List[Recompensa] = []
        self.conquistas: List[Conquista] = []

    @property
    def classe_nome(self) -> str:
        return self.__class__.__name__

    @property
    def esta_vivo(self) -> bool:
        return self.hp_atual > 0

    def ganhar_experiencia(self, cantidad: int):
        self.experiencia += cantidad
        print(f"✨ {self.nome} recebeu +{cantidad} XP! (Total: {self.experiencia} XP)")
        
        # Sobe de nível a cada 100 XP
        xp_necessaria = self.nivel * 100
        while self.experiencia >= xp_necessaria:
            self.experiencia -= xp_necessaria
            self.nivel += 1
            self.hp_max += 20
            self.hp_atual = self.hp_max
            self.dano_base += 5
            print(f"🎉 PARABÉNS! {self.nome} subiu para o Nível {self.nivel}!")
            xp_necessaria = self.nivel * 100

    def aceitar_missao(self, missao: Missao):
        if self.nivel < missao.nivel_minimo:
            print(f"❌ {self.nome} precisa ser nível {missao.nivel_minimo} para aceitar '{missao.titulo}'.")
            return
        
        missao.status = StatusMissao.EM_ANDAMENTO
        self.missoes_ativas.append(missao)
        print(f"📜 {self.nome} aceitou a missão: [{missao.titulo}]")

    def concluir_missao(self, missao: Missao):
        if missao not in self.missoes_ativas:
            return

        self.missoes_ativas.remove(missao)
        self.missoes_concluidas.append(missao)
        missao.status = StatusMissao.CONCLUIDA

        print(f"\n✅ MISSAO CONCLUÍDA por {self.nome}: '{missao.titulo}'!")
        self.ganhar_experiencia(missao.experiencia)

        if missao.recompensa:
            self.inventario.append(missao.recompensa)
            print(f"🎁 Recompensa obtida: {missao.recompensa.nome}")

        if missao.conquista:
            self.conquistas.append(missao.conquista)
            print(f"🏆 Conquista Desbloqueada: [{missao.conquista.nome}]")

    def atacar(self, alvo: 'Personagem'):
        if not self.esta_vivo:
            return
        print(f"⚔️ {self.nome} ({self.classe_nome}) ataca {alvo.nome} causando {self.dano_base} de dano!")
        alvo.receber_dano(self.dano_base)

    def receber_dano(self, cantidad: int):
        self.hp_atual = max(0, self.hp_atual - cantidad)
        print(f"💔 {self.nome} HP: {self.hp_atual}/{self.hp_max}")
        if not self.esta_vivo:
            print(f"☠️ {self.nome} foi derrotado!")


# Subclasses de Personagens
class Mago(Personagem):
    def __init__(self, id_personagem: int, nome: str):
        super().__init__(id_personagem, nome, hp_max=80, mana_max=150, dano_base=25)

class Guerreiro(Personagem):
    def __init__(self, id_personagem: int, nome: str):
        super().__init__(id_personagem, nome, hp_max=150, mana_max=40, dano_base=18)

class ChefeBurlador(Personagem):
    """Inimigo Especial de Boss Fight."""
    def __init__(self, nome: str):
        super().__init__(999, nome, hp_max=120, mana_max=0, dano_base=15)


# =====================================================================
# 3. GERENCIADOR DA CAMPANHA
# =====================================================================

class CampanhaAtiva:
    def __init__(self, id_campanha: int, titulo: str, descricao: str):
        self.id_campanha = id_campanha
        self.titulo = titulo
        self.descricao = descricao
        self.status = StatusCampanha.NAO_INICIADA
        self.capitulo_atual = 1
        
        self.jogadores: List[Personagem] = []
        self.quadro_de_missoes: List[Missao] = []

    def iniciar_campanha(self):
        self.status = StatusCampanha.EM_ANDAMENTO
        print(f"\n🚀 === CAMPANHA INICIADA: {self.titulo} ===")
        print(f"📖 {self.descricao}\n")

    def registrar_jogador(self, jogador: Personagem):
        self.jogadores.append(jogador)
        print(f"🛡️ {jogador.nome} o {jogador.classe_nome} entrou na campanha!")

    def adicionar_missao(self, missao: Missao):
        self.quadro_de_missoes.append(missao)

    def simular_boss_fight(self, chefao: ChefeBurlador):
        print(f"\n👹 --- BOSS FIGHT: {chefao.nome} APARECEU! ---")
        turno = 1
        
        while chefao.esta_vivo and any(j.esta_vivo for j in self.jogadores):
            print(f"\n--- Turno {turno} ---")
            for jogador in self.jogadores:
                if jogador.esta_vivo and chefao.esta_vivo:
                    jogador.atacar(chefao)
            
            if chefao.esta_vivo:
                # O Boss ataca o primeiro jogador vivo
                alvo = next((j for j in self.jogadores if j.esta_vivo), None)
                if alvo:
                    chefao.atacar(alvo)
            turno += 1

        if not chefao.esta_vivo:
            print(f"\n🎉 VITORIA! O Boss {chefao.nome} foi derrotado pela equipe!")
            for jogador in self.jogadores:
                if jogador.esta_vivo:
                    jogador.ganhar_experiencia(150)

    def exibir_leaderboard(self):
        print("\n🏆 ================= RANKING DA CAMPANHA =================")
        ranking = sorted(self.jogadores, key=lambda j: (j.nivel, j.experiencia), reverse=True)
        for pos, j in enumerate(ranking, 1):
            print(f" {pos}º Lugar | {j.nome} ({j.classe_nome}) - Nível {j.nivel} | {j.experiencia} XP | Itens: {len(j.inventario)}")
        print("=========================================================\n")


# =====================================================================
# 4. EXECUÇÃO DA SIMULAÇÃO DA CAMPANHA
# =====================================================================

if __name__ == "__main__":
    # 1. Instanciar a Campanha
    campanha = CampanhaAtiva(
        id_campanha=1,
        titulo="A Jornada do Código Sagrado",
        descricao="Supere os desafios de programação para salvar o reino dos Bugs!"
    )

    # 2. Criar e Adicionar Jogadores
    mago = Mago(id_personagem=1, nome="Merlin Pythonico")
    guerreiro = Guerreiro(id_personagem=2, nome="Conan o Compilador")
    
    campanha.registrar_jogador(mago)
    campanha.registrar_jogador(guerreiro)
    campanha.iniciar_campanha()

    # 3. Criar Recompensas, Conquistas e Missões do Capítulo 1
    recompensa_1 = Recompensa(1, "Livro de Sintaxe", "Aumenta entendimento de funções", "Item")
    conquista_1 = Conquista(1, "Primeiro Script", "Completou o primeiro desafio", "Missao 101")

    missao_1 = Missao(
        id_missao=101,
        titulo="Desafio 01: Variáveis e Loops",
        descricao="Implemente os exercícios do Capítulo 1.",
        dificuldade="Fácil",
        experiencia=120, # Dá XP suficiente para subir ao nível 2
        nivel_minimo=1,
        recompensa=recompensa_1,
        conquista=conquista_1
    )

    # 4. Jogadores aceitam e completam missões
    mago.aceitar_missao(missao_1)
    mago.concluir_missao(missao_1)

    guerreiro.aceitar_missao(missao_1)
    guerreiro.concluir_missao(missao_1)

    # 5. Evento Especial: Boss Fight no final do Capítulo
    boss_modulo_1 = ChefeBurlador(nome="Bug do Loop Infinito")
    campanha.simular_boss_fight(boss_modulo_1)

    # 6. Exibir o Placar do Leaderboard ao final
    campanha.exibir_leaderboard()