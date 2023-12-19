import random

class object:
    def __init__(self, value, suit):
        '''
        initializes card value and suit
        '''
        self.value = value
        self.suit = suit
        
class Card(object):
    def __init__(self, value, suit):
        '''
        inherits value and suit from superclass object
        '''
        super().__init__(value, suit)

    def __repr__(self):
        '''
        returns the card value and name as a string representation
        '''
        return f'Card({self.value} of {self.suit})'

    def __eq__(self, other):
        '''
        returns true or false based off of if two cards are equal to each other
        '''
        if (self.suit == other.suit) and (self.value == other.value):
            return True
        else:
            return False

    def __lt__(self, other):
        '''
        returns the lesser card; using the cards suit (alphabetical a<z) 
        then value to determine true or false
        '''
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.value < other.value

class Deck(object):
    def __init__(self, value = range(1, 14), suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']):
        '''
        initializes a deck for each value/suit combination by putting each combination
        in a list self.deck, with default parameters of 1-13 and Clubs - Spades
        '''
        super().__init__(value, suit)
        self.deck = []                      #self.deck is my variable for card_list
        for value in self.suit:
            for suit in self.value:
                self.deck.append(Card(suit, value))

    def __len__(self):
        '''
        returns number of cards in deck
        '''
        return len(self.deck)

    def sort(self):
        '''
        sorts the cards in ascending order
        '''
        return self.deck.sort()

    def __repr__(self):
        '''
        returns string representation of the deck
        '''
        return str(self.deck)

    def shuffle(self):
        '''
        shuffles the deck
        '''
        random.shuffle(self.deck)

    def draw_top(self, i=-1):
        '''
        removes and returns the top card of the deck, the last item
        is treated as the 'top' of the deck. Raises a runtime error
        if someone tries to draw from empty deck
        '''
        if len(self.deck) > 0:
            return self.deck.pop(i)
        else:
            raise RuntimeError('Cannot draw from empty deck')

class Hand(Deck):
    def __init__(self, cards):
        '''
        initializes a hand with a passed collection of cards
        '''
        self.deck = []         #self.hand is my variable for card_list
        for card in cards:
            self.deck.append(card)

    def __repr__(self):
        '''
        returns string representation of hand 
        '''
        return [str(card) for card in self.deck]

    def play(self, card):
        '''
        returns the selected card while removing it from hand
        simulates playing a card
        '''
        if card in self.deck:
            self.deck.remove(card)
            return card
        else:
            raise RuntimeError('Tried to play a card that is not in hand')
