from enum import IntEnum
from functools import total_ordering
from itertools import chain
from typing import (Any, Callable, DefaultDict, List, Iterable, NamedTuple,
                    Optional, Sequence, Tuple, Union)


def are_consecutive(numbers: Sequence[int]) -> bool:
    """Return True if list represents consecutive numbers."""
    return list(range(numbers[0], numbers[-1]+1)) == numbers


def multimax(iterable: Iterable, key: Callable = lambda x: x) -> List:
    """Return a list of all maximum values."""
    item_scores = [
        (key(item), item)
        for item in iterable
    ]
    max_key = max(score for score, _ in item_scores)
    return [
        item
        for score, item in item_scores
        if score == max_key
    ]


class Categories(IntEnum):
    high_card = 1
    one_pair = 2
    two_pair = 3
    three_of_a_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9


class BaseCard(NamedTuple):
    rank: str
    suit: str


@total_ordering
class Card(BaseCard):

    """Card with rank and suit."""

    VALUES: str = '23456789TJQKA'
    ACE_RANK = 11

    @property
    def numeric_rank(self) -> int:
        return self.VALUES.index(self.rank) + 2

    def __eq__(self, other: Any) -> Union[bool, type(NotImplemented)]:
        return self.rank == other.rank

    def __lt__(self, other: Any) -> Union[bool, type(NotImplemented)]:
        return self.rank < other.rank


class BaseScore(NamedTuple):
    category: Categories
    cards: Iterable[Card]


class Score(BaseScore):

    """Score of a poker hand."""

    def __new__(cls, category: Categories, cards: Iterable[Card]) -> 'Score':
        cards = list(cards)
        all_are_cards = all(isinstance(c, Card) for c in cards)
        if len(cards) != 5 or not all_are_cards:
            raise ValueError("5 cards required")
        if not isinstance(category, Categories):
            raise TypeError("Category invalid type")
        return super().__new__(cls, category, cards)


def group_cards_by_rank(cards: Iterable[Card]) -> List[List[Card]]:
    """Return a list of card lists grouped by rank."""
    def len_and_vals(cards: List[Card]) -> Tuple[int, List[Card]]:
        return len(cards), cards
    cards_by_rank = DefaultDict(list)
    for card in cards:
        cards_by_rank[card.rank].append(card)
    return sorted(cards_by_rank.values(), key=len_and_vals, reverse=True)


def get_same_rank_score(cards: Iterable[Card]) -> Score:
    """Return score for full house, 3/4 of a kind, pairs, or high card."""
    rank_groups = group_cards_by_rank(cards)
    cards = chain.from_iterable(rank_groups)
    most, second_most = len(rank_groups[0]), len(rank_groups[1])
    if most == 4:
        return Score(Categories.four_of_a_kind, cards)
    elif most == 3:
        if second_most == 2:
            return Score(Categories.full_house, cards)
        else:
            return Score(Categories.three_of_a_kind, cards)
    elif most == 2:
        if second_most == 2:
            return Score(Categories.two_pair, cards)
        else:
            return Score(Categories.one_pair, cards)
    else:
        return Score(Categories.high_card, cards)


def get_flush_score(cards: Iterable[Card]) -> Optional[Score]:
    """Return flush score or None."""
    all_suits_match = len(set(c.suit for c in cards)) == 1
    if all_suits_match:
        return Score(Categories.flush, sorted(cards, reverse=True))


def get_straight_score(cards: Iterable[Card]) -> Optional[Score]:
    """Return straight score or None."""
    cards = sorted(cards, reverse=True)
    values = sorted(card.numeric_rank for card in cards)
    first_val, *rest_vals = values
    first_card, *rest_cards = cards
    if first_val == Card.ACE_RANK and are_consecutive(rest_vals):
        return Score(Categories.straight, rest_cards + [first_card])
    elif are_consecutive(values):
        return Score(Categories.straight, cards)


def get_straight_flush_score(cards: Iterable[Card]) -> Optional[Score]:
    """Return straight flush score or None."""
    flush_score = get_flush_score(cards)
    straight_score = get_straight_score(cards)
    if flush_score and straight_score:
        return Score(Categories.straight_flush, straight_score.cards)


def score_hand(hand: Tuple[str, str]) -> Score:
    """Return best hand score."""
    cards = [Card(*c) for c in hand]
    scores = [
        get_same_rank_score(cards),
        get_straight_score(cards),
        get_flush_score(cards),
        get_straight_flush_score(cards),
    ]
    return max(
        score
        for score in scores
        if score is not None
    )


def poker(hands: Iterable[Tuple[str, str]]) -> Iterable[Tuple[str, str]]:
    """Return a list of all hands with the maximum score."""
    return multimax(hands, key=score_hand)
