import os
import requests
import random
from dotenv import load_dotenv
from app import choose_difficulty

# Load the .env file to get the API key
load_dotenv()

# Get API key from .env file
api_key = os.getenv('CURRENCY_API_KEY')

def get_guess_from_user():
    user_input = int(input("Please guess a number in ILS: "))  # Get user's guess in ILS
    return user_input

# Define a function to get the current USD to ILS exchange rate
def get_money_interval():
    url = "https://api.currencyapi.com/v3/latest"
    params = {
        'apikey': api_key,
        'base_currency': 'USD',
        'currencies': 'ILS'
    }
    
    # Make the API request
    response = requests.get(url, params=params)
    
    # Parse the JSON response to get the exchange rate
    usd_to_ils = response.json()['data']['ILS']['value']
    
    return usd_to_ils

def compare_results(final_value):
    user_guess = get_guess_from_user()
    
    # Compare user's guess with the final value
    if user_guess >= final_value - 7 and user_guess <= final_value + 7:  # Allowing a margin of 7 NIS
        print("You're right!")
        return True
    else:
        print(f"You're wrong! The correct answer was: {final_value:.2f} ILS")
        return False

def play():
    # Call the choose_difficulty function to get the user's choice
    difficulty = choose_difficulty()

    # Generate a random USD amount (between 0 and 100)
    random_usd_amount = random.randint(0, 100)  
    
    # Get the current exchange rate from USD to ILS
    exchange_rate = get_money_interval()

    # Convert the random USD amount to ILS
    converted_amount = random_usd_amount * exchange_rate
    
    # Apply the difficulty modifier based on the chosen difficulty
    if difficulty == "1":
        adjusted_amount = converted_amount - 1 
    elif difficulty == "2":
        adjusted_amount = converted_amount - 2 
    elif difficulty == "3":
        adjusted_amount = converted_amount - 3 
    elif difficulty == "4":
        adjusted_amount = converted_amount - 4 
    elif difficulty == "5":
        adjusted_amount = converted_amount - 5 
    else:
        adjusted_amount = converted_amount  # Default if invalid input (this shouldn't happen if validation is done in choose_difficulty)

    # Final value to be compared with user guess
    final_value = adjusted_amount  # The final value in ILS

    # Print the converted value in ILS for the player
    print(f"Converted amount in ILS: {converted_amount:.2f} ILS")

    # Compare results
    result = compare_results(final_value)  # Compare with the final converted value

    return result

# Start the game
if __name__ == "__main__":
    play()





    
