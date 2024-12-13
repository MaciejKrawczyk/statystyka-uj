import numpy as np
import matplotlib.pyplot as plt


def probability_of_loss(p, capital_a, total_capital):
    q = 1 - p
    if p == 0.5:
        prob_a_loses = 1 - (capital_a / total_capital)
    else:
        prob_a_loses = ((q/p) ** capital_a - (q/p) ** total_capital) / (1 - (q/p) ** total_capital)
    return prob_a_loses


initial_capital_A = 50
initial_capital_B = 50
total_capitals =  initial_capital_A + initial_capital_B

p_all = np.arange(0.01, 1, 0.01)

probabilities_a = []

for p in p_all:
    prob_a = probability_of_loss(p, initial_capital_A, total_capitals)
    probabilities_a.append(prob_a)


plt.figure(figsize=(10, 6))
plt.plot(p_all, probabilities_a, label="Prawdopodobieństwo ruiny gracza A", color="blue")
plt.axvline(0.5, color="red", linestyle="--", label="p = 0.5 (równomierne szanse)")
plt.title("Prawdopodobieństwo ruiny gracza A\nw zależności od prawdopodobieństwa wygrania tury (p)")
plt.xlabel("Prawdopodobieństwo wygrania tury przez gracza A (p)")
plt.ylabel("Prawdopodobieństwo ruiny gracza A")
plt.legend()
plt.grid()
plt.show()
