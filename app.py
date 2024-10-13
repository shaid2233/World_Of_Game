import sys

def welcome(username):
    username = input("what your name?")
    print(f"“Hi {username} and welcome to the World of Games: The Epic Journey”")
    welcome()






def start_play():
        player_choice = input(
                "\n Please Enter... \n1 for Memory Game \n2 for Guess Game , \n3 for Currency Roulette:\n\n"
            )
        if player_choice not in ['1', '2','3']:
            print( "you must enter 1, 2 or 3. ")
            return start_play

        diffculty_level = input ("Enter Dfficulty level between 1 and 5:")
        if diffculty_level not in  ['1', '2','3', '4', '5']:
            print("you must enter 1, 2 or 3, 4 or 5.")
            return start_play

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return start_play()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")



start_play()



