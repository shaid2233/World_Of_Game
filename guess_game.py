import random

def generate_number():
    random_number = random.randint(0, 100)  # Random number between 0 and 100
    print(f"Random number (for debugging): {random_number}")
    return random_number

def get_guess_from_user():
    user_input = int(input("Please guess a number between 0 and 100: "))
    return user_input

def compare_values(val1, val2, tolerance):
    if abs(val1 - val2) <= tolerance:
        print(f"Great! Your guess of {val2} is close enough to {val1} (within a tolerance of {tolerance}).")
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")

# Main game flow
def start_game():
    # Generate the random number
    val1 = generate_number()
    
    # Get user's choice for difficulty level
    choice = input("Enter the difficulty level (1-5): ")

    # Set tolerance based on the user's choice
    tolerances = {
        "1": 20,
        "2": 15,
        "3": 10,
        "4": 5,
        "5": 1
    }
    
    # Validate the choice and assign tolerance
    if choice in tolerances:
        tolerance = tolerances[choice]
    else:
        print("Invalid choice. Please select a level between 1 and 5.")
        return

    # Get the user's guess
    val2 = get_guess_from_user()

    # Compare the values using the selected tolerance
    compare_values(val1, val2, tolerance)

# Start the game
start_game()
