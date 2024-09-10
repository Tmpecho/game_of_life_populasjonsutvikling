from dataclasses import dataclass

import numpy as np
from scipy import signal

EMPTY_CELL: str = " "
FULL_CELL: str = "#"


@dataclass
class Cell:
    row: int
    column: int


class Grid:
    def __init__(self, grid_height: int = 40, grid_width: int = 40, grid_start_density: float = 0.2) -> None:
        self.grid_height: int = grid_height
        self.grid_width: int = grid_width
        self.grid_start_density: float = grid_start_density

        # The grid itself and not the object
        self.cell_matrix: np.ndarray = self._create_random_grid

    @property
    def _create_random_grid(self) -> np.ndarray:
        return np.random.choice([FULL_CELL, EMPTY_CELL], size=(self.grid_height, self.grid_width),
                                p=[self.grid_start_density, 1 - self.grid_start_density])


class GridUpdater:
    def __init__(self, grid: Grid) -> None:
        self.grid: Grid = grid

    @classmethod
    def update_grid(cls, grid: Grid) -> None:
        """Update the grid according to the rules of Conway's Game of Life."""
        instance: GridUpdater = cls(grid)
        temporary_grid: np.ndarray = np.copy(instance.grid.cell_matrix)

        kernel: np.array = np.array([[1, 1, 1],
                                     [1, 0, 1],
                                     [1, 1, 1]])

        # Signal magic
        neighbours_counts: np.ndarray = signal.convolve2d(
            (temporary_grid == FULL_CELL), kernel, mode='same')

        instance._update_full_cells(temporary_grid, neighbours_counts)
        instance._update_empty_cells(temporary_grid, neighbours_counts)

    def _update_full_cells(self, temporary_grid: np.ndarray, neighbours_counts: np.ndarray) -> None:
        self.grid.cell_matrix = np.where(
            (temporary_grid == FULL_CELL) & (
                (neighbours_counts < 2) | (neighbours_counts > 3)), EMPTY_CELL,
            temporary_grid)

    def _update_empty_cells(self, temporary_grid: np.ndarray, neighbours_counts: np.ndarray) -> None:
        self.grid.cell_matrix = np.where((temporary_grid == EMPTY_CELL) & (neighbours_counts == 3), FULL_CELL,
                                         self.grid.cell_matrix)


def count_all_cells(grid: Grid) -> int:
    return [cell == FULL_CELL for row in grid.cell_matrix for cell in row].count(True)
