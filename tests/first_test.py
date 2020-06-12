import pytest


# test that 2 == 2
def test_two_equals_two():
    assert 2 == 2

def sum_numbers(num_one, num_two):
    return num_one + num_two

def test_sum_numbers():
    result = sum_numbers(1, 2)
    assert result == 3

def test_sum_numbers_with_strings():
    result = sum_numbers('1', '2')
    assert result == 3

def game():
    num_one = input("please supply number")
    num_two = input("please supply second number and Ill add it up for you")
    return sum_numbers(num_one, num_two)


if __name__ == "__main__":
    game()

# create a function that sums up two numbers
def test_sum_number_the_real_way():
    result = 1 + 2
    assert result == 3

