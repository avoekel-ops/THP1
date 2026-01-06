import random

menu = """
Pick your move:

1. Flip a coin
2. Roll a dice
3. Draw a card
4. Exit

Selection:
"""

def flip_coin():
    coin = random.randint(1,2)
    if coin == 1:
        return "Heads"
    elif coin == 2:
        return "Tails"

def roll_dice(dice_sides):
    return random.randint(1, dice_sides)

def roller():
    print("Which dice do you want to roll?")
    print("1. 6-sided")
    print("2. 8-sided")
    print("3. 10-sided")
    print("4. 12-sided")

    user_choice = input("Your choice: ")

    if user_choice == "1":
        dice_sides = 6
    elif user_choice == "2":
        dice_sides = 8
    elif user_choice == "3":
        dice_sides = 10
    elif user_choice == "4":
        dice_sides = 12
    else:
        print("Invalid input. Please try again.")
        return

    result = roll_dice(dice_sides)
    print("You rolled a", result)

def draw_card():
    rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack", "Ace"]
    joker_input = input("Include Jokers? Y/N: ")
    if joker_input == "Y":
        rank.append("Joker")
    if joker_input == "N":
        pass
    card = random.choice(rank)
    rank.remove(card)
    return card


user_input = input(menu)
while user_input != '4':
    if user_input == '1':
        print(flip_coin())
    elif user_input == '2':
        roller()
    elif user_input == '3':
        print(draw_card())
    else:
        print('Invalid input. Please try again')

    user_input = input(menu)