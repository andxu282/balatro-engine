from models import Card, Deck, ScoringHand
from collections import Counter

CHIPS_PER_HAND = {
    ScoringHand.HIGH_CARD: 5,
    ScoringHand.PAIR: 10,
    ScoringHand.TWO_PAIR: 20,
    ScoringHand.THREE_OF_A_KIND: 30,
    ScoringHand.STRAIGHT: 30,
    ScoringHand.FLUSH: 35,
    ScoringHand.FULL_HOUSE: 40,
    ScoringHand.FOUR_OF_A_KIND: 60,
    ScoringHand.STRAIGHT_FLUSH: 100,
    ScoringHand.FIVE_OF_A_KIND: 120,
    ScoringHand.FLUSH_HOUSE: 140,
    ScoringHand.FLUSH_FIVE: 160,
}

MULT_PER_HAND = {
    ScoringHand.HIGH_CARD: 1,
    ScoringHand.PAIR: 2,
    ScoringHand.TWO_PAIR: 2,
    ScoringHand.THREE_OF_A_KIND: 3,
    ScoringHand.STRAIGHT: 4,
    ScoringHand.FLUSH: 4,
    ScoringHand.FULL_HOUSE: 4,
    ScoringHand.FOUR_OF_A_KIND: 7,
    ScoringHand.STRAIGHT_FLUSH: 8,
    ScoringHand.FIVE_OF_A_KIND: 12,
    ScoringHand.FLUSH_HOUSE: 14,
    ScoringHand.FLUSH_FIVE: 16,
}

def get_hand_type(hand: Deck) -> ScoringHand:
    assert len(hand.cards) <= 5
    
    # Count occurrences of each rank and suit
    rank_counts = Counter(card.rank for card in hand.cards)
    suit_counts = Counter(card.suit for card in hand.cards)
    
    # Sort ranks for checking straights
    sorted_ranks = sorted(card.rank.value for card in hand.cards)
    
    # Check if hand is a flush (all same suit)
    is_flush = len(suit_counts) == 1
    
    # Check if hand is a straight
    is_straight = (len(sorted_ranks) == 5 and 
                  sorted_ranks[-1] - sorted_ranks[0] == 4 or
                  sorted_ranks == [2, 3, 4, 5, 14])
    
    # Get counts of rank occurrences
    values = sorted(rank_counts.values(), reverse=True)
    # Check for specific hands from highest to lowest rank
    if is_flush and values == [3, 2]: # Flush house
        return ScoringHand.FLUSH_HOUSE
        
    if is_flush and values == [5]: # Flush five
        return ScoringHand.FLUSH_FIVE

    if is_flush and is_straight: # Straight flush
        return ScoringHand.STRAIGHT_FLUSH
    
    if values == [5]: # Five of a kind
        return ScoringHand.FIVE_OF_A_KIND

    if values == [4, 1]: # Four of a kind
        return ScoringHand.FOUR_OF_A_KIND
        
    if values == [3, 2]: # Full house
        return ScoringHand.FULL_HOUSE
        
    if is_flush: # Regular flush
        return ScoringHand.FLUSH
        
    if is_straight: # Regular straight
        return ScoringHand.STRAIGHT
        
    if values == [3, 1, 1]: # Three of a kind
        return ScoringHand.THREE_OF_A_KIND
        
    if values == [2, 2, 1]: # Two pair
        return ScoringHand.TWO_PAIR
        
    if values == [2, 1, 1, 1]: # One pair
        return ScoringHand.PAIR
        
    # If nothing else matches, it's a high card
    return ScoringHand.HIGH_CARD

def get_score(combo: Deck):
    if len(combo.cards) == 0:
        return 0
    hand_type = get_hand_type(combo)
    
    # Sort hand by rank frequency first, then by rank value
    # This ensures paired/matching cards are grouped together
    rank_counts = Counter(card.rank for card in combo.cards)
    sorted_hand = sorted(combo.cards, 
                        key=lambda card: (-rank_counts[card.rank], -card.rank.value))
    chips = CHIPS_PER_HAND[hand_type] 
    mult = MULT_PER_HAND[hand_type]

    match hand_type:
        case ScoringHand.HIGH_CARD:
            # Only highest card counts
            chips += sorted_hand[0].chips
            
        case ScoringHand.PAIR:
            # Only the paired cards count
            chips += sorted_hand[0].chips * 2
            
        case ScoringHand.TWO_PAIR:
            # Both pairs count separately
            first_pair = sorted_hand[0].chips * 2
            second_pair = sorted_hand[2].chips * 2
            chips += first_pair + second_pair
            
        case ScoringHand.THREE_OF_A_KIND:
            # Only the three matching cards count
            chips += sorted_hand[0].chips * 3
            
        case ScoringHand.STRAIGHT | ScoringHand.FLUSH | ScoringHand.FULL_HOUSE | ScoringHand.STRAIGHT_FLUSH | ScoringHand.FIVE_OF_A_KIND | ScoringHand.FLUSH_HOUSE | ScoringHand.FLUSH_FIVE:
            chips += sum(card.chips for card in combo.cards)
            
        case ScoringHand.FOUR_OF_A_KIND:
            # Only the four matching cards count
            chips += sorted_hand[0].chips * 4
        case _:
            raise ValueError(f"Invalid hand type: {hand_type}")
        
    return chips * mult