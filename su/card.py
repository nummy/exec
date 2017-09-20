class Card(object):
    # List to map int number to face character
    face_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # List to map int number to suit character
    suit_list = ['c','d', 'h', 's']

    def __init__(self, face=0, suit=0):
        """ Initialize card with face number and suit number"""
        self.card_face = face      # init card face
        self.card_suit = suit      # init card suit

    def get_face(self):
        """ Accessor for card face """
        return self.card_face

    def set_face(self, face):
        """ Mutator for card face """
        self.card_face = face

    def get_suit(self):
        """ Accesor for card face """
        return self.card_suit

    def set_suit(self, suit):
        """Mutator for card suit"""
        self.card_suit = suit

    def __str__(self):
        """convert card into a printable string"""
        return "%s%s" % (self.face_list[self.card_face], self.suit_list[self.card_suit])

    def __eq__(self, other):
        """If two cards are equal, return True, otherwise False"""
        if not isinstance(other, Card):
            # other is not a instance of the class Card
            return False
        if self.card_suit == other.get_suit() and self.card_face == other.get_face():
            # face and suit must be the same
            return True
        else:
            return False
