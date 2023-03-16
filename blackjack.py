'''
Skapa ett program som simulerar ett blackjack-spel mellan en spelare och en dator.

·         Spelet spelas med en vanlig kortlek som blandas innan varje runda.

·         Varje spelare får två kort i början av spelet. Datorn visar bara upp ett av sina kort.

·         Spelaren kan välja att ta fler kort (hit) eller stanna på sina nuvarande kort (stand).

·         Spelaren kan fortsätta att ta kort tills hen når 21 poäng eller över.

·         Om spelaren går över 21 poäng förlorar hen direkt.

·         När spelaren stannar, spelar datorn sin tur. Datorn måste ta kort så länge summan av korten är mindre än 17 poäng och stanna när datorns kortsumma är 17 poäng eller mer.

·         Om datorn går över 21 poäng vinner spelaren oavsett vilka kort spelaren har.

·         Om varken spelaren eller datorn går över 21 poäng så vinner den som har högst kortsumma.
'''

import random


class Card:
    '''
    Creates lists with ranks and suits and 
    param get_value: used later to count aces in Player class.
    '''
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "Hearts Spades Diamonds Clubs".split()

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_value(self):
        return self._rank

    def __str__(self) -> str:
        return f"{Card.ranks[self._rank-1]} {Card.suits[self._suit-1]}"


class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self._cards)

    def give(self):
        if len(self._cards) > 0:
            return self._cards.pop()


class Player:
    def __init__(self, deck, name='User'):
        self._deck = deck
        self._name = name
        self._hand = []
        self._points = 0
        self._aces = 0

    def new_card(self):
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
    
    def cards(self):
        return ', '.join(str(card) for card in self._hand)
    
    def write_out(self):
        print(f'{self._name} har: {self.cards()} och poäng: {self._points}')


class User(Player):
    pass

class Computer(Player):
    pass

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
