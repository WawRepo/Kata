import copy


def sudoku_solver(board):
    if not validate_initial_board(board):
        raise Exception('I know Python!')

    solutions = []
    solution = solver(board, solutions)
    if solution:
        return solution
    else:
        return False


def solver(board, solutions):
    available_values_len_tab = [[[available_values(i, j, board), len(available_values(i, j, board))]
                                 for j in range(0, 9)] for i in range(0, 9)]

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
    # solution
    if x is None and y is None:
        # print  len(solutions), solutions
        solutions.append(copy.deepcopy(board))
        return board

    next_board = copy.deepcopy(board)
    next_board = board
    solution = False
    while len(available_values_len_tab[x][y][0]) > 0:
        if len(solutions) > 1:
            return False
        next_board[x][y] = available_values_len_tab[x][y][0].pop()
        solver(next_board, solutions)
        next_board[x][y] = 0

    if len(solutions) == 1:
        return solutions[0]
    else:
        return False


def validate_initial_board(board):
    # check size
    if len(board) != 9:
        return False
    for i in range(0, 9):
        if len(board[i]) != 9:
            return False
    # check values
    if False in set(sum([[is_numeric_1_9_range(board[i][j]) for j in range(0, 9)] for i in range(0, 9)], [])):
        return False
    # check miltiplies on number in horizontal/vertical/square
    if True in set(sum([[check_if_value_is_already_used(i, j, board) for j in range(0, 9)] for i in range(0, 9)], [])):
        return False

    return True


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


def is_numeric_1_9_range(number):
    if not unicode(str(number), 'utf-8').isnumeric():
        return False
    if number < 0 or number > 9:
        return False
    return True


def check_if_value_is_already_used(i, j, board):
    tmp, board[i][j] = board[i][j], 0

    if tmp == 0:
        return False

    used_values = (get_horizontal_values(i, j, board) | get_vertical_values(i, j, board) | get_square_values(
        i, j, board))

    board[i][j] = tmp

    if tmp in used_values:
        return True
    else:
        return False