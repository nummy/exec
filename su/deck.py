import random
from card import Card


class Deck(object):

    def __init__(self, value_start, value_end, number_of_suits):
        """Initialize the deck"""
        self.cards = []  # Store all the cards in a list
        for i in range(value_start - 1, value_end):
            for j in range(number_of_suits):
                # create a  card
                card = Card(i, j)
                # append the card to the deck
                self.cards.append(card)

    def shuffle(self):
        """ Shuffle deck using shuffle method in random module. """
        random.shuffle(self.cards)

    def add_card(self, card):
        """Add a card to the deck"""
        if isinstance(card, Card):
            if not isIn(card):
                self.cards.append(card)

    def isIn(self, card):
        """If the card in the deck, return True, otherwise, return False """
        for c in self.cards:
            if c == card:
                return True
        return False


    def isEmpty( self ):
        """ Is The deck emprty? If empty, return True"""
        return len(self.cards) == 0

    def __len__( self ):
        """ Return the number of cards"""
        return len(self.cards)

    def __str__( self ):
        """ Return printable string representing deck"""
        return ", ".join([str(card) for card in self.cards])

    def draw(self, cols=13):
        """ display cols cards per row"""
        for index, card in enumerate(self.cards):
            if index%cols == 0:
                print()
            print("{:3s} ".format(str(card)), end="" )
        print()

    def deal(self):
        """ Return top card from deck"""
        if len(self.cards) == 0:
            # return None if no card in the deck
            return None
        else:
            return self.cards.pop()
