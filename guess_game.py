import random
from utils import choose_difficulty


def generate_number():
    random_number = random.randint(0, 100)  # Random number between 0 and 100
    return random_number


def get_guess_from_user():
    user_input = int(input("Please guess a number between 0 and 100: "))
    return user_input


def compare_values(val1, val2, tolerance):
    return abs(val1 - val2) <= tolerance


def play():

    val1 = generate_number()

    # Get user's choice for difficulty level
    choice = input("Enter the difficulty level (1-5): ")

    tolerances = {"1": 20, "2": 15, "3": 10, "4": 5, "5": 1}

    if choice in tolerances:
        tolerance = tolerances[choice]
    else:
        print("Invalid choice. Please select a level between 1 and 5.")
        return
    val2 = get_guess_from_user()

    result = compare_values(val1, val2, tolerance)
    if result:
        print(
            f"Great! Your guess of {val2} is close enough to {val1} (within a tolerance of {tolerance})."
        )
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")
    return result
