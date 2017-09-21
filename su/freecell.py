from card import Card
from deck import Deck


MENU = """
=======================================================
Commands:
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    H         Display the commands
    Q         Quit
=======================================================
"""


class NotFreecell(object):

    def __init__(self):
        """Initiate the game, The game has 4 cells , 4 foundations and 8 tableaus. In the begining, they are empty"""
        self.deck = Deck(1, 13, 4)   # store 52 cards
        self.deck.shuffle()
        self.cells = [[], [], [], [], []]   # list of 4 list
        self.foundations = [[], [], [], []]  # list of 4 list
        # All the cards are dealt from left to right(from tableaus 1 to 8), so in the end, there will have
        # 7 cards in tableaus 1 through 4, 6 cards in tableaus 5 through 8
        self.tableaus = [[], [], [], [], [], [], [], []]  # list of 8 list
        # deal the cards, initiate the tableaus
        for i in range(0, len(self.deck)):
            self.tableaus[i % 8].append(self.deck.deal())


    def valid_fnd_move(self, src_card, dest_card):
        """
        Is the movement to the foundation valid ?
        """
        if src_card is None:
            print("Invalid command: because of no card from the source") 
            return False
        if dest_card is None:
            if src_card.get_face() == 0:
                return True
            else:
                print("Invalid move: Source card is not an Ace")
                return False
        else:
            if src_card.get_suit() == dest_card.get_suit() and src_card.get_face() == dest_card.get_face()+1:
                return True
            else:
                print("Invalid command because of source card and destination card are not matching ") 
                return False


    def valid_tab_move(self, src_card, dest_card):
        """
        Is the tab move valid?
        """    
        if src_card is None:
            print("Invalid command: because of no card from the source") 
            return False
        if dest_card is None:
            return True
        else:
            if src_card.get_suit() == dest_card.get_suit():
                print("Invalid move: Wrong suit") 
                return False
            else:
                if src_card.get_face() != dest_card.get_face()-1:
                    print("Invalid move: Wrong face") 
                    return False
                return True

    def valid_cell_move(self, src_card, dest_card):
        """
        Is the cell move valid ?
        """    
        if dest_card is None:
            return True
        else:
            print("Invalid command: because of dest cell is not empty")
            return  False

    def tableau_to_cell(self, tab, cell):
        """
        move card from tableau to cell
        """
        if len(tab) == 0:
            src_card = None
        else:
            src_card = tab[-1]
        if len(cell) == 0:
            dest_card = None
        else:
            dest_card = cell[-1]
        if self.valid_cell_move(src_card, dest_card):
            tab.remove(src_card)
            cell.append(src_card)

    def tableau_to_foundation(self, tab, fnd):
        """
        move card from tableau to foundation
        """
        if len(tab) == 0:
            src_card = None
        else:
            src_card = tab[-1]
        if len(fnd) == 0:
            dest_card = None
        else:
            dest_card = fnd[-1]
        if self.valid_fnd_move(src_card, dest_card):
            tab.remove(src_card)
            fnd.append(src_card)

    def tableau_to_tableau(self, tab1, tab2):
        """
        move card from tableau to tableau
        """
        if len(tab1) == 0:
            src_card = None
        else:
            src_card = tab1[1]
        if len(tab2) == 0:
            dest_card = None
        else:
            dest_card = tab2[-1]
        if self.valid_tab_move(src_card, dest_card):
            tab1.remove(src_card)
            tab2.append(src_card)

    def cell_to_foundation(self, cell, fnd):
        """
        move card from cell to foundation
        """
        if len(cell) == 0:
            src_card = None
        else:
            src_card = cell[-1]
        if len(fnd) == 0:
            dest_card = None
        else:
            dest_card = fnd[-1]
        if self.valid_fnd_move(src_card, dest_card):
            cell.remove(src_card)
            fnd.append(src_card)

    def cell_to_tableau(self, cell, tab):
        """
        Add your function header here.
        """
        if len(cell) == 0:
            src_card = None   # source card
        else:
            src_card = cell[-1]
        if len(tab) == 0:
            dest_card = None   # destination card
        else:
            dest_card = tab[-1]
        print(src_card)
        print(dest_card)
        if self.valid_tab_move(src_card, dest_card):
            cell.remove(src_card)
            tab.append(dest_card)

    def is_winner(self):
        """
        Decide if player win the game?
        """ 
        win = True   # win flag
        for foundation in self.foundations:
            if len(foundation) != 13 or foundation[-1].get_face() != 12:
                win = False
                break
        return win

    def parse_command(self, command):
        """parse the command, get choice, source and destination"""
        choices = ["TF", "TC", "TT", "CF", "CT"]
        arr = command.strip().split()  # parse string to arr
        x = 0 # store source position
        y = 0 # store destination position
        choice = "" # store choice
        if len(arr) == 3:
            # handle exception
            if arr[0].upper() not in choices or not arr[1].isdigit() or not arr[2].isdigit():
                print("Arguments are wrong, Please input again")
                choice = None
            else:
                choice = arr[0].upper()
                x = int(arr[1])
                y = int(arr[2])
        else:
            choice = None
            print("Invalid Command: lack of arguments")
        return choice, x, y

    def move(self, choice, x, y):
        """move card"""
        if choice == "TC":
            # move card from tableau to cell
            tab = self.tableaus[x]   # source position from tableaus
            cell = self.cells[y]     # destination position from cells
            self.tableau_to_cell(tab, cell)  # move card from source to destination
            return
        if choice == "TF":
            # move card from tableau to foundation
            tab = self.tableaus[x]       # source position frmo tableaus
            fnd = self.foundations[y]    # destination in the foundations
            self.tableau_to_foundation(tab, fnd) # move card from source to destination
            return
        if choice == "TT":
            # move card from tableau to tableau
            tab1 = self.tableaus[x]      # source position from tableaus
            tab2 = self.tableaus[y]      # destination position in the tableaus
            self.tableau_to_tableau(tab1, tab2)  # move card from source to destination
            return
        if choice == "CF":
            # move card from cell to foundation
            cell = self.cells[x]        # source position in cells
            fnd = self.foundations[y]   # destination position in the foundations
            self.cell_to_foundation(cell, fnd)   # move card from source to destination
            return
        if choice == "CT":
            # move card from cell to tableau
            cell = self.cells[x]       # source position in cells
            tab = self.tableaus[y]     # destination position in foundations
            self.cell_to_tableau(cell, tab)  # movoe card from source to destination
            return

    def display(self):
        """
        display the game board
        """
        # Labels for cells and foundations
        print("=======Cells========  ====Foundations=====")
        print("---1----2----3----4--  --1----2----3----4--")
        print(" ", end="")
        cells = []  # store 4 cell characters
        for cell in self.cells:
            if len(cell) == 0:
                cells.append("")
            else:
                cells.append(str(cell[-1]))
        foundations = [] # store 4 foundation characters
        for foundation in self.foundations:
            if len(foundation) == 0:
                foundations.append("")
            else:
                foundations.append(str(foundation[-1]))
        # lable for cells and foundations
        label = "[{0[0]:>3}][{0[1]:>3}][{0[2]:>3}][{0[3]:>3}]  [{1[0]:>3}][{1[1]:>3}][{1[2]:>3}][{1[3]:>3}]".format(
            cells, foundations)
        print(label)
        # Labels for tableaus
        print("=================tableaus=================")
        print("---1----2----3----4----5----6----7----8---")
        height = 0
        for item in self.tableaus:
            if height < len(item):
                height = len(item)
        for i in range(0, height):
            items = []
            for j in range(0, 8):
                try:
                    data = str(self.tableaus[j][i])
                except IndexError as e:
                    data = ""
                items.append(data)
            label = "{0[0]:>5}{0[1]:>5}{0[2]:>5}{0[3]:>5}{0[4]:>5}{0[5]:>5}{0[6]:>5}{0[7]:>5}".format(items)
            print(label)


    def start(self):
        # start the game
        self.display()
        print(MENU)
        command = input("Please input the command: ").strip().lower()
        while command != 'q':
            if command != "h":
                choice, x, y = self.parse_command(command)
                if choice is None:
                    print("Please Try again.\n")
                else:
                    self.move(choice, x-1, y-1)
                    if self.is_winner():
                        print("You won!")
                        break
                self.display()
            else:
                print(MENU)
                self.display()
            command = input("Please input the command: ").strip().lower()

NotFreecell().start()
