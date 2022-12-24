class Grid:

    def __init__(self, row_hints:list(list(int)), col_hints:list(list(int))) -> None:
        # set variables
        self.width = len(col_hints)
        self.height = len(row_hints)
        self.row_hints = row_hints
        self.col_hints = col_hints
        
        # initialize grid and set all values to none
        # grid is stored in grid[y][x] form for easier printing
        self.grid = []
        for y in self.height:
            self.grid.append([])
            for x in self.width:
                self.grid[y].append(None)
        
    # getters and setters
    def get(self, x:int, y:int) -> bool:
        return self.grid[y][x]

    def set(self, x:int, y:int, v:bool) -> None:
        self.grid[y][x] = v

    def row_hint(self, y:int) -> list(int):
        return self.row_hints[y]

    def col_hint(self, x:int) -> list(int):
        return self.col_hints[x]

    def row(self, y:int) -> list(bool):
        return self.grid[y]

    def col(self, x:int) -> list(bool):
        col = []
        for y in range(len(self.height)):
            col.append(self.get(x,y))
        return col
    

