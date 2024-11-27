# kapitał (k) gracza A przy N turach
from collections import Counter

a = 50  # kapitał gracza A
b = 50  # kapitał gracza B
pA = 0.2  # prawdopodobieństwo wygrania tury przez gracza A
N = [1, 10, 50, 60, 70, 80]  # liczba tur
# szukane: Pk, k

# dla każdego N
# Podpowiedź: Trzeba przeprowadzić wiele rozgrywek aby móc wyznaczyć prawdopodobieństwo
# prawdopodobienstwo trafiena kapitału gracza A dla różnych kapitałów

import matplotlib.pyplot as plt
from simulation_functions import get_probability_of_winning_simulation

for n in N:
    outcome = get_probability_of_winning_simulation(pA, a, b, no_of_turns_per_game_loop=n)
    print(outcome.no_of_playerA_money_per_turn_per_game)
    print(outcome.no_of_playerB_money_per_turn_per_game)
    # Aggregate results for player A
    all_money_values = [money for game in outcome.no_of_playerA_money_per_turn_per_game for money in game]
    money_distribution = Counter(all_money_values)

    # Prepare data for plotting
    x_values = sorted(money_distribution.keys())
    y_values = [money_distribution[x] / sum(money_distribution.values()) for x in x_values]
    print('&&&&&&&&&&&&&&')
    print(x_values)
    print(y_values)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, width=1.0, edgecolor="black")
    plt.xlabel("Amount of Money (Player A)")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Player A's Money After Simulations")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()