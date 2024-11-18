import os

SCORES_FILE_NAME = "Scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    """Add score to the scores file."""
    try:
        # Read current score or initialize to 0
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as f:
                current_score = int(f.read().strip() or 0)
        else:
            current_score = 0
        
        # Calculate new score
        new_score = current_score + POINTS_OF_WINNING(difficulty)
        
        # Write new score to file
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(new_score))
        
        return new_score
    except Exception as e:
        print(f"Error managing score: {e}")
        return None