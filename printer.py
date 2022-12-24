from abc import ABC, abstractmethod
from grid import Grid

class Printer(ABC):

    def __init__(self, grid:Grid) -> None:
        self.grid = grid
    
    def update(self, grid:Grid) -> None:
        self.grid = grid

    def print(self) -> None:
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                cell = self.grid.get(x,y)
                if cell: pass


