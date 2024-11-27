# Trajektoria liczby wygranych dla jednego z dwóch graczy A,B
from simulation_functions import simulate_game
import matplotlib.pyplot as plt

a = 10
b = 20 - a
pA = [0.2, 0.5, 0.8]
# Szukane: dla każdego pA
# wykres: liczba wygranych prez wybranego gracza do numeru tury
# Trajektorie dla 3 gier najlepiej na jednym wykresie


# Simulate and plot for each probability
for pA_value in pA:
    for game_no in range(3):  # Simulate three games for each probability
        outcome = simulate_game(pA_value, a, b, max_turns=50)
        cumulative_wins_A = [sum(outcome.playerA_won_turns[:i]) for i in range(1, len(outcome.playerA_won_turns) + 1)]
        plt.plot(range(1, len(cumulative_wins_A) + 1), cumulative_wins_A, label=f'pA={pA_value}, Game {game_no + 1}')

# Labeling the plot
plt.title('Cumulative Wins for Player A Over Turns')
plt.xlabel('Turn Number')
plt.ylabel('Cumulative Wins for Player A')
plt.legend()
plt.grid(True)
plt.show()