def game_board():
    spaces = [['_', '_', '_'] for x in range(3)]
    return spaces


def print_board(board_to_print):
    for space in board_to_print:
        print(' '.join(space))


def place_piece(turn, board, x, y):
    if turn % 2 == 0:
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'
    return board


def keyboard_config(input):
    if input == 7:
        return 0, 0
    elif input == 8:
        return 0, 1
    elif input == 9:
        return 0, 2

    elif input == 4:
        return 1, 0
    elif input == 5:
        return 1, 1
    elif input == 6:
        return 1, 2

    elif input == 1:
        return 2, 0
    elif input == 2:
        return 2, 1
    elif input == 3:
        return 2, 2

    else:
        print("Invalid selection, please try again")


def find_winner(board):

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == 'X':
        return True
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == 'O':
        return True

    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == 'X':
        return True
    if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == 'O':
        return True

    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == 'X':
        return True
    if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == 'O':
        return True

    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == 'X':
        return True
    if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == 'O':
        return True

    if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == 'X':
        return True
    if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == 'O':
        return True

    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == 'X':
        return True
    if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == 'O':
        return True

    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == 'X':
        return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == 'O':
        return True

    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == 'X':
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == 'O':
        return True
    else:
        return False


def check_for_tie(tie_game):
    if tie_game == 8:
        return True


def player(turn):
    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    return player


def get_location(turn):
    while True:
        try:
            location = int(input(
                f'Player "{player(turn)}"s turn.  Use numeric keypad to select where your piece goes 1 - 9: '))
            return location
        except:
            print("That's not a valid option!")


def check_place(board, x, y):
    if board[x][y] == '_':
        return True
    else:
        print("That position is already taken!")
        return False


def main():
    tie_game = 0
    turn = 2
    player(turn)
    board = game_board()
    print_board(board)
    while True:
        location = get_location(turn)
        x, y = keyboard_config(location)
        while check_place(board, x, y) == False:
            location = get_location(turn)
            x, y = keyboard_config(location)

        place_piece(turn, board, x, y)

        print_board(board)
        if find_winner(board) == True:
            print(f'Congratulations "{player(turn)}"!, You Won!')
            break

        if check_for_tie(tie_game):
            print('Tie Game!  You both Lose!')
            break

        turn += 1
        tie_game += 1


if __name__ == '__main__':
    main()
