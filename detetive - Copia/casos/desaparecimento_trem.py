from modelos.caso import Caso
from modelos.suspeito import Suspeito
from modelos.testemunha import Testemunha
from modelos.evidencia import Evidencia

caso2 = Caso(
    """
╔══════════════════════════════════════════════════════════╗
║                  DEPARTAMENTO DE POLÍCIA                 ║
║                  ARQUIVO CONFIDENCIAL                    ║
╠══════════════════════════════════════════════════════════╣
║ CASO: 002                                                ║
║ NOME: O DESAPARECIMENTO NO TREM                          ║
║ STATUS: EM INVESTIGAÇÃO                                  ║
╠══════════════════════════════════════════════════════════╣
║ VÍTIMA: Sofia Bezerra                                    ║
║ IDADE : 19 anos                                          ║
║ LOCAL : Expresso Oriente                                 ║
╠══════════════════════════════════════════════════════════╣
║ DESCRIÇÃO:                                               ║
║ Durante uma viagem noturna de trem, uma estudante        ║
║ universitária chamada Sofia desaparece misteriosamente.  ║
║ Contamos com a sua ajuda, detetive, para descobrir       ║
║ o que aconteceu.                                         ║
╠══════════════════════════════════════════════════════════╣
║ DETETIVE RESPONSÁVEL: Você.                              ║
╚══════════════════════════════════════════════════════════╝
""", '\n===== CASO RESOLVIDO! =====\nApós analisar todas as evidências, você descobre que Sofia não foi sequestrada.\nSofia era testemunha de um crime e vinha recebendo ameaças.\nCom medo, ela planejou cuidadosamente o próprio desaparecimento.\nEla pesquisou horários de trem, cidades vizinhas e locais para morar.\nTambém deixou o celular para trás para dificultar seu rastreamento.\nA pessoa vista desembarcando na estação de Santa Clara era a própria Sofia.\nCASO ENCERRADO!'
)

suspeitos = [
    Suspeito(
        'Lucas Oliveira.',
        'Namorado da vítima.',
        'Homem negro; cabelo preto, curto e cacheado; 23 anos de idade; 180 cm de altura; pesa 85 kg; usa óculos.',
        'Ela parecia nervosa nas últimas semanas.',
        caso2
    ),
    Suspeito(
        'Marina Silva.',
        'Melhor amiga da vítima.',
        'Mulher branca; cabelo ruivo, longo e liso; 22 anos de idade; 168 cm de altura; pesa 66 kg; tem uma cicatriz na palma da mão esquerda.',
        'Ela me disse que precisava resolver um problema sozinha.',
        caso2
    ),
    Suspeito(
        'Roberto Costa.',
        'Funcionário do trem.',
        'Homem branco; cabelo preto, curto e liso; 46 anos de idade; 188 cm de altura; pesa 89 kg; usa óculos.',
        'Vi uma garota parecida com ela andando para outro vagão.',
        caso2
    ),
    Suspeito(
        'Sofia Bezerra.',
        'Vítima.',
        'Mulher parda; cabelo preto, curto e liso; 19 anos de idade; 169 cm de altura; pesa 68 kg.',
        'Vi uma garota parecida com ela andando para outro vagão.',
        caso2
    )
]

caso2.set_culpado(suspeitos[3])

testemunhas = [
    Testemunha(
        'Dona Helena.',
        'Mulher negra; cabelo grisalho, médio e cacheado; 71 anos de idade; 161 cm de altura; passageira.',
        'Ela parecia nervosa e olhava para trás o tempo todo.',
        caso2
    ),
    Testemunha(
        'Davi Lopes.',
        'Homem branco; cabelo loiro, curto e cacheado; 32 anos de idade; 183 cm de altura; funcionário.',
        'Vi Sofia entrando no banheiro com uma mochila grande.',
        caso2
    ),
    Testemunha(
        'Seu João.',
        'Homem negro; cabelo grisalho, curto e cacheado; 75 anos de idade; 170 cm de altura; passageiro.',
        'Vi uma jovem parecida com ela desembarcando na estação de Santa Clara.',
        caso2
    )
]

evidencias = [
    Evidencia(
        'Histórico de mensagens com o Lucas.',
        'As mensagens mostram que eles tiveram uma briga.',
        caso2
    ),
    Evidencia(
        'Histórico de pesquisas',
        'O histórico de pesquisa de Sofia mostra que ela buscou horários de trens, cidades vizinhas, aluguéis de apartamento.',
        caso2
    ),
    Evidencia(
        'Última localização do celular dela',
        'Mostra que o celular permaneceu no trem mesmo após o desaparecimento. Isso é estranho: como ela desapareceu sem o celular?',
        caso2
    ),
    Evidencia(
        'Bilhete rasgado',
        'Parte de uma passagem é encontrada perto do assento dela. A passagem é para uma estação anterior ao destino final.',
        caso2
    ),
    Evidencia(
        'Mochila abandonada',
        'Contém objetos pessoais, mas alguns estão faltando.',
        caso2
    ),
    Evidencia(
        'Foto de passageiro',
        'Mostra Sofia perto da porta do trem.',
        caso2
    ),
    Evidencia(
        'Câmera do corredor',
        'Registra Sofia caminhando sozinha.',
        caso2
    ),
    Evidencia(
        'Câmera da plataforma',
        'Mostra alguém com roupas parecidas desembarcando.',
        caso2
    )
]