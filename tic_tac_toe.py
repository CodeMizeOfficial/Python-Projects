#  Variables
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
players = ['X', 'O']

#  Colours
Red = '\033[0;31;49m'
ClrX = '\033[0;33;49m'
ClrO = '\033[0;34;49m'
Normal = '\033[0;0;0m'

#  Functions
def Board(board, Red = Red, ClrX = ClrX, ClrO = ClrO, Normal = Normal):
    colourPrint = []
    for piece in board:
        if piece == 'X': colourPrint.append(ClrX)
        elif piece == 'O': colourPrint.append(ClrO)
        else: colourPrint.append('')
    print(f'''  {Red}+---+---+---+
    | {colourPrint[0]}{board[0]}{Red} | {colourPrint[1]}{board[1]}{Red} | {colourPrint[2]}{board[2]}{Red} |
    +---+---+---+
    | {colourPrint[3]}{board[3]}{Red} | {colourPrint[4]}{board[4]}{Red} | {colourPrint[5]}{board[5]}{Red} |
    +---+---+---+
    | {colourPrint[6]}{board[6]}{Red} | {colourPrint[7]}{board[7]}{Red} | {colourPrint[8]}{board[8]}{Red} |
    +---+---+---+{Normal}''')

def Chance(player, board):
    move = int(input(f'Move -> {player}: '))-1
    while board[move] != ' ':
        print('Move already occupied!')
        move = int(input(f'Move -> {player}: '))-1
    
    board[move] = player
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    return player, board

Board([1, 2, 3, 4, 5, 6, 7, 8, 9])
player = 'X'
for _ in range(9):
    player, board = Chance(player, board)
    print(player)
    Board(board)
