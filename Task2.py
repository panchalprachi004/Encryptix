import math
HUMAN = 'O'
AI = 'X'
EMPTY = ' '
board = [EMPTY] * 9

def print_board(b):
    for i in range(3):
        print('|'.join(b[i*3:(i+1)*3]))
        if i < 2:
            print("-----")
def is_winner(b, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]            
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combinations)
def is_draw(b):
    return EMPTY not in b and not is_winner(b, HUMAN) and not is_winner(b, AI)
def get_available_moves(b):
    return [i for i in range(9) if b[i] == EMPTY]
def minimax(b, depth, is_maximizing):
    if is_winner(b, AI):
        return 1
    if is_winner(b, HUMAN):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(b):
            b[move] = AI
            score = minimax(b, depth + 1, False)
            b[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(b):
            b[move] = HUMAN
            score = minimax(b, depth + 1, True)
            b[move] = EMPTY
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = -1
    for i in get_available_moves(board):
        board[i] = AI
        score = minimax(board, 0, False)
        board[i] = EMPTY
        if score > best_score:
            best_score = score
            move = i
    board[move] = AI
    print(f"AI chooses position {move}")

def human_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] == EMPTY:
                board[move] = HUMAN
                break
            else:
                print("Cell already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number between 0 and 8.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are O, AI is X. Board positions are:")
    print("0|1|2\n3|4|5\n6|7|8")
    print()

    first = input("Do you want to go first? (y/n): ").lower() == 'y'

    while True:
        print_board(board)
        if is_winner(board, HUMAN):
            print("You win!")
            break
        elif is_winner(board, AI):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        if first:
            human_move()
            first = False
        else:
            ai_move()
            first = True

if __name__ == "__main__":
    main()
