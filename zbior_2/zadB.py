# Wyznaczyć eksperymentalnie Πi EXP:
# Program: Start z wybranego węzła x = 0,1,2 → Losowanie kolejnego węzła zgodnie z praw
# dopodobieństwem → Przejście do nowego węzła → Losowanie kolejnego węzła ..... → ... → ...
# Warunki: Przeprowadzenie Nmax =104 losowań
# Obliczenia: Πi EXP = N/N,
# gdzie Ni - ile razy odwiedzony został węzeł “i” (x=0,1,2), N → (0, Nmax)
import random


#  Do wykonania:
#  Sporządzić wykres zbieżności jak w Zadaniu A
#  Przeprowadzić taką samą analizę dla startu z pozostałych węzłów
#  Porównać otrzymane wyniki z Zadaniem A

#  Pytanie: Dlaczego opuściliśmy rozważanie Π po drugim indeksie?

import random
import matplotlib.pyplot as plt

# Prawdopodobieństwa przejścia między węzłami (macierz przejść)
transition_matrix = {
    0: [0.64, 0.32, 0.04],
    1: [0.4, 0.5, 0.1],
    2: [0.25, 0.5, 0.25]
}

def get_next_node(current_node: 1 | 2 | 3):
    """
    Funkcja zwraca kolejny węzeł na podstawie aktualnego węzła i macierzy przejść.
    """
    probabilities = transition_matrix[current_node]
    return random.choices([0, 1, 2], probabilities)[0]

def simulate_random_walk(start_node: 1 | 2 | 3, n_max: int):
    """
    Symuluje losowe przejścia między węzłami.

    Args:
        start_node (int): Węzeł początkowy (0, 1 lub 2).
        n_max (int): Liczba kroków symulacji.

    Returns:
        list: Zawiera liczbę odwiedzin każdego węzła.
        list: Zawiera wartości zbieżności dla każdego kroku.
    """
    visit_counts = [0, 0, 0]  # Liczba odwiedzin każdego węzła
    current_node = start_node

    convergence = []  # Zbieżność częstotliwości odwiedzin

    for step in range(1, n_max + 1):
        # Aktualizuj licznik odwiedzin
        visit_counts[current_node] += 1

        # Licz częstotliwości odwiedzin i zapisuj je
        frequencies = [count / step for count in visit_counts]
        convergence.append(frequencies.copy())

        # Wybierz następny węzeł
        current_node = get_next_node(current_node)

    return visit_counts, convergence

def plot_convergence(convergence, n_max, start_node):
    """
    Rysuje wykres zbieżności częstotliwości odwiedzin do wartości teoretycznych.

    Args:
        convergence (list): Zawiera częstotliwości odwiedzin w każdym kroku.
        n_max (int): Liczba kroków symulacji.
        start_node (int): Węzeł początkowy.
    """
    steps = range(1, n_max + 1)
    plt.figure(figsize=(10, 6))

    for node in range(3):
        plt.plot(steps, [freq[node] for freq in convergence], label=f'Węzeł {node}')

    plt.xlabel('Liczba kroków')
    plt.ylabel('Częstotliwość odwiedzin')
    plt.title(f'Zbieżność częstotliwości odwiedzin (start z węzła {start_node})')
    plt.legend()
    plt.grid()
    plt.show()

# Parametry symulacji
n_max = 10_000

for start_node in range(3):
    visit_counts, convergence = simulate_random_walk(start_node, n_max)
    print(f'Start z węzła {start_node} - Odwiedziny: {visit_counts}')
    plot_convergence(convergence, n_max, start_node)