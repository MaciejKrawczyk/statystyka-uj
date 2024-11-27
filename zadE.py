# maksymalna długość rozgrywki Lmax
a = 50
b = 50
# szukane:
# Lmax z 1000 gier
# wykres: Lmax do pA
import matplotlib.pyplot as plt
from simulation_functions import simulate_game, get_probability_of_winning_simulation

no_of_games = 10000
pA_values = [0.05 + i * 0.05 for i in range(18)]
Lmax_values = []


for pA in pA_values:
    game_outcome = get_probability_of_winning_simulation(pA, 50, 50, no_of_games)
    Lmax_values.append(max(game_outcome.no_of_turns_per_game))  # Track maximum turns

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(pA_values, Lmax_values, marker='o', color='blue', label='Lmax vs pA')
plt.title('Maksymalna długość rozgrywki Lmax w zależności od pA')
plt.xlabel('pA (szansa wygranej gracza A)')
plt.ylabel('Lmax (maksymalna liczba tur)')
plt.grid(True)
plt.legend()
plt.show()