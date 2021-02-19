'''THIS IS THE BLACK JACK GAME PROJECT'''

import random

#CREATE SOME SORT OF WELCOME MESSAGE THAT ASSKS FOR NAME AND IF PLAYER IS READY TO PLAY?
suits = ('Hearts', 'Diamonds','Spades','Clubs')
ranks = ('Two','Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of "+self.suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)  ##How do I return the string value of the deck??
        return self.all_cards


def initial_deal():
    player_c1 = shuffled_deck.pop(0)
    player_hand.append(player_c1)
    dealer_c1 = shuffled_deck.pop(0)
    dealer_hand.append(dealer_c1)

    player_c2 = shuffled_deck.pop(0)
    player_hand.append(player_c2)
    dealer_c2 = shuffled_deck.pop(0)
    dealer_hand.append(dealer_c2)

    # LATER WILL HAVE TO ADD THE ACTUAL PLAYER NAME
    print('Here is the initial deal!')
    print('\n' * 2)
    print(f'Player Hand: \n{player_c1}\n{player_c2}')
    print('\n' * 2)
    print(f'Dealer Hand: \n{dealer_c1}\n XXXXXX')


def bust_check(hand):  # will have to call on player hand or dealer hand
    i = 0
    v = 0

    for item in hand:
        x = hand[i]
        v = v + x.value
        print(x)
        if v > 21:
            for item in hand:
                q = item.rank
                if q == 'Ace':
                    v = v - 10
                    break
            if v > 21:
                print('BUST!')
                print(f'Total value of hand: {v}\n')
                return True

        else:
            i = i + 1

    print(f'Total value of hand: {v}\n')
    return v


def win_check(player_hand, dealer_hand):
    pi = 0
    pv = 0
    di = 0
    dv = 0
    for item in player_hand:
        x = player_hand[pi]
        pv = pv + x.value

        if pv > 21:
            for item in player_hand:
                pq = item.rank
                if pq == 'Ace':
                    pv = pv - 10
                    break
        else:
            pi = pi + 1

    for item in dealer_hand:
        x = dealer_hand[di]
        dv = dv + x.value

        if dv > 21:
            for item in player_hand:
                dq = item.rank
                if dq == 'Ace':
                    dv = dv - 10
                    break
        else:
            di = di + 1
    if pv > dv:
        print('Player wins')
        return 1

    elif dv > pv:
        print('Dealer wins')
        return 2
    else:
        print('push')
        return 3

    print(f'Player hand: {pv}, and dealer hand {dv}\n')


def look_for_bet():
    bet_2_big = True
    while bet_2_big == True:
        print(f'Your wallet has {wallet}')
        bet_value = int(input('How much would you like to bet? '))
        print('\n')
        if bet_value > wallet or bet_value<0:
            pass
        else:
            print(f'OK! You are betting ${bet_value}')
            bet_2_big = False
    return bet_value

'''THE ABOVE ARE CLASSES AND FUNCTIONS TO CREAT THE PARTS OF THE GAME 
    BELOW IS THE CODE THAT CREATES THE GAME FLOW'''

import os
clear = lambda: os.system('cls')


wallet = 100
opening = input(f'Welcome to Black Jack!  Your wallet has ${wallet}.\n Are you ready to play? Type Y to start')
opening = opening.upper()
if opening == 'Y':
    game_play = True
else:
    print('Ok.  Goodybye!')

while game_play == True:

    game_round = True

    while game_round == True:
        clear()
        new_deck = Deck()
        shuffled_deck = new_deck.shuffle_deck()
        player_hand = []
        dealer_hand = []
        at_risk = look_for_bet()
        initial_deal()

        player_turn = True
        while player_turn == True:

            response = input('Player, type capital Y if you would like a hit ')
            print('\n')
            # need to have way to ask again if is neither Y or N

            if response == 'Y':
                print('\n' * 2)
                print('Player Hand')
                next_card = shuffled_deck.pop(0)
                player_hand.append(next_card)
                v = bust_check(player_hand)
                if v == True:
                    print("The player busted!")
                    player_turn = False
                    dealer_turn = False
                    wallet = wallet - at_risk
                    game_round = False
                else:
                    pass
                # insert a class or func here that asks to play again
            else:
                print('Ok.  Dealers turn.')
                print('\n')
                player_turn = False
                dealer_turn = True

        while dealer_turn == True:

            v = bust_check(dealer_hand)
            # insert a win check
            if v >= 17:
                dealer_turn = False
                print('\n')
                print('The dealer is done.')
                print('\n')
                w = win_check(player_hand, dealer_hand)
                if w == 1:
                    wallet = wallet + at_risk
                    game_round = False
                elif w == 2:
                    wallet = wallet - at_risk
                    game_round = False
                else:
                    game_round = False
            else:
                next_card = shuffled_deck.pop(0)
                dealer_hand.append(next_card)
                v = bust_check(dealer_hand)
                if v == True:
                    print('\n')
                    print("The dealer busted!")
                    dealer_turn = False
                    wallet = wallet + at_risk
                    game_round = False
                    # insert a class or func here that asks to play again
                else:
                    dealer_turn = True
    print(f'Your wallet has ${wallet}\n')
    again = input('Would you like to play again? Type Y if yes.')
    clear()
    again = again.upper()
    if again != 'Y':
        clear()
        print(f'Ok. You are leaving the game with ${wallet}.')
        print('Good bye!')
        game_play = False


