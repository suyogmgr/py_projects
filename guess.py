import random

lowest_num = 1
highest_num = 10

random_num = random.randint(lowest_num, highest_num)

while True:
    user_input = int(input("Guess a number from 1 - 10: "))

    if user_input == random_num:
        print("CORRECT!!")
        break
    else:
        print("Try again")