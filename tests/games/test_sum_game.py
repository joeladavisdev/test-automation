from sum_game import sum_numbers


def test_sum_numbers():
    result = sum_numbers(1, 2)
    assert result == 3

def test_sum_numbers_with_strings():
    result = sum_numbers('1', '2')
    assert result == 3