from typing import List, Optional
from src.models.estudante import Estudante
from src.models.personagem import Personagem
from src.models.missao import Missao
from src.models.enums import StatusMissao


class Jogo:
    """Gerenciador principal da sessão do jogador."""

    def __init__(self, jogador: Personagem):
        self._jogador = jogador
        self._quadro_missoes: List[Missao] = []

    @property
    def jogador(self) -> Personagem:
        return self._jogador

    def adicionar_missao(self, missao: Missao):
        self._quadro_missoes.append(missao)

    def listar_missoes_disponiveis(self) -> List[Missao]:
        """Retorna apenas as missões que o jogador tem nível para realizar."""
        return [
            m
            for m in self._quadro_missoes
            if m.status == StatusMissao.DISPONIVEL
            and self._jogador.nivel >= m.nivel_minimo
        ]

    def exibir_painel_jogador(self):
        """Exibe os dados e status do jogador na tela."""
        p = self._jogador
        print("\n" + "=" * 45)
        print(f"👤 JOGADOR: {p.nome} | Classe: {p.classe_nome}")
        print(f"📊 Nível: {p.nivel} | XP: {p.experiencia}/{p.nivel * 100}")
        print(f"❤️  HP: {p.hp_atual}/{p.hp_max} | 💧 Mana: {p.mana_atual}/{p.mana_max}")
        print(f"🎒 Inventário ({len(p.inventario)} itens): {', '.join([i.nome for i in p.inventario]) or 'Vazio'}")
        print(f"🏆 Conquistas ({len(p.conquistas)}): {', '.join([c.nome for c in p.conquistas]) or 'Nenhuma'}")
        print("=" * 45 + "\n")