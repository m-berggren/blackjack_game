class Card:
    ranks = "Ess 2 3 4 5 6 7 8 9 10 Knekt Dam Kung".split()
    suits = "Hjärter Spader Ruter Klöver".split()

    bj_dict = {
        "Ess": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "8": 8,
        "9": 9,
        "10": 10,
        "Knekt": 11,
        "Dam": 12,
        "Kung": 13,
    }

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def give_card(self):
        rank_value = str(self._rank)

        return Card.bj_dict[rank_value]

    def __str__(self):
        return Card.suits[self._suit], Card.ranks[self._rank]


class Deck:
    pass
