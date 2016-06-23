"""Game 'board' and environment for the mbti_types interactions."""

from random import choice

import mbti_types


NEIGHBORHOOD_SIZE = 8  # Must be a multiple of 8.

types = dict(
    istj=mbti_types.Istj,
    isfj=mbti_types.Isfj,
    infj=mbti_types.Infj,
    intj=mbti_types.Intj,
    istp=mbti_types.Istp,
    isfp=mbti_types.Isfp,
    infp=mbti_types.Infp,
    intp=mbti_types.Intp,
    estp=mbti_types.Estp,
    esfp=mbti_types.Esfp,
    enfp=mbti_types.Enfp,
    entp=mbti_types.Entp,
    estj=mbti_types.Estj,
    esfj=mbti_types.Esfj,
    enfj=mbti_types.Enfj,
    entj=mbti_types.Entj,
)

choice_typed = zip(types.keys(), types.values())


class Grid(list):
    """Overloaded list with some convenience methods for the grid."""

    def __init__(self, grid):
        """Add initial grid."""
        self += grid

    def cell(self, row, col):
        """Try to get a cell."""
        try:
            return self[row][col]
        except IndexError:
            return None

    def get_neighborhood(self, col=0, row=0):
        """Get the neighborhood of a given cell.

        Example of neighborhood below:

        [1] [2] [3]
        [4] [X] [5]
        [6] [7] [8]
        """
        # Top row
        tl = self.cell(row - 1, col - 1)
        tc = self.cell(row, col - 1)
        tr = self.cell(row - 1, col + 1)
        # Left and right
        ml, mr = self.cell(row - 1, col), self.cell(row + 1, col)
        # Bottom row
        bl = self.cell(row + 1, col - 1)
        bc = self.cell(row, col + 1)
        br = self.cell(row + 1, col + 1)
        return [
            tl, tc, tr,
            ml, mr,
            bl, bc, br,
        ]


def new_grid(size):
    """Generate an empty grid of `size`."""
    return [[0 for _ in range(size)] for _ in range(size)]


def get_pos(grid, x, y):
    """Get a position."""
    return grid[x][y]


def evaluate(currcell, neighbors):
    """Evaluate the current cell against its neighbors."""
    for neighbor in neighbors:
        if neighbor is not None:
            neighbor.interact_with(currcell)


def random_grid(size=10):
    """Generate a grid of random types."""
    grid = new_grid(size)
    for rownum, row in enumerate(grid):
        for colnum, _ in enumerate(row):
            name, typecls = choice(choice_typed)
            grid[rownum][colnum] = typecls(name)
    return grid


def run_game(types, grid=None, iterations=5):
    """Run a game.

    NEIGHBORHOOD_SIZE determines the surrounding elements, in much the same
    format as Conway's game of life.

    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]

    x = lst[0][2]  # Row one, column three (2, here)
    """
    if grid is None:
        grid = Grid(random_grid(size=10))
    curr_step = iterations

    while curr_step > 0:
        for rownum, row in enumerate(grid):
            for colnum, col in enumerate(row):
                neighbors = grid.get_neighborhood(row=rownum, col=colnum)
                currcell = grid.cell(rownum, colnum)
                evaluate(currcell, neighbors)
        curr_step -= 1

if __name__ == '__main__':
    run_game(mbti_types)
