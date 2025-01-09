import numpy as np
import time
from scipy.stats import norm


def normal_pdf(x):
    """Funkcja gęstości rozkładu normalnego standardowego."""
    return norm.pdf(x)


def metoda_akceptacji_eliminacji(n_punkty, a, b, M):
    """
    Metoda akceptacji/eliminacji (Acceptance-Rejection).

    Parametry:
    - n_punkty: liczba punktów do wygenerowania.
    - a, b: przedział rozkładu propozycji (np. uniform).
    - M: stała zapewniająca, że f(x) <= M * g(x) dla wszystkich x.

    Zwraca:
    - liczba zaakceptowanych punktów
    - czas wykonania symulacji
    """
    start_time = time.time()

    # Generowanie punktów z rozkładu propozycji (uniform)
    x = np.random.uniform(a, b, n_punkty)
    u = np.random.uniform(0, 1, n_punkty)

    # Obliczanie warunku akceptacji
    f_x = normal_pdf(x)
    g_x = 1 / (b - a)  # PDF rozkładu uniform
    akceptacja = u < (f_x) / (M * g_x)

    liczba_zaakceptowanych = np.sum(akceptacja)

    end_time = time.time()
    czas = end_time - start_time

    return liczba_zaakceptowanych, czas


def metoda_hit_and_miss(n_zaakceptowanych, a, b, M):
    """
    Metoda hit-and-miss.

    Parametry:
    - n_zaakceptowanych: liczba punktów do zaakceptowania.
    - a, b: przedział rozkładu propozycji (np. uniform).
    - M: stała zapewniająca, że f(x) <= M * g(x) dla wszystkich x.

    Zwraca:
    - całkowita liczba wygenerowanych punktów
    - czas wykonania symulacji
    """
    start_time = time.time()

    liczba_zaakceptowanych = 0
    liczba_propozycji = 0

    while liczba_zaakceptowanych < n_zaakceptowanych:
        # Generowanie w partiach dla efektywności
        batch_size = min(n_zaakceptowanych - liczba_zaakceptowanych, 100000)
        x = np.random.uniform(a, b, batch_size)
        u = np.random.uniform(0, 1, batch_size)

        f_x = normal_pdf(x)
        g_x = 1 / (b - a)
        akceptacja = u < (f_x) / (M * g_x)

        zaakceptowane = np.sum(akceptacja)
        liczba_zaakceptowanych += zaakceptowane
        liczba_propozycji += batch_size

    end_time = time.time()
    czas = end_time - start_time

    return liczba_propozycji, czas


def main():
    # Parametry rozkładu propozycji
    a = -10
    b = 10
    M = 8  # Stała dla metody akceptacji/eliminacji

    # Krok 1: Metoda akceptacji/eliminacji
    n_punkty = 10000
    liczba_zaakceptowanych, czas1 = metoda_akceptacji_eliminacji(n_punkty, a, b, M)
    procent_zaakceptowanych = (liczba_zaakceptowanych / n_punkty) * 100

    print("Metoda Akceptacji/Eliminacji:")
    print(f"Liczba wygenerowanych punktów: {n_punkty}")
    print(f"Liczba zaakceptowanych punktów: {liczba_zaakceptowanych}")
    print(f"Procent zaakceptowanych: {procent_zaakceptowanych:.2f}%")
    print(f"Czas wykonania: {czas1:.4f} sekund\n")

    # Krok 2: Metoda Hit-and-Miss
    n_zaakceptowanych = 10000
    liczba_propozycji, czas2 = metoda_hit_and_miss(n_zaakceptowanych, a, b, M)
    procent_zaakceptowanych_hit = (n_zaakceptowanych / liczba_propozycji) * 100

    print("Metoda Hit-and-Miss:")
    print(f"Liczba zaakceptowanych punktów: {n_zaakceptowanych}")
    print(f"Całkowita liczba wygenerowanych punktów: {liczba_propozycji}")
    print(f"Procent zaakceptowanych: {procent_zaakceptowanych_hit:.2f}%")
    print(f"Czas wykonania: {czas2:.4f} sekund")


if __name__ == "__main__":
    main()
