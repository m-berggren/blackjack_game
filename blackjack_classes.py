import random


class Card:
    ''' Sets up lists and dictionaries to look up and return card values and suits.'''

    ranks = 'Ess 2 3 4 5 6 7 8 9 10 Knekt Dam Kung'.split()
    suits = 'Hjärter Spader Ruter Klöver'.split()

    values_dict = {'1': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, '11': 10, '12': 10, '13': 10}

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def get_value(self) -> int:
        ''' Get rank value from values_dict as aces counts as 11,
        and all pictured cards valued 10.
        '''

        rank_value = str(self._rank)
        return Card.values_dict[rank_value]
    
    def __str__(self) -> str:
        
        # Uses 'Card.' over 'self.' as this class is called through other classes.
        return f'{Card.suits[self._suit - 1]} {Card.ranks[self._rank - 1]}'


class Deck():
    ''' Creates a shuffled list of 4*13 tuples through Card class.'''

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in range(1, 5)
                                        for rank in range(1, 14)]
        random.shuffle(self._cards)

    def give_card(self) -> tuple:
        ''' Gets the first iteration and removes it from list of _cards.'''

        if self._cards:
            return self._cards.pop()
        


class Player():
    ''' Creates 'Player' class for each participant to store values, print result and
    operates on 'Deck'- and 'Card' class.
    '''
    
    def __init__(self, deck, name):
        self._deck = deck
        self._name = name
        self._hand = []
        self._points = 0
        self._aces = 0

    def cards(self) -> str:
        ''' Concatenates cards stored on hand from list to string.'''
        
        return ', '.join(str(card) for card in self._hand)
    
    def new_card(self) -> None:
        ''' Utilizes 'Deck'- and 'Card' classes and
        checks if ace should be 11 or 1 points.'''

        card = self._deck.give_card()
        self._hand.append(card)

        if card.get_value() == 11:
            self._aces += 1
        
        self._points += card.get_value()

        if self._points > 21 and self._aces > 0:
            self._points -= 10  # Counts ace as 1 instaed of 11.
            self._aces -= 1

    def write_out(self) -> None:
        print(f'{self._name} har: {self.cards()} och poäng: {self._points}.')


class User(Player):
    ''' Expands on 'Player' class. The game's main loop runs.'''

    def __init__(self, deck, name='Du'):
        super().__init__(deck, name)
        self.beginning()
    
    def beginning(self):
        ''' Two cards are dealt and shown in the beginning for user.'''

        self.new_card()
        self.new_card()
        self.write_out()

    def play(self) -> int:
        ''' Runs until points either >= 21 or user decides to 'stand'.'''

        while True:
            if self._points >= 21 or not play_on():
                break

            self.new_card()
            self.write_out()
        return self._points


class Computer(Player):
    ''' Runs after 'User' class until points from 'Play' method are over 16.'''

    def __init__(self, deck, name="Datorn"):
        super().__init__(deck, name)
        self.beginning()
    
    def beginning(self):
        ''' Two cards are dealt but only one is shown in the beginning.'''

        self.new_card()
        self.write_out()
        self.new_card()

    def play(self) -> int:
        ''' Runs while points are equal or less than 16.'''

        while self._points <= 16:
            self.new_card()
        self.write_out()
        return self._points

def play_on():
    ''' Choice for user to stay or take another card.
    Runs until 'hit' or 'stand' is typed.
    '''

    choice = '\nSkriv "hit" för att ta fler kort eller "stand" för att stanna: \n'
    string = str(input(choice))
    
    if string.lower() == "hit":
        print()
        return True
    elif string.lower() == "stand":
        print()
        return False
    else:
        play_on()