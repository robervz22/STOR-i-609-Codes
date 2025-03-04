import random
from itertools import product

"""
Class PigGame
    Arguments:
    -num_players: Number of players
    -num_dices : Number of dices
    -target: Game's target value
"""


class PigGame:
    # Construction
    def __init__(self, num_players: int, num_dices: int, target: int):
        self.num_players = num_players
        self.num_dices = num_dices
        self.target = target
        self.scores = num_players * [0]
        # Additional data
        self.prob_failure = 1 - (5 / 6) ** self.num_dices
        dice_values = range(2, 7)
        outcomes = product(dice_values, repeat=self.num_dices)
        self.ev = ((1 / 5) ** self.num_dices) * sum(
            sum(outcome) for outcome in outcomes
        )

    """
    Strategies: Function that applies an strategy given a strike 
        Arguments:
        - round: List of the corresponding rollings of a player
        - player id: Index of player
        - id_strategy: The strategy corresponding to the player id. Possible values: "Random", "Hold", "Expectation"
        Output:
        - hold: True if the strategy decides to hold, False otherwise
    """

    def strategy(self, round: list[int], player_id: int, id_strategy="Random") -> bool:
        if id_strategy == "Random":
            if (
                random.uniform(0, 1) < 0.5
                or self.scores[player_id] + sum(round) >= self.target
            ):
                hold = True
            else:
                hold = False
            return hold

        if id_strategy == "Hold":
            if len(round) == 5 or self.scores[player_id] + sum(round) >= self.target:
                hold = True
            else:
                hold = False
            return hold

        if id_strategy == "Expectation":
            payoff = (1 - self.prob_failure) * (self.ev) - self.prob_failure * sum(
                round
            )
            if payoff < 0 or self.scores[player_id] + sum(round) >= self.target:
                hold = True
            else:
                hold = False
            return hold

    """
    Play: Function that plays one pig game
        Arguments:
        -strategies: List of strategies corresponding to each player
        Output:
        -index of the strategy that wins the game. If returns -1 it means that the maximum number of rounds was wasted.
            It returns -2 if theres is an error 
    """

    def play(self, strategies: list) -> int:
        if len(strategies) != self.num_players:
            print("Error: Number of strategies should be the same as number of players")
            return -2
        iter_max = 1000
        count, round, player_id = 0, [], 0
        while all(x < self.target for x in self.scores) and count < iter_max:
            roll_value = random.sample(range(1, 7), self.num_dices)
            # finish game
            if any(x == 1 for x in roll_value):
                player_id = (player_id + 1) % self.num_players
                round = []
            # make a decision
            else:
                round.append(sum(roll_value))
                hold = self.strategy(round, player_id, strategies[player_id])
                if hold:
                    self.scores[player_id] = self.scores[player_id] + sum(round)
                    round = []
                    player_id = (player_id + 1) % self.num_players
            if player_id == 0:
                count += 1

        # check if the maximum number of runs was reached
        if count < iter_max:
            max_score = max(self.scores)
            if max_score >= self.target:
                argmax_score = self.scores.index(max_score)
                return argmax_score  # returns the index of the winner
        else:
            max_score = max(self.score)
            if max_score >= self.target:
                argmax_score = self.score.index(max_score)
                return argmax_score
            return -1  # returns -1 if there is not winner after iter max

    """
    Reset: Function that resets the scores of the players
    """

    def reset(self):
        self.scores = self.num_players * [0]


# Define class
pig_game = PigGame(3, 2, 50)
strategies = ["Random", "Hold", "Expectation"]

# Try several games
random.seed(12345)  # seed for replicability
simulation = []  # store index of winners
for _ in range(1000):
    simulation.append(pig_game.play(strategies))
    pig_game.reset()

# Print number of games won by each strategy
for i in range(len(strategies)):
    print(
        f"Strategy {strategies[i]} won {simulation.count(i)} games of {len(simulation)}"
    )
