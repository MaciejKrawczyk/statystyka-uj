import random


def simulate_game_eq1(player1_chance: float, player1_money: int, player2_money: int):
    p = player1_chance
    q = 1 - p
    a = player1_money
    b = player2_money
    M = a + b
    if p != 0.5:
        pRuinA = ((q / p) ** a - (q / p) ** M) / (1 - (q / p) ** M)
    else:
        pRuinA = (M - a) / M
    return {
        "no_of_turns": 0,
        "playerA_wins": pRuinA > 0.5,
        "playerB_wins": pRuinA < 0.5,
    }


def simulate_game1(
        player1_chance: float,
        player1_money: int,
        player2_money: int
):
    while True:
        if player1_money <= 0 or player2_money <= 0:
            break  # Stop if a player runs out of money

        # Simulate a turn
        outcome = random.random()
        # print(outcome)
        if outcome < player1_chance:
            # Player 1 wins
            player1_money += 1
            player2_money -= 1
        else:
            # Player 2 wins
            player1_money -= 1
            player2_money += 1

    return {
        "no_of_turns": 0,
        "playerA_wins": player2_money == 0,
        "playerB_wins": player1_money == 0,
    }
