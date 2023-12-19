from Board import Board
import tkinter as tk
from tkinter import messagebox
import time

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("4x4x4 Tic Tac Toe")
        self.master.configure(bg='misty rose')  # Set the background color for the entire program
        # Create the game board and place it in the center of the window
        self.board = Board()
        self.create_widgets()
        self.set_players("x")
        self.update_status()

    def set_players(self, player):
        self.player = self.board.set_player(player)
        self.Ai_player = self.board.set_AI_player()

    def create_widgets(self):
        self.buttons = [
            [
                [
                    tk.Button(
                        self.master, text='', width=4, height=2,
                        command=lambda layer=l, row=r, col=c: self.make_move(layer, row, col),
                        bg='coral'  # Set the background color for buttons to coral
                    )
                    for c in range(4)
                ]
                for r in range(4)
            ]
            for l in range(4)
        ]

        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].grid(row=row + layer * 4, column=col + layer * 4, padx=5, pady=0)

        self.status_label = tk.Label(self.master, text=f"Current Player: {self.board.current_player}", bg='misty rose')
        self.status_label.grid(row=16, columnspan=4)
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game, bg='light coral')
        self.reset_button.grid(row=17, columnspan=4)
        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game, bg='light coral')
        self.start_button.grid(row=18, columnspan=4)
        self.exit_button = tk.Button(self.master, text="Exit Game", command=self.master.destroy, bg='light coral')
        self.exit_button.grid(row=19, columnspan=4)

    def reset_game(self):
        self.board.reset_board()
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].config(text='', bg='coral')  # Reset text and color
        self.set_players("x")
        self.update_status()

    def start_game(self):
        self.reset_game()
        self.set_players("x")
        self.update_status()

    def make_move(self, layer, row, col):
        if self.board.get_value(layer, row, col) == '':
            if self.board.current_player == self.board.current_player:
                self.board.set_value(layer, row, col)
                self.buttons[layer][row][col].config(text=self.board.current_player, bg='light coral')  # Set text and color
                self.board.turn()
                self.update_status()

            if not self.board.is_full() and self.board.current_player == self.Ai_player:
                # ****************
                # add here your best_move return and pass it to self.board.set_value(layer, row, col)
                # ****************
                    if self.board.current_player == self.board.AI_player:
                        best_move = self.get_best_move()
                        if best_move:
                            layer, row, col = best_move
                            self.board.set_value(layer, row, col)
                            self.buttons[layer][row][col].config(text=self.board.AI_player)
                            self.board.turn()
                            self.update_status()

            if self.board.is_win('x') or self.board.is_win('o'):  # Corrected 'O' to 'o
                winner = 'Player X' if self.board.is_win('x') else 'Player O'
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()

            if self.board.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.board.reset_board()

    def update_status(self):
        self.status_label.config(text=f"Current Player: {self.board.current_player}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
