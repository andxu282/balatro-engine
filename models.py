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

SUIT_TO_STRING = {
    Suit.HEARTS: "H",
    Suit.DIAMONDS: "D",
    Suit.CLUBS: "C",
    Suit.SPADES: "S",
}

RANK_TO_STRING = {
    Rank.TWO: "2",
    Rank.THREE: "3",
    Rank.FOUR: "4",
    Rank.FIVE: "5",
    Rank.SIX: "6",
    Rank.SEVEN: "7",
    Rank.EIGHT: "8",
    Rank.NINE: "9",
    Rank.TEN: "T",
    Rank.JACK: "J",
    Rank.QUEEN: "Q",
    Rank.KING: "K",
    Rank.ACE: "A",
}

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        self.chips = CHIPS_PER_CARD[rank]

    def __str__(self):
        return f"{RANK_TO_STRING[self.rank]}{SUIT_TO_STRING[self.suit]}"
    
    def __repr__(self):
        return f"Card(suit={self.suit}, rank={self.rank})"

    def __eq__(self, other):
        # First check if other is actually a Card
        if not isinstance(other, Card):
            return False
        # Compare both rank and suit
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    def __init__(self):
        deck = []
        for suit in Suit:
            for rank in Rank:
                deck.append(Card(suit, rank))
        self.cards = deck
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def discard(self, cards: list[Card]):
        for card in cards:
            self.cards.remove(card)

    def add(self, cards: list[Card]):
        self.cards.extend(cards)

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

class Move(Enum):
    DISCARD = "discard"
    PLAY = "play"

CHIPS_PER_CARD = {
    Rank.TWO: 2,
    Rank.THREE: 3,
    Rank.FOUR: 4,
    Rank.FIVE: 5,
    Rank.SIX: 6,
    Rank.SEVEN: 7,
    Rank.EIGHT: 8,
    Rank.NINE: 9,
    Rank.TEN: 10,
    Rank.JACK: 10,
    Rank.QUEEN: 10,
    Rank.KING: 10,
    Rank.ACE: 11,
}

class GameState:
    def __init__(
            self,
            hand: Deck,
            deck: Deck,
            num_hands: int,
            num_discards: int,
            score: int,
            current_score: int,
            hand_size: int,
            num_cards_in_deck: int):
        self.hand = hand
        self.deck = deck
        self.num_hands = num_hands
        self.num_discards = num_discards
        self.score = score
        self.current_score = current_score
        self.hand_size = hand_size


    def __str__(self):
        return f"GameState(hand={self.hand}, deck={self.deck}, num_hands={self.num_hands}, num_discards={self.num_discards}, score={self.score}, current_score={self.current_score}, hand_size={self.hand_size})"
    
