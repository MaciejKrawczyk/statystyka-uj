import numpy as np
import matplotlib.pyplot as plt
import time

# Ustawienie ziarna losowego dla powtarzalności wyników (opcjonalne)
np.random.seed(42)


# Funkcja gęstości rozkładu normalnego N(0,1)
def normal_pdf(x):
    return 1.0 / np.sqrt(2.0 * np.pi) * np.exp(-0.5 * x ** 2)


# Funkcja gęstości rozkładu Lorentza
def lorentz_pdf(x, C):
    return (C / np.pi) * (1 / (x ** 2 + 1))


# Stała skalująca C
C = 1.6

###############################################################################
# (I) Generowanie 10 000 punktów-kandydatów metodą Lorentza i sprawdzenie akceptacji
###############################################################################
N = 10000

start_time_part1 = time.time()

# Generujemy N punktów z rozkładu Lorentza (Cauchy)
X_candidates = np.random.standard_cauchy(N)

# Ze względu na skończone zasoby obliczeniowe, ograniczamy zakres X do [-10, 10]
# Ponieważ prawdopodobieństwo generowania wartości poza tym zakresem jest bardzo małe
mask = (X_candidates >= -10) & (X_candidates <= 10)
X_candidates = X_candidates[mask]
actual_N = X_candidates.size

# Generujemy N punktów u ~ Uniform(0,1)
U = np.random.uniform(0, 1, actual_N)

# Obliczamy g(x) dla każdego kandydata
G = lorentz_pdf(X_candidates, C)

# Obliczamy f(x) dla każdego kandydata
F = normal_pdf(X_candidates)

# Sprawdzamy, które punkty zostały zaakceptowane
accepted_indices = U <= (F / G)

# Wyciągamy zaakceptowane X
X_accepted_part1 = X_candidates[accepted_indices]

# Zliczamy procentowo, ile punktów zostało zaakceptowanych
accepted_count_part1 = X_accepted_part1.size
accepted_ratio_part1 = (accepted_count_part1 / actual_N) * 100.0

end_time_part1 = time.time()
time_part1 = end_time_part1 - start_time_part1

print("=== Część I ===")
print(f"Liczba kandydatów (po odcięciu ekstremów): {actual_N}")
print(f"Liczba zaakceptowanych punktów: {accepted_count_part1}")
print(f"Procentowy udział zaakceptowanych: {accepted_ratio_part1:.2f}%")
print(f"Czas trwania symulacji (sekundy): {time_part1:.5f}\n")

###############################################################################
# (II) Generowanie dokładnie 10 000 liczb z rozkładu normalnego
#     (potrzebujemy zmiennej liczby punktów kandydatów)
###############################################################################

start_time_part2 = time.time()

M = 0  # licznik wszystkich wylosowanych punktów
X_accepted_part2 = []

# Dopóki nie mamy 10k zaakceptowanych, generujemy kolejne paczki
block_size = 10000  # Rozmiar bloku do generowania na raz

while len(X_accepted_part2) < 10000:
    # Generujemy blok punktów z rozkładu Lorentza
    X_candidates_block = np.random.standard_cauchy(block_size)

    # Ograniczamy zakres do [-10, 10]
    mask_block = (X_candidates_block >= -10) & (X_candidates_block <= 10)
    X_candidates_block = X_candidates_block[mask_block]
    current_block_size = X_candidates_block.size

    # Generujemy u ~ Uniform(0,1)
    U_block = np.random.uniform(0, 1, current_block_size)

    # Obliczamy g(x) i f(x) dla bloku
    G_block = lorentz_pdf(X_candidates_block, C)
    F_block = normal_pdf(X_candidates_block)

    # Sprawdzamy akceptację
    accepted_indices_block = U_block <= (F_block / G_block)
    X_accepted_block = X_candidates_block[accepted_indices_block]

    # Dodajemy zaakceptowane punkty do listy
    X_accepted_part2.extend(X_accepted_block)

    # Zwiększamy licznik łącznej liczby punktów
    M += block_size

# Przycinamy listę do dokładnie 10 000 punktów
X_accepted_part2 = np.array(X_accepted_part2[:10000])

end_time_part2 = time.time()
time_part2 = end_time_part2 - start_time_part2

# Obliczamy, jaki był procent zaakceptowanych wobec wszystkich wygenerowanych
# W tym przypadku M to liczba wygenerowanych bloków * block_size
# Jednak ze względu na odcięcie ekstremów, dokładniejsze jest:
# Procent = (10000 / M_actual_generated) * 100
# gdzie M_actual_generated to liczba wygenerowanych kandydatów po odcięciu ekstremów

# W Części I odcięliśmy wartości poza [-10,10]. Tutaj również powinniśmy policzyć faktycznie wygenerowane kandydaty
# Aby uprościć, przyjmujemy, że na każdą iterację generujemy 'block_size' kandydatów,
# ale po odcięciu ekstremów, liczba faktycznych kandydatów jest mniej.

