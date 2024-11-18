import sys
import memory_game
import guess_game
import currency_roulette
import score

GAMES_LIST = ['Memory Game', 'Guess Game', 'Currency Roulette']
GAME_MODULES = {
    'Memory Game': memory_game,
    'Guess Game': guess_game,
    'Currency Roulette': currency_roulette
}
DIFFICULTY_LEVELS = [1, 2, 3, 4, 5]

def welcome():
    username = input("What is your name? ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey!")
    return username

def start_play():
    print("\nPlease choose a game to play:")
    for i, game in enumerate(GAMES_LIST, 1):
        print(f"{i}. {game}")

    while True:
        try:
            game_choice = int(input("\nEnter the number of the game you want to play: "))
            if 1 <= game_choice <= len(GAMES_LIST):
                game_name = GAMES_LIST[game_choice - 1]
                break
            else:
                print("Invalid game selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            difficulty = int(input(f"\nSelect difficulty level (1-5): "))
            if difficulty in DIFFICULTY_LEVELS:
                break
            else:
                print("Difficulty must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    game_module = GAME_MODULES[game_name]
    is_won = game_module.play(difficulty)

    if is_won:
        score.add_score(difficulty)
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost this time.")

def play_again():
    while True:
        choice = input("\nPlay again? (Y/N): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("\n🎮 🎉 Thanks for playing! 🎉 🎮")
            sys.exit()
        else:
            print("Invalid input. Please enter Y or N.")

def main():
    welcome()
    while True:
        start_play()
        if not play_again():
            break

if __name__ == "__main__":
    main()