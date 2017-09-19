from card import Card
from deck import Deck


class NotFreecell(object):

    def __init__(self):
        """Initiate the game, The game has 4 cells , 4 foundations and 8 tableaus. In the begining, they are empty"""
        self.deck = Deck(1,13,4)   # store 52 cards
        self.deck.shuffle()
        self.cells = [[], [], [], [], []]   # list of 4 list
        self.foundations = [[], [], [], []] # list of 4 list 
        # All the cards are dealt from left to right(from tableaus 1 to 8), so in the end, there will have 
        # 7 cards in tableaus 1 through 4, 6 cards in tableaus 5 through 8 
        self.tableaus = [[], [], [], [], [], [], [], []] # list of 8 list
        # deal the cards, initiate the tableaus
        for i in range(0, len(self.deck)):
            self.tableaus[i%8].append(self.deck.deal())

    def display(self):
        """
        display the game board
        """
        #Labels for cells and foundations
        print("    =======Cells========  ====Foundations=====")
        print("    --1----2----3----4--  --1----2----3----4--")
        print("    ", end="")
        temp_cells = []
        for cell in self.cells:
            if len(cell) == 0:
                temp_cells.append("")
            else:
                temp_cells.append(str(cell[-1]))
        temp_foundations = []
        for foundation in self.foundations:
            if len(foundation) == 0:
                temp_foundations.append("")
            else:
                temp_foundations.append(str(foundation[-1]))
        # to print a card using formatting, convert it to string:
        label1 = "[{0[0]:>3}][{0[1]:>3}][{0[2]:>3}][{0[3]:>3}]  [{1[0]:>3}][{1[1]:>3}][{1[2]:>3}][{1[3]:>3}]".format(temp_cells, temp_foundations)
        print(label1)
        #Labels for tableaus
        print("    =================Tableaus=================")
        print("    ---1----2----3----4----5----6----7----8---")
        max_length = max([len(item) for item in self.tableaus])
        for i in range(0, max_length):
            items = []
            for j in range(0, 8):
                try:
                    data = str(self.tableaus[j][i])
                except IndexError as e:
                    data = ""
                items.append(data)
            label = "    {0[0]:>5}{0[1]:>5}{0[2]:>5}{0[3]:>5}{0[4]:>5}{0[5]:>5}{0[6]:>5}{0[7]:>5}".format(items)
            print(label)

NotFreecell().display()
