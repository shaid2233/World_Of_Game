import sys
import currency_roulette
import memory_game
import guess_game
import score

games_list = ['memory_game', 'guess_game', 'currency_roulette']
difficulty_levels = [1,2,3,4,5]


def welcome():
    username = input("What is your name? ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey!")

# todo delete

def start_play():
    print("\nStart the game!")

    game_name = ''
    difficulty_level = 0

    while game_name not in games_list and difficulty_level not in difficulty_levels:
        game_name = input(f'type the game you want to play: \n{games_list[0]}'
                                                          f'\n{games_list[1]}'
                                                          f'\n{games_list[2]}'
                                                          f'\n\n')

        difficulty_level = input(f'\nPlease select a difficulty level: {difficulty_levels}\n\n')

        if game_name not in games_list:
            print(
                f"Invalid choice! Please select from available options"
            )
        else:
            break

    # todo check why you need result
    result = eval(game_name).play(difficulty_levels)



def play_again():
    choice = get_valid_input(
        "\nPlay again? (Y for Yes or Q to Quit): ", ["y", "q", "Y", "Q"]
    ).lower()
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
