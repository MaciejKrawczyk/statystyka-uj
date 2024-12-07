# Możliwości:
# x = 0 (0 zalogowanych użytkowników na serwerze)
# x = 1 (1 zalogowany użytkownik na serwerze)
# x = 2 (2 zalogowanych użytkowników na serwerze)
# Prawdopodobieństwo logowania:
#
# Niezalogowani użytkownicy:
#   P logowania = 0.2
#   P pozostania niezalogowanym = 0.8
# Zalogowani użytkownicy:
#   P wylogowania = 0.5
#   P pozostania zalogowanym = 0.5

import numpy as np

all_possible_states = 2  # login/logout
p_login_logout = 0.5
p_login_stay = 0.5
p_logout_login = 0.2
p_logout_stay = 0.8

P = np.array([
    [p_logout_stay * p_logout_stay, p_logout_login * p_logout_stay * all_possible_states,
     p_logout_login * p_logout_login],
    [p_logout_stay * p_login_logout, p_login_stay * p_logout_stay + p_login_logout * p_logout_login,
     p_login_stay * p_logout_login],
    [p_login_logout * p_login_logout, p_login_logout * p_login_stay * 2, p_login_stay * p_login_stay]
])

P_p = np.array([
    [0.8, 0.2, 0],
    [0.5, 0.50, 0],
    [0.0, 0.50, 0.5]
])