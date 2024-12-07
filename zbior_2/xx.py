import numpy as np
from math import comb


def calculate_transition_matrix(X, P_login, P_logout, P_stay_logged_in, P_stay_logged_out):
    """
    Calculate the transition matrix for X users.

    Parameters:
        X (int): Maximum number of users.
        P_login (float): Probability of a user logging in.
        P_logout (float): Probability of a user logging out.
        P_stay_logged_in (float): Probability of a user staying logged in.
        P_stay_logged_out (float): Probability of a user staying logged out.

    Returns:
        np.ndarray: Transition matrix of shape (X+1, X+1).
    """
    # States: 0 to X users logged in
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


# Example usage
X = 2  # Maximum number of users
P_login = 0.2
P_logout = 0.5
P_stay_logged_in = 0.5
P_stay_logged_out = 0.8

transition_matrix = calculate_transition_matrix(X, P_login, P_logout, P_stay_logged_in, P_stay_logged_out)
print(transition_matrix)
