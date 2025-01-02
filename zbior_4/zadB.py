"""
Symulacja procesu kolejkowego (na podstawie procesu Poissona)

Legenda:
- Tempo przychodzenia zadań do serwera: λA
- Odstęp czasu pomiędzy przychodzeniem nowych zadań: tiA=-(ln(1-n))/λA, gdzie n→Uniform(0,1)
- Tempo wykonywania zadań przez serwer: λS
- Czas wykonywania kolejnych zadań: tiS=-(ln(1-n))/λS, gdzie n→Uniform(0,1)
Jednocześnie serwer może wykonywać tylko jedno zadanie.

Zadanie:
Stworzyć wykres
a) liczby zadań w kolejce od czasu
b) liczby wykonanych zadań od czasu dla
I) λA = 1/20 i λS = 1/15
II) λA = 1/20 i λS = 1/100
III) λA = 1/20 i λS = 1/5
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametry symulacji
simulation_time = 1000  # Całkowity czas symulacji

# Funkcja generująca czasy przychodzenia lub wykonywania zadań
def generate_interarrival_times(rate, size):
    return -np.log(1 - np.random.uniform(0, 1, size)) / rate

# Symulacja procesu kolejkowego
def simulate_queue(lambda_arrival, lambda_service, simulation_time):
    time = 0
    queue = []
    completed_tasks = 0
    queue_lengths = []
    completed_tasks_over_time = []

    # Generowanie czasów przychodzenia i obsługi zadań
    arrival_times = generate_interarrival_times(lambda_arrival, 10000)
    service_times = generate_interarrival_times(lambda_service, 10000)

    next_arrival = arrival_times[0]
    next_service_end = float('inf')
    arrival_index = 0
    service_index = 0

    while time < simulation_time:
        if next_arrival <= next_service_end:
            time = next_arrival
            queue_lengths.append(len(queue))
            completed_tasks_over_time.append(completed_tasks)

            if len(queue) == 0:
                next_service_end = time + service_times[service_index]
                service_index += 1
            queue.append(time)
            arrival_index += 1
            if arrival_index < len(arrival_times):
                next_arrival = time + arrival_times[arrival_index]
            else:
                next_arrival = float('inf')
        else:
            time = next_service_end
            queue_lengths.append(len(queue))
            completed_tasks_over_time.append(completed_tasks)

            queue.pop(0)
            completed_tasks += 1

            if len(queue) > 0:
                next_service_end = time + service_times[service_index]
                service_index += 1
            else:
                next_service_end = float('inf')

    return queue_lengths, completed_tasks_over_time

# Wartości parametrów
scenarios = [
    (1/20, 1/15, "\u03bbA=1/20, \u03bbS=1/15"),
    (1/20, 1/100, "\u03bbA=1/20, \u03bbS=1/100"),
    (1/20, 1/5, "\u03bbA=1/20, \u03bbS=1/5")
]

# Wykresy
for lambda_arrival, lambda_service, label in scenarios:
    queue_lengths, completed_tasks_over_time = simulate_queue(lambda_arrival, lambda_service, simulation_time)

    plt.figure()
    plt.plot(queue_lengths, label="Liczba zada\u0144 w kolejce")
    plt.plot(completed_tasks_over_time, label="Liczba wykonanych zada\u0144")
    plt.title(f"Symulacja procesu kolejkowego ({label})")
    plt.xlabel("Czas")
    plt.ylabel("Liczba zada\u0144")
    plt.legend()
    plt.grid()
    plt.show()
