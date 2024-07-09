"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        return True
    elif s.isalnum():
        return True
    elif not int(s[:2]).isdigit():
        return True

main()
"""


""" 
fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}
fruit = input("Item: ").lower().s
print(f"Calories: {fruits[fruit]}")
"""

"""
def is_valid(s):
    # Check if s has at least two letters
    if len(s) < 2:
        return False
    num_letters = 0
    num_part_after_num = 0
    for c in s:
        # Check if all characters are letters or numbers
        if not c.isalnum():
            return False
        if c.isdigit():
            num_part_after_num += 1
        if c.isalpha():
            num_letters += 1
    # Check if the first character is a letter
    if not s[0].isalpha():
        return False
    # Check if the plate starts with at least two letters
    if num_letters < 2:
        return False
    # Check if the number part is at the end of the plate
    if num_part_after_num > 0:
        if not s[0:2].isalpha() or not s[-num_part_after_num:].isdigit():
            return False
    # Check if the number part is not empty and does not start with a 0
    if num_part_after_num > 1 and s[-num_part_after_num] == '0':
        return False
    # Check if the plate has at most 6 characters
    if len(s) > 6:
        return False
    return True


plate = input("Plate: ")
if is_valid(plate):
    print("Valid")
else:
    print("Invalid")
"""


# def get_fuel():
#     while True:
#         try:
#              x = 0
#              y = 0
#              value = input("Fraction: ")
#              x, y = value.split("/")

#              if int(x) > int(y):
#                   print("x cannot be greater")

#              percentage = round(int(x) / int(y) * 100)

#              if percentage <= 1:
#                  return print("E")
#              elif percentage > 100:
#                   pass
#              elif percentage <= 99:
#                  return print("F")
#              else:
#                   return print(f"{percentage}%")

#         except(ZeroDivisionError, ValueError):
#                 pass


# get_fuel()


"""
def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    while True:    
        try:
            user = input("Item: ").strip().title()
        except EOFError:
            break

        if user:
            if user in menu:
                cost = menu[user]
                total += cost
                print(f"${total:.2f}")
        
main()
"""

"""
grocery = ["apple", "apple", "banana", "banana", "banana", "banana"]
grocery_dict = {}
for i in grocery:
    if i in grocery_dict:
        grocery_dict[i] += 1
    else:
        grocery_dict[i] = 1


for i, grocery in enumerate(grocery_dict):
    print(i, grocery)
"""

"""
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        user_input = input("Date:").strip()

        if "/" in user_input:
            month, day, year = user_input.split("/")
            month, day, year = int(month), int(day), int(year)
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                continue

        elif "," in user_input:
            month_day, year = user_input.split(",")
            day = month_day[-1]
            index = month_day[:-2]
            month = months.index(index) + 1
            month, day, year = int(month), int(day), int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                continue
    except ValueError:
        pass
"""

"""
import sys 
import random
from pyfiglet import Figlet

font_list = Figlet().getFonts()


if len(sys.argv) >= 2:
    if sys.argv[1] not in ("-f", "--font"):
        sys.exit("-f or --f needed")

    if sys.argv[2] not in font_list:
        sys.exit("Not a Font")
        
    elif len(sys.argv) < 3:
        usr_input = input("Input: ")
        random_font = random.choice(font_list)
        ran_font = Figlet().setFont(font=random_font)
        f = Figlet(font=random_font) 
        print(f.renderText(f"{usr_input}"))
        
    else:
        usr_input = input("Input: ")
        usr_font = sys.argv[2]
        f = Figlet(font=usr_font) 
        print(f.renderText(f"{usr_input}"))
"""


# name_list = ["suyog","bipan","ganesh","ram","sita"]
"""

def adieu(name_list):
    if len(name_list) == 1:
        print(f"Adieu, adieu, to {name_list[0]}")

    elif len(name_list) == 2:
        print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")

    else:
        edited_name_list = ", ".join(name_list[:-1])
        print(f"Adieu, adieu, to {edited_name_list}, and {name_list[-1]}")

