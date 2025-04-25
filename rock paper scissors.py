import random

# Simulates a single Rock, Paper, Scissors throw
def throw_rps():
    """Returns 'Rock', 'Paper', or 'Scissors' at random"""
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)

# Determines the winner of one round
def play_round(player1_throw, player2_throw):
    """
    Compares two throws and prints the round result.
    """
    outcomes = {
        ('Rock', 'Scissors'): 'Player 1 wins the round',
        ('Scissors', 'Rock'): 'Player 2 wins the round',
        ('Paper', 'Rock'): 'Player 1 wins the round',
        ('Rock', 'Paper'): 'Player 2 wins the round',
        ('Scissors', 'Paper'): 'Player 1 wins the round',
        ('Paper', 'Scissors'): 'Player 2 wins the round',
    }

    if player1_throw == player2_throw:
        print(f"Both players threw {player1_throw}. It's a tie!")
    else:
        result = outcomes.get((player1_throw, player2_throw))
        print(f"Player 1: {player1_throw} | Player 2: {player2_throw} → {result}")

# Runs the whole game
def main():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    player1_score = 0
    player2_score = 0
    tie_score = 0

    try:
        rounds = int(input("How many rounds would you like to play? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        player1_throw = throw_rps()
        player2_throw = throw_rps()

        # Score tracking logic
        if player1_throw == player2_throw:
            tie_score += 1
        elif (player1_throw == 'Rock' and player2_throw == 'Scissors') or \
             (player1_throw == 'Scissors' and player2_throw == 'Paper') or \
             (player1_throw == 'Paper' and player2_throw == 'Rock'):
            player1_score += 1
        else:
            player2_score += 1

        play_round(player1_throw, player2_throw)

    # Display final results
    print("\n📊 Final Results:")
    print(f"Player 1 Wins: {player1_score}")
    print(f"Player 2 Wins: {player2_score}")
    print(f"Ties: {tie_score}")

    if player1_score > player2_score:
        print(" Player 1 is the overall winner!")
    elif player2_score > player1_score:
        print(" Player 2 is the overall winner!")
    else:
        print(" It's an overall tie!")

if __name__ == "__main__":
    main()
