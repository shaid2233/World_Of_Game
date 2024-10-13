import sys


def welcome():
    username = input("What is your name? ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    while True:
        player_choice = input(
            "\nPlease Enter...\n1 for Memory Game\n2 for Guess Game\n3 for Currency Roulette:\n\n"
        )
        if player_choice in ["1", "2", "3"]:
            return player_choice
        print("You must enter 1, 2 or 3.")


def choose_difficulty():
    while True:
        difficulty_level = input("Enter Difficulty level between 1 and 5: ")
        if difficulty_level in ["1", "2", "3", "4", "5"]:
            return difficulty_level
        print("You must enter 1, 2, 3, 4 or 5.")


def play_again():
    while True:
        playagain = input("\nPlay again? (Y for Yes or Q to Quit): ").lower()
        if playagain == "y":
            return True
        elif playagain == "q":
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")
        else:
            print("Please enter Y or Q.")


welcome()
start_play()
choose_difficulty()
play_again()
