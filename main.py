############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from replit import clear
from art import logo


def deal_card():
    """Deals a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealt_card = random.choice(cards)
    return dealt_card


def calculate_score(list_of_item):
    """Calculates the sum"""
    calculated = sum(list_of_item)
    if calculated == 21 and len(list_of_item) == 2:
        return 0
    if calculated > 21:
        if 11 in list_of_item:
            list_of_item.remove(11)
            list_of_item.append(1)
        return sum(list_of_item)
    return calculated


def compare(score1, score2):
    """Compares the scores and returns the result"""
    if score1 > 21 and score2 > 21:
        return 'You went over. You lose'
    elif score1 == score2:
        return 'draw'
    elif score2 == 0:
        return 'you lose, opponent has black'
    elif score1 == 0:
        return 'blackjack, you win!!'
    if score1 > 21:
        return 'you lose, you went over'
    elif score2 > 21:
        return 'you win opponent went over'
    elif score1 > score2:
        return 'you win'
    else:
        return 'you lose'


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_another = input('''Do you want to draw another card.'y' for yes and 'n' for no\n''')
            if draw_another == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
        
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(score1 = user_score, score2 = computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n") == "y":
    clear()
    play_game()
