# Tic-Tac-Toe AI 🎮🤖  

Este é um projeto de agente inteligente para o clássico jogo da velha, implementado em Python. O agente utiliza o algoritmo **MiniMax** para prever os movimentos do jogador humano e tomar decisões estratégicas, garantindo sempre o melhor resultado possível.

## 📝 Descrição do Projeto

O objetivo principal do agente é:
- **Analisar o ambiente** (o estado atual do tabuleiro).
- **Tomar decisões autônomas** para maximizar suas chances de vitória ou, no pior caso, garantir um empate.
- Fornecer uma interface gráfica interativa para o jogo.

Este projeto busca criar um agente inteligente para o jogo da velha (Tic-Tac-Toe). O objetivo principal do agente é analisar o estado atual do tabuleiro e tomar decisões autônomas para maximizar suas chances de vitória ou, no pior caso, garantir um empate.

Como o Agente Funciona:
Sensores:

O agente monitora o estado do tabuleiro a cada jogada do jogador humano.
Ele verifica as células preenchidas (marcadas com "X" ou "O") para tomar decisões.
O agente também avalia o tabuleiro para detectar se o jogador humano está prestes a ganhar ou se ele próprio pode vencer.
Atuadores:

O atuador do agente é a colocação do símbolo "O" em uma célula do tabuleiro após a avaliação das jogadas possíveis.
O agente realiza sua jogada com base na avaliação feita pelo algoritmo Hill Climbing, atualizando o tabuleiro em tempo real.
Base de Conhecimento:

A base de conhecimento do agente é construída pelas regras do jogo e pela função heurística usada no algoritmo Hill Climbing.
O Hill Climbing é uma técnica de otimização local que permite ao agente tomar decisões com base em movimentos que proporcionam a maior melhoria no estado atual do jogo.
Método de Tomada de Decisão (Hill Climbing):

O agente utiliza o algoritmo Hill Climbing para avaliar todas as possíveis jogadas no tabuleiro.
Em vez de explorar todas as possibilidades como o MiniMax, o Hill Climbing foca em melhorar iterativamente o estado atual, movendo-se para o próximo estado com a maior "pontuação" de vitória.
A cada jogada, o agente escolhe a ação que leva ao melhor resultado imediato (geralmente o que maximiza suas chances de vitória ou bloqueia o oponente).
Interface Gráfica:

A interface gráfica foi desenvolvida com a biblioteca tkinter, proporcionando uma experiência visual simples e intuitiva para o usuário.
O tabuleiro é exibido como uma matriz 3x3, onde cada célula é um botão que pode ser clicado pelo jogador.
Objetivos do Agente:
Maximizar as chances de vitória do agente: O agente tenta sempre ganhar, utilizando o Hill Climbing para prever e reagir às jogadas do jogador.
Evitar a derrota: Caso não seja possível ganhar, o agente faz o possível para empatar o jogo, evitando a perda.
Jogo balanceado: O agente foi projetado para ser desafiador, mas não invencível, garantindo uma experiência divertida para o jogador humano.

---

## 🎯 Funcionalidades

- Jogo interativo em uma interface gráfica.
- Agente inteligente utilizando o algoritmo Hill Climbing para previsão e tomada de decisões estratégicas.
- Garantia de que o agente nunca perde.
- Cenários de vitória, empate ou derrota simulados.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Bibliotecas:** 
  - `tkinter` (interface gráfica padrão do Python)
  - Nenhuma instalação adicional é necessária.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado. 
  - [Download Python](https://www.python.org/downloads/)

### Passos para Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   
2. Execute o script principal:
   ```bash
   python tic_tac_toe.py
