import matplotlib.pyplot as plt
import numpy as np

from main import simulate_game

# Parameters
playerA_money = 50  # Initial money for Player 1
playerB_money = 50  # Initial money for Player 2
turns = 1000  # Number of simulations per chance value

# Initialize data for plotting
chances_A = []
lost_games_A = []

# Simulate for different chances of Player A winning
for playerA_chance in [i / 100.0 for i in range(1, 100)]:
    playerB_chance = 1.0 - playerA_chance
    no_of_won_games_B = 0

    for _ in range(turns):
        result = simulate_game(playerA_chance, playerA_money, playerB_money)
        if result["playerB_wins"]:
            no_of_won_games_B += 1

    # Store data for plotting
    chances_A.append(playerA_chance)
    lost_games_A.append(no_of_won_games_B)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(chances_A, lost_games_A, marker='o', linestyle='-', color='b', label="Player B's Lost Games")
plt.title("Symulacje gry - Przegrane gry przez gracza 2 do szansy wygrania gracza 2")
plt.xlabel("Przegrane gry A")
plt.ylabel("Szansa wygranej A")
plt.grid(True)
plt.legend()
plt.show()

# ----


# Parameters
a = 50  # Fortune of player A
b = 50  # Fortune of player B
M = a + b  # Total fortune
plot_pTourWinA = np.linspace(0.01, 0.99, 100)  # Range of p values
plot_pRuinA = []

all_win_loos_rate = []

for p in plot_pTourWinA:
    q = 1 - p
    if p != 0.5:
        pRuinA = ((q / p) ** a - (q / p) ** M) / (1 - (q / p) ** M)
    else:
        pRuinA = (M - a) / M
    plot_pRuinA.append(pRuinA)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(plot_pTourWinA, plot_pRuinA, marker='o', linestyle='-', color='b', label="Player B's Lost Games")
plt.title("Symulacje gry - Przegrane gry przez gracza 2 do szansy wygrania gracza 2")
plt.xlabel("Przegrane gry A")
plt.ylabel("Szansa wygranej A")
plt.grid()
plt.legend()
plt.show()
