# Liczba tur (L) do ukończenia gry
from collections import Counter
import matplotlib.pyplot as plt
from simulation_functions import get_probability_of_winning_simulation

a = 50
b = 50
pA = [0.2, 0.5, 0.8]
# szukane: dla każdego pA
# wykres: P(L) do L
# oraz średnia długość gry

num_simulations = 1000

# jak czesto trafiała się konkretna ilość tur

for i in range(len(pA)):
    outcome = get_probability_of_winning_simulation(pA[i], a, b)
    turns_counter = Counter(outcome.no_of_turns_per_game)
    turns, frequencies = zip(*sorted(turns_counter.items()))
    probabilities = [freq / outcome.no_of_games for freq in frequencies]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(turns, probabilities, width=1.0, edgecolor='black', align='center')
    plt.title(f"Liczba tur do ukończenia gry (szansa gracza A = {pA[i]})", fontsize=14)
    plt.xlabel("L", fontsize=12)
    plt.ylabel("P(L)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()