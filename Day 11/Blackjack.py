import random
############### Blackjack Project #####################


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
global user_cards
user_cards = []
global user_card_value
user_card_value = int()

global computer_cards
computer_cards = []
global computer_card_value
computer_card_value = int()

gameStillRunning = True

def calculate_score(cards):
    sum_cards = int()
    for i in cards:
        sum_cards += i
    return sum_cards

def deal_card(hand):
    hand.append(cards[random.randint(0,12)])

def dealer_card_draw():
    deal_card(computer_cards)
    deal_card(computer_cards)
    computer_card_value = calculate_score(computer_cards)
    while calculate_score(computer_cards) < 17:
        deal_card(computer_cards)
        if calculate_score(computer_cards) > 21 and 11 in computer_cards:
            index = computer_cards.index(11)
            computer_cards[index] = 1

dealer_card_draw()
deal_card(user_cards)
deal_card(user_cards)
print(f"The dealers first card is {computer_cards[0]}")

while gameStillRunning == True:
    print(f"Your current cards are {user_cards}")
    if 11 in user_cards and 10 in user_cards and len(user_cards) == 2:
        if 11 in computer_cards and 10 in computer_cards and len(computer_cards) == 2:
            print("Both you and the dealer have blackjack. Nobody wins.")
            gameStillRunning = False
            break
        else:
            print("Blackjack. You win")
            gameStillRunning = False
            break
    if calculate_score(user_cards) > 21 and 11 not in user_cards:
        gameStillRunning = False
        print("You Lose!")
        break
    if calculate_score(user_cards) > 21 and 11 in user_cards:
        index = user_cards.index(11)
        user_cards[index] = 1
    cardOrNot = input("Do you want another card? Type yes or no: ")
    if (cardOrNot).lower() == "yes":
        deal_card(user_cards)
        if calculate_score(user_cards) > 21 and 11 in user_cards:
            index = user_cards.index(11)
            user_cards[index] = 1
        print(f"Your cards are now {user_cards}, and your total is {calculate_score(user_cards)}")
    if (cardOrNot).lower() == "no":
        if calculate_score(user_cards) <= 21:
            if calculate_score(computer_cards) > 21:
                print(f"The dealer busts, with a score of {calculate_score(computer_cards)}. You Win")
                gameStillRunning = False
                break
            if calculate_score(computer_cards) == calculate_score(user_cards):
                print(f"You and the dealer tie, you with a deck of {user_cards} and a score of {calculate_score(user_cards)}, verseus the dealer with a deck of {computer_cards} and a score of {calculate_score(computer_cards)}")
                gameStillRunning = False
                break
            if calculate_score(user_cards) > calculate_score(computer_cards):
                print(f"You win with a deck of {user_cards} and a score of {calculate_score(user_cards)}, verseus the dealer with a deck of {computer_cards} and a score of {calculate_score(computer_cards)}")
                gameStillRunning = False
                break
            if calculate_score(user_cards) < calculate_score(computer_cards):
                print(f"You lose with a deck of {user_cards} and a score of {calculate_score(user_cards)}, verseus the dealer with a deck of {computer_cards} and a score of {calculate_score(computer_cards)}")
                gameStillRunning = False
                break
        if calculate_score(user_cards) > 21:
            print(f"You bust with a deck of {user_cards} and a score of {calculate_score(user_cards)}")
            gameStillRunning = False
            break


    
