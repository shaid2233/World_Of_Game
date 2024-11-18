import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    """Clear the screen based on operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')