def main():
    name_list = []
    try:
         while True:
            usr_name = input("Name: ")
            name_list.append(usr_name)
    except EOFError:
        print()
        pass
    
    adieu(name_list)


main()
"""

"""
import random

while True:
    try:
        usr_input = int(input("Level: "))
    except ValueError:
        continue 

    if usr_input <= 0:
        continue
    else:
        random_num = random.randint(1,usr_input)
        break


while True:
    try:
        usr_guess = int(input("Guess: "))
    except ValueError:
        continue
    
    if usr_guess > random_num:
        print("Too large!")
    elif usr_guess < random_num:
        print("Too small!")
    else:
        print("Just right!")
        break
"""

"""
import random

def get_level():
    while True:
        options = [1, 2, 3]
        try:
            level = int(input("Level: "))
            if level not in options:
                raise ValueError
            else:
                return level
        except ValueError:
            continue

def generate_integer(get_level):
    score = 0
    
    for _ in range(10):    
        if get_level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
            tries = 3
            ans = x + y
            while True:

                if tries == 0:
                    print(f"{x} + {y} = {ans}")
                    break
                try:
                    usr_ans = int(input(f"{x} + {y} = "))
                except ValueError:
                    tries -= 1
                    print("EEE")
                    continue

                if ans != usr_ans:
                    tries -= 1
                    print("EEE")
                    continue
                elif ans == usr_ans:
                    score += 1
                    break 
            
    
        elif get_level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
            tries = 3
            ans = x + y
            while True:

                if tries == 0:
                    print(f"{x} + {y} = {ans}")
                    break
                
                usr_ans = int(input(f"{x} + {y} = "))

                if ans != usr_ans:
                    tries -= 1
                    print("EEE")
                    continue
                elif ans == usr_ans:
                    score += 1
                    break 
            

        elif get_level == 3:
            x = random.randint(100,999)
            y = random.randint(100,999)
            tries = 3
            ans = x + y
            while True:

                if tries == 0:
                    print(f"{x} + {y} = {ans}")
                    break
                
                usr_ans = int(input(f"{x} + {y} = "))

                if ans != usr_ans:
                    tries -= 1
                    print("EEE")
                    continue
                elif ans == usr_ans:
                    score += 1
                    break 
    print(f"{score}")
        

def main():
    generate_integer(get_level())

main()
"""

"""
import sys
import requests
import json


def bitcoin_rate():

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # print(json.dumps(response.json(), indent=2))

    dollar = response.json()
    us_dollar = dollar["bpi"]["USD"]["rate_float"]
    bitcoin = float(sys.argv[1])
    return f"${bitcoin * us_dollar:,.4f}"


def main():
    while True:
        try:
            if len(sys.argv) != 2:
                print("Missing command-line argument")
                break
            elif float(sys.argv[1]):
                print(bitcoin_rate())
                break
        except ValueError:
            print("working")
            break


main()
"""

"""
import sys
import os

def file_reader(file_name):
    loc = 0
    try:
        with open(file_name) as test:
            for line in test:
                stripped_lines = line.strip()
                if stripped_lines and not stripped_lines.startswith("#"):
                    loc += 1
    except FileNotFoundError:
        sys.exit("No file found")
        
    return loc

def main():
    if len(sys.argv) < 2:
        sys.exit("Two few command lines")
    elif len(sys.argv) > 2:
        sys.exit("Two many command lines")

    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        sys.exit("Not a python file")


    if not os.path.isfile(file_name):
        sys.exit(f"No file named {file_name} exist")

    lines_of_code = file_reader(file_name)
    print(lines_of_code)

if __name__ == "__main__":
    main()
"""

#pizza 
from tabulate import tabulate
import sys
import os

with open(sys.argv[1]) as csv:
    for line in csv:
        stripped_csv = line.strip()
        lines = stripped_csv.readlines()
        headers = [lines[:0]]
        print(headers)