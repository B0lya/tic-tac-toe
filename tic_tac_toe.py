print("Игра крестики-нолики для двух игроков")

board = [['-'] * 3 for _ in range(3)]

def create_board(board):
   print('  0 1 2')
   [['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']]
   for i in range(len(board)):
      print(str(i), *board[i])

def take_input(board, user):
    valid = False
    while not valid:
        x = input(f'Ходит {user}\n  Введите координату по вертикали: ')
        y = input('  Введите координату по диагонали: ')
        try:
            x = int(x)
            y = int(y)
        except:
            print('Некорректный ввод, обе координаты должны быть цыфрами от 0 до 2')
            continue
        if not (x >= 0 and x < 3 and y>=0 and y<3):
            print('Некорректный ввод, обе координаты должны быть цыфрами от 0 до 2')
            continue
        if board[x][y] != '-':
            print('Эта клеточка занята, выберите другую')
            continue
        break
    return x, y


def check_win(board, user):
    win_cord = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
                ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                ((0,2), (1,1), (2,0)), ((0,0), (1,1), (2,2)))
    for cord in win_cord:
        symbols=[]
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

def main(board):
    count=0
    while True:
        create_board(board)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = take_input(board,user)
            board[x][y] = user
        elif count == 9:
            print('Ничья')
            break
        if check_win(board, user):
            print(f"Выйграл {user}")
            create_board(board)
            break
        count += 1

main(board)