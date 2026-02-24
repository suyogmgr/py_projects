menu = {
    "Momo" : 100.0,
    "Chowmin": 120.0,
    "Samosa" : 25.0,
    "Chiya" : 30.0
}

tray = []
total = 0

print("---------- MENU ----------")

for key, value in menu.items():
    print(f"{key:10} : Rs.{value:.2f}")

print("--------------------------")

while True:
    food = input("Select an item(q to quit): ")

    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        tray.append(food)
        
    else:
        print("No such item in the menu")
    
    
for food in tray:
    print(food, end=" ")

    print()

    total += menu.get(food)
print(total)

