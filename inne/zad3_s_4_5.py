import numpy as np
import matplotlib.pyplot as plt


def probability_of_loss(p, capital_a, total_capitals, simulation_no):
    total_round_no = []
    for i in range(simulation_no):
        total_rounds = 0
        current_capital_a = capital_a
        while total_capitals > current_capital_a > 0:
            if np.random.rand() <= p:
                current_capital_a += 1
            else:
                current_capital_a -= 1
            total_rounds += 1
        total_round_no.append(total_rounds)

    round_count = np.bincount(total_round_no)
    return round_count / simulation_no, np.mean(total_round_no)


initial_capital_A = 50
initial_capital_B = 50
total_capitals = initial_capital_A + initial_capital_B
simulation_no = 1000
p3 = 4 / 5

probabilities_a3, average_rounds = probability_of_loss(p3, initial_capital_A, total_capitals, simulation_no)

plt.figure(figsize=(10, 6))
plt.plot(range(len(probabilities_a3)), probabilities_a3, label="p = 4/5", color="green")
print(f"Średnia długość rozgrywki dla p = {p3}: {average_rounds} tur")
plt.title("Prawdopodobieństwo ruiny gracza A\nw zależności od kapitału a)")
plt.xlabel("Kapitał gracza A")
plt.ylabel("Prawdopodobieństwo ruiny gracza A")
plt.legend()
plt.grid()
plt.show()
