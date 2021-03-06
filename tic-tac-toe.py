board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_board():
    for i in range(3):
        print()
        for j in range(3):
            print(board[i][j], end='')
            if j < 2:
                print('|', end='')
    print()

def take_input():
    pos = input("Enter a number : ")
    pos = int(pos) - 1
    return pos


def place_player(pos, player):
    row = pos // 3
    column = pos % 3
    board[row][column] = player
    return 1

def check_row(i):
    x = 0
    o = 0
    for j in range(3):
        if board[i][j] == 'X':
                x += 1

        if board[i][j] == 'O':
            o += 1
    if x == 3:
        print("X won")
        quit()

    elif o == 3:
        print("O won")
        quit()

def check_column(j):
    x = 0
    o = 0
    for i in range(3):

        if board[i][j] == 'X':
                x += 1

        if board[i][j] == 'O':
            o += 1

    if x == 3:
        print("X won")
        quit()

    elif o == 3:
        print("O won")
        quit()


def check_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return
            else:
                continue
    print("The game is tied!!")
    quit()
    if x == 3:
        print("X won")
        quit()

    elif o == 3:
        print("O won")
        quit()


def check_diagonals(a, b, c):
    var = [a, b, c]
    x = 0
    o = 0
    for i in var:
        if i == 'X':
            x += 1

        if i == 'O':
            o += 1

    if i == 3:
        print("X won")
        quit()

    elif i == 3:
        print("O won")
        quit()


def main():
    global game_on
    game_on = True
    count = 0
    while game_on:
        if count % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        print_board()
        pos = take_input()
        count += place_player(pos, player)
        check_tie()

        for j in range(3):
            check_column(j)
            check_row(j)
            check_diagonals(board[0][0], board[1][1], board[2][2])
            check_diagonals(board[0][2], board[1][1], board[2][0])


if __name__ == '__main__':
    main()
