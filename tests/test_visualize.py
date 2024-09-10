from ..grid import Grid, FULL_CELL
from ..main import count_all_cells


def test_count_all_cells():
    grid = Grid()
    assert isinstance(count_all_cells(grid), int)
    assert count_all_cells(grid) == sum(cell == FULL_CELL for row in grid.cell_matrix for cell in row)
