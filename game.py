from models import Card, Deck, Move
from utils import get_score
from itertools import combinations

def get_best_move(hand: list[Card], num_discards: int):
    if num_discards == 0:
        return Move.PLAY
    else:


'''
Returns the best set of cards to discard from a hand (up to 5 cards).

Parameters:
    hand: list[Card]

Returns:
    list[Card]

Example:
    hand = [AH, KH, QH, JH, 9C, 8D, 5S, 3S]
    output = [9C, 8D, 5S, 3S]
'''
def get_best_discard(hand: list[Card]):
    pass

'''
Returns the best set of cards to play from a hand (up to 5 cards).

Parameters:
    hand: list[Card]

Returns:
    list[Card]
'''
def get_best_play(hand: list[Card]):
    pass

'''
Simulates the engine playing a round of an ante.

Parameters:
    score: int -> the score needed to beat the blind (300 for the first round)
    reward: int -> the amount of money you get for winning a hand (3 by default)
    num_hands: int -> number of hands you have (4 by default)
    num_discards: int -> number of discards you have (3 by default)
    deck: Deck -> the deck of cards you're playing with (regular 52 card deck by default)
    hand_size: int -> the number of cards in your hand (8 by default)
    money: int -> the amount of money you have (0 by default)

Returns:
    int, int -> the score of the engine after the round, the amount of money you have after the round
'''
def play_round(score: int = 300, reward: int = 3, num_hands: int = 4, num_discards: int = 4, deck: Deck = Deck(), hand_size: int = 8, money: int = 0) -> int:
    # your score
    curr_score: int = 0
    # your hand  
    hand: list[Card] = []
    # While the player still has hands to play and the score is less than the target score
    while (num_hands > 0 and curr_score < score):
        # Replenish the hand up to hand size (8 by default)
        hand = draw_cards(deck, hand_size)

        # Gets the best move (discard or play)
        move = get_best_move(hand, num_discards)

        match move:
            case Move.DISCARD:
                cards_to_discard = get_best_discard(hand)
                deck.discard(cards_to_discard)
                num_discards -= 1
            case Move.PLAY:
                cards_to_play = get_best_play(hand)
                deck.discard(cards_to_play)
                # Add the score to the current score
                curr_score += get_score(cards_to_play)
                num_hands -= 1

    return curr_score, money

'''
Simulates the engine playing an entire game.
'''
def play_game():
    money = 4
    num_hands = 4
    num_discards = 3
    consumable_slots = 2

# Finds the highest scoring hand from a hand of cards
def best_scoring_hand(hand: list[Card]):
    pass

