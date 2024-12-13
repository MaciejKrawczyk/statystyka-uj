import numpy as np
import matplotlib.pyplot as plt


def probability_of_loss(capital_a, total_capital):
    prob_a_loses = 1 - (capital_a / total_capital)
    return prob_a_loses

p = 0.5

initial_capital_A = 50
initial_capital_B = 50
total_capitals = initial_capital_A + initial_capital_B

capital_all = np.arange(0, 100, 1)

probabilities_a = []

for capital in capital_all:
    prob_a = probability_of_loss(capital, total_capitals)
    probabilities_a.append(prob_a)

plt.figure(figsize=(10, 6))
plt.plot(capital_all, probabilities_a, label="Prawdopodobieństwo ruiny gracza A", color="blue")
plt.title("Prawdopodobieństwo ruiny gracza A\nw zależności od kapitału a)")
plt.xlabel("Kapitał gracza A")
plt.ylabel("Prawdopodobieństwo ruiny gracza A")
plt.legend()
plt.grid()
plt.show()


