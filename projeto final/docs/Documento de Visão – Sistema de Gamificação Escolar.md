# Documento de Visão – RPG Escolar

*RPG educacional de terminal para o ensino de Programação Orientada a Objetos*

Projeto Final da disciplina de Programação Orientada a Objetos. Equipe: Aleff Lohan, Anny Beatriz, Elis Vitória e Keyty Winslet.

## 1. Nome do sistema

**Sistema de Gamificação Escolar**. O sistema reúne, em um único menu, três missões jogáveis: *O Armário Misterioso*, *A Vila dos Amaldiçoados* e *Os Jogos da Sobrevivência*.

## 2. Descrição do problema

Conceitos de Programação Orientada a Objetos, como classes, herança, encapsulamento, polimorfismo e tratamento de exceções, costumam ser apresentados de forma abstrata. Estudantes iniciantes memorizam definições, mas têm dificuldade em reconhecê-las em código real. Exercícios tradicionais de lista são pouco motivadores e dão retorno tardio, o que aumenta a desistência e a sensação de que a disciplina é difícil.

## 3. Justificativa

A gamificação transforma a prática em uma aventura com narrativa, desafios, recompensas e consequências. Ao errar uma charada ou perder uma vida, o estudante recebe retorno imediato e repete o conteúdo em contexto. Um jogo em Python executado no terminal exige apenas o interpretador, o que o torna acessível em qualquer computador de laboratório. Além disso, o próprio código do jogo (classes de personagens, missões, conquistas e recompensas) funciona como exemplo prático dos conceitos que ensina.

## 4. Objetivo geral

Desenvolver um RPG em modo texto, em Python, que reforce o aprendizado de Programação Orientada a Objetos por meio de missões narrativas com perguntas e desafios de código, progressão de personagem e salvamento de progresso.

### Objetivos específicos

- Apresentar conceitos de POO e de Python (herança, encapsulamento, métodos, try/except) em forma de charadas e desafios.
- Motivar o estudante com níveis, experiência, moedas, itens e conquistas.
- Permitir que o jogador retome a aventura de onde parou.
- Aplicar na própria implementação os conceitos da POO aprendidos até então.

## 5. Público-alvo

- **Principal:** estudantes iniciantes de disciplinas de Programação Orientada a Objetos, em cursos técnicos e de graduação da área de computação.
- **Secundário:** professores que queiram usar o jogo como atividade complementar ou de revisão.
- **Pré-requisitos do usuário:** noções básicas de lógica e de leitura de código Python; não é necessário conhecimento de jogos.

## 6. Funcionalidades

### 6.1 Menu principal

- Acesso às três missões, à consulta de progresso, aos créditos e à saída do jogo.
- Validação de opções inválidas e retorno seguro ao menu caso uma missão seja interrompida.

### 6.2 Missão 1 – O Armário Misterioso

- Exploração de três locais (Biblioteca, Sala de Matemática e Laboratório de Ciências), cada um com uma charada sobre POO ou Python.
- Cada acerto revela uma pista da senha do armário.
- Abertura do armário com a senha completa, que concede experiência e um item (a chave dourada antiga) para uso futuro.

### 6.3 Missão 2 – A Vila dos Amaldiçoados

- Narrativa sobre a vila de Eldoria, a maldição do feiticeiro Morvan e a busca pelo Cristal da Aurora.
- Três desafios de múltipla escolha (portão encantado, ponte das sombras e cristal da aurora) sobre objetos, tratamento de erro e encapsulamento.
- Sistema de três vidas: cada resposta errada tira uma vida, e o resultado final (vitória ou derrota) é gravado em arquivo.

### 6.4 Missão 3 – Os Jogos da Sobrevivência

- Criação de personagem com escolha de classe (Mago, Arqueiro ou Guerreiro), cada uma com atributos e habilidades próprios.
- Sequência de cinco desafios com combate por turnos contra inimigos de dificuldade crescente.
- Uso de ataque normal, ataque especial, habilidade de classe e poções de vida e de mana.
- Conversa com personagens, loja de suprimentos, conquistas e evolução de nível.
- Salvamento e carregamento do progresso em arquivo JSON.

### 6.5 Progresso e créditos

- Consulta rápida do personagem salvo e do resultado da missão de Eldoria.
- Tela de créditos com a equipe.

## 7. Escopo

### 7.1 Dentro do escopo

- Aplicação de linha de comando em Python, para um único jogador, executada localmente.
- As três missões descritas, com narrativa, perguntas e combate.
- Persistência local em arquivos (`progresso_rpg.json` e `resultado_eldoria.txt`).
- Modelagem em classes: personagem, classes de jogo, estudante, missão, recompensa e conquista.

### 7.2 Fora do escopo (nesta versão)

- Interface gráfica, som, imagens ou versão web.
- Ranking online.
- Cadastro de usuários, autenticação e integração com sistemas acadêmicos.
- Editor para adaptação de stats.
- Relatórios de desempenho dos estudantes.

### 7.3 Premissas e restrições

- Requer Python 3 instalado e execução pelo terminal na pasta do projeto.
- O progresso depende do diretório em que o programa é executado, pois os arquivos são lidos e gravados por nome relativo.
- Projeto acadêmico, com prazo e equipe de quatro integrantes.

## 8. Regras de negócio específicas

| Código | Regra |
| --- | --- |
| RN01 | O jogador deve escolher uma classe (Mago, Arqueiro ou Guerreiro) ao criar o personagem; cada classe tem pontos de vida, mana, dano e habilidade distintos. |
| RN02 | Na missão do armário, a senha só pode ser digitada depois que as três charadas forem resolvidas, e uma charada já resolvida não pode ser repetida. |
| RN03 | A senha correta do armário concede a experiência da missão e o item chave dourada antiga; a missão não pode ser concluída duas vezes. |
| RN04 | Na Vila dos Amaldiçoados, o jogador começa com três vidas, e cada resposta incorreta retira uma vida. |
| RN05 | Respostas fora das alternativas válidas (A, B ou C) não retiram vida. |
| RN06 | Ao chegar a zero vidas, a missão termina em derrota; ao concluir os três desafios com vidas restantes, termina em vitória. O resultado é gravado com nome do jogador, resultado e vidas restantes. |
| RN07 | Habilidades especiais consomem mana, e o jogador só pode usá-las se tiver mana suficiente. |
| RN08 | O Guerreiro reduz o dano recebido pelo valor de sua armadura, com dano mínimo de 1. |
| RN09 | A experiência obtida em missões e combates faz o personagem subir de nível, e missões podem exigir um nível mínimo para ficarem disponíveis. |
| RN10 | Vencer inimigos concede experiência e moedas, e as moedas podem ser gastas na loja em suprimentos como poções. |
| RN11 | Conquistas são desbloqueadas uma única vez por personagem, ao cumprir seu requisito. |
| RN12 | O jogador pode salvar e retomar o progresso da missão de sobrevivência; sem salvamento compatível, uma nova aventura é iniciada. |
| RN13 | Uma missão só passa de *Disponível* para *Em andamento* e depois *Concluída*, nessa ordem. |