"""Create 4x4x4 3d tic tac toe player vs computer"""
import numpy as np
import pandas as pd
import random as rnd

def draw_board(board):
    """This function print's the game board as panda data frames"""
    frame1 = pd.DataFrame(board[0])
    frame2 = pd.DataFrame(board[1])
    frame3 = pd.DataFrame(board[2])
    frame4 = pd.DataFrame(board[3])

    frame1.index = ['A', 'B', 'C', 'D']
    frame2.index = ['E', 'F', 'G', 'H']
    frame3.index = ['I', 'J', 'K', 'L']
    frame4.index = ['M', 'N', 'O', 'P']

    print(frame1)
    print(frame2)
    print(frame3)
    print(frame4)

def swap_player_turn(player_turn):
    if player_turn == 'X':
        return 'O'
    elif player_turn == 'O':
        return 'X'

def input_player_move(board, player_turn):
    move = input('Enter a move: ')

    if move[0] == 'A':
        b = 0
        r = 0
    elif move[0] == 'B':
        b = 0
        r = 1
    elif move[0] == 'C':
        b = 0
        r = 2
    elif move[0] == 'D':
        b = 0
        r = 3
    elif move[0] == 'E':
        b = 1
        r = 0
    elif move[0] == 'F':
        b = 1
        r = 1
    elif move[0] == 'G':
        b = 1
        r = 2
    elif move[0] == 'H':
        b = 1
        r = 3
    elif move[0] == 'I':
        b = 2
        r = 0
    elif move[0] == 'J':
        b = 2
        r = 1
    elif move[0] == 'K':
        b = 2
        r = 2
    elif move[0] == 'L':
        b = 2
        r = 3
    elif move[0] == 'M':
        b = 3
        r = 0
    elif move[0] == 'N':
        b = 3
        r = 1
    elif move[0] == 'O':
        b = 3
        r = 2
    elif move[0] == 'P':
        b = 3
        r = 3
    
    c = int(move[1])

    board[b, r, c] = player_turn

