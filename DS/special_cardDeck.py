import collections
import random

Card = collections.namedtuple("Card", ["rank", "suit"])

suit_map = {"Spade": 3, "Hearts": 2, "Diamond": 1, "Clubs": 0}

# TODO
# def rank_cards(card):
#     rank_value = CardDeck.ranks.index(card.rank)
#     return rank_value + suit_map[card.suit] * len(suit_map)


class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = reversed("Spade Hearts Diamond Clubs".split())

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        random.shuffle(self._cards)


deck = CardDeck()
print(len(deck))
print(deck[0])
