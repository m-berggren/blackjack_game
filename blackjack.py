"""
Skapa ett program som simulerar ett blackjack-spel mellan en spelare och en dator.

·         Spelet spelas med en vanlig kortlek som blandas innan varje runda.

·         Varje spelare får två kort i början av spelet. Datorn visar bara upp ett av sina kort.

·         Spelaren kan välja att ta fler kort (hit) eller stanna på sina nuvarande kort (stand).

·         Spelaren kan fortsätta att ta kort tills hen når 21 poäng eller över.

·         Om spelaren går över 21 poäng förlorar hen direkt.

·         När spelaren stannar, spelar datorn sin tur. Datorn måste ta kort så länge summan av korten är mindre än 17 poäng och stanna när datorns kortsumma är 17 poäng eller mer.

·         Om datorn går över 21 poäng vinner spelaren oavsett vilka kort spelaren har.

·         Om varken spelaren eller datorn går över 21 poäng så vinner den som har högst kortsumma.
"""

import random


class Card:
    '''
    Creates lists with ranks and suits, then used to create a deck with Deck class.

    Args:
        ranks (list): List of all available value types in a deck.
        suits (list): List of all available card types in a deck.
        rank (int): Used to store value of a single card.
        suit (str): Used to store a single card's type.

    Attributes:
        _rank (int): Used 
        _suit (str):
    '''

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "Hearts Spades Diamonds Clubs".split()

    def __init__(self, rank, suit) -> None:
        self._rank = rank
        self._suit = suit

    def get_value(self) -> int:
        '''
        Will be used in Player class to determine how many ace cards are found.
        
        Return:
            int: Value of a card, used to increment total points in Player class.
        '''
        return self._rank

    def __str__(self) -> str:
        '''
        
        Return:
            str: 
        '''
        return f"{Card.ranks[self._rank-1]} {Card.suits[self._suit-1]}"


class Deck:
    '''
    Initiates list comprehension by looping over suits with iterator of 4 and ranks with 13,
    appending each cardm combination into a list with wach instance being of class type Card.´

    Attributes:
        _cards (list): This is where the deck lies. It builds on the Card class.
    '''

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self._cards)

    def give(self) -> tuple:
        '''
        Takes a card from deck, stores and removes from the list '_cards'.

        Return:
            tuple: Item from deck in the form of 'Card(rank, suit)'.
        '''

        if len(self._cards) > 0:
            return self._cards.pop()


class Player:
    '''
    Sets up 
    
    Args:
        deck (list): Using list from Deck class.
        name (str): Child classes will set their own 'name'.
        start (int): 

    Attributes:
        _deck (list):
        _name (str): 
        _hand (list):
        _points (int):
        _aces (int):
        _start (int):
    '''
    def __init__(self, deck, name="User", start=1) -> None:
        self._deck = deck
        self._name = name
        self._hand = []
        self._points = 0
        self._aces = 0
        self._start = start

    def new_card(self) -> None:
        '''
        TBC
        
        Attributes:
            card (tuple):
            _hand (list):
            _points (int):
            _aces (int):
        '''
        card = self._deck.give()
        self._hand.append(card)

        if card.get_value() == 1:
            self._points += 14
            self._aces += 1
        else:
            self._points += card.get_value()
        if self._points > 22 and self._aces > 0:
            self._points -= 13
            self._aces -= 1
        
    def beginning(self) -> None:
        '''
        TBC

        Attributes:
            new_card (none):
        
        '''
        for _ in range(self._start):
            self.new_card()

    def cards(self) -> str:
        '''
        TBC

        Return:
            str: For displaying list of gathered cards as a string.
        '''
        return ", ".join(str(card) for card in self._hand)

    def write_out(self) -> None:
        '''
        TBC
        
        '''
        print(f"{self._name} har: {self.cards()} och poäng: {self._points}")


class User(Player):
    '''
    TBC

    Args:

    Attributes:
    
    '''
    def __init__(self, deck, name='Du', start=2) -> None:
        super().__init__(deck, name, start)
        self.beginning()
        self.write_out()

    def play(self) -> int:
        '''
        TBC
        
        Attributes:
            new_card (tuple):
            write_out (str):
        
        Return:
            int:
        '''

        while True:
            if self._points > 21: break
            self.new_card()
            self.write_out()
            if self._points > 21 or not play_on('Ett kort till? (hit/stand)'):
                break
        return self._points

class Computer(Player):
    '''
    TBC


    Args:
        deck (list):
        name (str):
        start (int):
    '''

    def __init__(self, deck, name='Datorn', start=1) -> None:
        super().__init__(deck, name, start)


def play_on(question) -> bool:
    '''
    TBC

    Attributes:
        string (str):

    Return:
        bool:
    '''
    string = str(input(question))

    if string.lower() == 'hit':
        return True
    elif string.lower() == 'stand':
        return False
    else:
        play_on(str(input('Skriv in "hit" för att ta fler kort eller "stand" för att stanna.')))


# Main()


"""
Ge spelare och dator två kort, visa 1 från datorn
Input, fler kort?
Ta ett kort
Lägg till i lista
Spara ess i lista
Om över 22 p kolla om några sparade ess och räkna ner
Datorn tar fler kort om < 17

"""
