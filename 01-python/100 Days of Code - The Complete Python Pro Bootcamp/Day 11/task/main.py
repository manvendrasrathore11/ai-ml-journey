n  = int(input("enter number to find out armstrong number"))
org = n
sum = 0
while n > 0 :
    a = n%10
    sum = sum + a*a*a
    n = n//10
if org == sum:
    print("enterd number in armstrong ")
else :
    print("entered number is not armstrong ")

import random

logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
print(logo)


def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = [random.choice(cards), random.choice(cards)]
    com_cards = [random.choice(cards), random.choice(cards)]
    yours_total = sum(your_cards)
    com_total = sum(com_cards)
    print(f"    Your cards : {your_cards} , current Score: {yours_total}")
    print(f"    computer's first card: {com_cards[0]}")
    if yours_total == 21:
        print("You Win with a Blackjack")

    elif com_total == 21:
        print("computer win with BLackjack")


    else:
        for i in range(0, 11):
            if yours_total > 21:
                if your_cards[i] == 11:
                    your_cards[i] = 1

    choice_to_move = input("Type 'y' to get another card , Type 'n' to pass:")
    if choice_to_move == 'y':
        your_cards.append(random.choice(cards))


your_choice = input(" Do you want to play a of Blackjack ?Type 'y' For yes and 'n' for No ").lower()
if your_choice == 'y':
    black_jack()

