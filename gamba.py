import random

def spin_row():
    symbols = ['🥭', '🍓', '🍎', '🍊', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('-' * 50)
    print(" | ".join(row))
    print('-' * 50)

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🥭':
            return bet * 2
        elif row[0] == '🍓':
            return bet * 3
        elif row[0] == '🍎':
            return bet * 4
        elif row[0] == '🍊':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0


def main():
    balance = 100.00
    print("*" * 50)

    print("Welcome to pygamble")
    print("🥭 🍓 🍎 🍊 ⭐")

    print("*" * 50)

    while balance > 0:
        print(f"Rs.{balance:.2f}")
        bet = input("Enter the amount you want to spend: ")

        if not bet.isdigit():
            print("The input needs to be a valid amount")
            continue
        
        bet = int(bet)

        if bet <= 0:
            print("Amount cannot be less than or equal to 0")
            continue

        balance -= bet
        
        row = spin_row()
        print_row(row)
        payout_mny = payout(row, bet)
        
        if payout_mny > 0:
            print(f"You won {payout_mny}")
        else:
            print("You lost")
        balance += payout_mny
        print(balance)


    

if __name__ == "__main__":
    main()
    