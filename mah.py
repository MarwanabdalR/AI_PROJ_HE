import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("4x4x4 Tic Tac Toe")

        self.current_player = "X"
        self.board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]

        self.buttons = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    self.buttons[i][j][k] = tk.Button(
                        master,
                        text="",
                        font=("Helvetica", 14),
                        width=4,
                        height=2,
                        command=lambda i=i, j=j, k=k: self.click(i, j, k),
                    )
                    self.buttons[i][j][k].grid(row=i, column=j * 4 + k)

    def click(self, i, j, k):
        if not self.is_valid_move(i, j, k) or self.is_winner():
            return

        self.board[i][j][k] = self.current_player
        self.buttons[i][j][k].config(text=self.current_player)
        self.check_winner()
        self.switch_player()

        if self.current_player == "O" and not self.is_winner():
            self.computer_move()

    def is_valid_move(self, i, j, k):
        return self.board[i][j][k] is None

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def is_winner(self):
        for i in range(4):
            if self.check_2d_winner(self.board[i]) or \
               self.check_2d_winner([row[i] for row in self.board]) or \
               self.check_2d_winner([[self.board[j][k][i] for k in range(4)] for j in range(4)]):
                return True

        return False

    def check_2d_winner(self, board):
        for row in board:
            if all(cell == "X" for cell in row) or all(cell == "O" for cell in row):
                return True

        for col in zip(*board):
            if all(cell == "X" for cell in col) or all(cell == "O" for cell in col):
                return True

        if all(board[i][i] == "X" for i in range(4)) or all(board[i][i] == "O" for i in range(4)) or \
           all(board[i][3 - i] == "X" for i in range(4)) or all(board[i][3 - i] == "O" for i in range(4)):
            return True

        return False

    def check_winner(self):
        if self.is_winner():
            winner = "X" if self.current_player == "O" else "O"
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()

    def reset_game(self):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    self.board[i][j][k] = None
                    self.buttons[i][j][k].config(text="")

    def computer_move(self):
        best_score = float("-inf")
        best_move = None

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if self.is_valid_move(i, j, k):
                        self.board[i][j][k] = "O"
                        score = self.minimax(0, False)
                        self.board[i][j][k] = None

                        if score > best_score:
                            best_score = score
                            best_move = (i, j, k)

        if best_move:
            self.board[best_move[0]][best_move[1]][best_move[2]] = "O"
            self.buttons[best_move[0]][best_move[1]][best_move[2]].config(text="O")
            self.check_winner()
            self.switch_player()

    def minimax(self, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "tie": 0}

        result = self.evaluate()
        if result in scores:
            return scores[result]

        if is_maximizing:
            best_score = float("-inf")
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if self.is_valid_move(i, j, k):
                            self.board[i][j][k] = "O"
                            score = self.minimax(depth + 1, False)
                            self.board[i][j][k] = None
                            best_score = max(score, best_score)
            return best_score

        else:
            best_score = float("inf")
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if self.is_valid_move(i, j, k):
                            self.board[i][j][k] = "X"
                            score = self.minimax(depth + 1, True)
                            self.board[i][j][k] = None
                            best_score = min(score, best_score)
            return best_score

    def evaluate(self):
        if self.is_winner():
            return "X" if self.current_player == "O" else "O"
        elif all(self.board[i][j][k] is not None for i in range(4) for j in range(4) for k in range(4)):
            return "tie"
        else:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
