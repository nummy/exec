import re
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
    H         Display this menu of commands
    Q         Quit the game
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
        Is the foundation move valid?
        """
        if src_card is None:
            raise RuntimeError("Error: invalid command because of no card from the source") 
        if dest_card is None:
            if src_card.get_face() == 1:
                pass
            else:
                raise RuntimeError("Invalid move: Source card is not an Ace") 
        else:
            if src_card.suit() == dest_card.get_suit() and src_card.get_face() == dest_card.get_face()+1:
                pass
            else:
                raise RuntimeError("Error: invalid command because of source card and destination card are not matching ") 


    def valid_tab_move(self, src_card, dest_card):
        """
        Is the tab move valid?
        """    
        if src_card is None:
            raise RuntimeError("Error: invalid command because of no card from the source") 
        if dest_card is None:
            pass
        else:
            if src_card.get_suit() == dest_card.get_suit():
                raise RuntimeError("Invalid move: Wrong suit") 
            else:
                if src_card.get_face() != dest_card.get_face()-1:
                    raise RuntimeError("Invalid move: Wrong face") 

    def valid_cell_move(self, src_card, dest_card):
        """
        Is the cell move valid ?
        """    
        if dest_card is None:
            pass
        else:
            raise RuntimeError("Error: invalid command because of dest cell is not empty")   

    def tableau_to_cell(self, tab, cell):
        """
        move card from tableau to cell
        """    
        temp_tab = None if len(tab)==0 else tab[-1]
        temp_cell = None if len(cell)==0  else cell[-1]
        self.valid_cell_move(temp_tab, temp_cell)
        tab.remove(temp_tab)
        cell.append(temp_tab)

    def tableau_to_foundation(self, tab, fnd):
        """
        move card from tableau to foundation
        """    
        temp_tab = None if len(tab)==0 else tab[-1]
        temp_fnd = None if len(fnd)==0  else fnd[-1]
        self.valid_fnd_move(temp_tab, temp_fnd)
        tab.remove(temp_tab)
        fnd.append(temp_tab)

    def tableau_to_tableau(self, tab1, tab2):
        """
        move card from tableau to tableau
        """    
        temp_tab1 = None if len(tab1)==0 else tab1[-1]
        temp_tab2 = None if len(tab2)==0  else tab2[-1]
        self.valid_tab_move(temp_tab1, temp_tab2)
        tab1.remove(temp_tab1)
        tab2.append(temp_tab1)

    def cell_to_foundation(self, cell, fnd):
        """
        move card from cell to foundation
        """    
        temp_cell = None if len(cell)==0 else cell[-1]
        temp_fnd = None if len(fnd)==0  else fnd[-1]
        self.valid_fnd_move(temp_cell, temp_fnd)
        cell.remove(temp_cell)
        fnd.append(temp_cell)

    def cell_to_tableau(self, cell, tab):
        """
        Add your function header here.
        """    
        temp_cell = None if len(cell)==0 else cell[-1]
        temp_tab = None if len(tab)==0  else tab[-1]
        self.valid_tab_move(temp_cell, temp_tab)
        cell.remove(temp_cell)
        tab.append(temp_cell)

    def is_winner(self):
        """
        Is player win the game?
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
        arr = re.split(r"\s+", command.strip())  # parse string to arr
        x = 0 # store source position
        y = 0 # store destination position
        choice = "" # store choice
        if len(arr) == 3:
            # handle exception
            if arr[0].upper() not in choices or not isinstance(x, int) or not isinstance(y, int):
                raise RuntimeError("Arguments are wrong, Please input again")
            else:
                choice = arr[0].upper()
                x = int(arr[1])
                y = int(arr[2])
        else:
            raise RuntimeError("Command can't been parsed")
        return choice, x, y

    def move(self, choice, x, y):
        """move card"""
        if choice == "TC":
            tab = self.tableaus[x]   # source position from tableaus
            cell = self.cells[y]     # destination position from cells
            selff.tableau_to_cell(tab, cell)  # move card from source to destination
            return
        if choice == "TF":
            tab = self.tableaus[x]       # source position frmo tableaus
            fnd = self.foundations[y]    # destination in the foundations
            self.tableau_to_foundation(tab, fnd) # move card from source to destination
            return
        if choice == "TT":
            tab1 = self.tableaus[x]      # source position from tableaus
            tab2 = self.tableaus[y]      # destination position in the tableaus
            self.tableau_to_tableau(tab1, tab2)  # move card from source to destination
            return
        if choice == "CF":
            cell = self.cells[x]        # source position in cells
            fnd = self.foundations[y]   # destination position in the foundations
            self.cell_to_foundation(cell, fnd)   # move card from source to destination
            return
        if choice == "CT":
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
        label1 = "[{0[0]:>3}][{0[1]:>3}][{0[2]:>3}][{0[3]:>3}]  [{1[0]:>3}][{1[1]:>3}][{1[2]:>3}][{1[3]:>3}]".format(
            temp_cells, temp_foundations)
        print(label1)
        # Labels for tableaus
        print("=================tableaus=================")
        print("---1----2----3----4----5----6----7----8---")
        max_length = max([len(item) for item in self.tableaus])
        for i in range(0, max_length):
            items = []
            for j in range(0, 8):
                try:
                    data = str(self.tableaus[j][i])
                except IndexError as e:
                    data = ""
                items.append(data)
            label = "{0[0]:>5}{0[1]:>5}{0[2]:>5}{0[3]:>5}{0[4]:>5}{0[5]:>5}{0[6]:>5}{0[7]:>5}".format(
                items)
            print(label)


    def start(self):
        #HERE IS THE MAIN BODY OF OUR CODE
        self.display()
        print(MENU)
        command = input("prompt: ").strip().lower()
        while command != 'q':
            if command == "h":
                print(MENU)
                self.display()
                command = input("prompt: ").strip().lower()
            else:
                try:
                    choice, x, y = self.parse_command(command)
                    self.move(choice, x-1, y-1)
                    if self.is_winner():
                        print("You won the game!")
                        break
                # Catch Any RuntimeError
                except RuntimeError as error_message:
                    print("{:s}".format(str(error_message)))
                    print("Try again.\n")
                self.display()
                command = input("prompt: ").strip().lower()

NotFreecell().start()
