import logging
import os
from multiprocessing import Pool
from timeit import default_timer as timer

from grid import Grid, GridUpdater, count_all_cells
from visualize import plot_simulation_results

os.environ['TERM']: str = 'xterm'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

SIMULATION_TOTAL_COUNT: int = 100
GENERATION_LIMIT: int = 1000

DENSITY_START: float = 0.03
DENSITY_INCREMENT: float = 0.06
GRID_SIZE_START: int = 20
GRID_SIZE_END: int = 300
GRID_SIZE_STEP: int = 40

populations: list = []


def run_simulation(grid) -> list:
    """Run a single simulation with the given grid until the generation limit is reached."""
    populations_: list = []
    generation_number: int = 0
    while generation_number < GENERATION_LIMIT:
        population_count: int = count_all_cells(grid)
        GridUpdater.update_grid(grid)

        generation_number += 1
        populations_.append(population_count)

    return populations_


def run_simulation_wrapper(args) -> list:
    return run_simulation(*args)


def run_simulations(all_populations, density, grid_size, p) -> None:
    """Run multiple simulations for a given grid size and density."""
    grids: list = [(Grid(grid_size, grid_size, grid_start_density=density),)
                   for _ in range(SIMULATION_TOTAL_COUNT)]
    populations: list = p.map(run_simulation_wrapper, grids)

    all_populations.append((grid_size, populations, density))


def main() -> None:
    grid_start_densities: list = [
        round(i * DENSITY_INCREMENT + DENSITY_START, 2) for i in range(1, 10)]
    grid_sizes: list = list(
        range(GRID_SIZE_START, GRID_SIZE_END + 1, GRID_SIZE_STEP))
    all_populations: list = []

    logging.info("Starting simulations...")
    start_time: float = timer()
    with Pool() as p:  # Use all available cores
        for grid_size in grid_sizes:
            for density in grid_start_densities:
                start_time_: float = timer()

                run_simulations(all_populations, density, grid_size, p)

                end_time_: float = timer()
                logging.info(
                    f"Time taken for {SIMULATION_TOTAL_COUNT} simulations at {density * 100:.0f}% density "
                    f"and grid size {grid_size}x{grid_size}: {end_time_ - start_time_:.3f} seconds")

    end_time: float = timer()
    logging.info(
        f"All simulations completed in {end_time - start_time:.3f} seconds")
    logging.info("Plotting results...")
    start_time: float = timer()

    plot_simulation_results(all_populations, grid_start_densities)

    end_time: float = timer()
    logging.info(
        f"{SIMULATION_TOTAL_COUNT * len(grid_start_densities) * len(grid_sizes)} total simulations plotted "
        f"in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    start: float = timer()

    main()

    end: float = timer()
    logging.info(f"Time taken: {end - start:2f}")
