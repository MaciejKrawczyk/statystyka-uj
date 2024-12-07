# “Ruina gracza dla 2 graczy A,B”

a = 50
b = 50
# szukane: P (ruiny A) do pA
# oraz porównanie z wynikiem analitycznym

no_of_games = 100
pA_values = [0.01 + i * 0.01 for i in range(100)]


from simulation_functions import simulate_game, simulate_game_eq
import matplotlib.pyplot as plt
# Adjusted for probabilities on the y-axis
import matplotlib.pyplot as plt

# Symulacje
no_of_ruins_simulation = {}
for i in range(len(pA_values)):
    no_of_ruins_simulation[pA_values[i]] = [simulate_game(pA_values[i], a, b, ).playerB_wins for _ in range(no_of_games)]
ruins_probs = [sum(no_of_ruins_simulation[pA_values[i]]) / no_of_games for i in range(len(pA_values))]

# Równanie
no_of_ruins_simulation_eq = {}
for i in range(len(pA_values)):
    no_of_ruins_simulation_eq[pA_values[i]] = [simulate_game_eq(pA_values[i], a, b, ).playerB_wins for _ in range(no_of_games)]
ruins_probs_eq = [sum(no_of_ruins_simulation_eq[pA_values[i]]) / no_of_games for i in range(len(pA_values))]

plt.figure(figsize=(12, 7))
plt.plot(pA_values, ruins_probs, marker='o', linestyle='-', color='purple', label='Wynik wyliczony symulacyjnie')
plt.plot(pA_values, ruins_probs_eq, marker='o', linestyle='-', color='blue', label='Wynik wyliczony za pomocą równania')
plt.title('Ruina gracza dla 2 graczy A,B')
plt.ylabel('Prawdopodobieństwo ruiny gracza A')
plt.xlabel('pA')
plt.grid(True)
plt.legend()

plt.show()
