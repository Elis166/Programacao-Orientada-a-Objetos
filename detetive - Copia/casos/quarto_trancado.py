from modelos.caso import Caso
from modelos.suspeito import Suspeito
from modelos.testemunha import Testemunha
from modelos.evidencia import Evidencia

caso1 = Caso(
    """
╔══════════════════════════════════════════════════════════╗
║                  DEPARTAMENTO DE POLÍCIA                 ║
║                  ARQUIVO CONFIDENCIAL                    ║
╠══════════════════════════════════════════════════════════╣
║ CASO: 001                                                ║
║ NOME: O QUARTO TRANCADO                                  ║
║ STATUS: EM INVESTIGAÇÃO                                  ║
╠══════════════════════════════════════════════════════════╣
║ VÍTIMA: Ricardo Menezes                                  ║
║ IDADE : 48 anos                                          ║
║ LOCAL : Escritório da Mansão Menezes                     ║
╠══════════════════════════════════════════════════════════╣
║ DESCRIÇÃO:                                               ║
║ Às 7h15 da manhã, o empresário Ricardo Menezes, 48 anos, ║
║ é encontrado morto em seu escritório particular dentro de║
║ sua mansão.                                              ║
║ A porta estava trancada por dentro. As janelas estavam   ║
║ fechadas e possuíam grades. Nenhum sinal de arrombamento ║
║ foi encontrado.                                          ║
║ Tudo indica um suicídio, mas algumas evidências não      ║
║ fazem sentido.                                           ║
╠══════════════════════════════════════════════════════════╣
║ DETETIVE RESPONSÁVEL: Você.                              ║
╚══════════════════════════════════════════════════════════╝
""", "\n===== CASO RESOLVIDO! =====\nO culpado era Carla Souza.\nMotivação:\nCarla desviava dinheiro da empresa.\nRicardo descobriu a fraude e ameaçou denunciá-la.\nPara evitar ser presa, Carla assassinou Ricardo\ne tentou simular um suicídio."
)

suspeitos = [
    Suspeito(
        "Ana Menezes",
        "Esposa da Vítima, casados à 20 anos.",
        "Mulher branca; loira; 39 anos; 1,62m de altura; pesa 88kg.",
        "Ricardo estava muito estressado ultimamente.",
        caso1
    ),

    Suspeito(
        "Lucas Menezes",
        "Filho da vítima.",
        "Homem branco; cabelo preto; 16 anos; 1,75m de altura;  pesa 60kg.",
        "Ouvi um barulho por volta das 22h30.",
        caso1
    ),

    Suspeito(
        "Eduardo Costa",
        "Sócio da vítima.",
        "Homem pardo; cabelo castanho; 40 anos; 1,60m de altura; pesa 72kg.",
        "Discutimos naquela tarde, mas não fui eu.",
        caso1
    ),

    Suspeito(
        "Carla Souza",
        "Secretária de longa data da vítima.",
        "Mulher branca; cabelo ruivo; tem 32 anos; 1,77 de altura; pesa 64kg.",
        "Fui embora antes do jantar, por volta das 18h.",
        caso1
    ),
    Suspeito(
        "Ricardo Menezes",
        "Vítima.",
        "Homem branco; cabelo preto; tem 48 anos; 1,64 de altura; pesa 70kg.",
        "N/A",
        caso1
    )
]

caso1.set_culpado(suspeitos[3])

testemunhas = [
    Testemunha(
        "Pedro Santos",
        "Vizinho, mora na casa ao lado.",
        "Por volta das 21h, vi alguém entrando pela porta dos fundos. Estava escuro demais, só sei que a pessoa era alta.",
        caso1
    )
]

evidencias = [
    Evidencia(
        "Faca de cozinha",
        "Encontrada próxima da mão direita da vítima.",
        caso1
    ),

    Evidencia(
        "Mensagem no computador",
        "Suposta carta de suicídio digitada às 23:48.",
        caso1
    ),

    Evidencia(
        "Relatório financeiro",
        "Providenciado por Ana; indica desvios de dinheiro da conta de Ricardo.",
        caso1
    ),
    Evidencia(
        "Mensagens de Ricardo",
        "'Preciso resolver umas coisas com ela agora.' destinada à um sócio, 21:52.",
        caso1
    ),
    Evidencia(
        "Chaves-reserva",
        "Possui as digitais de um funcionário do escritório.",
        caso1
    )
]