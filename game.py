from models import Card
from utils import get_score

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

def get_best_move(hand: list[Card], num_discards: int):
    pass

def play_round(score: int, num_hands: int, num_discards: int):
    curr_score = 0
    hand = []
    # While the player still has hands to play and the score is less than the target score
    while (num_hands > 0 and curr_score < score):
        # Draw 8 cards from the deck
        hand = draw_cards(deck, 8)

        # Does the best move (discard or play)
        get_best_move(hand, num_discards)

        # Add the score to the current score
        curr_score += get_score(hand)

def main():
    pass
