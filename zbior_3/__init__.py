import math
import random


# Function to calculate the PDF of a normal distribution
def normal_probability_density_function(x, mean, std_dev):
    """
    mean -  μ
    std_dev -  σ
    """
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))


def get_box_muller_random_numbers(x1, x2):
    y1 = math.sqrt((-2 * math.log(x1))) * math.cos(2 * math.pi * x2)
    y2 = math.sqrt((-2 * math.log(x1))) * math.sin(2 * math.pi * x2)
    return y1, y2


# Generate random numbers using Box-Muller Transform
def generate_normal_random_numbers(n_samples):
    random_numbers = []
    for _ in range(n_samples // 2):  # Each iteration produces 2 samples
        x1, x2 = random.random(), random.random()
        y1, y2 = get_box_muller_random_numbers(x1, x2)
        random_numbers.extend([y1, y2])
    return random_numbers