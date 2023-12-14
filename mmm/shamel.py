import tkinter as tk
from tkinter import messagebox
import math
from itertools import permutations


class Board:
    players = ['x', 'O', '']

    def __init__(self):
        self.board = [[['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]]
        self.current_player = self.players[0]  # Set default player to 'x'
        self.AI_player = None

    def set_player(self, player):
        if player in self.players:
            self.current_player = player
        else:
            raise ValueError("Invalid player. Choose from:", self.players)

    def set_AI_player(self):
        if self.current_player == 'x':
            self.AI_player = 'O'
        elif self.current_player == 'O':
            self.AI_player = 'x'
        elif self.current_player == '':
            None
        else:
            raise ValueError("Invalid current player. Cannot determine AI player.")

    def set_value(self, layer, row, column):
        if self.board[layer][row][column] == '':
            self.board[layer][row][column] = self.current_player
        else:
            print("Cell already occupied.")

    def get_value(self, layer, row, column):
        return self.board[layer][row][column]

    def turn(self):
        # Switch the current player after each turn
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def is_win(self, player):
        # Check rows
        for layer in self.board:
            for row in layer:
                if all(cell == player for cell in row):
                    return True

        # Check columns
        for col in range(4):
            for layer in self.board:
                if all(row[col] == player for row in layer):
                    return True

        # Check diagonals within layers
        for layer in self.board:
            if all(layer[i][i] == player for i in range(4)) or all(layer[i][3 - i] == player for i in range(4)):
                return True

        # Check across layers
        for col in range(4):
            for row in range(4):
                if all(self.board[l][row][col] == player for l in range(4)):
                    return True

        # Check diagonals between layers
        if all(self.board[i][i][i] == player for i in range(4)) or all(self.board[i][i][3 - i] == player for i in range(4)):
            return True

        if all(self.board[i][3 - i][i] == player for i in range(4)) or all(self.board[i][3 - i][3 - i] == player for i in range(4)):
            return True

        return False

    def is_empty(self):
        # Check if the entire board is empty
        return all(self.board[layer][row][column] == '' for layer in range(4) for row in range(4) for column in range(4))

    def is_full(self):
        # Check if the entire board is full
        return all(self.board[layer][row][column] != '' for layer in range(4) for row in range(4) for column in range(4))

    def get_invalid_spaces(self):
        invalid_spaces = []
        for layer in range(4):
            for row in range(4):
                for column in range(4):
                    if self.board[layer][row][column] not in self.players:
                        invalid_spaces.append((layer, row, column))
        return invalid_spaces

    def reset_board(self):
        for layer in range(4):
            for row in range(4):
                for column in range(4):
                    self.board[layer][row][column] = ''

    def is_symmetric(self, player, layer, row, column):
        # Check symmetry across layers
        if [self.board[l][row][column] for l in range(4)] != [player] * 4:
            return False
        # Check symmetry across rows
        if [self.board[layer][r][column] for r in range(4)] != [player] * 4:
            return False

        # Check symmetry across columns
        if [self.board[layer][row][c] for c in range(4)] != [player] * 4:
            return False

        return True

    def symmetric_equivalent_boards(self):
        # Generate all symmetrically equivalent board states
        symmetrical_boards = []
        for perm in permutations(range(4)):
            for flip in [False, True]:
                new_board = self.board.copy()
                if flip:
                    new_board = [[[new_board[i][j][k] for k in range(4)] for j in range(4)] for i in perm]
                else:
                    new_board = [[[new_board[k][j][i] for k in range(4)] for j in range(4)] for i in perm]
                symmetrical_boards.append(new_board)
        return symmetrical_boards

    def heuristic_evaluation(self):
        # Replace this with your actual heuristic evaluation
        return 0


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("4x4x4 Tic Tac Toe")

        self.board = Board()
        self.create_widgets()
        self.set_players("x")
        self.update_status()

    def set_players(self, player):
        self.board.set_player(player)
        self.board.set_AI_player()

    def create_widgets(self):
        self.buttons = [[[tk.Button(self.master, text='', width=4, height=2, command=lambda layer=l, row=r, col=c: self.make_move(layer, row, col))
                        for c in range(4)] for r in range(4)] for l in range(4)]

        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].grid(row=row + layer * 4, column=col + layer * 4, padx=5, pady=0)

        self.status_label = tk.Label(self.master, text=f"Current Player: {self.board.current_player}")
        self.status_label.grid(row=16, columnspan=4)
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=17, columnspan=4)
        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.grid(row=18, columnspan=4)
        self.exit_button = tk.Button(self.master, text="Exit Game", command=self.master.destroy)
        self.exit_button.grid(row=19, columnspan=4)

    def reset_game(self):
        self.board.reset_board()
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].config(text='')
        self.update_status()

    def start_game(self):
        self.reset_game()
        self.set_players("x")
        self.update_status()

    def make_move(self, layer, row, col):
        if self.board.get_value(layer, row, col) == '':
            self.board.set_value(layer, row, col)
            self.buttons[layer][row][col].config(text=self.board.current_player)
            self.board.turn()
            self.update_status()

            if self.board.current_player == self.board.AI_player:
                # ****************
                # Add here your minimax algorithm with heuristic
                # Call self.board.set_value(layer, row, col) with the best move
                # ****************
                # self.board.turn()  (note remove "#" from this line)
                self.update_status()

            if self.board.is_win('x') or self.board.is_win('O'):  # Corrected 'O' to 'o'
                winner = 'Player X' if self.board.is_win('x') else 'Player O'
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.board.reset_board()

            if self.board.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.board.reset_board()

    def update_status(self):
        self.status_label.config(text=f"Current Player: {self.board.current_player}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
