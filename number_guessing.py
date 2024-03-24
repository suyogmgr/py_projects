import random

random_range = int(input("Enter the range of the guess:"))

if random_range <= 0:
    print("Please enter a number greater than zero")


random_num = random.randrange(0,random_range)
guesses = 0

while True:
    userGuess = int(input("Gusess the number:"))
    
    guesses += 1

    if userGuess == random_num:
        print("You have guessed the correct number")
        break
    elif userGuess > random_range:
        print("Your guess can't be greater than the guess range")
    elif userGuess < random_num:
        print("You guess was smaller")
    elif userGuess > random_num:
        print("Your guess was greater")
    
print("You guessed it correctly in", guesses, "tries")