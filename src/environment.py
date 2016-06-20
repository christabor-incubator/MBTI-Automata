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


def new_grid(size):
    """Generate an empty grid of `size`."""
    return [
        [0 for _ in range(size)] for _ in range(size)
    ]


def get_pos(grid, x, y):
    """Get a position."""
    return grid[x][y]


def random_grid(grid, size=10):
    """Generate a grid of random types."""
    grid = new_grid(size)
    for rownum, row in enumerate(grid):
        for colnum, _ in enumerate(row):
            name, typecls = choice(choice_typed)
            grid[rownum][colnum] = typecls(name)
    return grid


def run_game(types, grid=None, iterations=10):
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
        grid = random_grid(10)
    curr_step = iterations
    while curr_step > 0:
        for rownum, row in enumerate(grid):
            for colnum, col in enumerate(row):
                curr_type = grid[rownum][colnum]
                print('curr_type @ {x},{y} = '.format(
                    x=rownum, y=colnum), curr_type.name.upper())
        curr_step -= 1

if __name__ == '__main__':
    run_game(mbti_types)
