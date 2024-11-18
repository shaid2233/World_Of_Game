import random
import time

def generate_sequence(difficulty):
    """Generate a list of random numbers."""
    return [random.randint(1, 101) for _ in range(difficulty)]

def display_sequence(sequence):
    """Display the sequence briefly."""
    print("Remember these numbers:")
    print(" ".join(map(str, sequence)))
    time.sleep(0.7)
    # Clear screen or use a clear function if available
    print("\n" * 50)

def get_list_from_user(difficulty):
    """Prompt user to input the sequence."""
    print(f"Enter {difficulty} numbers (space-separated):")
    while True:
        try:
            user_list = list(map(int, input().split()))
            if len(user_list) == difficulty:
                return user_list
            else:
                print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Please enter valid numbers.")

def is_list_equal(generated_list, user_list):
    """Compare user's list with generated list."""
    return generated_list == user_list

def play(difficulty):
    """Play the Memory Game."""
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_sequence)