# Dla precyzyjnego obliczenia, powinniśmy śledzić liczbę faktycznie wygenerowanych kandydatów
# Po uproszczeniu, przyjmujemy M_eff = liczba wygenerowanych bloków * block_size * (proporcja po odcięciu)
# Jednak dokładne śledzenie wymaga modyfikacji pętli, co dla przejrzystości pominiemy.

# Zamiast tego, można policzyć całkowitą liczbę faktycznie wygenerowanych kandydatów
# Poniżej przedstawiam poprawioną wersję pętli z liczeniem faktycznych kandydatów

# Resetowanie zmiennych
start_time_part2 = time.time()
M_actual_generated = 0  # liczba faktycznie wygenerowanych kandydatów po odcięciu ekstremów
X_accepted_part2 = []

while len(X_accepted_part2) < 10000:
    # Generujemy blok punktów z rozkładu Lorentza
    X_candidates_block = np.random.standard_cauchy(block_size)

    # Ograniczamy zakres do [-10, 10]
    mask_block = (X_candidates_block >= -10) & (X_candidates_block <= 10)
    X_candidates_block = X_candidates_block[mask_block]
    current_block_size = X_candidates_block.size

    if current_block_size == 0:
        continue  # Brak kandydatów w zakresie, przechodzimy do następnego bloku

    # Aktualizujemy licznik faktycznie wygenerowanych kandydatów
    M_actual_generated += block_size  # Liczymy całkowitą liczbę wygenerowanych punktów (włączając odcięte)

    # Generujemy u ~ Uniform(0,1)
    U_block = np.random.uniform(0, 1, current_block_size)

    # Obliczamy g(x) i f(x) dla bloku
    G_block = lorentz_pdf(X_candidates_block, C)
    F_block = normal_pdf(X_candidates_block)

    # Sprawdzamy akceptację
    accepted_indices_block = U_block <= (F_block / G_block)
    X_accepted_block = X_candidates_block[accepted_indices_block]

    # Dodajemy zaakceptowane punkty do listy
    X_accepted_part2.extend(X_accepted_block)

# Przycinamy listę do dokładnie 10 000 punktów
X_accepted_part2 = np.array(X_accepted_part2[:10000])

end_time_part2 = time.time()
time_part2 = end_time_part2 - start_time_part2

# Obliczamy procent zaakceptowanych wobec wszystkich wygenerowanych kandydatów
# gdzie M_actual_generated to liczba wygenerowanych kandydatów (w tym odrzuconych)
accepted_ratio_part2 = (10000 / M_actual_generated) * 100.0

print("=== Część II ===")
print(f"Liczba wygenerowanych kandydatów (M): {M_actual_generated}")
print(f"Liczba zaakceptowanych punktów: {len(X_accepted_part2)}")
print(f"Procentowy udział zaakceptowanych (10k / M): {accepted_ratio_part2:.2f}%")
print(f"Czas trwania symulacji (sekundy): {time_part2:.5f}\n")

###############################################################################
# Wykresy
###############################################################################

# 1. Histogram zaakceptowanych wartości z części I i II
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Część I
axes[0].hist(X_accepted_part1, bins=100, density=True, alpha=0.6, color='blue', edgecolor='black')
axes[0].set_title("Część I: Rozkład zaakceptowanych punktów (Hit-and-Miss)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("Gęstość")

# Nakreślamy teoretyczną krzywą N(0,1)
x_plot = np.linspace(-5, 5, 1000)
axes[0].plot(x_plot, normal_pdf(x_plot), 'r-', lw=2, label='Normal(0,1)')
axes[0].legend()

# Część II
axes[1].hist(X_accepted_part2, bins=100, density=True, alpha=0.6, color='green', edgecolor='black')
axes[1].set_title("Część II: Rozkład zaakceptowanych punktów (Dokładnie 10k)")
axes[1].set_xlabel("x")

axes[1].plot(x_plot, normal_pdf(x_plot), 'r-', lw=2, label='Normal(0,1)')
axes[1].legend()

plt.tight_layout()
plt.show()

# 2. Dodatkowy wykres: porównanie histogramów części I i II na jednym subplot
plt.figure(figsize=(10, 6))
plt.hist(X_accepted_part1, bins=100, density=True, alpha=0.6, color='blue', edgecolor='black', label='Część I')
plt.hist(X_accepted_part2, bins=100, density=True, alpha=0.4, color='green', edgecolor='black', label='Część II')
plt.plot(x_plot, normal_pdf(x_plot), 'r-', lw=2, label='Normal(0,1)')

plt.title("Porównanie histogramów części I i II")
plt.xlabel("x")
plt.ylabel("Gęstość")
plt.legend()
plt.tight_layout()
plt.show()
