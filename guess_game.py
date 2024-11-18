import random

def generate_number(difficulty):
    """Generate a random number between 0 and difficulty."""
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):
    """Prompt user to guess a number within the specified range."""
    while True:
        try:
            guess = int(input(f"Guess a number between 0 and {difficulty}: "))
            if 0 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number between 0 and {difficulty}.")
        except ValueError:
            print("Please enter a valid number.")

def compare_results(secret_number, user_guess):
    """Compare user's guess with the secret number."""
    return secret_number == user_guess

def play(difficulty):
    """Play the Guess Game."""
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)