import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(style='whitegrid')


def plot_simulation_results(all_populations: list, densities: list) -> None:
    num_rows = num_cols = 3  # Create a 3x3 grid of subplots

    # Plot 1: Population Over Time by Start Density
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 15))

    # Initialize an empty DataFrame
    df_all = pd.DataFrame()

    for i, (grid_size, populations, density) in enumerate(all_populations):
        for population in populations:
            # Create a DataFrame for the current grid size
            df = pd.DataFrame(population, columns=['Population'])
            df['Generation'] = df.index
            df['Grid Size'] = f'{grid_size}x{grid_size}'
            df['Density'] = density

            # Append the DataFrame to the main DataFrame
            df_all = pd.concat([df_all, df])

    # Save the DataFrame to a CSV file
    # df_all.to_csv(
    #     '/Users/johan/IdeaProjects/progmod/src/game_of_life_project/simulation_data/simulation_data1.csv',
    #     index=False)

    """
    for i, density in enumerate(densities):
        ax = axs[i // num_cols, i % num_cols]
        df_density = df_all[df_all['Density'] == density]

        # Plot the data for the current density
        sns.lineplot(x='Generation', y='Population',
                     hue='Grid Size', data=df_density, ax=ax)
        ax.set_title(f"Start density {density * 100:.0f}%")

    plt.tight_layout()
    plt.show()

    # Save the DataFrame to a CSV file
    
    # Plot 2: Final Population Distribution by Start Density
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Density', y='Population', hue='Grid Size', data=df_all)
    plt.title("Final Population Distribution by Start Density")
    plt.show()

    # Plot 3: KDE Plot of Final Population by Start Density
    plt.figure(figsize=(10, 6))
    sns.kdeplot(x='Density', y='Population',
                hue='Grid Size', data=df_all, fill=True)
    plt.title("KDE Plot of Final Population by Start Density")
    plt.show()

    
    # Plot 5: Swarm Plot of Final Population by Start Density
    plt.figure(figsize=(10, 6))
    sns.swarmplot(x='Density', y='Population', hue='Grid Size', data=df_all)
    plt.title("Swarm Plot of Final Population by Start Density")
    plt.show()
    

    print(df_all)
    """