from cryptography.fernet import Fernet


def add():
    username = input("Enter your username: ")
    passwd  = input("Enter your password: ")

    with open("passwords.txt", "a") as f:
        f.write(username + " | " + passwd + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            usr, pwd = data.split("|")
            print("Username: ", usr, "Password: ", pwd)

while True:
    mode = input("Would you like to add a new password or view an existing one (view/add) Q to quit? ").lower()
    
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Choose a valid option!")
        continue