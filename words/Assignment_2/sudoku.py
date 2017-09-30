from collections import Counter
import copy


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
        self.num = 0
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
                start_row = i * 3
                start_col = j * 3
                box = []
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
        """Fill digit in for tex output"""
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
            output += "% Line {}\n".format(i + 1)
            arr = self.fill_digit(self.grids[i])
            output += " ".join(arr[:3]) + "\n"
            output += " ".join(arr[3:6]) + "\n"
            if i % 3 == 2:
                output += " ".join(arr[6:9]) + "\\hline\n"
            else:
                output += " ".join(arr[6:9]) + "\n"
            if i != 8:
                output += "\n"

        output += FOOTER
        filename = self.name + "_bare1.tex"
        fp = open(filename, "w")
        fp.write(output)

    def counter(self, grids):
        """count the occurence of digit in grids"""
        c = Counter()
        for row in grids:
            c.update(row)
        data = list(c.items())
        data = [item[0] for item in data if item[0] != 0]
        return data

    def get_box(self, grids, start_row, start_col):
        """get the box by the position oof first digit in the box"""
        box = []
        for m in range(3):
            row = start_row + m
            for n in range(3):
                col = start_col + n
                box.append(grids[row][col])
        return box

    def get_box_with_position(self, grids, start_row, start_col):
        """get the box by the position oof first digit in the box"""
        box = []
        for m in range(3):
            row = start_row + m
            for n in range(3):
                col = start_col + n
                box.append((grids[row][col], (row, col)))
        return box

    def get_forced_cells(self, grids):
        """Get the forced cells"""
        digits = self.counter(grids)
        forced_cells = []
        for digit in digits:
            starts = []  # store the positon of the start elem in the box, the digit is not in the box
            for i in range(3):
                for j in range(3):
                    start_row = i * 3
                    start_col = j * 3
                    box = self.get_box(grids, start_row, start_col)
                    if digit not in box:
                        starts.append((start_row, start_col))
            for start in starts:
                entry_cells = self.get_entry_cell(
                    grids, start[0], start[1], digit)
                if len(entry_cells) == 1:
                    forced_cells.append([entry_cells[0], digit])
        return forced_cells

    def get_empty_cells(self, grids, start_row, start_col):
        """Get the empty cells for the box"""
        empty_cells = []  # store the empty cell position in the box
        for i in range(3):
            row = start_row + i
            for j in range(3):
                col = start_col + j
                if grids[row][col] == 0:
                    empty_cells.append((row, col))
        return empty_cells

    def get_entry_cell(self, grids, start_row, start_col, digit):
        """Get the entry cell, if it's the only one ,return the entry position"""
        empty_cells = self.get_empty_cells(grids, start_row, start_col)
        positions = self.get_digit_position(grids, digit)
        for position in positions:
            digit_row = position[0]
            digit_col = position[1]
            empty_cells = self.remove_cell(empty_cells, digit_row, digit_col)
        return empty_cells

    def remove_cell(self, cells, row, col):
        """Remove empty cell if conflicted"""
        res = []
        for cell in cells:
            if cell[0] == row:
                pass
            elif cell[1] == col:
                pass
            else:
                res.append(cell)
        return res

    def get_digit_position(self, grids, digit):
        """Get the positions of the digits in cells"""
        positions = []
        for i in range(9):
            for j in range(9):
                if grids[i][j] == digit:
                    positions.append((i, j))
        return positions

    def fill_forced_cells(self, raw_grids):
        grids = copy.deepcopy(raw_grids)
        forced_cells = self.get_forced_cells(grids)
        while len(forced_cells) > 0:
            for cell, digit in forced_cells:
                grids[cell[0]][cell[1]] = digit
                self.num += 1
            forced_cells = self.get_forced_cells(grids)
        return grids

    def forced_tex_ouptut(self):
        """
        outputs some Latex code to a file, use these code to produce a pictorial 
        representation of the grid to which the forced digits technique has been applied; 
        """
        grids = self.fill_forced_cells(self.grids)
        output = HEADER
        for i in range(9):
            output += "% Line {}\n".format(i + 1)
            arr = self.fill_digit(grids[i])
            output += " ".join(arr[:3]) + "\n"
            output += " ".join(arr[3:6]) + "\n"
            if i % 3 == 2:
                output += " ".join(arr[6:9]) + "\\hline\n"
            else:
                output += " ".join(arr[6:9]) + "\n"
            if i != 8:
                output += "\n"

        output += FOOTER
        filename = self.name + "_forced1.tex"
        fp = open(filename, "w")
        fp.write(output)

    def get_marked_digits(self, grids, row, col):
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        box = self.get_box(grids, start_row, start_col)
        box_set = set()
        for item in box:
            if item != 0:
                box_set.add(item)
        row_set = set()
        for item in grids[row]:
            if item != 0:
                row_set.add(item)
        col_set = set()
        for i in range(9):
            col_set.add(grids[i][col])
        return set(range(1, 10)) - box_set - row_set - col_set

    def fill_marked_digit(self, row):
        """Fill digit in for tex output"""
        arr = []
        for elem in row:
            if isinstance(elem, set):
                LT, RT, LB, RB = self.seperate_digits(elem)
                arr.append(r"\N{%s}{%s}{%s}{%s}{} &" % (LT, RT, LB, RB))
            else:
                arr.append(r"\N{}{}{}{}{" + str(elem) + "} &")
        arr[-1] = arr[-1].replace("&", "\\\\ \hline")
        return arr

    def seperate_digits(self, digits):
        LT = []
        RT = []
        LB = []
        RB = []
        digits = list(digits)
        digits.sort()
        for digit in digits:
            if digit < 3:
                LT.append(str(digit))
            elif digit < 5:
                RT.append(str(digit))
            elif digit < 7:
                LB.append(str(digit))
            else:
                RB.append(str(digit))
        return " ".join(LT), " ".join(RT), " ".join(LB), " ".join(RB)

    def markup_grids(self, grids):
        marked_grids = []
        for i in range(9):
            marked_grids.append([])
            for j in range(9):
                digit = grids[i][j]
                if digit == 0:
                    marked_digits = self.get_marked_digits(grids, i, j)
                    marked_grids[i].append(marked_digits)
                else:
                    marked_grids[i].append(digit)
        return marked_grids


    def marked_tex_output(self):
        """
        outputs some Latex code to a file, use these codes to to produce a pictorial 
        representation of the grid to which the forced digits technique has been applied 
        and that has been marked;
        """
        grids = self.fill_forced_cells(self.grids)
        marked_grids = self.markup_grids(grids)
        output = HEADER
        for i in range(9):
            output += "% Line {}\n".format(i + 1)
            arr = self.fill_marked_digit(marked_grids[i])
            output += " ".join(arr[:3]) + "\n"
            output += " ".join(arr[3:6]) + "\n"
            if i % 3 == 2:
                output += " ".join(arr[6:9]) + "\\hline\n"
            else:
                output += " ".join(arr[6:9]) + "\n"
            if i != 8:
                output += "\n"
        output += FOOTER
        filename = self.name + "_marked1.tex"
        fp = open(filename, "w")
        fp.write(output)

    def workout(self, grids, marked_grids, cancel_box):
        """
        outputs some Latex code to a file, use these codes to produce a pictorial 
        representation of the grid to which the forced digits technique has been 
        applied, that has been marked, and to which the preemptive set technique 
        has been applied.
        """
       
        visited = []
        
        sets, position = self.get_preemptive_sets(visited, marked_grids)
        while sets:
            self.cross_out(grids, marked_grids, sets, position, cancel_box)
            forced_cells = self.get_forced_cells(grids)
            while len(forced_cells) > 0:
                for cell, digit in forced_cells:
                    grids[cell[0]][cell[1]] = digit
                    marked_grids[cell[0]][cell[1]] = digit
                    self.num += 1
                    #print("#1 forced fill: digit=%s, counter=%s, positon=(%s, %s)" %(digit, self.num, cell[0] +1, cell[1]+1))
                    self.cross_out_by_digit(
                        grids, marked_grids, digit, cell[0], cell[1], cancel_box)
                forced_cells = self.get_forced_cells(grids)
            visited.append(sets)
            sets, position = self.get_preemptive_sets(visited, marked_grids)
        self.pretty_print(grids)
        return grids

    def worked_tex_output(self):
        cancel_box = self.init_cancel_box()
        grids = self.fill_forced_cells(self.grids)
        marked_grids = self.markup_grids(grids)
        worked_grids = self.workout(grids, marked_grids, cancel_box)
        print(cancel_box)
        print(self.isValid(worked_grids))

    def init_cancel_box(self):
        res = []
        for i in range(9):
            res.append([])
            for j in range(9):
                res[i].append([])
        return res


    def pretty_print(self, grids):
        for row in grids:
            print(row)
        print()

    def cross_out(self, grids, marked_grids,  preemptive_set, position, cancel_box):
        digits = preemptive_set[0]
        boxes = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                 {1, 2}, {2, 3}, {1, 3},
                 {4, 5}, {5, 6}, {4, 6},
                 {7, 8}, {8, 9}, {7, 9}]
        marks = preemptive_set[0]
        pos = preemptive_set[1]
        if position[0] == "R":
            row_index = position[1]
            self.cross_out_row(grids, marked_grids, row_index, digits, pos, cancel_box)
            if len(marks) <= 3:
                columns = set()
                for p in pos:
                    columns.add(p[1])  # get column index
                if columns in boxes:
                    # they are in the same box, cross out other digit in the
                    start_row = (row_index//3)*3
                    start_col = (list(columns)[0]//3)*3
                    self.cross_out_box(grids, marked_grids, start_row, start_col, digits, pos, cancel_box)

        elif position[0] == "C":
            col_index = position[1]
            self.cross_out_col(grids, marked_grids, col_index, digits, pos, cancel_box)
            if len(marks) <= 3:
                # in the same box
                rows = set()
                for p in pos:
                    rows.add(p[0])
                if rows in boxes:
                    start_row = (list(rows)[0]//3)*3
                    start_col = (col_index//3)*3
                    self.cross_out_box(grids, marked_grids, start_row, start_col, digits, pos, cancel_box)
        else:
            start_row = position[1]
            start_col = position[2]
            self.cross_out_box(grids, marked_grids, start_row, start_col, digits, pos, cancel_box)
            if len(marks) <= 3:
                # check if they are in the same row or coolumn
                # check if the are in the same row
                rows = set()
                cols = set()
                for p in pos:
                    rows.add(p[0])
                    cols.add(p[1])
                if len(rows) == 1:
                    # in the same row
                    #pass
                    self.cross_out_row(grids, marked_grids, rows.pop(), digits, pos, cancel_box)
                if len(cols) == 1:
                    # in the same col
                    #pass
                    self.cross_out_col(grids, marked_grids, cols.pop(), digits, pos, cancel_box)

    def cross_out_col(self, grids, marked_grids, col_index, digits, pos_lst, cancel_box):
        for i in range(9):
            marked_cell = marked_grids[i][col_index]
            position = (i, col_index)
            if isinstance(marked_cell, set) and position not in pos_lst:
                cancel_box[i][col_index] = cancel_box[i][col_index] + list(marked_cell&digits)
                marked_grids[i][col_index] = marked_cell - digits
                if len(marked_grids[i][col_index]) == 1:
                    elem = marked_grids[i][col_index].pop()
                    marked_grids[i][col_index] = elem
                    grids[i][col_index] = elem
                    self.num += 1
                    self.cross_out_by_digit(
                        grids, marked_grids, elem, i, col_index, cancel_box)

    def cross_out_row(self, grids, marked_grids, row_index, digits, pos_lst, cancel_box):
        for i in range(9):
            marked_cell = marked_grids[row_index][i]
            position = (row_index, i)
            if isinstance(marked_cell, set) and position not in pos_lst:
                cancel_box[row_index][i] = cancel_box[row_index][i]  + list(marked_cell&digits)
                marked_grids[row_index][i] = marked_cell - digits
                if len(marked_grids[row_index][i]) == 1:
                    elem = marked_grids[row_index][i].pop()
                    marked_grids[row_index][i] = elem
                    grids[row_index][i] = elem
                    self.num += 1
                    self.cross_out_by_digit(
                        grids, marked_grids, elem, row_index, i, cancel_box)

    def cross_out_box(self, grids, marked_grids, start_row, start_col, digits, pos_list, cancel_box):
        for i in range(3):
            for j in range(3):
                position = (start_row+i, start_col+j)
                marked_cell = marked_grids[start_row + i][start_col + j]
                if isinstance(marked_cell, set) and position not in pos_list:
                    cancel_box[start_row+i][start_col+j] = cancel_box[start_row+i][start_col+j]  + list(marked_cell&digits)
                    marked_grids[start_row + i][start_col +
                                                j] = marked_cell - digits
                    if len(marked_grids[start_row + i][start_col + j]) == 1:
                        elem = marked_grids[start_row + i][start_col + j].pop()
                        marked_grids[start_row + i][start_col + j] = elem
                        grids[start_row + i][start_col + j] = elem
                        self.num += 1
                        self.cross_out_by_digit(
                            grids, marked_grids, elem, start_row + i, start_col + j, cancel_box)

    def cross_out_by_digit(self, grids, marked_grids, digit, row, col,cancel_box):
        # cross each row and each column
        for i in range(9):
            marked_cell = marked_grids[row][i]
            if isinstance(marked_cell, set) and digit in marked_cell:
                cancel_box[row][i].append(digit)
                marked_cell.remove(digit)
                if len(marked_cell) == 1:
                    elem = marked_grids[row][i].pop()
                    marked_grids[row][i] = elem
                    grids[row][i] = elem
                    self.num += 1
            marked_cell = marked_grids[i][col]
            if isinstance(marked_cell, set) and digit in marked_cell:
                marked_cell.remove(digit)
                cancel_box[i][col].append(digit)
                if len(marked_grids[i][col]) == 1:
                    elem = marked_grids[i][col].pop()
                    marked_grids[i][col] = elem
                    grids[i][col] = elem
                    self.num += 1
        for i in range(3):
            for j in range(3):
                row = (row // 3) * 3 + i
                col = (col // 3) * 3 + j
                marked_cell = marked_grids[row][col]
                if isinstance(marked_cell, set) and digit in marked_cell:
                    cancel_box[row][col].append(digit)
                    marked_cell.remove(digit)
                    if len(marked_grids[row][col]) == 1:
                        elem = marked_grids[row][col].pop()
                        marked_grids[row][col] = elem
                        grids[row][col] = elem
                        self.num += 1


    def get_preemptive_sets(self, visited, grids):
        # check row
        for i in range(9):
            row = []
            for index, item in enumerate(grids[i]):
                row.append((item, (i, index)))
            data = self.get_preemptive_set(row)
            if data:
                for item in data:
                    if item not in visited:
                        position = "R", i
                        return item, position
        # check col
        for i in range(9):
            col = []
            for j in range(9):
                col.append((grids[j][i], (j, i)))
            data = self.get_preemptive_set(col)
            if data:
                for item in data:
                    if item not in visited:
                        position = "C", i
                        return item, position
        # check box
        for i in range(3):
            for j in range(3):
                start_row = i * 3
                start_col = j * 3
                box = self.get_box_with_position(grids, start_row, start_col)
                data = self.get_preemptive_set(box)
                if data:
                    for item in data:
                        if item not in visited:
                            position = "B", start_row, start_col
                            return item, position
        return None, None

    def get_preemptive_set(self, lst):
        lst = [item for item in lst if isinstance(item[0], set)]
        lst = sorted(lst, key=lambda x: len(x[0]), reverse=True)
        result = []
        while len(lst) != 0:
            digit_set, position = lst.pop(0)
            res = [digit_set, [position]]
            m = len(digit_set)
            count = 1
            removed = []
            for item, position in lst:
                if item.issubset(digit_set):
                    count += 1
                    res[1].append(position)
                    removed.append((item, position))
            if m == count and m != 1:
                result.append(res)
                for item in removed:
                    lst.remove(item)
        return result

    def isValid(self, grids):
        # check if the game over
        # check row
        for i in range(9):
            row = grids[i]
            row = [item for item in row if isinstance(item, int)]
            if set(row) != set(range(1, 10)):
                return False
        # check column
        for i in range(9):
            col = []
            for j in range(9):
                col.append(grids[j][i])
            col = [item for item in col if isinstance(item, int)]
            if set(col) != set(range(1, 10)):
                return False
        # check box
        for i in range(3):
            for j in range(3):
                start_row = i * 3
                start_col = j * 3
                box = self.get_box(grids, start_row, start_col)
                box = [item for item in box if isinstance(item, int)]
                if set(box) != set(range(1, 10)):
                    return False
        return True


Sudoku("./test/sudoku_4.txt").worked_tex_output()
