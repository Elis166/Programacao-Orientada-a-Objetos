from modelos.caso import Caso
from modelos.suspeito import Suspeito
from modelos.testemunha import Testemunha
from modelos.evidencia import Evidencia

caso3 = Caso("""
╔══════════════════════════════════════════════════════════╗
║                  DEPARTAMENTO DE POLÍCIA                 ║
║                  ARQUIVO CONFIDENCIAL                    ║
╠══════════════════════════════════════════════════════════╣
║ CASO: 003                                                ║
║ NOME: NUNCA MINTA                                        ║
║ STATUS: EM INVESTIGAÇÃO                                  ║
╠══════════════════════════════════════════════════════════╣
║ VÍTIMA: Dra. Adrienne Hale                               ║
║ IDADE : Desconhecida                                     ║
║ LOCAL : Mansão Hale (Isolada pela Nevasca)               ║
╠══════════════════════════════════════════════════════════╣
║ DESCRIÇÃO:                                               ║
║ A Dra. Adrienne Hale sumiu há anos. O caso estava        ║
║ arquivado até que um jovem casal, Tricia e Ethan, comprou║
║ a mansão isolada dela e ficou preso lá dentro devido a   ║
║ uma nevasca histórica. Ethan ligou para a polícia        ║
║ dizendo ter encontrado uma sala secreta com arquivos, mas║
║ a ligação caiu. Você ganhou acesso remoto ao servidor da ║
║ casa para investigar os dados antes que a nevasca passe. ║
╠══════════════════════════════════════════════════════════╣
║ DETETIVE RESPONSÁVEL: Você.                              ║
╚══════════════════════════════════════════════════════════╝
""", "\n===== CASO RESOLVIDO! =====\nApós analisar todas as evidências, você descobre o plano de Tricia.\nLuke fugiu porque Tricia o stalkeava e o ameaçou, fazendo ele parecer o culpado perfeito.\nEthan descobriu o que Tricia fez após o casamento, e foi cúmplice por medo e ganância, \nusando o dinheiro da falecida doutora para pagar as dívidas.\nTricia planejou tudo. Ela levou Ethan para a mansão naquela noite de nevasca não por acaso, \nmas para encontrar a sala secreta e fingir que o caso foi resolvido por terceiros, limpando o nome dela para sempre. \nEla é a mente criminosa.")

suspeitos = [
    Suspeito(
        'Tricia',
        'Compradora da mansão, recém-casada com Ethan.',
        'Mulher civil, aparenta fragilidade, relata tonturas frequentes e pavor do isolamento.',
        'Ela diz ser apenas uma fã de arquitetura que encontrou a casa por um anúncio comum.',
        caso3
    ),
    Suspeito(
        'Ethan',
        'Marido de Tricia. Corretor de imóveis falido.',
        'Homem de negócios, deseja liquidar as finanças e demonstra tremores nas mãos e nervosismo.',
        'Afirma que trouxe a esposa para a mansão para iniciarem uma vida nova longe das dívidas.',
        caso3
    ),
    Suspeito(
        'Luke',
        'Ex-namorado e ex-paciente da Dra. Hale.',
        'Histórico clínico de comportamento explosivo, ciúme patológico e agressividade.',
        'Nenhum depoimento formal coletado em tempo real. Fugiu na noite do crime.',
        caso3
    )
]

caso3.set_culpado(suspeitos[0])

evidencias = [
    Evidencia(
        'Diário Digital de Tricia',
        'Este lugar me dá arrepios. Ethan insistiu para virmos ver a casa, mas sinto que a Dra. Hale ainda está aqui de alguma forma. Quero ir embora.',
        caso3
    ),
    Evidencia(
        'Gravação Oculta (Chave Gravador de Fita)',
        'Gravação secreta da Dra. Hale: A paciente "Tricia" na verdade se chama EJ. Ela era obcecada pela doutora e mostra traços psicopatas.',
        caso3
    ),
    Evidencia(
        'Mensagem Apagada (Celular de Tricia)',
        'Análise de metadados: "Ela finalmente parou de respirar. A casa é nossa." enviada na noite do crime.',
        caso3
    ),
    Evidencia(
        'Extrato Bancário de Ethan',
        'Ethan recebeu uma transferência massiva vinda diretamente da conta da Dra. Hale após o desaparecimento dela.',
        caso3
    ),
    Evidencia(
        'Histórico de Chamadas de Ethan',
        'O histórico de ligações mostra que Ethan ligou para Luke 15 vezes exatamente no dia do crime.',
        caso3
    ),
    Evidencia(
        'Rastreio do SIM Card de Luke',
        'O sinal do celular de Luke sumiu às 23h da noite do crime, logo após ele comprar uma passagem de fuga só de ida.',
        caso3
    ),
    Evidencia(
        'Última Fita Desbloqueada (Noite do Crime)',
        'Voz de Tricia (Fria, sem gaguejar): "Você achou que podia me tratar como uma paciente boba? Eu mudei meu cabelo por você. Eu peguei o Ethan por você. E agora, eu vou ter a sua vida... o Ethan vai me ajudar a esconder você, porque ele me ama." [Sons de luta corporal]',
        caso3
    ),
    Evidencia(
        'Fitas gravadas pela Dra. Hale',
        'Luke não aceita o fim. Ele se tornou violento. Ele me ameaçou, disse que se eu não fosse dele, não seria de mais ninguém. Temo pela minha vida.',
        caso3
    ),
    Evidencia(
        'Sessões de Pacientes Anônimos',
        'Dra. Hale diz no áudio: "EJ, você está obcecada por mim. Você está copiando meu cabelo, minhas roupas, e agora está perseguindo meu namorado, Luke. Você se aproximou de Ethan apenas porque ele era o corretor que cuidava das minhas propriedades. Isso precisa parar."',
        caso3
    ),
    Evidencia(
        'Atendente da Polícia (Ligação de Ethan)',
        'O homem parecia desesperado. Ele disse que tinha achado uma sala secreta e que a esposa dele não era quem ele pensava, mas a ligação foi cortada abruptamente.',
        caso3
    )
]