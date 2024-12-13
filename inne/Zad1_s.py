import numpy as np
import matplotlib.pyplot as plt


def probability_of_loss(p, capital_a, total_capitals, simulation_no):
    loses_count_A = 0
    for i in range(simulation_no):
        current_capital_a = capital_a
        while total_capitals > current_capital_a > 0:
            if np.random.rand() <= p:
                current_capital_a += 1
            else:
                current_capital_a -= 1

        if current_capital_a <= 0:
            loses_count_A += 1

    return loses_count_A / simulation_no


initial_capital_A = 50
initial_capital_B = 50
total_capitals =  initial_capital_A + initial_capital_B
simulation_no = 5000

p_all = np.arange(0.01, 1, 0.01)

probabilities_a = []

for p in p_all:
    prob_a = probability_of_loss(p, initial_capital_A, total_capitals, simulation_no)
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
