from art import logo
import random as r
import os
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
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_over = False
    computer_score = 0
    user_score = 0
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}\nCurrent Score: {user_score}')
        print(f'Computer first card: {computer_cards[0]}')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input('Type "y" to get another card or "n" to stop: ')
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f'Your final hand: {user_cards}\nFinal Score: {user_score}')
    print(f'Computer final hand: {computer_cards}\nFinal Score: {computer_score}')
    print(compare(user_score,computer_score))
def compare(user_score,computer_score):
    if user_score == computer_score:
        return f'Both have a score of {user_score}. It\'s a draw!'
    elif computer_score == 0:
        return 'You lose, computer has a blackjack!'
    elif user_score == 0:
        return 'Congratulations! You got a blackjack!'
    elif user_score > 21:
        return 'Sorry you busted!Lose....'
    elif computer_score > 21:
        return 'Congratulations! You win because the computer busted.'
    elif user_score>computer_score:
        return 'Congrats! You win this round.'
    elif computer_score>user_score:
        return 'Sorry... Computer wins this round.'
    
restart = 'y'
while restart == 'y':
    print(logo)
    start_game()
    restart = input('Do you want to play again? "y" or "n": ')
    os.system('clear')           