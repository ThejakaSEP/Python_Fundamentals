import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def get_hand():
    return random.choice(cards)

def get_result(dealer_deck,player_deck):
    dealer_sum = 0
    player_sum = 0

    for card in  dealer_deck:
        dealer_sum+=card

    for card in player_deck:
        player_sum+=card

    if player_sum > dealer_sum:
        print(f'Your final hand : {player_deck}')
        print(f'Dealer\'s final hand: {dealer_deck}')
        print('You Win!!!')

    elif player_sum < dealer_sum or player_sum > 21:
        print(f'Your final hand : {player_deck}')
        print(f'Dealer\'s final hand: {dealer_deck}')
        print('You Lose!!!')

    else:
        print(f'Your final hand : {player_deck}')
        print(f'Dealer\'s final hand: {dealer_deck}')
        print('Draw!!!')

def play(answer):
    if answer == 'y':
        dealer_deck = []
        player_deck = []

        for i in range(2):
            dealer_deck.append(get_hand())
            player_deck.append(get_hand())

        print(f'Your cards : {player_deck}')
        print(f'Dealer\'s first card: {dealer_deck[0]}')

        continue_status = 'y'

        while continue_status == 'y':

            continue_status = input('Type \'y\' to get another card, type \'n\' to pass:')

            if continue_status == 'y':
                player_deck.append(get_hand())
                print(f'Your cards : {player_deck}')
                print(f'Dealer\'s first card: {dealer_deck[0]}')
            else:
                get_result(dealer_deck,player_deck)
                break

answer = 'y'
while answer == 'y':

    answer = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\' :')
    play(answer)