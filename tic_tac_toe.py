import tkinter as tk
import math

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha - Agente Inteligente")
        
        # Representação do tabuleiro
        self.board = [""] * 9  
        self.current_player = "X"  # "X" é o jogador humano, "O" é o agente

        # Criação dos botões
        self.buttons = [
            tk.Button(self.window, text="", font=("Arial", 24), height=2, width=5,
                      command=lambda i=i: self.on_click(i)) for i in range(9)
        ]

        # Posicionamento dos botões no grid
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

        self.window.mainloop()

    def on_click(self, index):
        """Gerencia o clique do jogador humano."""
        if self.board[index] == "" and self.current_player == "X":
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner("X"):
                self.display_winner("Parabéns! Você venceu!")
                return
            if "" not in self.board:
                self.display_winner("Empate!")
                return
            self.current_player = "O"
            self.agent_move()

    def agent_move(self):
        """Decisão do agente usando MiniMax."""
        _, move = self.minimax(self.board, True)
        if move is not None:
            self.board[move] = "O"
            self.buttons[move].config(text="O")
            if self.check_winner("O"):
                self.display_winner("O agente venceu!")
                return
            if "" not in self.board:
                self.display_winner("Empate!")
                return
            self.current_player = "X"

    def minimax(self, board, is_maximizing):
        """Implementação do MiniMax."""
        if self.check_winner("X"):
            return -1, None
        if self.check_winner("O"):
            return 1, None
        if "" not in board:
            return 0, None

        if is_maximizing:
            best_score = -math.inf
            best_move = None
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score, _ = self.minimax(board, False)
                    board[i] = ""
                    if score > best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move
        else:
            best_score = math.inf
            best_move = None
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score, _ = self.minimax(board, True)
                    board[i] = ""
                    if score < best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move

    def check_winner(self, player):
        """Verifica se o jogador venceu."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]             # Diagonais
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def display_winner(self, message):
        """Exibe o vencedor e reseta o jogo."""
        winner_window = tk.Toplevel(self.window)
        winner_window.title("Resultado")
        tk.Label(winner_window, text=message, font=("Arial", 18)).pack(pady=10)
        tk.Button(winner_window, text="Jogar Novamente", command=lambda: self.reset_game(winner_window)).pack(pady=5)
        tk.Button(winner_window, text="Sair", command=self.window.quit).pack(pady=5)

    def reset_game(self, winner_window):
        """Reseta o tabuleiro para uma nova partida."""
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")
        winner_window.destroy()


# Iniciar o jogo
if __name__ == "__main__":
    TicTacToe()