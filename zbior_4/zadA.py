import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_rate = 1  # Rate parameter λ [1/min]
time_end = 90    # Total observation time [min]

# Function to generate exponential samples using inverse transform method
def generate_exponential_inverse_transform(lambda_rate, size=1):
    u = np.random.uniform(0, 1, size)  # Generate uniform random variables
    t = -np.log(1 - u) / lambda_rate   # Apply the inverse CDF of exponential distribution
    return t

# Generate inter-arrival times using the inverse transform method
np.random.seed(42)  # For reproducibility
inter_arrival_times = generate_exponential_inverse_transform(lambda_rate, size=1000)

# Generate event times
event_times = np.cumsum(inter_arrival_times)

# Filter events within the observation period
event_times = event_times[event_times <= time_end]

# Generate a trajectory (time vs event count)
event_counts = np.arange(1, len(event_times) + 1)

# Plot the Poisson process trajectory
plt.figure(figsize=(10, 6))
plt.step(event_times, event_counts, where="post")
plt.title("Poisson Process Trajectory (λ = 1 [1/min])")
plt.xlabel("Time [min]")
plt.ylabel("Event Count")
plt.grid(True)
plt.show()
