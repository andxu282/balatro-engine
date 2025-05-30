from enum import Enum
import random

class Suit(Enum):
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"
    
    def __repr__(self):
        return f"Card(suit={self.suit.name}, rank={self.rank.name})"
    
def create_deck():
    deck = []
    for suit in Suit:
        for rank in Rank:
            deck.append(Card(suit, rank))
    return deck

class Deck:
    def __init__(self):
        self.cards = create_deck()

    def shuffle(self):
        random.shuffle(self.cards)

class ScoringHand(Enum):
    HIGH_CARD = "high card"
    PAIR = "pair"
    TWO_PAIR = "two pair"
    THREE_OF_A_KIND = "three of a kind"
    STRAIGHT = "straight"
    FLUSH = "flush"
    FULL_HOUSE = "full house"
    FOUR_OF_A_KIND = "four of a kind"
    STRAIGHT_FLUSH = "straight flush"
    FIVE_OF_A_KIND = "five of a kind"
    FLUSH_HOUSE = "flush house"
    FLUSH_FIVE = "flush five"
