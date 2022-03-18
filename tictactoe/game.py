cells = "_________" # underscore is a cell
cell_list = list(cells)


def draw_grid(cell):
    """
    Scalable creating of game grid,
    depends on size of cell.
    """
    cell = cell.replace("_", " ", len(cell))
    print("---------")
    for i in range(0, len(cell), 3):
        print('| ' + ' '.join(cell[i:i + 3]) + ' |')
    print("---------")


def analyze():
    """
    Analyzing game state for win and draw
    """
    win_X = ("X", "X", "X")
    win_O = ("O", "O", "O")
    vert_win = ((cell_list[0], cell_list[3], cell_list[6]), (cell_list[1], cell_list[4], cell_list[7]), (cell_list[2], cell_list[5], cell_list[8]))
    hor_win = ((cell_list[0], cell_list[1], cell_list[2]), (cell_list[3], cell_list[4], cell_list[5]), (cell_list[6], cell_list[7], cell_list[8]))  
    diag_win = ((cell_list[0], cell_list[4], cell_list[8]), (cell_list[2], cell_list[4], cell_list[6]))                     
    if win_X in vert_win or win_X in hor_win or win_X in diag_win:
        return "X wins"
    elif win_O in vert_win or win_O in hor_win or win_O in diag_win:
        return "O wins"
    elif cell_list.count("_") == 0:
        return "Draw"


def moves_check():
    """
    checking input and state
    when cell is occupied
    """
    global check_grid
    global xy
    check_grid = ((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3))
    move_x = input("Enter the coordinates: ")
    while move_x.replace(" ", "", len(move_x)).isnumeric() is False:
        print("You should enter numbers!")
        move_x = input("Enter the coordinates: ")
    xy = tuple([int(i) for i in move_x.split(" ")])
    while xy[0] not in range(1,4) or xy[1] not in range(1,4):
        print("Coordinates should be from 1 to 3!")
        move_x = input("Enter the coordinates: ")
        xy = tuple([int(i) for i in move_x.split(" ")])
    while cell_list[check_grid.index(xy)] != "_":
        print("This cell is occupied! Choose another one!")
        move_x = input("Enter the coordinates: ")
        xy = tuple([int(i) for i in move_x.split(" ")])


def movex():
    """
    move for X
    """
    if cell_list[check_grid.index(xy)] == "_":
        cell_list[check_grid.index(xy)] = "X"
        draw_grid(cell="".join(cell_list))


def moveo():
    """
    move for O
    """
    if cell_list[check_grid.index(xy)] == "_":
        cell_list[check_grid.index(xy)] = "O"
        draw_grid(cell="".join(cell_list))


def game_():
    draw_grid(cell=cells)
    while True:
        moves_check()
        movex()
        analyze()
        if analyze() != None:
            print(analyze())
            break
        else:
            moves_check()
            moveo()
            analyze()
            if analyze() != None:
                print(analyze())
                break
        
        
game_()