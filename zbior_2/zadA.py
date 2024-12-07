# Zad A

import numpy as np
import matplotlib.pyplot as plt

import consts

# a) Wyznaczyć macierz przejść P

P = consts.P

print(P)

# b) Znaleźć rozkład graniczny/stan stacjonarny na podstawie PN dla dużych N

P15 = np.linalg.matrix_power(P, 15)

print(P15)

# c) Sprawdzić kryterium zbieżności typu PN - PN-1 < ε

epsilon = 0.0001
max_power = 15


def get_iterations_count():
    previous_p = P
    iterations = 0
    for i in np.arange(2, max_power + 2):
        iterations += 1
        current_p = np.linalg.matrix_power(P, i)
        result = np.linalg.norm(current_p - previous_p, ord='fro') < epsilon
        previous_p = current_p
        if result:
            return iterations
    return iterations


print(get_iterations_count())


# d) Narysować wykres

def prepare_data_for_plot(iterations, state_i, state_j):
    current_p = 0
    previous_p_p_n = P[state_i, state_j]
    P_p_n = [previous_p_p_n]
    for i in np.arange(2, iterations + 2):
        current_p = np.linalg.matrix_power(P, i)[state_i, state_j]
        P_p_n.append(current_p)
    return P_p_n, current_p

def create_plot_A(i):
    data = [prepare_data_for_plot(15, j, i) for j in range(3)]

    plt.figure(figsize=(10, 6))

    for p, e in data:
        plt.plot(range(1, len(p) + 1), p, label=r"$P_{i,j}^N$", marker='o', color='blue')
        plt.axhline(y=e, color='red', linestyle='--', label="Stan stacjonarny")

    plt.xlabel("Liczba kroków N", fontsize=12)
    plt.ylabel(r"$P_{ij}^N$", fontsize=12)
    plt.title("Zbieżność prawdopodobieństwa $P_{ij}^N$", fontsize=14)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


create_plot_A(0)
create_plot_A(1)
create_plot_A(2)


def create_plot_A_once():
    data = [(prepare_data_for_plot(15, j, i), j, i) for i in range(3) for j in range(3)]

    plt.figure(figsize=(12, 8))

    for (p, e), j, i in data:
        plt.plot(range(1, len(p) + 1), p, label=f"$P_{{{i},{j}}}^N$", marker='o')
        plt.axhline(y=e, linestyle='--', label=f"Stan stacjonarny $P_{{{i},{j}}}$")

    plt.xlabel("Liczba kroków N", fontsize=12)
    plt.ylabel(r"$P_{ij}^N$", fontsize=12)
    plt.title("Zbieżność prawdopodobieństwa $P_{ij}^N$", fontsize=14)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

create_plot_A_once()