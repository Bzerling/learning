cells = input("Enter cells: ")
cell_list = list(cells)


def draw_grid(cell):
    cell = cell.replace("_", " ", len(cell))
    print("---------")
    for i in range(0, len(cell), 3):
        print('| ' + ' '.join(cell[i:i + 3]) + ' |')
    print("---------")


def analyze(): # analyze the game state
    win_X = ["X", "X", "X"]
    win_O = ["O", "O", "O"]
    vert_win = [[cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]]]
    hor_win = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]  
    diag_win = [[cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]                     
    if cells.count('X') - cells.count("O") > 1: # Detecting impossible state when X is 2 or more
        print('Impossible')
        return
    elif cells.count('O') - cells.count("X") > 1: # Detecting impossible state when O is 2 or more
        print('Impossible')
        return
    if win_X in vert_win or win_X in hor_win or win_X in diag_win: # X won
        if win_O in vert_win or win_O in hor_win or win_O in diag_win: # Detecting impossible state both won
            print('Impossible')
        else:
            print('X wins')
    elif win_O in vert_win or win_O in hor_win or win_O in diag_win: # O won
        print('O wins')
    elif cells.count(' ') > 0: # if side has three in a row but the grid still has empty cell
        print('Game not finished')
    else:
        print('Draw')



draw_grid(cell=cells)
analyze()
