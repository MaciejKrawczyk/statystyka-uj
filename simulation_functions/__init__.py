from asyncio.windows_events import INFINITE
from dataclasses import dataclass
from random import random


class GameOutcome:
    def __init__(self, playerA_wins: bool, playerB_wins: bool, no_of_turns: int, final_playerA_money: int = -1,
                 final_playerB_money: int = -1, playerA_won_turns: list[bool] = [], playerB_won_turns: list[bool] = []):
        self.playerA_wins = playerA_wins
        self.playerB_wins = playerB_wins
        self.no_of_turns = no_of_turns
        self.final_playerA_money = final_playerA_money
        self.final_playerB_money = final_playerB_money
        self.playerA_won_turns = playerA_won_turns
        self.playerB_won_turns = playerB_won_turns


@dataclass
class GameOutcome2:
    probability_of_playerB_winning: float
    probability_of_playerA_winning: float
    no_of_turns_per_game: list[int]
    no_of_games: int
    no_of_playerA_money_per_turn_per_game: list[list[int]]
    no_of_playerB_money_per_turn_per_game: list[list[int]]

@dataclass
class GameOutcomeEq:
    probability_of_playerB_winning: float
    probability_of_playerA_winning: float


def get_probability_of_winning_simulation(playerA_chance: float, playerA_money: int, playerB_money: int,
                                          no_of_games=100, no_of_turns_per_game_loop=1000000000) -> GameOutcome2:
    print(f"playerA chance: {playerA_chance}, playerA_money: {playerA_money}, playerB_money: {playerB_money}")
    games_won_by_playerA = 0
    games_won_by_playerB = 0
    no_of_turns_per_game = []
    no_of_playerA_money_per_turn_per_game = []
    no_of_playerB_money_per_turn_per_game = []

    for _ in range(no_of_games):
        current_playerA_money = playerA_money
        current_playerB_money = playerB_money
        turns = 0
        playerA_money_per_turn = []
        playerB_money_per_turn = []

        while turns < no_of_turns_per_game_loop:
            if current_playerA_money == 0:
                games_won_by_playerB += 1
                break
            elif current_playerB_money == 0:
                games_won_by_playerA += 1
                break

            if random() < playerA_chance:
                current_playerA_money += 1
                current_playerB_money -= 1
            else:
                current_playerA_money -= 1
                current_playerB_money += 1

            playerA_money_per_turn.append(current_playerA_money)
            playerB_money_per_turn.append(current_playerB_money)
            turns += 1

        no_of_turns_per_game.append(turns)
        no_of_playerA_money_per_turn_per_game.append(playerA_money_per_turn)
        no_of_playerB_money_per_turn_per_game.append(playerB_money_per_turn)
    print(f"games_won_A: {games_won_by_playerA}, games_won_B: {games_won_by_playerB}")
    return GameOutcome2(
        probability_of_playerB_winning=games_won_by_playerB / no_of_games,
        probability_of_playerA_winning=games_won_by_playerA / no_of_games,
        no_of_turns_per_game=no_of_turns_per_game,
        no_of_games=no_of_games,
        no_of_playerA_money_per_turn_per_game=no_of_playerA_money_per_turn_per_game,
        no_of_playerB_money_per_turn_per_game=no_of_playerB_money_per_turn_per_game,
    )


def simulate_game(
        playerA_chance: float,
        playerA_money: int,
        playerB_money: int,
        max_turns: int = 1000
) -> GameOutcome:
    i = 0
    playerA_won_turns = []
    playerB_won_turns = []
    for _ in range(max_turns):
        if playerA_money == 0 or playerB_money == 0:
            break

        outcome = random()
        if outcome < playerA_chance:
            # Player 1 wins
            playerA_won_turns.append(True)
            playerB_won_turns.append(False)
            playerA_money += 1
            playerB_money -= 1
        else:
            # Player 2 wins
            playerA_won_turns.append(False)
            playerB_won_turns.append(True)
            playerA_money -= 1
            playerB_money += 1
        i += 1
    return GameOutcome(
        playerA_wins=playerB_money == 0,
        playerB_wins=playerA_money == 0,
        no_of_turns=i,
        final_playerA_money=playerA_money,
        final_playerB_money=playerB_money,
        playerA_won_turns=playerA_won_turns,
        playerB_won_turns=playerB_won_turns
    )


def get_probability_of_winning_equation(playerA_chance_of_winning: float, playerA_money: int,
                                        playerB_money: int) -> GameOutcomeEq:
    p = playerA_chance_of_winning
    q = 1 - p  # playerB_chance
    a = playerA_money
    b = playerB_money
    M = a + b
    if p != 0.5:
        pRuinA = ((q / p) ** a - (q / p) ** M) / (1 - (q / p) ** M)
    else:
        pRuinA = (M - a) / M
    return GameOutcomeEq(
        probability_of_playerB_winning=pRuinA,
        probability_of_playerA_winning=1 - pRuinA,
    )


def simulate_game_eq(playerA_chance: float, playerA_money: int, playerB_money: int,
                     max_turns: int = 1000) -> GameOutcome:
    p = playerA_chance
    q = 1 - p  # playerB_chance
    a = playerA_money
    b = playerB_money
    M = a + b
    i = 0
    playerA_won_turns = []
    playerB_won_turns = []
    for _ in range(max_turns):
        if a == 0 or b == 0:
            break

        outcome = random()
        if p != 0.5:
            pRuinA = ((q / p) ** a - (q / p) ** M) / (1 - (q / p) ** M)
            if outcome > pRuinA:
                # Player 1 wins
                playerA_won_turns.append(True)
                playerB_won_turns.append(False)
                a += 1
                b -= 1
            else:
                # Player 2 wins
                playerA_won_turns.append(False)
                playerB_won_turns.append(True)
                a -= 1
                b += 1
        else:
            pRuinA = 1 - (a / M)
            if outcome > pRuinA:
                # Player 1 wins
                playerA_won_turns.append(True)
                playerB_won_turns.append(False)
                a += 1
                b -= 1
            else:
                # Player 2 wins
                playerA_won_turns.append(False)
                playerB_won_turns.append(True)
                a -= 1
                b += 1

        i += 1

    return GameOutcome(
        playerA_wins=b == 0,
        playerB_wins=a == 0,
        no_of_turns=i,
        final_playerA_money=a,
        final_playerB_money=b,
        playerA_won_turns=playerA_won_turns,
        playerB_won_turns=playerB_won_turns
    )
