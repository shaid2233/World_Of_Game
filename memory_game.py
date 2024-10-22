from app import choose_difficulty
import random

difficulty = choose_difficulty()

def generate_sequence():
    if difficulty == "1":
        rand_list =[random.randint(1,101) for _ in range(1)]
    elif difficulty == "2":
         rand_list =[random.randint(1,101) for _ in range(2)]
    elif difficulty == "3":
         rand_list =[random.randint(1,101) for _ in range(3)]
    elif difficulty == "4":
         rand_list =[random.randint(1,101) for _ in range(4)]
    elif difficulty == "5":
         rand_list =[random.randint(1,101) for _ in range(5)]
    print(rand_list)
generate_sequence()



