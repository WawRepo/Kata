# position_square dict
import copy

def sudoku_solver(board):
    available_values_tab = [[available_values(i, j, board) for j in range(0, 9)] for i in range(0, 9)]
    available_values_len_tab = [[[available_values_tab[i][j], len(available_values_tab[i][j])] for j in range(0, 9)] for
                                i in range(0, 9)]
    min_len = 9
    x, y = None, None
    for i in range(0, 9):
        for j in range(0, 9):
            if available_values_len_tab[i][j][1] > 0 and board[i][j] == 0:
                if min_len > available_values_len_tab[i][j][1]:
                    min_len = available_values_len_tab[i][j][1]
                    x, y = i, j
            # game unsolvable
            elif available_values_len_tab[i][j][1] == 0 and board[i][j] == 0:
                return False
    #solution
    if x is None and y is None:
        return board

    next_board = copy.deepcopy(board)
    solution = False
    while not solution:
        if len(available_values_len_tab[x][y][0]) == 0:
            return False
        else:
            next_board[x][y] = available_values_len_tab[x][y][0].pop()
        solution = sudoku_solver(next_board)
    return solution


def available_values(i, j, problem):
    return {j for j in range(1, 10)} - (
        get_horizontal_values(i, j, problem) | get_vertical_values(i, j, problem) | get_square_values(
        i, j, problem))

def get_square_values(i, j, problem):
    x_start = 3 * (i // 3)
    y_start = 3 * (j // 3)
    return set(sum([problem[x_start + i][y_start: y_start + 3] for i in range(0, 3)], [])) - {0}

def get_horizontal_values(i, j, problem):
    return {x for x in problem[i] if x != 0}

def get_vertical_values(i, j, problem):
    return {problem[x][j] for x in range(0, 9) if problem[x][j] != 0}



