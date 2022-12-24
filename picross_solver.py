from grid import Grid

class PicrossSolver():
    
    def __init__(self, grid:Grid) -> None:
        self.grid = grid

    def solve(self) -> Grid:

        for y in range(self.grid.height):
            row_hint = self.grid.row_hint(y)
            for i in range(len(row_hint)):
                hint = row_hint[i]
                l = sum(row_hint[:i]) + len(row_hint[:i])
                r = sum(row_hint[i+1:]) + len(row_hint[i+1:])
                s = l + r
                m = self.grid.width - len()


    def check(self) -> bool:

        # check all rows if the hints equal the values
        for y in range(self.grid.height):
            count = 0; row = []
            for cell in self.grid.row(y):
                if cell: count += 1 # increase count for each cell that is found consecutively
                elif not cell: row.append(count); count = 0 # if false then chain added to total
                else: return False # should be no Nones
            if row != self.grid.row_hint(y): return False

        # check all cols if the hints equal the values
        for x in range(self.grid.width):
            count = 0; col = []
            for cell in self.grid.col(x):
                if cell: count += 1 # increase count for each cell that is found consecutively
                elif not cell: col.append(count); count = 0 # if false then chain added to total
                else: return False # should be no Nones
            if col != self.grid.col_hint(x): return False

        
        return True # only returns true if all tests passed




