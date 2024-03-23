print("Welcome to my quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok lets play :)")
score = 0

answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What dose RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What dose ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

print("You got "+ str(score) + "questions correct")
print("You got "+ str((score/3) * 100) + "%")