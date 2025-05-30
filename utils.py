from models import Card, ScoringHand

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

def get_hand_type(hand: list[Card]) -> ScoringHand:
    assert len(hand) <= 5

def get_score(hand: list[Card]):
    assert len(hand) <= 5
    hand_type = get_hand_type(hand)

    # TODO: add support for pair, 2-pair, 3-of-a-kind, 4-of-a-kind
    match hand_type:
        case ScoringHand.HIGH_CARD:
            chips = CHIPS_PER_HAND[hand_type] + hand[0].rank.value
            mult = MULT_PER_HAND[hand_type]
            return chips * mult
        case ScoringHand.PAIR:
            return hand[0].rank.value * 2
        case ScoringHand.TWO_PAIR:
            return hand[0].rank.value * 2 + hand[2].rank.value * 2
        case ScoringHand.THREE_OF_A_KIND:
            return hand[0].rank.value * 3
        case ScoringHand.STRAIGHT, ScoringHand.FLUSH, ScoringHand.FULL_HOUSE, ScoringHand.STRAIGHT_FLUSH, ScoringHand.FIVE_OF_A_KIND, ScoringHand.FLUSH_HOUSE, ScoringHand.FLUSH_FIVE:
            chips = CHIPS_PER_HAND[hand_type] + sum(card.rank.value for card in hand)
            mult = MULT_PER_HAND[hand_type]
            return chips * mult
        case ScoringHand.FOUR_OF_A_KIND:
            return hand[0].rank.value * 4
        case _:
            raise ValueError(f"Invalid hand type: {hand_type}")