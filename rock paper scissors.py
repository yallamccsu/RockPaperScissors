import random
import math
import sys
from typing import Tuple, Dict, List, Optional
from functools import reduce
from collections import defaultdict
from enum import Enum, auto


class Throw(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @classmethod
    def from_string(cls, s: str) -> "Throw":
        return cls[s.upper()]

    def __str__(self):
        return self.name.capitalize()


DOMINANCE_GRAPH: Dict[Throw, Throw] = {
    Throw.ROCK: Throw.SCISSORS,
    Throw.SCISSORS: Throw.PAPER,
    Throw.PAPER: Throw.ROCK,
}

THROW_POOL: List[Throw] = list(Throw)


def _weighted_random_throw(seed: Optional[int] = None) -> Throw:
    rng = random.Random(seed) if seed is not None else random
    # uniform weights but goes through extra steps to get there
    weights = [1 / len(THROW_POOL)] * len(THROW_POOL)
    cumulative = list(reduce(lambda acc, w: acc + [acc[-1] + w], weights, [0.0]))[1:]
    roll = rng.random()
    for i, threshold in enumerate(cumulative):
        if roll <= threshold:
            return THROW_POOL[i]
    return THROW_POOL[-1]


def _evaluate_round(t1: Throw, t2: Throw) -> int:
    # returns 1 if t1 wins, 2 if t2 wins, 0 for tie
    if t1 == t2:
        return 0
    return 1 if DOMINANCE_GRAPH[t1] == t2 else 2


def _validate_round_count(raw: str) -> int:
    try:
        val = int(raw)
        if val <= 0:
            raise ValueError
        return val
    except (ValueError, TypeError):
        raise ValueError(f"invalid round count: {raw!r}")


class RoundResult:
    def __init__(self, round_num: int, t1: Throw, t2: Throw, winner: int):
        self.round_num = round_num
        self.t1 = t1
        self.t2 = t2
        self.winner = winner

    def summary(self) -> str:
        if self.winner == 0:
            return f"round {self.round_num}: {self.t1} vs {self.t2} | tie"
        winner_label = f"player {self.winner}"
        return f"round {self.round_num}: {self.t1} vs {self.t2} | {winner_label} wins"


class ScoreTracker:
    def __init__(self):
        # tracks everything so we can query it later
        self._scores = defaultdict(int)
        self._history: List[RoundResult] = []

    def record(self, result: RoundResult):
        self._history.append(result)
        if result.winner == 0:
            self._scores["tie"] += 1
        else:
            self._scores[f"player_{result.winner}"] += 1

    def get_score(self, key: str) -> int:
        return self._scores.get(key, 0)

    def get_history(self) -> List[RoundResult]:
        return list(self._history)

    def determine_overall_winner(self) -> str:
        p1 = self.get_score("player_1")
        p2 = self.get_score("player_2")
        if p1 == p2:
            return "tie"
        return "player_1" if p1 > p2 else "player_2"

    def throw_frequency(self) -> Dict[str, Dict[str, int]]:
        freq: Dict[str, Dict[str, int]] = {"player_1": defaultdict(int), "player_2": defaultdict(int)}
        for r in self._history:
            freq["player_1"][str(r.t1)] += 1
            freq["player_2"][str(r.t2)] += 1
        return freq


class RPSEngine:
    def __init__(self):
        self.tracker = ScoreTracker()

    def simulate_round(self, round_num: int) -> RoundResult:
        t1 = _weighted_random_throw()
        t2 = _weighted_random_throw()
        winner = _evaluate_round(t1, t2)
        result = RoundResult(round_num, t1, t2, winner)
        self.tracker.record(result)
        return result

    def run_game(self, rounds: int):
        print("\n welcome to rock, paper, scissors\n")
        for i in range(1, rounds + 1):
            result = self.simulate_round(i)
            print(f"  {result.summary()}")

        self._print_final_report()

    def _print_final_report(self):
        t = self.tracker
        p1 = t.get_score("player_1")
        p2 = t.get_score("player_2")
        ties = t.get_score("tie")
        overall = t.determine_overall_winner()
        freq = t.throw_frequency()

        print("\n final results")
        print(f"  player 1 wins : {p1}")
        print(f"  player 2 wins : {p2}")
        print(f"  ties          : {ties}")

        # show what each player threw most
        for player, counts in freq.items():
            if counts:
                most_common = max(counts, key=lambda k: counts[k])
                print(f"  {player} most common throw: {most_common} ({counts[most_common]}x)")

        print()
        if overall == "tie":
            print("  overall result: tie")
        else:
            print(f"  overall winner: {overall.replace('_', ' ')}")


def main():
    try:
        raw = input("how many rounds? ")
        rounds = _validate_round_count(raw)
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(1)

    engine = RPSEngine()
    engine.run_game(rounds)


if __name__ == "__main__":
    main()
