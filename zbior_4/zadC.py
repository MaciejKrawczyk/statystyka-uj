import numpy as np
import matplotlib.pyplot as plt


# Funkcja generująca czasy przychodzenia lub wykonywania zadań
def generate_interarrival_times(rate, size):
    return -np.log(1 - np.random.uniform(0, 1, size)) / rate


# Symulacja procesu kolejkowego z obliczaniem czasu w systemie i liczby zadań w systemie
def simulate_queue_little(lambda_arrival, lambda_service, simulation_time):
    time = 0
    queue = []
    total_time_in_system = 0
    total_tasks = 0
    queue_lengths = []

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

            arrival_time = queue.pop(0)
            total_time_in_system += time - arrival_time
            total_tasks += 1

            if len(queue) > 0:
                next_service_end = time + service_times[service_index]
                service_index += 1
            else:
                next_service_end = float('inf')

        queue_lengths.append(len(queue))

    avg_tasks_in_system = np.mean(queue_lengths)
    avg_time_in_system = total_time_in_system / total_tasks if total_tasks > 0 else 0

    return avg_time_in_system, avg_tasks_in_system


# Parametry symulacji
simulation_time = 10_000
num_simulations = 1000
scenarios = [
    (1 / 20, 1 / 15, "λA=1/20, λS=1/15"),
    (1 / 20, 1 / 100, "λA=1/20, λS=1/100"),
    (1 / 20, 1 / 5, "λA=1/20, λS=1/5")
]

# Symulacja i weryfikacja prawa Little’a
results = []
for lambda_arrival, lambda_service, label in scenarios:
    total_avg_time_in_system = 0
    total_avg_tasks_in_system = 0

    for _ in range(num_simulations):
        avg_time_in_system, avg_tasks_in_system = simulate_queue_little(lambda_arrival, lambda_service, simulation_time)
        total_avg_time_in_system += avg_time_in_system
        total_avg_tasks_in_system += avg_tasks_in_system

    avg_time_in_system = total_avg_time_in_system / num_simulations
    avg_tasks_in_system = total_avg_tasks_in_system / num_simulations

    little_result = avg_time_in_system * lambda_arrival

    results.append((label, avg_time_in_system, avg_tasks_in_system, little_result, lambda_arrival))

# Wyświetlanie wyników
import pandas as pd

results_df = pd.DataFrame(results, columns=["Scenario", "E(R) (sredni czas w systemie)",
                                            "E(x) (srednia liczba zadan w systemie)", "E(R)*lambda_A (Little)",
                                            "lambda_A"])

# Wykres wyników
fig, ax = plt.subplots(figsize=(10, 6))
for index, row in results_df.iterrows():
    ax.bar(row["Scenario"], row["E(x) (srednia liczba zadan w systemie)"], label=f"E(x) for {row['Scenario']}")

ax.set_title("Wyniki symulacji prawa Little'a")
ax.set_ylabel("E(x) (średnia liczba zadań w systemie)")
ax.set_xlabel("Scenario")
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
