import math
import random
import numpy as np
import matplotlib.pyplot as plt

def box_muller_generator(iteration_number):
    values = []
    for i in range(iteration_number):
        x1 = random.random()
        x2 = random.random()
        y1 = math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi * x2)
        y2 = math.sqrt(-2 * math.log(x1)) * math.sin(2 * math.pi * x2)
        values.append(y1)
        values.append(y2)
    return values


def analytical(x):
    ro = 1
    u = 0
    return (1 / (ro * math.sqrt(2 * math.pi))) * math.exp(-((x - u) ** 2) / (2 * (ro ** 2)))

iteration_number = 10000
bins = 50

samples = box_muller_generator(iteration_number)
hist, bin_edges = np.histogram(samples, bins=bins, density=True)

bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

x = np.linspace(min(bin_edges), max(bin_edges), 1000)
fx = []
for i in x:
    fx.append(analytical(i))

plt.figure(figsize=(10, 6))
plt.hist(samples, bins=bins, density=True, alpha=0.6, color='blue', label='Histogram próbek')
plt.plot(x, fx, color='red', linewidth=2, label='Funkcja analityczna N(0,1)')
plt.title('Rozkład normalny N(0,1) - Histogram i Funkcja Analityczna')
plt.xlabel('Wartość')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend()
plt.grid()
plt.show()
