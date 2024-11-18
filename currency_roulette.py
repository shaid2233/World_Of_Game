import random
import requests

def get_money_interval(difficulty, total):
    """Calculate the acceptable range based on exchange rate and difficulty."""
    try:
        # Fetch current USD to ILS exchange rate
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        exchange_rate = response.json()['rates']['ILS']
        
        # Convert total to ILS
        converted_total = total * exchange_rate
        
        # Calculate acceptable range
        interval = 10 - difficulty
        
        return (converted_total - interval, converted_total + interval)
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def get_guess_from_user(total):
    """Prompt user to guess the converted value."""
    while True:
        try:
            guess = float(input(f"What is {total} USD in ILS? "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def compare_results(interval, user_guess):
    """Check if user's guess is within the acceptable range."""
    return interval[0] <= user_guess <= interval[1]

def play(difficulty):
    """Play the Currency Roulette Game."""
    total = random.randint(1, 100)
    
    interval = get_money_interval(difficulty, total)
    if not interval:
        return False
    
    user_guess = get_guess_from_user(total)
    return compare_results(interval, user_guess)