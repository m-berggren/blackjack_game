import random


class Card:
    """
    Creates lists with ranks and suits used for

    Args:

    """

    ranks = ["Ess"] + [str(n) for n in range(2, 11)] + "Knekt Dam Kung".split()
    suits = "Hjärter Spader Ruter Klöver".split()

    def __init__(self, suit, rank) -> None:
        self._rank = rank
        self._suit = suit

    def get_value(self) -> int:
        """
        Will be used in Player class to determine how many ace cards are found.

        Return:
            int: Value of a card, used to increment total points in Player class.
        """
        return self._rank

    def __str__(self) -> str:
        """

        Return:
            str:
        """
        return f"{Card.suits[self._suit-1]} {Card.ranks[self._rank-1]}"


class Deck:
    """
    Initiates list comprehension by looping over suits with iterator of 4 and ranks with 13,
    appending each cardm combination into a list with wach instance being of class type Card.´

    """

    def __init__(self) -> None:
        self._cards = [
            Card(suit, rank) for suit in range(1, 5) for rank in range(1, 14)
        ]
        random.shuffle(self._cards)

    def give_card(self) -> tuple:
        """
        Takes a card from deck, stores and removes from the list '_cards'.

        Return:
            tuple: Item from deck in the form of 'Card(rank, suit)'.
        """

        if len(self._cards) > 0:
            return self._cards.pop()


class Player:
    """
    Sets up ...

    Args:
        deck (list): Uses list from Deck class.
        name (str): Child classes will set their own 'name'.
    """

    def __init__(self, deck, name) -> None:
        self._deck = deck
        self._name = name
        self._hand = []
        self._points = 0
        self._aces = 0

    def new_card(self) -> None:
        """
        TBC

        """
        card = self._deck.give_card()
        self._hand.append(card)

        if card.get_value() == 1:
            self._points += 14
            self._aces += 1
        else:
            self._points += card.get_value()

        if self._points > 22 and self._aces > 0:
            self._points -= 13
            self._aces -= 1

    def cards(self) -> str:
        """
        TBC

        Return:
            str: For displaying list of gathered cards as a string.
        """
        return ", ".join(str(card) for card in self._hand)

    def write_out(self) -> None:
        """
        TBC

        """
        print(f"{self._name} har: {self.cards()} och poäng: {self._points}")


class User(Player):
    """
    TBC

    Args:
        deck (list)


    """

    def __init__(self, deck, name="Du") -> None:
        super().__init__(deck, name)
        self.beginning()

    def beginning(self):
        self.new_card()
        self.new_card()
        self.write_out()

    def play(self) -> int:
        """
        TBC

        Return:
            int:
        """

        while True:
            if self._points > 21 or not play_on():
                break
            self.new_card()
            self.write_out()
        return self._points


class Computer(Player):
    """
    TBC

    Args:

    """

    def __init__(self, deck, name="Datorn") -> None:
        super().__init__(deck, name)
        self.beginning()

    def beginning(self):
        self.new_card()
        self.write_out()
        self.new_card()

    def play(self):
        while self._points <= 16:
            self.new_card()
        self.write_out()
        return self._points


def play_on() -> bool:
    """
    TBC

    Return:
        bool:
    """
    string = str(
        input('\nSkriv "hit" för att ta fler kort eller "stand" för att stanna: \n')
    )

    if string.lower() == "hit":
        print()
        return True
    elif string.lower() == "stand":
        print()
        return False
    else:
        play_on()
