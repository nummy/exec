class Card(object):
    # face is an int (0-12), where aces are 0 and kings are 12.
    # Suit is an int (0-3), where clubs are 0 and spades are 3.
    # List to map int rank to printable character
    face_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # List to map int suit to printable character (index 0 used for no suit)
    # 0 is clubs, 2 is diamond, 3 is hearts, 4 is spades
    suit_list = ['c','d', 'h', 's']

    def __init__(self, face=0, suit=0):
        """ Initialize card to specified face (0-12) and suit (0-3). """
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

    def __str__(self):
        """convert card into a printable string"""
        return "{}{}".format(self.face_list[self.card_face], self.suit_list[self.card_suit])

    def __repr__(self):
        """ Convert card into a string for use in the shell. """
        return self.__str__()

    def __eq__(self, other):
        """ Return True, if Cards of equal rank and suit; False, otherwise. """
        if not instance(other, Card):
            return False
        if self.card_suit == other.get_suit() and self.card_face == other.get_face():
            return True
        else:
            return False
