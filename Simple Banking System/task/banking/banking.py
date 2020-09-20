# Write your code here
import random

cards = {}
balances = {}
rand = random.SystemRandom()


def create_card():
    new_card = str(random.randint(4000000000000000, 4000009999999999))
    if not luhn_check(new_card):
        create_card()
    new_pin = ''.join(str(random.randint(0, 9)) for _ in range(4))
    cards[new_card] = new_pin
    balances[new_card] = 0
    print("Your card has been created")
    print("Your card number:")
    print(new_card)
    print("Your card PIN")
    print(new_pin)
    menu()


def account(card):
    print("You have successfully logged in!")
    print()
    while True:
        print("""
            1. Balance
            2. Log out
            0. Exit""")
        command = int(input())
        if command == 1:
            print("Balance: " + str(balances[card]))
        elif command == 2:
            print("You have successfully logged out!")
            menu()
            break
        elif command == 0:
            print('Bye!')
            exit()


def luhn_check(card_number):
    last_digital = card_number[-1]
    card_number = card_number[:-1]
    sum_odd = 0
    for x in range(0, 15, 2):
        k = int(card_number[x]) * 2
        if k > 9:
            sum_odd += (k // 10 + k % 10)
        else:
            sum_odd += k
    sum_even = 0
    for y in range(1, 14, 2):
        sum_even += int(card_number[y])
    if last_digital == str((sum_odd + sum_even) % 10) == "0":
        return True
    elif last_digital == str(10 - (sum_odd + sum_even) % 10):
        return True
    return False


def login():
    print('Enter your card number:')
    card = input()
    print('Enter your pin:')
    pin = input()
    if card in cards and cards[card] == pin:
        account(card)
    else:
        print('Wrong card number or PIN!')
        menu()


def menu():
    print("""
    1. Create an account
    2. Log into account
    0. Exit
    """)
    command = int(input())

    if command == 0:
        print('Bye!')
        exit()
    elif command == 1:
        create_card()
    elif command == 2:
        login()


menu()
