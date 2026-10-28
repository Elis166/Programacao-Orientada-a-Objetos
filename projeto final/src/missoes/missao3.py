class Aventureiro:
    def __init__(self, nome: str):
        self.nome = nome
        self.__vidas = 3

    @property
    def vidas(self) -> int:
        return self.__vidas

    def perder_vida(self) -> None:
        self.__vidas = max(0, self.__vidas - 1)

    def __str__(self) -> str:
        return f'{self.nome} ({self.vidas} vidas)'


class PortaoMagico:
    def __init__(self):
        self.aberto = False

    def abrir(self):
        self.aberto = True


class Cristal:
    def __init__(self):
        self.__energia = 100
        self.ativado = False

    def liberar_energia(self):
        self.ativado = True
        return self.__energia


class Jogo:
    def __init__(self):
        self.jogador = None
        self.portao = PortaoMagico()
        self.cristal = Cristal()

    def mostrar(self, texto: str):
        print('\n' + texto + '\n')

    def perguntar(self, pergunta: str, alternativas: list[str], correta: str,
                  sucesso: str, falha: str) -> bool:
        self.mostrar(pergunta)
        for alternativa in alternativas:
            print(alternativa)

        while True:
            escolha = input('\nSua escolha (A, B ou C): ').strip().upper()
            if escolha in ('A', 'B', 'C'):
                break
            print('Escolha inválida. Digite A, B ou C (sem perder vida).')

        if escolha == correta:
            self.mostrar(sucesso)
            return True

        self.jogador.perder_vida()
        self.mostrar(falha)
        self.mostrar(f'Você perdeu uma vida! Restam {self.jogador.vidas}.')
        return False

    def iniciar(self):
        print('=== A VILA DOS AMALDIÇOADOS ===')
        nome = input('Qual é o nome do aventureiro? ').strip() or 'Aventureiro'
        self.jogador = Aventureiro(nome)
        self.mostrar(
            f'Era uma vez, uma vila chamada Eldoria, que era uma vila tranquila, protegida pelo Cristal da Aurora.\nUm dia, um feiticeiro chamado Morvan lançou uma maldição sobre o povo daquele lugar, fazendo com que\nse transformassem em criaturas todas as noites. Por muito tempo ficaram presos naquela maldição, até que, acidentalmente, um\naventureiro se perdeu depois de uma grande tempestade e foi parar ness misteriosa vila. Estranhou muito, pois as ruas estavam desertas,\nas casas, vazias. Pocurando abrigo, deu de cara com uma senhora chamada Helena,\nque lhe contou sobre a maldição e revelou que a única maneira de salvar Eldoria seria recuperar o Cristal da Aurora, escondido na Floresta Sombria.\nDeterminado a ajudar, o aventureiro aceitou a missão. Antes de partir, recebeu de Helena um amuleto com três cargas mágicas, que\nrepresentavam suas três vidas. A cada escolha errada, perderia uma carga e, caso perdesse todas, sua jornada chegaria ao fim.\nPegou o amoleto e partiu em direção à floresta, sem imaginar os desafios que o\naguardavam.'
        )

        # DESAFIO 1
        acertou = self.perguntar(
            'DESAFIO 1 — O PORTÃO ENCANTADO\n'
            'Uma inscrição revela:\n'
            'class PortaoMagico:\n'
            '    def __init__(self):\n'
            '        self.aberto = False\n'
            '    def abrir(self):\n'
            '        self.aberto = True\n'
            'portao = PortaoMagico()\n'
            'Qual comando abre o portão?',
            ['A) portao.abrir()', 'B) PortaoMagico.abrir()', 'C) portao.aberto()'],
            'A',
            'Os símbolos brilham e o portão se abre. Você segue pela trilha iluminada.',
            'O chão cede! Você cai no Túnel Esquecido e encontra uma saída para a floresta.'
        )
        if acertou:
            self.portao.abrir()
        if self.fim_por_derrota():
            return

        # DESAFIO 2
        self.mostrar('Você chega à Ponte das Sombras. Uma criatura mostra o encantamento: '
                     'energia = 10; custo = 0; resultado = energia / custo.')
        self.perguntar(
            'DESAFIO 2 — A PONTE DAS SOMBRAS\n'
            'Qual recurso trata o erro da divisão por zero sem encerrar o programa?',
            ['A) try e except ZeroDivisionError',
             'B) Apenas print()',
             'C) break para corrigir a divisão'],
            'A',
            'O encantamento reconhece o erro e permite atravessar a ponte com segurança.',
            'A ponte desaparece! Você segue pela margem do rio e encontra outra passagem.'
        )
        if self.fim_por_derrota():
            return

        # DESAFIO 3
        acertou = self.perguntar(
            'DESAFIO 3 — O CRISTAL DA AURORA\n'
            'No templo, uma inscrição revela:\n'
            'class Cristal:\n'
            '    def __init__(self):\n'
            '        self.__energia = 100\n'
            '    def liberar_energia(self):\n'
            '        return self.__energia\n'
            'cristal = Cristal()\n'
            'Qual comando permite obter a energia protegida?',
            ['A) cristal.__energia',
             'B) cristal.liberar_energia()',
             'C) cristal.energia = 100'],
            'B',
            'A barreira desaparece! Você recupera o Cristal da Aurora.',
            'Uma armadilha leva você à Câmara Esquecida. Depois de encontrar a saída, '
            'você consegue recuperar o cristal.'
        )
        if self.fim_por_derrota():
            return

        self.cristal.liberar_energia()
        self.mostrar('VITÓRIA! Você devolve o cristal à praça de Eldoria. '
                     'A maldição é quebrada e os moradores o nomeiam Guardião de Eldoria!')
        self.salvar_resultado('Vitória')

    def fim_por_derrota(self) -> bool:
        if self.jogador.vidas > 0:
            return False
        self.mostrar('GAME OVER! Suas três vidas acabaram. A maldição continua em Eldoria.')
        self.salvar_resultado('Derrota')
        return True

    def salvar_resultado(self, resultado: str):
        try:
            with open('resultado_eldoria.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(f'Jogador: {self.jogador.nome}\n')
                arquivo.write(f'Resultado: {resultado}\n')
                arquivo.write(f'Vidas restantes: {self.jogador.vidas}\n')
            print('Resultado salvo em resultado_eldoria.txt')
        except OSError as erro:
            print(f'Não foi possível salvar o resultado: {erro}')


if __name__ == '__main__':
    Jogo().iniciar()
