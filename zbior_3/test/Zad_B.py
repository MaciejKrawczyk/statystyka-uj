import math
import random
import numpy as np
import matplotlib.pyplot as plt

def box_muller_generator():
    x1 = random.random()
    x2 = random.random()
    y1 = math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi * x2)
    return y1

def exponential_generator():
    u = random.random()
    lam = 1
    # F(x) = 1−e^(−λx)
    # u = 1−e ^ (−λx)
    # x= −ln(1−u) / λ

    x = -math.log(1 - u) / lam
    return x

def uniform_generator():
    start = 0
    end = 1
    u = random.random()
    x = start + (end - start) * u
    return x

def sum_of_generated(n, expected_sum, generator_fun):
    sums = []
    for i in range(n):
        total = 0
        for _ in range(expected_sum):
            total += generator_fun()
        sums.append(total)
    return sums


def show_plot(differences, title):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(differences, bins=50, alpha=0.7, color='blue', density=True)
    plt.title(title)
    plt.xlabel('Różnica')
    plt.ylabel('Liczba wystąpień')
    plt.grid(True)

    # Histogram z logarytmiczną skalą na osi pionowej
    plt.subplot(1, 2, 2)
    plt.hist(differences, bins=50, alpha=0.7, color='blue', density=True)
    plt.yscale('log')
    plt.title('Histogram różnic (logarytmiczna skala)')
    plt.xlabel('Różnica')
    plt.ylabel('Liczba wystąpień (log)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


iteration_number = 10000
bins = 50
expected_sum = 10

# A ----------------------------------------------------------------------------------------

# Rozkład normalny

sums_normal = sum_of_generated(iteration_number, expected_sum, box_muller_generator)
plt.figure(figsize=(10, 6))
plt.hist(sums_normal, bins=bins, density=True, alpha=0.7, color='blue', label='Normalny')
plt.title(f'Sumy 10 liczb z rozkładu normalnego')
plt.xlabel('Wartość sumy')
plt.ylabel('Gęstość')
plt.grid()
plt.legend()
plt.show()


# Rozkład wykładniczy

sums_normal = sum_of_generated(iteration_number, expected_sum, exponential_generator)
plt.figure(figsize=(10, 6))
plt.hist(sums_normal, bins=bins, density=True, alpha=0.7, color='blue', label='Normalny')
plt.title(f'Sumy 10 liczb z rozkładu normalnego')
plt.xlabel('Wartość sumy')
plt.ylabel('Gęstość')
plt.grid()
plt.legend()
plt.show()

# Rozkład jednorodny

sums_normal = sum_of_generated(iteration_number, expected_sum, uniform_generator)
plt.figure(figsize=(10, 6))
plt.hist(sums_normal, bins=bins, density=True, alpha=0.7, color='blue', label='Normalny')
plt.title(f'Sumy 10 liczb z rozkładu normalnego')
plt.xlabel('Wartość sumy')
plt.ylabel('Gęstość')
plt.grid()
plt.legend()
plt.show()


# B ----------------------------------------------------------------------------------------

box_muller_generations = [box_muller_generator() for _ in range(iteration_number)]
exponential_generations = [exponential_generator() for _ in range(iteration_number)]
uniform_generations = [uniform_generator() for _ in range(iteration_number)]

box_muller_generations.sort()
exponential_generations.sort()
uniform_generations.sort()

differences_normal = np.diff(box_muller_generations)
show_plot(differences_normal, "Histogram różnic między próbkami dla rozkładu normalnego")

differences_exponential = np.diff(exponential_generations)
show_plot(differences_exponential, "Histogram różnic między próbkami dla rozkładu wykładniczego")

differences_exponential = np.diff(uniform_generations)
show_plot(uniform_generator(), "Histogram różnic między próbkami dla rozkładu jednorodnego")