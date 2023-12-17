import random

def create_board():
    return [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]

def print_board(board):
    for layer in board:
        for row in layer:
            print(" | ".join([" " if cell is None else cell for cell in row]))
            print("-" * 31)
        print("\n" + "=" * 31)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(4):
        for j in range(4):
            if all(board[i][j][k] == player for k in range(4)):
                return True
            if all(board[i][k][j] == player for k in range(4)):
                return True
            if all(board[k][i][j] == player for k in range(4)):
                return True
        if all(board[i][k][k] == player for k in range(4)):
            return True
        if all(board[i][k][3 - k] == player for k in range(4)):
            return True
        if all(board[k][i][k] == player for k in range(4)):
            return True
        if all(board[k][i][3 - k] == player for k in range(4)):
            return True
    for j in range(4):
        for k in range(4):
            if all(board[k][i][j] == player for i in range(4)):
                return True
    for k in range(4):
        if all(board[k][i][i] == player for i in range(4)):
            return True
        if all(board[k][i][3 - i] == player for i in range(4)):
            return True
    return False

def is_full(board):
    return all(all(all(cell is not None for cell in row) for row in layer) for layer in board)

def get_empty_cells(board):
    return [(i, j, k) for i in range(4) for j in range(4) for k in range(4) if board[i][j][k] is None]

def evaluate(board):
    # Heuristic: Number of possible winning moves for X minus the number for O
    x_wins = sum(is_winner(board, 'X' * i) for i in range(2, 5))
    o_wins = sum(is_winner(board, 'O' * i) for i in range(2, 5))
    return x_wins - o_wins

def minimax(board, depth, maximizing_player):
    if depth == 0 or is_winner(board, 'X') or is_winner(board, 'O') or is_full(board):
        return evaluate(board)

    empty_cells = get_empty_cells(board)

    if maximizing_player:
        max_eval = float('-inf')
        for cell in empty_cells:
            i, j, k = cell
            board[i][j][k] = 'X'
            eval = minimax(board, depth - 1, False)
            board[i][j][k] = None
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            i, j, k = cell
            board[i][j][k] = 'O'
            eval = minimax(board, depth - 1, True)
            board[i][j][k] = None
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    empty_cells = get_empty_cells(board)
    best_move = None
    best_eval = float('-inf')

    for cell in empty_cells:
        i, j, k = cell
        board[i][j][k] = 'X'
        move_eval = minimax(board, 3, False)
        board[i][j][k] = None

        if move_eval > best_eval:
            best_eval = move_eval
            best_move = (i, j, k)

    return best_move

def main():
    board = create_board()
    print("Initial Board:")
    print_board(board)

    while not is_winner(board, 'X') and not is_winner(board, 'O') and not is_full(board):
        x_move = find_best_move(board)
        print(f"\nX's Move: {x_move}")
        board[x_move[0]][x_move[1]][x_move[2]] = 'X'
        print_board(board)

        if is_winner(board, 'X') or is_full(board):
            break

        o_move = random.choice(get_empty_cells(board))
        print(f"\nO's Move: {o_move}")
        board[o_move[0]][o_move[1]][o_move[2]] = 'O'
        print_board(board)

    if is_winner(board, 'X'):
        print("\nX wins!")
    elif is_winner(board, 'O'):
        print("\nO wins!")
    else:
        print("\n It's")

main()
find_best_move()