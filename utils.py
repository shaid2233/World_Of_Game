scores_file_name = "scores.txt"
bad_return_code = -1


def screen_cleaner():
    import os 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Usage
screen_cleaner() 
    
    
