class SudokuError(Exception):
    pass


class Sudoku(object):
    def __init__(self, filename):
        self.filename = filename
        self.grids = []
        fp = open(filename, "r")
        lines = []
        for line in fp:
            line = line.strip()
            line = line.replace(" ", "")
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
            if len(set(row)) != len(row):
                return "There is clearly no solution."
        # check columns
        for i in range(9):
            cols = []
            for j in range(9):
                cols.append(self.grids[j][i])
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
                print(box)






    def bare_tex_output(self):
        """
        outputs Latex code to a file, use these code to produce a pictorial 
        representation of the grid
        """
        pass

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

Sudoku("./test/sudoku_1.txt").preassess()