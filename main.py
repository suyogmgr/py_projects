questions = ("What is a cat?",
            "What is 1 + 1?",
            "What is 3 * 3?")
options = (
            ("A. Animal", "B. Bird", "C.Cartoon", "D. Digital"),
            ("A. 4", "B. 9", "C. 2", "D. 8"),
            ("A. 2", "B. 4", "C. 7", "D. 9")
        )

answer = ("A", "C", "D")


guesses = []
score = 0
question_num = 0 

for question in questions:
    print(50 * '-')
    print(question)

    for option in options[question_num]:
        print(option, end=" ") 
    print()
    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
       print("CORRECT!!")
       score += 1
    else:
        print(f"The correct answer was {answer[question_num]}")

    
    question_num += 1


print(50 * '-')
print("RESULTS")

print(f"You got {score} poiints")
for guess in guesses:
    print(guess, end=" ")

print()

for answers in answer:
    print(answers, end=" ")