# Two-Player RPS Simulation Engine

A Python-based Rock, Paper, Scissors simulation engine for two automated 
players. Tracks round outcomes, win streaks, and throw frequency across a 
full session, then generates a structured post-game report.

## Features

- Simulates any number of rounds between two automated players
- Tracks wins, losses, and ties across the full session
- Computes each player's longest consecutive win streak
- Records throw frequency and identifies each player's most used throw
- Full input validation with clean error handling
- Post-game summary report printed automatically at session end

## How to Run

```bash
python "rock paper scissors.py"
```

No external dependencies. Requires Python 3 with a standard installation.

## Sample Output

```
  round 1: rock vs scissors | player 1 wins
  round 2: paper vs paper | tie
  round 3: scissors vs rock | player 2 wins
  ...

  final score
  ------------------------------
  player 1 wins  : 5
  player 2 wins  : 3
  ties           : 2

  longest streaks
  player 1       : 3
  player 2       : 2

  most thrown
  player 1       : rock (4x)
  player 2       : scissors (5x)

  overall winner: player 1
```

## Technical Highlights

- `Throw` enum replaces raw strings for clean outcome representation
- Dominance graph dictionary drives all win logic independently of display
- `RoundResult` dataclass captures the full state of every round
- `GameReport` auto-computes all stats including streaks and frequency on initialization
- `RPSEngine` maintains an isolated RNG and full session log
- Rendering logic fully separated from simulation logic

## Tech Stack

Python 3 | dataclasses | enums | functools | collections
