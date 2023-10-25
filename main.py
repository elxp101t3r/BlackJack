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