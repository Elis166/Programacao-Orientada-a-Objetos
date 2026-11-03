from src.models.personagem import Personagem

class Mago(Personagem):
    PERFIL = {
        "hp": 90,
        "mana": 60,
        "ataque": (12, 22),
        "especial": (28, 40),
        "custo_especial": 15,
        "habilidade": "Escudo Arcano",
        "custo_habilidade": 10,
    }

    def __init__(self, id_personagem: int, nome: str, estudante):
        super().__init__(
            id_personagem, nome, estudante,
            hp_max=self.PERFIL["hp"],
            mana_max=self.PERFIL["mana"],
            dano_base=self.PERFIL["ataque"][0],
        )
        self.poder_magico = 30


class Guerreiro(Personagem):
    PERFIL = {"hp": 130,
               "mana": 35,
                "ataque": (18, 28),
                "especial": (27, 42),
                "custo_especial": 14, 
                "habilidade": "Defesa de Ferro", 
                "custo_habilidade": 10}
    
    def __init__(self, id_personagem: int, nome: str, estudante):
        # HP alto e mana baixa
        super().__init__(id_personagem, nome, estudante, hp_max=160, mana_max=30, dano_base=20)
        self.armadura = 5


class Arqueiro(Personagem):
    PERFIL = {
        "hp": 105, "mana": 45, "ataque": (15, 25), "especial": (25, 38), "custo_especial": 12, "habilidade": "Mira Perfeita", "custo_habilidade": 10
    }
    def __init__(self, id_personagem: int, nome: str, estudante):
        # status equilibrados e alta chance crítica
        super().__init__(id_personagem, nome, estudante, hp_max=110, mana_max=70, dano_base=22)
        self.precisao = 0.85