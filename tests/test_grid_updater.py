import pytest

from ..grid import Grid, GridUpdater, EMPTY_CELL, FULL_CELL


@pytest.fixture
def grid():
    return Grid(3, 3)


def test_update_full_cells(grid):
    raise NotImplementedError


def test_update_empty_cells(grid):
    raise NotImplementedError


def test_update_grid(grid):
    grid.cell_matrix = [
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
    ]

    expected_grid = [
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL],
        [EMPTY_CELL, FULL_CELL, EMPTY_CELL]
    ]

    GridUpdater.update_grid(grid)
    assert grid.cell_matrix == expected_grid


def test_update_empty_grid(grid):
    grid.cell_matrix = [
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
    ]
    GridUpdater.update_grid(grid)
    assert all(cell == EMPTY_CELL for row in grid.cell_matrix for cell in row)


def test_update_full_grid(grid):
    grid.cell_matrix = [
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL],
        [FULL_CELL, FULL_CELL, FULL_CELL]
    ]
    expected_grid = [
        [FULL_CELL, EMPTY_CELL, FULL_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [FULL_CELL, EMPTY_CELL, FULL_CELL]
    ]
    GridUpdater.update_grid(grid)
    assert grid.cell_matrix == expected_grid
