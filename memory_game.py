import random
import time
import ast

difficulty = choose_difficulty()


def generate_sequence(difficulty_levels):
    rand_list = []

    # todo for loop
    for difficulty in difficulty_levels:
        # for each difficulty add reverse wait time
        rand_list = [random.randint(1, 101) for _ in range(difficulty)]
        # 1 -> 5, 2 -> 4, 3-> 3, 4- > 2, 5 -> 1
        time.sleep(difficulty_levels[-difficulty])



    print("Remember these numbers:", rand_list)
    time.sleep(2)  # Give player time to memorize
    print("\n" * 50)  # Clear screen
    return rand_list


def get_list_from_user():
    user_input = input("Enter the numbers you saw (e.g., [1, 2, 3]): ")
    try:
        # Convert string input to actual list
        return ast.literal_eval(user_input)
    except:
        print("Invalid input! Please use format: [1, 2, 3]")
        return []


def is_list_equal(list1, list2):
    if list1 == list2:
        print("Great job! You remembered correctly!")
        return True
    else:
        print(f"Not quite. The numbers were: {list1}")
        print(f"You entered: {list2}")
        return False


def play(difficulty_levels):
    # Generate the random sequence
    random_numbers = generate_sequence(difficulty_levels)

    # Get user's guess
    user_numbers = get_list_from_user()

    return is_list_equal(random_numbers, user_numbers)

