import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

num_users = 100
P_log_in = 0.2
P_stay_logged_out = 0.8
P_log_out = 0.5
P_stay_logged_in = 0.5
N = 10_000

def calculate_transition_matrix(X, P_login, P_logout, P_stay_logged_in, P_stay_logged_out):
    states = list(range(X + 1))

    # Initialize transition matrix
    transition_matrix = np.zeros((len(states), len(states)))

    # Calculate probabilities for each transition
    for current_state in states:
        for next_state in states:
            prob = 0
            for staying_in in range(max(0, next_state - (X - current_state)), min(current_state, next_state) + 1):
                logging_out = current_state - staying_in
                logging_in = next_state - staying_in

                if logging_out < 0 or logging_in < 0:
                    continue

                prob += (
                        comb(current_state, staying_in) *  # Ways to choose users who stay logged in
                        comb(X - current_state, logging_in) *  # Ways to choose users who log in
                        (P_stay_logged_in ** staying_in) *
                        (P_logout ** logging_out) *
                        (P_login ** logging_in) *
                        (P_stay_logged_out ** (X - current_state - logging_in))
                )
            transition_matrix[current_state, next_state] = prob

    return transition_matrix


def simulate(init_state, simulations_number):
    n = P.shape[0]
    selected_node_count = np.zeros(n)
    simulation_results = []
    current_node = init_state
    for i in range(1, simulations_number + 1):
        selected_node_count[current_node] += 1
        current_node = np.random.choice(n, p=P[current_node])

        if i % 100 == 0:
            simulation_results.append(selected_node_count / i)
        print(f"Node {current_node} selected {selected_node_count[current_node]} times")
    return np.array(simulation_results)

P = calculate_transition_matrix(num_users, P_log_in, P_log_out, P_stay_logged_in, P_stay_logged_out)

results = {}
for i in range(P.shape[0]):
    results[i] = simulate(i, N)

for i in results:
    for j in range(P.shape[0]):
        plt.plot(range(100, N + 1, 100), results[i][:, j], label=f'Node {j} (start {i})')


plt.xlabel("Liczba kroków N", fontsize=12)
plt.ylabel(r"$P_{i}^N$", fontsize=12)
plt.title("Zbieżność prawdopodobieństwa $P_{ij}^N$", fontsize=14)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()