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



    def forced_tex_ouptut(self):
        """
        outputs some Latex code to a file, use these code to produce a pictorial 
        representation of the grid to which the forced digits technique has been applied; 
        """
        pass

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


Sudoku("./test/sudoku_4.txt").bare_tex_output()