import copy


def solve_puzzle(hints, board=[[]]):
    """    https://www.codewars.com/kata/4-by-4-skyscrapers    """

    if len(board) == 1:
        board = [[0 for j in range(0, 4)] for i in range(0, 4)]

    available_values_len_tab = get_avaialble_values(board)
    x, y = get_next_position_with_minimal_len(board, available_values_len_tab)

    # validate vs hints:
    for i, hint_value in enumerate(hints):
        if not validate_view_by_hint(view_for_hint(i, board), hint_value):
            return False

    # solution
    if x is None and y is None:
        return board

    next_board = copy.deepcopy(board)
    solution = False
    while not solution:
        if len(available_values_len_tab[x][y][0]) == 0:
            return False
        else:
            next_board[x][y] = available_values_len_tab[x][y][0].pop()
            solution = solve_puzzle(hints, next_board)
    return tuple([tuple(x) for x in solution])


def get_avaialble_values(board):
    available_values_len_tab = [[[available_values(i, j, board), len(available_values(i, j, board))]
                                 for j in range(0, 4)] for i in range(0, 4)]
    return available_values_len_tab


def get_next_position_with_minimal_len(board, available_values_len_tab):
    min_len = 5
    x, y = None, None
    for i in range(0, 4):
        for j in range(0, 4):
            if available_values_len_tab[i][j][1] > 0 and board[i][j] == 0:
                if min_len > available_values_len_tab[i][j][1]:
                    min_len = available_values_len_tab[i][j][1]
                    x, y = i, j
    return x, y


def visible_count(view):
    top = view[0]
    view_ct = 0
    for building in view:
        if building >= top:
            view_ct += 1
            top = building
    return view_ct


def get_horizontal_values(i, problem):
    return {x for x in problem[i] if x != 0}


def get_vertical_values(j, problem):
    return {problem[x][j] for x in range(0, 4) if problem[x][j] != 0}


def available_values(i, j, problem):
    return {j for j in range(1, 5)} - (
        get_horizontal_values(i, problem) | get_vertical_values(j, problem))


def view_for_hint(i, problem):
    if 0 <= i <= 3:
        return [problem[x][i] for x in range(0, 4)]
    if 4 <= i <= 7:
        return [x for x in problem[i % 4]][::-1]
    if 8 <= i <= 11:
        return [problem[x][3 - i % 8] for x in range(0, 4)][::-1]
    if 12 <= i <= 15:
        return [x for x in problem[3 - i % 12]]


def validate_view_by_hint(view, hint_value):
    if view.count(0) == 0 and hint_value != 0:
        if visible_count(view) == hint_value:
            return True
        else:
            return False
    #to adjust for more complicatred cases
    return True
