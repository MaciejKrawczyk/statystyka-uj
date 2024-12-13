import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_sums = 10000  # Number of sums for the first part
num_samples = 100000  # Number of samples for the second part

# Generating data and calculating sums
np.random.seed(42)

# a) Normal distribution
normal_data = np.random.normal(size=(num_sums, 100))
normal_sums = np.sum(normal_data, axis=1)

# b) Exponential distribution
exponential_data = np.random.exponential(scale=1.0, size=(num_sums, 100))
exponential_sums = np.sum(exponential_data, axis=1)

# c) Uniform distribution
uniform_data = np.random.uniform(low=0.0, high=1.0, size=(num_sums, 100))
uniform_sums = np.sum(uniform_data, axis=1)

# Plotting histograms for sums
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(normal_sums, bins=50, density=True, alpha=0.7, color='blue')
plt.title("Sum of 100 Normal Random Variables")

plt.subplot(1, 3, 2)
plt.hist(exponential_sums, bins=50, density=True, alpha=0.7, color='green')
plt.title("Sum of 100 Exponential Random Variables")

plt.subplot(1, 3, 3)
plt.hist(uniform_sums, bins=50, density=True, alpha=0.7, color='orange')
plt.title("Sum of 100 Uniform Random Variables")

plt.tight_layout()
plt.show()

# Large samples for the second part
normal_large = np.random.normal(size=num_samples)
exponential_large = np.random.exponential(scale=1.0, size=num_samples)
uniform_large = np.random.uniform(low=0.0, high=1.0, size=num_samples)

# Sorting the data
normal_large_sorted = np.sort(normal_large)
exponential_large_sorted = np.sort(exponential_large)
uniform_large_sorted = np.sort(uniform_large)

# Differences between consecutive elements
normal_differences = np.diff(normal_large_sorted)
exponential_differences = np.diff(exponential_large_sorted)
uniform_differences = np.diff(uniform_large_sorted)

# Plotting histograms for differences
plt.figure(figsize=(15, 10))

plt.subplot(3, 2, 1)
plt.hist(normal_differences, bins=50, density=True, alpha=0.7, color='blue')
plt.title("Differences: Normal Distribution")

plt.subplot(3, 2, 2)
plt.hist(normal_differences, bins=50, density=True, alpha=0.7, log=True, color='blue')
plt.title("Log-Scale: Normal Distribution")

plt.subplot(3, 2, 3)
plt.hist(exponential_differences, bins=50, density=True, alpha=0.7, color='green')
plt.title("Differences: Exponential Distribution")

plt.subplot(3, 2, 4)
plt.hist(exponential_differences, bins=50, density=True, alpha=0.7, log=True, color='green')
plt.title("Log-Scale: Exponential Distribution")

plt.subplot(3, 2, 5)
plt.hist(uniform_differences, bins=50, density=True, alpha=0.7, color='orange')
plt.title("Differences: Uniform Distribution")

plt.subplot(3, 2, 6)
plt.hist(uniform_differences, bins=50, density=True, alpha=0.7, log=True, color='orange')
plt.title("Log-Scale: Uniform Distribution")

plt.tight_layout()
plt.show()

# Commentary:
# The Central Limit Theorem explains the results of the sums for large samples.
# Differences between sorted values highlight the underlying distribution's density.
