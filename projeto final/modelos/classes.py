from personagem import Personagem

class Mago(Personagem):
    def __init__(self, id_personagem: int, nome: str, estudante):
        # HP menor, mana alta e dano equilibrado
        super().__init__(id_personagem, nome, estudante, hp_max=80, mana_max=150, dano_base=15)
        self.poder_magico = 30

    def usar_habilidade_especial(self, alvo: Personagem):
        custo_mana = 40
        if self._mana_atual < custo_mana:
            print(f"{self._nome} não tem mana suficiente ({self._mana_atual}/{custo_mana})!")
            return
        
        self._mana_atual -= custo_mana
        dano_total = self._dano_base + self.poder_magico
        print(f"{self._nome} lança **Bola de Fogo** em {alvo.nome}!")
        alvo.receber_dano(dano_total)


class Guerreiro(Personagem):
    def __init__(self, id_personagem: int, nome: str, estudante):
        # HP alto e mana baixa
        super().__init__(id_personagem, nome, estudante, hp_max=160, mana_max=30, dano_base=20)
        self.armadura = 5

    def receber_dano(self, quantidade: int):
        """Passiva do Guerreiro: reduz o dano recebido usando a armadura."""
        dano_reduzido = max(1, quantidade - self.armadura)
        print(f"Armadura de {self._nome} absorveu {self.armadura} de dano!")
        super().receber_dano(dano_reduzido)

    def usar_habilidade_especial(self, alvo: Personagem):
        custo_mana = 15
        if self._mana_atual < custo_mana:
            print(f"{self._nome} não tem mana suficiente!")
            return
            
        self._mana_atual -= custo_mana
        dano_total = self._dano_base * 2
        print(f"🪓 {self._nome} usa **Golpe Pesado** em {alvo.nome}!")
        alvo.receber_dano(dano_total)


class Arqueiro(Personagem):
    def __init__(self, id_personagem: int, nome: str, estudante):
        # status equilibrados e alta chance crítica
        super().__init__(id_personagem, nome, estudante, hp_max=110, mana_max=70, dano_base=22)
        self.precisao = 0.85

    def usar_habilidade_especial(self, alvo: Personagem):
        custo_mana = 25
        if self._mana_atual < custo_mana:
            print(f"{self._nome} não tem mana suficiente!")
            return

        self._mana_atual -= custo_mana
        print(f"{self._nome} lança **Chuva de Flechas** em {alvo.nome}!")
        # Exemplo: dois ataques rápidos seguidos
        alvo.receber_dano(self._dano_base)
        alvo.receber_dano(self._dano_base)