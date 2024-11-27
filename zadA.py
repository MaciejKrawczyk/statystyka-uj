# “Ruina gracza dla 2 graczy A,B”
from simulation_functions import simulate_game, simulate_game_eq
import matplotlib.pyplot as plt

a = 50
b = 50
# szukane: P (ruiny A) do pA
# oraz porównanie z wynikiem analitycznym

no_of_games = 1000
pA_values = [0.01 + i * 0.01 for i in range(100)]

# symulacje
no_of_ruins_simulation = {}
for i in range(len(pA_values)):
    no_of_ruins_simulation[pA_values[i]] = [simulate_game(pA_values[i], a, b).playerB_wins for _ in range(no_of_games)]
ruins_counts = [sum(no_of_ruins_simulation[pA_values[i]]) for i in range(len(pA_values))]

# równanie
no_of_ruins_simulation_eq = {}
for i in range(len(pA_values)):
    no_of_ruins_simulation_eq[pA_values[i]] = [simulate_game_eq(pA_values[i], a, b).playerB_wins for _ in range(no_of_games)]
ruins_counts_eq = [sum(no_of_ruins_simulation_eq[pA_values[i]]) for i in range(len(pA_values))]

plt.figure(figsize=(12, 7))
plt.plot(pA_values, ruins_counts, marker='o', linestyle='-', color='purple', label='Number of Games Lost by Player A simulation')
plt.plot(pA_values, ruins_counts_eq, marker='o', linestyle='-', color='blue', label='Number of Games Lost by Player A equation')
plt.title('Number of Games Lost by Player A vs. Player A Win Probability (pA)')
plt.xlabel('pA (Win Probability of Player A)')
plt.ylabel('Number of Games Lost by Player A')
plt.grid(True)
plt.legend()

plt.show()