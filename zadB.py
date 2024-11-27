# Ruina gracza dla 2 graczy A,B

pA = 0.5
# a+b=100
# Szukane P (ruiny A) do a
# oraz porównanie z teorią

from simulation_functions import get_probability_of_winning_equation, \
    get_probability_of_winning_simulation
import matplotlib.pyplot as plt

no_of_games = 1000
a_values = [1 * i for i in range(100)]

# Simulations
probability_of_playerB_winning_simulation = {}
for i in range(100):
    probability_of_playerB_winning_simulation[i] = get_probability_of_winning_simulation(
        playerA_chance=pA,
        playerA_money=a_values[i],
        playerB_money=100-a_values[i]
    ).probability_of_playerB_winning
ruins_counts = [ probability_of_playerB_winning_simulation[a_values[i]] for i in range(100) ]

# Equation
probability_of_playerB_winning = {}
for i in range(100):
    probability_of_playerB_winning[a_values[i]] = get_probability_of_winning_equation(
        pA,
        a_values[i],
        100-a_values[i]
    ).probability_of_playerB_winning
ruins_counts_eq = [ probability_of_playerB_winning[a_values[i]] for i in range(100) ]


# Plotting
plt.figure(figsize=(12, 7))
plt.plot(
    a_values, ruins_counts, marker='o', linestyle='-', color='purple',
    label='Number of Games Lost by Player A simulation'
)
plt.plot(
    a_values, ruins_counts_eq, marker='o', linestyle='-', color='blue',
    label='Number of Games Lost by Player A equation'
)
plt.title('Number of Games Lost by Player A vs. Initial Money of Player A (a)')
plt.xlabel('a (Initial Money of Player A)')
plt.ylabel('Number of Games Lost by Player A')
plt.grid(True)
plt.legend()
plt.show()