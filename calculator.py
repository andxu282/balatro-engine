from typing import Tuple
from models import Card, Deck, Suit, Rank, GameState
from itertools import combinations
from utils import get_score

# Create a dummy deck for testing
# 2 suits, A through 7
dummy_deck = Deck([
    Card(Suit.HEARTS, Rank.TWO),
    Card(Suit.HEARTS, Rank.THREE),
    Card(Suit.HEARTS, Rank.FOUR),
    Card(Suit.HEARTS, Rank.FIVE),
    Card(Suit.HEARTS, Rank.SIX),
    Card(Suit.HEARTS, Rank.SEVEN),
    Card(Suit.HEARTS, Rank.ACE),
    Card(Suit.SPADES, Rank.TWO),
    Card(Suit.SPADES, Rank.THREE),
    Card(Suit.SPADES, Rank.FOUR),
    Card(Suit.SPADES, Rank.FIVE),
    Card(Suit.SPADES, Rank.SIX),
    Card(Suit.SPADES, Rank.SEVEN),
    Card(Suit.SPADES, Rank.ACE),
])

# Returns the expected value of this hand and the best combo to play from this hand
def get_best_combo(game_state: GameState, score: int) -> Deck:
    hand = game_state.hand
    deck = game_state.deck
    num_hands = game_state.num_hands
    if (num_hands == 0 or len(hand.cards) == 0):
        return Deck([])
    best_combo = None
    max_score = 0
    combos_to_play = combinations(hand.cards, 5)
    # go through every possible combo of 5 cards to play
    for combo_to_play in combos_to_play:
        # convert the combo to a deck
        combo_to_play = Deck(list(combo_to_play))
        # for every combo of 5 cards, we add the score of that combo and calculate
        # the expected value of the next hand by checking every single possible combo
        # of 5 cards from the remaining deck
        combos_from_deck = list(combinations(deck.cards, 5))
        # if there are no combos of 5, there's less than 5 cards left in the deck
        if (len(list(combos_from_deck)) == 0):
            combos_from_deck = [deck.cards.copy()]
        # go through every possible combo of 5 cards to replace the hand
        for combo_from_deck in combos_from_deck:
            combo_from_deck = Deck(list(combo_from_deck))
            # play the combo
            score += play_combo(hand, combo_to_play)
            # add the five cards to replace the hand
            add_cards_to_hand(hand, deck, combo_from_deck.cards)
            new_game_state = GameState(hand, deck, num_hands - 1, game_state.num_discards, game_state.score, game_state.current_score)
            # recurse to get the expected value of the next hand
            expected_value = get_score(get_best_combo(new_game_state, score)) / len(list(combos_from_deck))
            score += expected_value
            # add the five cards back to the deck
            deck.add(combo_from_deck.cards)
            if (score > max_score):
                max_score = score
                best_combo = combo_to_play
            score -= expected_value
            score -= get_score(combo_to_play)
            hand.discard(combo_from_deck.cards)
            hand.add(combo_to_play.cards)
    return best_combo


def play_combo(hand: Deck, combo: Deck) -> int:
    hand.discard(combo.cards)
    return get_score(combo)


def add_cards_to_hand(hand: Deck, deck: Deck, cards: list[Card]):
    hand.add(cards)
    deck.discard(cards)


def main():
    num_hands = 2
    num_discards = 0
    score = 300
    current_score = 0
    # preset starting hand
    hand = [
        Card(Suit.HEARTS, Rank.ACE),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.HEARTS, Rank.THREE),
        Card(Suit.HEARTS, Rank.FIVE),
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.SPADES, Rank.FOUR),
        Card(Suit.SPADES, Rank.FIVE),
        Card(Suit.SPADES, Rank.SEVEN),
    ]
    deck = [
        Card(Suit.HEARTS, Rank.FOUR),
        Card(Suit.HEARTS, Rank.SIX),
        Card(Suit.HEARTS, Rank.SEVEN),
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.SPADES, Rank.THREE),
        Card(Suit.SPADES, Rank.SIX),
    ]

    game_state = GameState(Deck(hand), Deck(deck), num_hands, num_discards, score, current_score)
    combo = get_best_combo(game_state, game_state.current_score)
    print("best combo", combo)
    print("score", get_score(combo))


if __name__ == "__main__":
    main()