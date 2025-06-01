from models import Deck, Rank, Suit, Card, ScoringHand
from utils import get_hand_type, get_score
import unittest

class TestUtils(unittest.TestCase):

    def test_get_hand_type(self):
        # HIGH CARD
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.CLUBS, Rank.EIGHT),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.HIGH_CARD)

        # PAIR
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.CLUBS, Rank.EIGHT),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.PAIR)

        # TWO PAIR
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.TWO_PAIR)

        # THREE OF A KIND
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.THREE_OF_A_KIND)

        # STRAIGHT
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.SPADES, Rank.FOUR),
            Card(Suit.CLUBS, Rank.FIVE),
            Card(Suit.DIAMONDS, Rank.SIX),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.STRAIGHT)

        # FLUSH
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SEVEN),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.FLUSH)

        # FULL HOUSE
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.DIAMONDS, Rank.SIX),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.FULL_HOUSE)

        # FOUR OF A KIND
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.SIX),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.FOUR_OF_A_KIND)

        # STRAIGHT FLUSH
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SIX),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.STRAIGHT_FLUSH)

        # FIVE OF A KIND
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.TWO),    
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.FIVE_OF_A_KIND)

        # FLUSH HOUSE
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.THREE),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.FLUSH_HOUSE)

        # FLUSH FIVE
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
        ])
        self.assertEqual(get_hand_type(hand), ScoringHand.FLUSH_FIVE)

    def test_get_score(self):
        # HIGH CARD
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.CLUBS, Rank.EIGHT),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_score(hand), 16)

        # PAIR
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.CLUBS, Rank.EIGHT),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_score(hand), 28)

        # TWO PAIR
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_score(hand), 72)

        # THREE OF A KIND
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.DIAMONDS, Rank.ACE),
        ])
        self.assertEqual(get_score(hand), 108)

        # STRAIGHT
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.SPADES, Rank.FOUR),
            Card(Suit.CLUBS, Rank.FIVE),
            Card(Suit.DIAMONDS, Rank.SIX),
        ])
        self.assertEqual(get_score(hand), 200)

        # FLUSH
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SEVEN),
        ])
        self.assertEqual(get_score(hand), 224)

        # FULL HOUSE
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.DIAMONDS, Rank.SIX),
        ])
        self.assertEqual(get_score(hand), 232)

        # FOUR OF A KIND
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.SIX),
        ])
        self.assertEqual(get_score(hand), 476)

        # STRAIGHT FLUSH
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SIX),
        ])
        self.assertEqual(get_score(hand), 960)

        # FIVE OF A KIND
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.TWO),    
            Card(Suit.CLUBS, Rank.TWO),
            Card(Suit.SPADES, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),    
        ])
        self.assertEqual(get_score(hand), 1560)

        # FLUSH HOUSE
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.THREE),
        ])
        self.assertEqual(get_score(hand), 2142)

        # FLUSH FIVE
        hand = Deck([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.TWO),    
        ])
        self.assertEqual(get_score(hand), 2720)
        





if __name__ == "__main__":
    unittest.main()