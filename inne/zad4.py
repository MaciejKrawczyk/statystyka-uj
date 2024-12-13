import numpy as np
import matplotlib.pyplot as plt


def simulation(p, capital_a, total_capital):
    current_wins = 0
    round_number = 0
    round_numbers = []
    win_numbers = []
    while (0 <= capital_a <= total_capital) or round_number >= 50:
        round_number += 1
        if np.random.rand() <= p:
            capital_a += 1
            current_wins += 1
        else:
            capital_a -= 1
        win_numbers.append(current_wins)
        round_numbers.append(round_number)

    return round_numbers, win_numbers


initial_capital_A = 10
initial_capital_B = 10
total_capitals = initial_capital_A + initial_capital_B

p1 = 1 / 5
p2 = 1 / 2
p3 = 4 / 5


round_numbers1, win_numbers1 = simulation(p1, 10, total_capitals)
round_numbers2, win_numbers2 = simulation(p1, 10, total_capitals)
round_numbers3, win_numbers3 = simulation(p1, 10, total_capitals)

plt.figure(figsize=(10, 6))
plt.plot(round_numbers1, win_numbers1, label = "p = 1/5", color="blue")
plt.plot(round_numbers2, win_numbers2, label = "p = 1/2", color="orange")
plt.plot(round_numbers3, win_numbers3, label = "p = 4/5", color="green")
plt.title("Liczba wygranych tur gracz A\nw zależności od numeru tury")
plt.ylabel("Liczba wygranych tur gracz A")
plt.xlabel("Numer tury")
plt.legend()
plt.grid()
plt.show()
