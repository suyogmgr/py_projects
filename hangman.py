import random
from collections import Counter

words = ["banana","apple","pear","orange","strawberry","grapes"]

fruit = random.choice(words)
print(fruit)

for _ in fruit:
    print("_", end="")
print()

lettergussed = ""
chances = len(fruit) + 2
flag = 0
correct = 0

while (chances != 0) and flag == 0:

    chances -= 1
    print()
    usr_input = input("Guess a word: ");

    if len(usr_input) > 1:
        print("Only a single letter allowed")
        continue

    if not usr_input.isalpha():
        print("No numbers or special symbols allowed")
        continue
    elif usr_input in lettergussed:
        print("Already guessed that letter")
        continue

    if usr_input in fruit:
        k = fruit.count(usr_input)

        for _ in range(k):
            lettergussed += usr_input
        
    for char in fruit:
        if char in lettergussed and (Counter(lettergussed) != Counter(fruit)):
            print(char, end=" ")
            correct +=1
        
        elif Counter(lettergussed) == Counter(fruit):
            print("The wrod is",fruit)
            print("Congratulations!, You won")
            flag = 1
            break #break out of for loop

        else:
            print("_",end=" ")