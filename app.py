import sys

def welcome():
    username = input("What is your name? ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey!")

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print(f"Invalid choice! Please enter one of the following: {', '.join(valid_options)}")

def choose_difficulty():
    return get_valid_input("Choose difficulty level (1-5): ", ["1", "2", "3", "4", "5"])

def start_play():
    print("\nPlease choose a game:")
    game_choice = get_valid_input(
        "\n1 for Memory Game\n2 for Guess Game\n3 for Currency Roulette:\n\n",
        ["1", "2", "3"]
    )
    if game_choice == "1":
        import memory_game
    elif game_choice == "2":
        import guess_game
    elif game_choice == "3":
         import currency_roulette
def play_again():
    choice = get_valid_input("\nPlay again? (Y for Yes or Q to Quit): ", ["y", "q", "Y", "Q"]).lower()
    if choice == "q":
        print("\n🎮 🎉 Thanks for playing! 🎉 🎮")
        sys.exit()
    return choice == "y"

def main():
    welcome()
    
    while True:
        start_play()  # Play the chosen game
        if not play_again():
            break

if __name__ == "__main__":
    main()