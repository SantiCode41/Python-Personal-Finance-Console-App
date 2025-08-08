from project import find_balance_col, calc_balance_values, color_code

def test_find_balance_col():
    assert find_balance_col(['NA', 'NA', 'Balance', 'NA']) == 2


def test_calc_balance_values():
    rows = [[1, 4, 'Item1', -400, 0, 'Notes1'], [1, 5, 'Item2', -200, 0, 'Notes2'], [1, 6, 'Item3', -100, 0, 'Notes3']]
    balance_col = 4
    starting_balance = 500


    assert calc_balance_values(rows, balance_col, starting_balance) == [[1, 4, 'Item1', -400, 500, 'Notes1'], [1, 5, 'Item2', -200, '300', 'Notes2'], [1, 6, 'Item3', -100, '200', 'Notes3']]


def test_color_code():
    ...
