scores_file_name = "scores.txt"
with open("scores.txt", "w") as file:
    file.write ("hello world")
    
bad_return_code = -1 

def choose_difficulty():
    def get_valid_input(prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input in valid_options:
                return user_input
            print(
                f"Invalid choice! Please enter one of the following: {', '.join(valid_options)}"
                )
            return get_valid_input("Choose difficulty level (1-5): ", ["1", "2", "3", "4", "5"])

def screen_cleaner():
    import os 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Usage
screen_cleaner() 
    
    