def create_goals(board):
    """This function returns a random goal for the ai"""
    list_of_goals = []

    # Create all possible horizontal lines on each board
    for b_num, b in enumerate(board):
        for r_num, r in enumerate(b):
            row = []
            for c_num, c in enumerate(r):
                row.append((b_num, r_num, c_num))
            list_of_goals.append(row)
    # Create all possible vertical lines on each board
    for b_num, b in enumerate(board):
        for c in range(4):
            column = []
            for r in range(4):
                column.append((b_num, r, c))
            list_of_goals.append(column)
    # Create all possible diaganol lines on each board
    for b in range(4):
        diag = []
        for r, c, in zip(range(4), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    for b in range(4):
        diag = []
        for r, c, in zip(range(3, -1, -1), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    # Create all possible lines through baord
    for r in range(4):
        for c in range(4):
            line = []
            for b in range(4):
                line.append((b, r, c))
            list_of_goals.append(line)
    # Create vertical through board diaganols
    for c in range(4):
        diag = []
        for r, b, in zip(range(4), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    for c in range(4):
        diag = []
        for r, b, in zip(range(3, -1, -1), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    # Create horizontal through board diaganols
    for r in range(4):
        diag = []
        for c, b in zip(range(4), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    for r in range(4):
        diag = []
        for c, b in zip(range(3, -1, -1), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    # Create corner to corner through board diaganols:
    diag = []
    for b, r, c in zip(range(4), range(4), range(4)):
        diag.append((b, r, c))
    list_of_goals.append(diag)
    diag = []
    for b, r, c in zip(range(4), range(4), range(3, -1, -1)):
        diag.append((b, r, c))
    list_of_goals.append(diag)
    diag = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(4)):
        diag.append((b, r, c))
    list_of_goals.append(diag)
    diag = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(3, -1, -1)):
        diag.append((b, r, c))
    list_of_goals.append(diag)

    return list_of_goals
def choose_random_goal(list_of_goals):
    """Return a random goal, and delete the goal from list of goals"""
    num = rnd.randrange(0, len(list_of_goals))
    goal = list_of_goals[num]
    list_of_goals.pop(num)
    return goal
def check_if_goal_valid(goal, board):
    for b, r, c in goal:
        if board[b, r, c] != ' ':
            return False
    return True


def check_for_wins(board):
    """This function returns an 'X' if X has won or an 'O' if O has won."""
    # Check Rows On each board:
    for b in board:
        for row in b:
            countO = 0
            countX = 0
            for column in row:
                if column == 'X':
                    countX += 1
                elif column == 'O':
                    countO += 1
            if countO == 4:
                return 'O'
            if countX == 4:
                return 'X'
    # Check Columns on each board:
    for b in board:
        for row in b.T:
            countX = 0
            countO = 0
            for column in row:
                if column == 'X':
                    countX += 1
                elif column == 'O':
                    countO += 1
            if countX == 4:
                return 'X'
            elif countO == 4:
                return 'O'
    # Check for diaganols on each board:
    for b in board:
        countX = 0
        countO = 0
        for i in range(4):
            if b[i, i] == 'X':
                countX += 1
            elif b[i, i] == 'O':
                countO += 1  
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
        
        countX = 0
        countO = 0
        for x, y in zip(range(3, -1, -1), range(4)):
            if b[x, y] == 'X':
                countX += 1
            elif b[x, y] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    # Check for line through board (3d row or column):
    for x in range(4):
        for y in range(4):
            countX = 0
            countO = 0
            for b in board:
                if b[x, y] == 'X':
                    countX += 1
                elif b[x, y] == 'O':
                    countO += 1
            if countX == 4:
                return 'X'
            elif countO == 4:
                return 'O'
    # Check for vertical through board daiaganols:
    for c in range(4):
        countO = 0
        countX = 0
        for r, b in zip(range(4), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    for c in range(4):
        countO = 0
        countX = 0
        for r, b in zip(range(3, -1, -1), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    # Check for horizontal through board diaganols:
    for r in range(4):
        countX = 0
        countO = 0
        for c, b in zip(range(4), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    for r in range(4):
        countX = 0
        countO = 0
        for c, b in zip(range(3, -1, -1), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    # Check for corner to corner diaganols
    countX = 0
    countO = 0
    for r, c, b in zip(range(4), range(4), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    countX = 0
    countO = 0
    for r, c, b in zip(range(4), range(3, -1, -1), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    countX = 0
    countO = 0
    for r, c, b in zip(range(3, -1, -1), range(4), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    countX = 0
    countO = 0
    for r, c, b in zip(range(3, -1, -1), range(3, -1, -1), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    
    return 'None'

def ai_move(board, goal, player_turn):
    """This function determines how to move for the AI"""
    if check_if_ai_could_win(board, player_turn) == False:
        if check_if_player_could_win(board, player_turn) == False:
            follow_goal(board, goal, player_turn)
def check_if_ai_could_win(board, player_turn):
    # Check rows
    for b in range(4):
        for r in range(4):
            count = 0
            blank_spaces = []
            for c in range(4):
                if board[b, r, c] == player_turn:
                    count += 1
                elif board[b, r, c] == ' ':
                    blank_spaces.append((b, r, c))
            if count == 3 and len(blank_spaces) == 1:
                b, r, c = blank_spaces[0]
                board[b, r, c] = player_turn
                return True
    # Check columns
    for b in range(4):
        for c in range(4):
            count = 0
            blank_spaces = []
            for r in range(4):
                if board[b, r, c] == player_turn:
                    count += 1
                elif board[b, r, c] == ' ':
                    blank_spaces.append((b, r, c))
            if count == 3 and len(blank_spaces) == 1:
                b, r, c = blank_spaces[0]
                board[b, r, c] = player_turn
                return True
    # Check Diaganols
    for b in range(4):
        count = 0
        blank_spaces = []
        for r, c in zip(range(4), range(4)):
            if board[b, r, c] == player_turn:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    for b in range(4):
        count = 0
        blank_spaces = []
        for r, c in zip(range(4), range(3, -1, -1)):
            if board[b, r, c] == player_turn:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    # Check line through board
    for r in range(4):
        for c in range(4):
            count = 0
            blank_spaces = []
            for b in range(4):
                if board[b, r, c] == player_turn:
                    count += 1
                elif board[b, r, c] == ' ':
                    blank_spaces.append((b, r, c))
            if count == 3 and len(blank_spaces) == 1:
                b, r, c = blank_spaces[0]
                board[b, r, c] = player_turn
                return True
    # Check vertical 3d diag
    for c in range(4):
        count = 0
        blank_spaces = []
        for b, r in zip(range(4), range(4)):
            if board[b, r, c] == player_turn:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    for c in range(4):
        count = 0
        blank_spaces = []
        for b, r in zip(range(4), range(3, -1, -1)):
            if board[b, r, c] == player_turn:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    # Check horizontal 3d diag
    for r in range(4):
        count = 0
        blank_spaces = []
        for b, c in zip(range(4), range(4)):
            if board[b, r, c] == player_turn:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    for r in range(4):
        count = 0
        blank_spaces = []
        for b, c in zip(range(4), range(3, -1, -1)):
            if board[b, r, c] == player_turn:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    # Check corner to corner diags
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(4), range(4)):
        if board[b, r, c] == player_turn:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(4), range(3, -1, -1)):
        if board[b, r, c] == player_turn:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(3, -1, -1)):
        if board[b, r, c] == player_turn:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(4)):
        if board[b, r, c] == player_turn:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    
    return False
def check_if_player_could_win(board, player_turn):
    opponent = swap_player_turn(player_turn)

    # Check rows
    for b in range(4):
        for r in range(4):
            count = 0
            blank_spaces = []
            for c in range(4):
                if board[b, r, c] == opponent:
                    count += 1
                elif board[b, r, c] == ' ':
                    blank_spaces.append((b, r, c))
            if count == 3 and len(blank_spaces) == 1:
                b, r, c = blank_spaces[0]
                board[b, r, c] = player_turn
                return True
    # Check columns
    for b in range(4):
        for c in range(4):
            count = 0
            blank_spaces = []
            for r in range(4):
                if board[b, r, c] == opponent:
                    count += 1
                elif board[b, r, c] == ' ':
                    blank_spaces.append((b, r, c))
            if count == 3 and len(blank_spaces) == 1:
                b, r, c = blank_spaces[0]
                board[b, r, c] = player_turn
                return True
    # Check Diaganols
    for b in range(4):
        count = 0
        blank_spaces = []
        for r, c in zip(range(4), range(4)):
            if board[b, r, c] == opponent:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    for b in range(4):
        count = 0
        blank_spaces = []
        for r, c in zip(range(4), range(3, -1, -1)):
            if board[b, r, c] == opponent:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    # Check line through board
    for r in range(4):
        for c in range(4):
            count = 0
            blank_spaces = []
            for b in range(4):
                if board[b, r, c] == opponent:
                    count += 1
                elif board[b, r, c] == ' ':
                    blank_spaces.append((b, r, c))
            if count == 3 and len(blank_spaces) == 1:
                b, r, c = blank_spaces[0]
                board[b, r, c] = player_turn
                return True
    # Check vertical 3d diag
    for c in range(4):
        count = 0
        blank_spaces = []
        for b, r in zip(range(4), range(4)):
            if board[b, r, c] == opponent:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    for c in range(4):
        count = 0
        blank_spaces = []
        for b, r in zip(range(4), range(3, -1, -1)):
            if board[b, r, c] == opponent:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    # Check horizontal 3d diag
    for r in range(4):
        count = 0
        blank_spaces = []
        for b, c in zip(range(4), range(4)):
            if board[b, r, c] == opponent:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    for r in range(4):
        count = 0
        blank_spaces = []
        for b, c in zip(range(4), range(3, -1, -1)):
            if board[b, r, c] == opponent:
                count += 1
            elif board[b, r, c] == ' ':
                blank_spaces.append((b, r, c))
        if count == 3 and len(blank_spaces) == 1:
            b, r, c = blank_spaces[0]
            board[b, r, c] = player_turn
            return True
    # Check corner to corner diags
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(4), range(4)):
        if board[b, r, c] == opponent:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(4), range(3, -1, -1)):
        if board[b, r, c] == opponent:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(3, -1, -1)):
        if board[b, r, c] == opponent:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    count = 0
    blank_spaces = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(4)):
        if board[b, r, c] == opponent:
            count += 1
        elif board[b, r, c] == ' ':
            blank_spaces.append((b, r, c))
    if count == 3 and len(blank_spaces) == 1:
        b, r, c = blank_spaces[0]
        board[b, r, c] = player_turn
        return True
    
    return False

                
                

def follow_goal(board, goal, player_turn):
    """This function follows the AI's preset goal."""
    b, r, c = goal[0]
    board[b, r, c] = player_turn
    goal.pop(0)

def play_tic_tac_toe():
    # Set up a blank board
    board = np.full((4, 4, 4), ' ')

    # Set current turn to X and turn_count to 0
    player_turn = 'X'
    turn_count = 0

    # Ask user if they want to go first
    player_first = input('Do you want to go first (Y/N): ')
    while player_first not in 'YN':
        print('Invalid response.')
        player_first = input('Do you want to go first (Y/N): ')
    
    # Create master list of goals, and pick random goal for AI
    list_of_goals = create_goals(board)
    goal = choose_random_goal(list_of_goals)
    
    # Draw biard
    draw_board(board)
    
    if player_first == 'Y':
        input_player_move(board, player_turn)
        player_turn = swap_player_turn(player_turn)
        turn_count += 1
        while check_if_goal_valid(goal, board) == False:
            goal = choose_random_goal(list_of_goals)
    else:
        ai_move(board, goal, player_turn)
        player_turn = swap_player_turn(player_turn)
        turn_count += 1


    while check_for_wins(board) == 'None':
        draw_board(board)

        if player_first == 'Y' and turn_count % 2 == 0 or player_first == 'N' and turn_count % 2 != 0:
            input_player_move(board, player_turn)
            player_turn = swap_player_turn(player_turn)
            turn_count += 1
            while check_if_goal_valid(goal, board) == False:
                goal = choose_random_goal(list_of_goals)
        else:
            ai_move(board, goal, player_turn)
            player_turn = swap_player_turn(player_turn)
            turn_count += 1
    

    draw_board(board)
    print(f'The winner is {check_for_wins(board)}')
    
play_tic_tac_toe()