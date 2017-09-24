from collections import Counter


class SudokuError(Exception):
    pass

HEADER = r"""\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline
"""

FOOTER = r'''\end{tabular}
\end{center}

\end{document}
'''

class Sudoku(object):
    def __init__(self, filename):
        self.filename = filename
        self.name = filename.replace(".txt", "")
        self.grids = []
        fp = open(filename, "r")
        lines = []
        for line in fp:
            line = line.strip()
            line = line.replace(" ", "")
            if line == "":
                continue
            if not line.isdigit():
                raise SudokuError("Incorrect Input")
            if len(line) != 9:
                raise SudokuError("Incorrect Input")
            if line != "":
                lines.append(line)
        if len(lines) != 9:
            raise SudokuError("Incorrect Input")
        for line in lines:
            arr = list(line)
            arr = [int(i) for i in arr]
            self.grids.append(arr)


    def preassess(self):
        """
        prints out to standard output whether the representation is correct 
        and has no digit that occurs twice on the same row, on the same column 
        or in the same box
        """
        # check rows
        for row in self.grids:
            row = [item for item in row if item != 0]
            if len(set(row)) != len(row):
                return "There is clearly no solution."
        # check columns
        for i in range(9):
            cols = []
            for j in range(9):
                cols.append(self.grids[j][i])
            cols = [item for item in cols if item != 0]
            if len(set(cols)) != len(cols):
                return "There is clearly no solution."
        # check boxes
        for i in range(3):
            for j in range(3):
                start_row = i*3
                start_col = j*3
                box  = []
                for m in range(3):
                    for n in range(3):
                        row = start_row + m
                        col = start_col + n
                        box.append(self.grids[row][col])
                box = [item for item in box if item != 0]
                if len(set(box)) != len(box):
                    return "There is clearly no solution."
        return "There might be a solution."

    def fill_digit(self, row):
        arr = []
        for elem in row:
            if elem == 0:
                arr.append(r"\N{}{}{}{}{} &")
            else:
                arr.append(r"\N{}{}{}{}{" + str(elem) + "} &")
        arr[-1] = arr[-1].replace("&", "\\\\ \hline")
        return arr

    def bare_tex_output(self):
        """
        outputs Latex code to a file, use these code to produce a pictorial 
        representation of the grid
        """
        output = HEADER
        for i in range(9):
            output += "% Line {}\n".format(i+1)
            arr = self.fill_digit(self.grids[i])
            output += " ".join(arr[:3]) + "\n"
            output += " ".join(arr[3:6]) + "\n"
            if i%3 == 2:
                output += " ".join(arr[6:9]) + "\\hline\n"
            else:
                output += " ".join(arr[6:9]) + "\n"
            if i != 8:
                output += "\n"

        output += FOOTER
        filename = self.name + "_bare1.tex"
        fp = open(filename, "w")
        fp.write(output)

    def counter(self):
        """count the occurence of digit in grids"""
        c = Counter()
        for row in self.grids:
            c.update(row)
        data = list(c.items())
        data = [item[0] for item in data if item[0]!=0]
        return data

    def get_box(self, start_row, start_col):
        """get the box by the position oof first digit in the box"""
        box  = []
        for m in range(3):
            for n in range(3):
                row = start_row + m
                col = start_col + n
                box.append(self.grids[row][col])
        return box

    def get_forced_cells(self):
        """Get the forced cells"""
        digits = self.counter()
        forced_cells = []
        for digit in digits:
            starts = []  # store the positon of the start elem in the box, the digit is not in the box
            for i in range(3):
                for j in range(3):
                    start_row = i*3
                    start_col = j*3
                    box = self.get_box(start_row, start_col)
                    if digit not in box:
                        starts.append((start_row, start_col))
            for start in starts:
                entry_cells = self.get_entry_cell(start[0], start[1], digit)
                if len(entry_cells) == 1:
                    forced_cells.append([entry_cells[0], digit])
        return forced_cells


    def get_entry_cell(self, start_row, start_col, digit):
        """Get the entry cell, if it's the only one ,return the entry position"""
        empty_cells = []  # store the empty cell position in the box 
        for i in range(3):
            row = start_row + i
            for j in range(3):
                col = start_col + j
                if self.grids[row][col] == 0:
                    empty_cells.append((row, col))
        positions = self.get_digit_position(digit)
        for position in positions:
            digit_row = position[0]
            digit_col = position[1]
            empty_cells = self.remove_cell(empty_cells, digit_row, digit_col)
        return empty_cells

    def remove_cell(self, cells, row, col):
        res = []
        for cell in cells:
            if cell[0] == row:
                pass
            elif cell[1] == col:
                pass
            else:
                res.append(cell)
        return res
                

    def get_digit_position(self, digit):
        positions = []
        for i in range(9):
            for j in range(9):
                if self.grids[i][j] == digit:
                    positions.append((i, j))
        return positions



    def forced_tex_ouptut(self):
        """
        outputs some Latex code to a file, use these code to produce a pictorial 
        representation of the grid to which the forced digits technique has been applied; 
        """
        forced_cells = self.get_forced_cells()
        while len(forced_cells) > 0:
            for cell, digit in forced_cells:
                self.grids[cell[0]][cell[1]] = digit
            forced_cells = self.get_forced_cells()
        output = HEADER
        for i in range(9):
            output += "% Line {}\n".format(i+1)
            arr = self.fill_digit(self.grids[i])
            output += " ".join(arr[:3]) + "\n"
            output += " ".join(arr[3:6]) + "\n"
            if i%3 == 2:
                output += " ".join(arr[6:9]) + "\\hline\n"
            else:
                output += " ".join(arr[6:9]) + "\n"
            if i != 8:
                output += "\n"

        output += FOOTER
        filename = self.name + "_forced1.tex"
        fp = open(filename, "w")
        fp.write(output)


    def marked_tex_output(self):
        """
        outputs some Latex code to a file, use these codes to to produce a pictorial 
        representation of the grid to which the forced digits technique has been applied 
        and that has been marked;
        """
        pass

    def worked_tex_output(self):
        """
        outputs some Latex code to a file, use these codes to produce a pictorial 
        representation of the grid to which the forced digits technique has been 
        applied, that has been marked, and to which the preemptive set technique 
        has been applied.
        """
        pass


Sudoku("./test/sudoku_5.txt").forced_tex_ouptut()