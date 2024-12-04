# Trajektoria liczby wygranych dla jednego z dwóch graczy A,B
from simulation_functions import get_probability_of_winning_simulation
import matplotlib.pyplot as plt

a = 10
b = 20 - a
pA = [0.2, 0.5, 0.8]
# Szukane: dla każdego pA
# wykres: liczba wygranych prez wybranego gracza do numeru tury
# Trajektorie dla 3 gier najlepiej na jednym wykresie


# Plot configurations
plt.figure(figsize=(12, 8))

# Loop over probabilities pA
for prob in pA:
    # Run the simulation
    outcome = get_probability_of_winning_simulation(prob, a, b)

    # Generate trajectories for 3 games
    for game_idx in range(3):  # Assuming `outcome.no_of_turns_won_by_playerA_per_game` stores data for multiple games
        results = []
        cumulative_wins = 0  # Keep track of cumulative wins

        # Process each turn in the game
        for turn in outcome.no_of_turns_won_by_playerA_per_game[game_idx]:
            cumulative_wins += 1 if turn else 0
            results.append(cumulative_wins)

        # Plot the trajectory for the current game
        # plt.plot(range(1, len(results) + 1), results, label=f'pA={prob}, game={game_idx + 1}')
        plt.step(range(1, len(results) + 1), results, label=f'pA={prob}, game={game_idx + 1}')

    # Finalize the plot
    plt.title('Liczba wygranych przez wybranego gracza do numeru tury (dla różnych pA i gier)')
    plt.xlabel('Numer tury')
    plt.ylabel('Liczba wygranych przez gracza A')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()