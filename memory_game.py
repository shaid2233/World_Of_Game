from app import choose_difficulty
import random
import time 
import ast  # Added for string to list conversion

difficulty = choose_difficulty()

def generate_sequence():
    if difficulty == "1":
        rand_list = [random.randint(1,101) for _ in range(1)]
        time.sleep(1)
    elif difficulty == "2":
        rand_list = [random.randint(1,101) for _ in range(2)]
        time.sleep(0.9)
    elif difficulty == "3":
        rand_list = [random.randint(1,101) for _ in range(3)]
        time.sleep(0.8)
    elif difficulty == "4":
        rand_list = [random.randint(1,101) for _ in range(4)]
        time.sleep(0.7)
    elif difficulty == "5":
        rand_list = [random.randint(1,101) for _ in range(5)]
        time.sleep(0.6)
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

def play_game():
    # Generate the random sequence
    random_numbers = generate_sequence()
    
    # Get user's guess
    user_numbers = get_list_from_user()
    
    # Compare them
    is_list_equal(random_numbers, user_numbers)

# Start the game
play_game()
     



