import sys

def welcome():
    username = input("What is your name? ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey!")

# Helper function to validate user input
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print(f"Invalid choice! Please enter one of the following: {', '.join(valid_options)}")

def start_play():
    print("\nPlease choose a game:")
    game_choice = get_valid_input(
        "\n1 for Memory Game\n2 for Guess Game\n3 for Currency Roulette:\n\n",
        ["1", "2", "3"]
    )
    return game_choice
import memory_game
def choose_difficulty():
    difficulty = get_valid_input("Enter Difficulty level between 1 and 5: ", ["1", "2", "3", "4", "5"])
    return difficulty

def play_memory_game():
    print("\nPlaying Memory Game...")
    # Placeholder for Memory Game logic
    return True

def play_guess_game():
    print("\nPlaying Guess Game...")
    # Placeholder for Guess Game logic
    return True

def play_currency_roulette():
    print("\nPlaying Currency Roulette...")
    # Placeholder for Currency Roulette logic
    return True

def play_game(game_choice, difficulty_level):
    if game_choice == "1":
        return play_memory_game()
    elif game_choice == "2":
        return play_guess_game()
    elif game_choice == "3":
        return play_currency_roulette()

def play_again():
    playagain = get_valid_input("\nPlay again? (Y for Yes or Q to Quit): ", ["y", "q"]).lower()
    if playagain == "y":
        return True
    elif playagain == "q":
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")

# Main game loop
def main():
    welcome()
    
    while True:
        game_choice = start_play()  # Choose a game
        difficulty = choose_difficulty()  # Choose difficulty
        play_game(game_choice, difficulty)  # Play the chosen game

        if not play_again():
            break

# Call the main function to start the program
if __name__ == "__main__":
    main()

