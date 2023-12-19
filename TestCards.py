from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):

#Test cases specific to the Card class
    def test_init(self):
        '''
        tests if the init function is properly implementing the values and suits 
        '''
        self.assertEqual('Card(5 of Clubs)', str(Card(5, 'Clubs')))

    def test_repr(self):
        '''
        tests if the repr function properly returns the value and suit in a string representation
        '''
        x = Card(5, 'Clubs')
        self.assertEqual('Card(5 of Clubs)', str(x))

    def test_eq(self):
        '''
        tests if the eq function properly compares cards to make sure they are equal
        '''
        self.assertTrue(Card(3, 'Clubs') == Card(3, 'Clubs'))
        self.assertFalse(Card(3, 'Clubs') == Card(5, 'Diamonds'))

    def test_lt(self):
        '''
        tests if the __lt__ function is returning true or false when it should
        '''
        self.assertTrue('Clubs' < 'Diamonds')
        self.assertFalse(10 < 5)
    

class TestDeck(unittest.TestCase):
#Test cases specific to the Deck class
    def test_init(self):
        '''
        tests if the decks init function defaults to a set of 52 cards with unique pairings 
        '''
        deck = Deck([5, 6], ['apples', 'points'])
        self.assertEqual(repr(deck), '[Card(5 of apples), Card(6 of apples), Card(5 of points), Card(6 of points)]')

    def test_len(self):
        '''
        tests the len function is returning proper length of the deck (52)
        '''
        deck = Deck()
        self.assertEqual(Deck.__len__(deck), 52)

    def test_repr(self):
        '''
        tests if repr function properly returns the value and suit in a string representation
        '''
        deck = Deck([5, 6], ['Clubs', 'Spades'])
        self.assertEqual(repr(deck), '[Card(5 of Clubs), Card(6 of Clubs), Card(5 of Spades), Card(6 of Spades)]')

    def test_sort(self):
        '''
        tests if the sort function is sorting the deck by ascending order,
        since you don't need to sort when initializing a deck I just tested the order
        of the initial deck
        '''
        deck = Deck([5, 6], ['apples', 'points'])
        self.assertEqual(repr(deck), '[Card(5 of apples), Card(6 of apples), Card(5 of points), Card(6 of points)]')
        
    def test_shuffle(self):
        '''
        tests the shuffle function to make sure it properly shuffles the deck
        '''
        deck = Deck([3, 9], ['Clubs', 'Spades'])
        self.assertFalse(Deck.shuffle(deck) == '[Card(3 of Clubs), Card(9 of Clubs), Card(3 of Spades), Card(9 of Spades)]')

    def test_draw_top(self):
        '''
        tests draw_top function to make sure it is removing and returning top card of the deck
        '''
        deck = Deck([5, 6], ['apples', 'points'])
        deck2 = Deck()
        deck3 = Deck([], [])
        self.assertEqual(str(Deck.draw_top(deck)), 'Card(6 of points)')
        self.assertEqual(str(Deck.draw_top(deck2)), 'Card(13 of Spades)')
        self.assertRaises(RuntimeError, Deck.draw_top(deck3)) 

class TestHand(unittest.TestCase):
#Test cases specific to the Hand class
    def test_init(self):
        '''
        tests that the init function passes in a collection of cards
        '''
        hand1 = Hand([Card(value, 'clubs') for value in range(3, 0, -1)])
        self.assertEqual(str(Hand.__repr__(hand1)), "['Card(3 of clubs)', 'Card(2 of clubs)', 'Card(1 of clubs)']")

    def test_repr(self):
        '''
        tests the repr function to make sure it returns a string representation
        of the hand
        '''
        h_clubs = Hand([Card(value, 'clubs') for value in range(3, 0, -1)])
        self.assertEqual(str(Hand.__repr__(h_clubs)), "['Card(3 of clubs)', 'Card(2 of clubs)', 'Card(1 of clubs)']")

    def test_play(self):
        '''
        tests that the play function removes and returns card from hand
        and raises runtime error if the card is not in hand
        '''
        hand = Hand([Card(value, 'clubs') for value in range(3, 0, -1)])
        self.assertEqual(str(hand.play(Card(1, 'Clubs'))), 'Card(1, Clubs')
        self.assertRaises(RuntimeError, (hand.play(Card(10, 'Hearts'))))
        
if __name__ == '__main__':
    unittest.main() # Runs all tests above
