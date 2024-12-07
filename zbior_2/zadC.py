# import numpy as np
# import random
# import matplotlib.pyplot as plt
# from scipy.special import comb
#
#
# def calculate_transition_matrix(X, P_login, P_logout, P_stay_logged_in, P_stay_logged_out):
#     """
#     Calculate the transition matrix for X users.
#
#     Parameters:
#         X (int): Maximum number of users.
#         P_login (float): Probability of a user logging in.
#         P_logout (float): Probability of a user logging out.
#         P_stay_logged_in (float): Probability of a user staying logged in.
#         P_stay_logged_out (float): Probability of a user staying logged out.
#
#     Returns:
#         np.ndarray: Transition matrix of shape (X+1, X+1).
#     """
#     states = np.arange(X + 1)
#     transition_matrix = np.zeros((X + 1, X + 1))
#
#     for current_state in states:
#         for next_state in states:
#             prob = 0
#             for staying_in in range(max(0, next_state - (X - current_state)), min(current_state, next_state) + 1):
#                 logging_out = current_state - staying_in
#                 logging_in = next_state - staying_in
#
#                 if logging_out < 0 or logging_in < 0:
#                     continue
#
#                 prob += (
#                     comb(current_state, staying_in) *
#                     comb(X - current_state, logging_in) *
#                     (P_stay_logged_in ** staying_in) *
#                     (P_logout ** logging_out) *
#                     (P_login ** logging_in) *
#                     (P_stay_logged_out ** (X - current_state - logging_in))
#                 )
#             transition_matrix[current_state, next_state] = prob
#
#     return transition_matrix
#
#
# def get_next_node(current_node, transition_matrix):
#     """
#     Returns the next node based on the current node and transition matrix.
#     """
#     probabilities = transition_matrix[current_node]
#     return random.choices(range(len(transition_matrix)), probabilities)[0]
#
#
# def simulate_random_walk(num_nodes, start_node, n_max):
#     """
#     Simulates a random walk between nodes.
#
#     Args:
#         num_nodes (int): Number of nodes.
#         start_node (int): Starting node.
#         n_max (int): Number of simulation steps.
#
#     Returns:
#         list: Visit counts for each node.
#         list: Convergence of visit frequencies for each node.
#     """
#     X = num_nodes - 1  # Maximum users is num_nodes - 1
#     P_login = 0.2
#     P_logout = 0.5
#     P_stay_logged_in = 0.5
#     P_stay_logged_out = 0.8
#
#     transition_matrix = calculate_transition_matrix(X, P_login, P_logout, P_stay_logged_in, P_stay_logged_out)
#     visit_counts = np.zeros(num_nodes, dtype=int)
#     current_node = start_node
#
#     convergence = []
#
#     for step in range(1, n_max + 1):
#         visit_counts[current_node] += 1
#         frequencies = visit_counts / step
#         convergence.append(frequencies.copy())
#         current_node = get_next_node(current_node, transition_matrix)
#
#     return visit_counts, convergence
#
#
# def plot_convergence(convergence, n_max, num_nodes, start_node):
#     """
#     Plots the convergence of visit frequencies for selected nodes.
#     """
#     steps = np.arange(1, n_max + 1)
#     plt.figure(figsize=(12, 6))
#
#     for node in range(min(10, num_nodes)):
#         plt.plot(steps, [freq[node] for freq in convergence], label=f'Node {node}')
#
#     plt.xlabel('Number of steps')
#     plt.ylabel('Visit frequency')
#     plt.title(f'Convergence of visit frequencies (starting at node {start_node})')
#     plt.legend()
#     plt.grid()
#     plt.show()
#
#
# # Simulation parameters
# n_max = 10_000
# num_nodes = 101
#
# # Simulations for different starting nodes
# for start_node in range(0, 101):
#     visit_counts, convergence = simulate_random_walk(num_nodes, start_node, n_max)
#     print(f'Starting from node {start_node} - Visits: {visit_counts[:10]}...')  # Display first 10 nodes
#     plot_convergence(convergence, n_max, num_nodes, start_node)

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

num_users = 100
P_log_in = 0.2
P_stay_logged_out = 0.8
P_log_out = 0.5
P_stay_logged_in = 0.5
N = 1000

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