import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Home")

        self.level_var = tk.StringVar()
        self.level_var.set("Easy")

        self.level_label = tk.Label(root, text="Select Level:")
        self.level_label.pack(pady=10)

        self.level_menu = tk.OptionMenu(root, self.level_var, "Easy", "Medium", "Hard")
        self.level_menu.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        level = self.level_var.get()
        game_window = tk.Toplevel(self.root)
        game_window.title(f"Tic Tac Toe - 4x4 - {level}")

        self.game_instance = TicTacToeGame(game_window, level)

class TicTacToeGame:
    def _init_(self, root, level):
        self.root = root
        self.level = level

        self.current_player = 'X'
        self.board = [[' ' for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                button = tk.Button(root, text='', width=8, height=4,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)

        if self.level != "Human":
            self.play_computer_move()

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button_text(row, col)

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

            if self.level != "Human":
                self.play_computer_move()

    def update_button_text(self, row, col):
        button = self.root.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][c] == self.current_player for c in range(4)):
            return True

        # Check column
        if all(self.board[r][col] == self.current_player for r in range(4)):
            return True

        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(4)) or \
           all(self.board[i][3 - i] == self.current_player for i in range(4)):
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(4) for j in range(4))

    def reset_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                button = self.root.grid_slaves(row=i, column=j)[0]
                button.config(text='')

    def play_computer_move(self):
        if self.level == "Easy":
            self.play_random_move()
        elif self.level == "Medium":
            # Implement medium-level AI (random move for now)
            self.play_random_move()
        elif self.level == "Hard":
            # Implement hard-level AI (random move for now)
            self.play_random_move()

    def play_random_move(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.on_button_click(row, col)

if __name__ == "__main__":
    root = tk.Tk()
    home_screen = TicTacToe(root)
    root.mainloop()