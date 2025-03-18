# Description: A simple tic-tac-toe game in Python.
board = [" " for _ in range(9)]


def display_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_winner(player):
    win_conditions = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8], 
        [0, 4, 8],  
        [2, 4, 6],  
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def is_full():
    return " " not in board


def play_game():
    current_player = "X"
    game_over = False

    while not game_over:
        display_board()

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            display_board()
            print(f"🎉 Player {current_player} wins! 🎉")
            game_over = True
            break

        if is_full():
            display_board()
            print("It's a draw! 🤝")
            game_over = True
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
