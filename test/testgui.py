import tkinter as tk
from tkinter import messagebox


import random

def ai_move():
    global turn, cells, game_over

    if not game_over:
        # Find a winning move for the AI
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if cells[i * BOARD_SIZE + j]["text"] == EMPTY_CELL:
                    cells[i * BOARD_SIZE + j]["text"] = PLAYER_O
                    if check_winner() == PLAYER_O:
                        turn = PLAYER_X
                        return

                    # Undo the move to check for opponent's winning move
                    cells[i * BOARD_SIZE + j]["text"] = EMPTY_CELL

        # Find a move to block opponent's winning move
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if cells[i * BOARD_SIZE + j]["text"] == EMPTY_CELL:
                    cells[i * BOARD_SIZE + j]["text"] = PLAYER_X
                    if check_winner() == PLAYER_X:
                        cells[i * BOARD_SIZE + j]["text"] = EMPTY_CELL
                        cells[i * BOARD_SIZE + j]["text"] = PLAYER_O
                        turn = PLAYER_X
                        return
                    cells[i * BOARD_SIZE + j]["text"] = EMPTY_CELL

        # Make a random move if no winning or blocking move found
        while True:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if cells[row * BOARD_SIZE + col]["text"] == EMPTY_CELL:
                cells[row * BOARD_SIZE + col]["text"] = PLAYER_O
                turn = PLAYER_X
                break



# Game constants
BOARD_SIZE = 16
EMPTY_CELL = ""
PLAYER_X = "X"
PLAYER_O = "O"

# Global variables
turn = PLAYER_X
cells = []
game_over = False

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe 4x4")

# Create the game board
board_frame = tk.Frame(window)
board_frame.pack()

for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        cell = tk.Button(board_frame, text=EMPTY_CELL, font=("Helvetica", 10), width=5, height=2)
        cell.grid(row=i, column=j)
        cell["command"] = lambda row=i, col=j: click_cell(row, col)
        cells.append(cell)



# Function to handle click on a cell
def click_cell(row, col):
    global turn, game_over

    if not game_over and cells[row * BOARD_SIZE + col]["text"] == EMPTY_CELL:
        cells[row * BOARD_SIZE + col]["text"] = turn
        turn = PLAYER_O if turn == PLAYER_X else PLAYER_X

        # Check for winner
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            game_over = True

        if not game_over and turn == PLAYER_O:
            # Make AI move after player's click
            ai_move()

        # Check for tie
        if not game_over and all(cell["text"] != EMPTY_CELL for cell in cells):
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True


# Function to check for winner
def check_winner():
    # Check rows and columns
    for i in range(BOARD_SIZE):
        row = [cells[i * BOARD_SIZE + j]["text"] for j in range(BOARD_SIZE)]
        column = [cells[j * BOARD_SIZE + i]["text"] for j in range(BOARD_SIZE)]
        if row.count(PLAYER_X) == BOARD_SIZE or column.count(PLAYER_X) == BOARD_SIZE:
            return PLAYER_X
        if row.count(PLAYER_O) == BOARD_SIZE or column.count(PLAYER_O) == BOARD_SIZE:
            return PLAYER_O

    # Check diagonals
    diagonal1 = [cells[i * BOARD_SIZE + i]["text"] for i in range(BOARD_SIZE)]
    diagonal2 = [cells[i * BOARD_SIZE + BOARD_SIZE - 1 - i]["text"] for i in range(BOARD_SIZE)]
    if diagonal1.count(PLAYER_X) == BOARD_SIZE or diagonal2.count(PLAYER_X) == BOARD_SIZE:
        return PLAYER_X
    if diagonal1.count(PLAYER_O) == BOARD_SIZE or diagonal2.count(PLAYER_O) == BOARD_SIZE:
        return PLAYER_O

    return None


# Start the game
window.mainloop()
