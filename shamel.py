import tkinter as tk
from tkinter import messagebox

class TicTacToe3D:
    def init(self):
        self.root = tk.Tk()
        self.root.title("3D Cubic Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]

        # Add "Start Game" and "Exit" buttons
        start_button = tk.Button(self.root, text="Start Game", font=('normal', 12),command=self.start_game)
        start_button.grid(row=0, column=5, padx=10, pady=10, sticky="nsew")

        exit_button = tk.Button(self.root, text="Exit", font=('normal', 12),command=self.root.destroy)
        exit_button.grid(row=1, column=5, padx=10, pady=10, sticky="nsew")

        # Create a larger grid for the 3D Tic Tac Toe
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    button = tk.Button(self.root, text="", font=('normal', 12), width=4, height=2,
                                       command=lambda l=layer, r=row, c=col: self.make_move(l, r, c))
                    button.grid(row=row, column=col + 1 + layer * 5, padx=5, pady=5, sticky="nsew")
                    self.board[layer][row][col] = button

        # Configure row and column weights to make the grid resizable
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def start_game(self):
        # Clear the board and start a new game
        self.current_player = 'X'
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.board[layer][row][col]['text'] = ""

    def make_move(self, layer, row, col):
        if not self.board[layer][row][col]['text']:
            self.board[layer][row][col]['text'] = self.current_player
            if self.check_win(layer, row, col):
                self.display_winner()
                self.start_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self, layer, row, col):
        # Check along the layer
        if self.check_line([self.board[layer][row][c]['text'] for c in range(4)]):
            return True

        # Check along the row
        if self.check_line([self.board[layer][r][col]['text'] for r in range(4)]):
            return True

        # Check along the column
        if self.check_line([self.board[l][row][col]['text'] for l in range(4)]):
            return True

        # Check diagonals
        if layer == row == col:
            if self.check_line([self.board[l][r][c]['text'] for l, r, c in zip(range(4), range(4), range(4))]):
                return True

        if layer == row == 3 - col:
            if self.check_line([self.board[l][r][c]['text'] for l, r, c in zip(range(4), range(4), range(3, -1, -1))]):
                return True

        if layer == 3 - row == col:
            if self.check_line([self.board[l][r][c]['text'] for l, r, c in zip(range(4), range(3, -1, -1), range(4))]):
                return True

        if layer == 3 - row == 3 - col:
            if self.check_line([self.board[l][r][c]['text'] for l, r, c in zip(range(4), range(3, -1, -1), range(3, -1, -1))]):
                return True

        # Check layers, rows, and columns
        if all(self.check_line([self.board[l][row][col]['text'] for l in range(4)]),
               self.check_line([self.board[layer][r][col]['text'] for r in range(4)]),
               self.check_line([self.board[layer][row][c]['text'] for c in range(4)])):
            return True

        return False

    def check_line(self, line):
        return len(set(line)) == 1 and line[0] is not None

    def display_winner(self):
        winner = f"Player {self.current_player} wins!"
        messagebox.showinfo("Game Over", winner)

if __name__ == "__main__":
    TicTacToe3D()
