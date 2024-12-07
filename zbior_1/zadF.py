# # kapitał (k) gracza A przy N turach
# from collections import Counter
#
# a = 50  # kapitał gracza A
# b = 50  # kapitał gracza B
# pA = 0.2  # prawdopodobieństwo wygrania tury przez gracza A
# N = [1, 10, 50, 60, 70, 80]  # liczba tur
# # szukane: Pk, k
#
# # dla każdego N
# # Podpowiedź: Trzeba przeprowadzić wiele rozgrywek aby móc wyznaczyć prawdopodobieństwo
# # prawdopodobienstwo trafiena kapitału gracza A dla różnych kapitałów
#
# import matplotlib.pyplot as plt
# from simulation_functions import get_probability_of_winning_simulation
# #
# # for n in N:
# #     outcome = get_probability_of_winning_simulation(pA, a, b, no_of_turns_per_game_loop=n)
# #     print(outcome.no_of_playerA_money_per_turn_per_game)
# #     print(outcome.no_of_playerB_money_per_turn_per_game)
# #     # Aggregate results for player A
# #     all_money_values = [money for game in outcome.no_of_playerA_money_per_turn_per_game for money in game]
# #     money_distribution = Counter(all_money_values)
# #
# #     # Prepare data for plotting
# #     x_values = sorted(money_distribution.keys())
# #     y_values = [money_distribution[x] / sum(money_distribution.values()) for x in x_values]
# #     print('&&&&&&&&&&&&&&')
# #     print(x_values)
# #     print(y_values)
# #
# #     # Plot results
# #     plt.figure(figsize=(10, 6))
# #     plt.plot(x_values, y_values)
# #     plt.xlabel("k")
# #     plt.ylabel("P(k)")
# #     plt.title("Kapitał (k) gracza A po N turach")
# #     plt.grid(axis='y', linestyle='--', alpha=0.7)
# #     plt.show()


import random
import matplotlib.pyplot as plt
from collections import Counter

def simulate_game(playerA_chance, playerA_money, playerB_money, rounds):
    """Simulates a single game for a fixed number of rounds."""
    for _ in range(rounds):
        if random.random() < playerA_chance:
            if playerB_money > 0:  # Player A wins the round
                playerA_money += 1
                playerB_money -= 1
        else:
            if playerA_money > 0:  # Player B wins the round
                playerA_money -= 1
                playerB_money += 1
        # Stop if one player loses all money
        if playerA_money == 0 or playerB_money == 0:
            break
    return playerA_money

def simulate_many_games(playerA_chance, initial_money, rounds_list, num_games=10000):
    """Simulates many games and tracks Player A's capital distribution."""
    results = {rounds: [] for rounds in rounds_list}
    for _ in range(num_games):
        for rounds in rounds_list:
            playerA_capital = simulate_game(playerA_chance, initial_money, initial_money, rounds)
            results[rounds].append(playerA_capital)
    return results

# Parameters
a = 50  # Initial capital for Player A
b = 50  # Initial capital for Player B
pA = 0.2  # Probability of Player A winning a turn
N = [1, 10, 50, 60, 70, 80]  # Number of rounds
num_games = 10000  # Number of games to simulate

# Run simulation
capital_distributions = simulate_many_games(pA, a, N, num_games)

# Plot results
plt.figure(figsize=(12, 8))
for rounds in N:
    capital_counts = Counter(capital_distributions[rounds])
    capitals, frequencies = zip(*sorted(capital_counts.items()))
    probabilities = [freq / num_games for freq in frequencies]
    plt.bar(capitals, probabilities, label=f'N={rounds}')

    plt.title("Probability Distribution of Player A's Capital")
    plt.xlabel("Player A's Capital")
    plt.ylabel("Probability")
    plt.legend()
    plt.grid()
    plt.show()
