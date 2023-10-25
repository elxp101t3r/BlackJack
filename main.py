from art import logo
import random as r
import replit as rep
def start_game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    def deal_card():
        if cards:
            random_card = r.choice(cards)
            cards.remove(random_card)
            return random_card
        else:
            print('There are no more cards..')
            return None
    user_cards = []
    computer_cards = []
    def calculate_score(user_cards):
        if sum(user_cards) == 21 and len(user_cards) == 2:
            return 0
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
        if sum(user_cards) is None:
            return 0
        return sum(user_cards)