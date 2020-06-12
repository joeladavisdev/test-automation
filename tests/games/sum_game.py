def sum_numbers(num_one, num_two):
    return num_one + num_two


def game():
    num_one = input("please supply number")
    num_two = input("please supply second number and Ill add it up for you")
    if sum_numbers(num_one, num_two) == "Please supply an int":
        print("please supply an int")
        game()
    else:
        print (sum_numbers(num_one, num_two))

if __name__ == "__main__":
    game()