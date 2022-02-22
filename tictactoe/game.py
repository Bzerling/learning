print('Enter cells: ')
x = input()
x = x.replace("_", " ", 9)
print('---------')
print('| ' + x[0], x[1], x[2] + ' |')
print('| ' + x[3], x[4], x[5] + ' |')
print('| ' + x[6], x[7], x[8] + ' |')
print('---------')


def analyze(): # analyze the game state
    win_X = ["X", "X", "X"]
    win_O = ["O", "O", "O"]
    vert_win = [[x[0], x[3], x[6]], [x[1], x[4], x[7]], [x[2], x[5], x[8]]]
    hor_win = [[x[0], x[1], x[2]], [x[3], x[4], x[5]], [x[6], x[7], x[8]]]  
    diag_win = [[x[0], x[4], x[8]], [x[2], x[4], x[6]]]                     
    if x.count('X') - x.count("O") > 1: # Detecting impossible state when X is 2 or more
        print('Impossible')
        return
    elif x.count('O') - x.count("X") > 1: # Detecting impossible state when O is 2 or more
        print('Impossible')
        return
    if win_X in vert_win or win_X in hor_win or win_X in diag_win: # X won
        if win_O in vert_win or win_O in hor_win or win_O in diag_win: # Detecting impossible state both won
            print('Impossible')
        else:
            print('X wins')
    elif win_O in vert_win or win_O in hor_win or win_O in diag_win: # O won
        print('O wins')
    elif x.count(' ') > 0: # if side has three in a row but the grid still has empty cell
        print('Game not finished')
    else:
        print('Draw')
