# generowanie liczb losowych metodą boxa-mullera
# https://www.if.pw.edu.pl/~agatka/numeryczne/wyklad_12.pdf -> str 13

# U - zmienna losowa

import numpy as np
import matplotlib.pyplot as plt

from zbior_3 import normal_probability_density_function, generate_normal_random_numbers

# Generate random numbers
n_samples = 100000
normal_random_numbers = generate_normal_random_numbers(n_samples)

# Plot histogram of generated random numbers
plt.hist(normal_random_numbers, bins=50, density=False, alpha=0.6, label='Histogram (Generated Data)')
# density tak dostosowuje wykres, aby sumarycznie, pola wszystkich słupków sumowały sie do 1

# Overlay the analytical normal distribution
mean = 0
std_dev = 1
x_values = np.linspace(-4, 4, 500)
pdf_values = [normal_probability_density_function(x, mean, std_dev) for x in x_values]
plt.plot(x_values, pdf_values, label='Analytical PDF', color='red')

# Add labels and legend
plt.title("Histogram of Generated Numbers vs Analytical PDF")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()
