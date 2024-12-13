import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt

points_number = 10 ** 4
iteration_number = 10000
x_min = -5
x_max = 5


def analytical(x):
    ro = 1
    u = 0
    return (1 / (ro * math.sqrt(2 * math.pi))) * math.exp(-((x - u) ** 2) / (2 * (ro ** 2)))


def uniform_generator(min, max):
    u = random.random()
    x = min + (max - min) * u
    return x


def lorentz_density(x):
    return 1 / (math.pi * (x**2 + 1))


def hybrid_acceptance_rejection(x_min, x_max, points_number, iteration_number, C):
    points_inside = []
    x_random = []
    y_random = []

    for _ in range(iteration_number):
        x = uniform_generator(x_min, x_max)
        y = uniform_generator(0, lorentz_density(x) * C)

        x_random.append(x)
        y_random.append(y)

        if y <= analytical(x):
            points_inside.append(x)

        if len(points_inside) >= points_number:
            break
    return points_inside, x_random, y_random



def show_plot(x_random, y_random, title):
    plt.figure(figsize=(10, 6))

    plt.scatter(
        [x_random[i] for i in range(len(x_random)) if y_random[i] <= analytical(x_random[i])],
        [y_random[i] for i in range(len(x_random)) if y_random[i] <= analytical(x_random[i])],
        color="blue", s=1, label="Accepted"
    )

    # Punkty odrzucone
    plt.scatter(
        [x_random[i] for i in range(len(x_random)) if y_random[i] > analytical(x_random[i])],
        [y_random[i] for i in range(len(x_random)) if y_random[i] > analytical(x_random[i])],
        color="red", s=1, label="Rejected"
    )

    x_values = [x / 100.0 for x in range(-500, 501)]
    y_values = [analytical(x) for x in x_values]
    plt.plot(x_values, y_values, color="black", linewidth=2, label="Normal density")

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


def find_c():
    x_values = np.linspace(x_min, x_max, iteration_number)
    normal_values = np.array([analytical(x) for x in x_values])
    lorentz_values = np.array([lorentz_density(x) for x in x_values])

    return max(lorentz_values) / max(normal_values)


C = find_c()

start_time = time.time()

points_inside_acc_rej, x_acc_rej, y_acc_rej = hybrid_acceptance_rejection(x_min, x_max, points_number, iteration_number, C)

end_time = time.time() - start_time

acceptance_ratio = (len(points_inside_acc_rej) / iteration_number) * 100

print(f"Maximum C: {C}")
print(f"Wygenerowano {len(points_inside_acc_rej)} liczb z rozkładu normalnego.")
print(f"Procentowy udział trafień: {acceptance_ratio:.2f}%")
print(f"Czas symulacji: {end_time:.4f} s")

show_plot(x_acc_rej, y_acc_rej, "Hybrydowa metoda eliminacji: generowanie liczb z rozkładu normalnego")

