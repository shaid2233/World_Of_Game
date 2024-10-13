import random


def generate_number():
    random_number = random.randint(0, 101)  # we generate random number
    print(random_number)
    return random_number


choice = input("Enter the number of your choice (1-5): ")
if choice == "1":
    compare_values0(val1, val2, tolerance=20)
elif choice == "2":
    compare_values1()
elif choice == "3":
    compare_values2()
elif choice == "4":
    compare_values3()
elif choice == "5":
    compare_values4()


def get_guess_from_user():
    user_input = int(input("Please guess a number between 0 to 100 "))
    return user_input


val1 = generate_number()


val2 = get_guess_from_user()


def compare_values0(val1, val2, tolerance=20):
    if abs(val1 - val2) <= tolerance:
        print(f"Great! Your guess of {val1} is close enough to {val2}.")
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")


compare_values0(val1, val2, tolerance=20)


def compare_values1(val1, val2, tolerance=15):
    if abs(val1 - val2) <= tolerance:
        print(f"Great! Your guess of {val1} is close enough to {val2}.")
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")


compare_values1(val1, val2, tolerance=15)


def compare_values2(val1, val2, tolerance=10):
    if abs(val1 - val2) <= tolerance:
        print(f"Great! Your guess of {val1} is close enough to {val2}.")
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")


compare_values2(val1, val2, tolerance=10)


def compare_values3(val1, val2, tolerance=5):
    if abs(val1 - val2) <= tolerance:
        print(f"Great! Your guess of {val1} is close enough to {val2}.")
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")


compare_values3(val1, val2, tolerance=5)


def compare_values4(val1, val2, tolerance=1):
    if abs(val1 - val2) <= tolerance:
        print(f"Great! Your guess of {val1} is close enough to {val2}.")
    else:
        print(f"Sorry, the actual number was {val1}, and your guess was {val2}.")


compare_values4(val1, val2, tolerance=1)
