#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col] and
                board[0][col] != " "):
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board):
        print_board(board)

        while True:
            try:
                row_input = (input
                             (f"Enter row (0, 1, or 2) for player{player}: ")
                             .strip())
                col_input = input(
                    f"Enter column (0, 1, or 2) for player {player}: ").strip()

                if not row_input or not col_input:
                    print(
                        "Input cannot be empty. Please enter a valid number."
                    )
                    continue

                row = int(row_input)
                col = int(col_input)

                if row not in range(3) or col not in range(3):
                    print(
                        "Invalid coordinates! Please enter row and column "
                        "between 0 and 2."
                    )
                    continue

                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue

                board[row][col] = player
                break

            except ValueError:
                print("Invalid input! Please enter valid integers only.")

        player = "O" if player == "X" else "X"

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

    print_board(board)
    print(f"Player {player} wins!")


if __name__ == "__main__":
    tic_tac_toe()
